from __future__ import annotations

import json
import sys
from pathlib import Path
from fastapi import FastAPI, HTTPException, status, Depends, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
from typing import Any, Annotated
from fastapi import Cookie
from datetime import datetime, timedelta
import uuid

import header
from src import gs
from src.logger import logger
from src.ai import GoogleGenerativeAI
from src.utils.file import recursively_get_file_path

base_path: Path = gs.path.endpoints / 'ai_games' / '101_basic_computer_games' / 'ru' / 'chat'
locales_path: Path = base_path /  'html' / 'locales'
_html: Path = base_path / 'html'  # Chemin vers l'application Angular


app = FastAPI()

# Configurer CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# Authentification
# ============================================================================

# class User(BaseModel):
#     username: str
#     password: str

# Dans un cas réel, cela devrait vérifier par rapport à une base de données ou similaire
USERS = {
    "user": "password123"
}

SESSION_DATA = {}

SESSION_COOKIE_NAME = "session_id"
SESSION_TTL = timedelta(hours=1)

async def get_current_user(session_id: Annotated[str | None, Cookie()] = None) -> str | None:
    if session_id is None or session_id not in SESSION_DATA:
      return None
    data = SESSION_DATA[session_id]
    if data["expires"] < datetime.utcnow():
        logger.warning("Session expirée. Supprimer la session")
        del SESSION_DATA[session_id]
        return None
    # prolonger l'expiration de la session
    data["expires"] = datetime.utcnow() + SESSION_TTL
    return data["user"]


@app.post("/api/login")
async def login(username: str = Form(), password: str = Form()) -> RedirectResponse:
    if username not in USERS or USERS[username] != password:
        logger.warning("Échec de la connexion : Nom d'utilisateur ou mot de passe invalide")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Identifiants invalides")

    session_id: str = str(uuid.uuid4())
    SESSION_DATA[session_id] = {
        "user": username,
        "expires": datetime.utcnow() + SESSION_TTL
    }
    logger.info(f"Connexion réussie pour l'utilisateur {username}")
    response: RedirectResponse = RedirectResponse(url='/', status_code=303) # Redirection après connexion
    response.set_cookie(key=SESSION_COOKIE_NAME, value=session_id, httponly=True, samesite="none", secure=True)
    return response


@app.post("/api/logout")
async def logout(session_id: Annotated[str | None, Cookie()] = None) -> JSONResponse:
    if session_id is None or session_id not in SESSION_DATA:
        logger.warning("Déconnexion échouée : session_id n'est pas valide")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Non autorisé")

    del SESSION_DATA[session_id]
    logger.info(f"Déconnexion réussie pour l'utilisateur avec session_id {session_id}")
    response: JSONResponse = JSONResponse(content={"message": "Déconnexion réussie"})
    response.delete_cookie(SESSION_COOKIE_NAME)
    return response


# ============================================================================
# Application principale
# ============================================================================

# Modèle de requête de chat
class ChatRequest(BaseModel):
    message: str


model: GoogleGenerativeAI | None = None
api_key: str = gs.credentials.gemini.games
system_instruction: str = ""


# Route racine
@app.get("/", response_class=HTMLResponse)
async def root(request: Request, current_user: str | None = Depends(get_current_user)) -> HTMLResponse:
    """Sert le fichier index.html principal pour l'application."""
    try:
        if current_user:
            index_file: Path = _html / 'index.html'
            if not index_file.exists():
                raise FileNotFoundError(f"Impossible de trouver index.html au chemin : {index_file}")
            html_content: str = index_file.read_text(encoding="utf-8")
            return HTMLResponse(content=html_content)
        else:
             login_file: Path = _html / 'login.html'
             if not login_file.exists():
                raise FileNotFoundError(f"Impossible de trouver login.html au chemin : {login_file}")
             html_content: str = login_file.read_text(encoding="utf-8")
             return HTMLResponse(content=html_content)


    except FileNotFoundError as e:
      logger.error(f"Erreur dans la racine : Fichier non trouvé : {e}", exc_info=True)
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"index.html non trouvé : {e}")
    except Exception as e:
        logger.error(f"Erreur dans la racine : {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Erreur de lecture des modèles : {str(e)}")


# Route de chat
@app.post("/api/chat")
async def chat(request: ChatRequest, current_user: str = Depends(get_current_user)) -> dict[str, Any]:
    """Gère les requêtes de chat et renvoie une réponse du bot."""
    global model
    try:
        if not model:
            model = GoogleGenerativeAI(api_key=api_key, model_name='gemini-2.0-flash-exp')
        response: str = await model.chat(request.message)
        return {"response": response}
    except Exception as ex:
        logger.error(f"Erreur dans le chat : {ex}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex))


def get_locale_file(lang: str) -> dict[str, str]:
    """Lit un fichier de locale basé sur la langue donnée."""
    locale_file: Path = locales_path / f'{lang}.json'
    try:
        with open(locale_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError as ex:
        logger.error(f"Erreur de lecture de la locale : {ex}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Locale non trouvée")
    except json.JSONDecodeError as ex:
        logger.error(f"Erreur de décodage json : {ex}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Fichier de locale invalide")
    except Exception as ex:
        logger.error(f"Erreur de lecture de la locale : {ex}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erreur de lecture des locales")


@app.get("/locales/{lang}.json")
async def locales(lang: str, current_user: str = Depends(get_current_user)) -> dict[str, str]:
    """Point de terminaison pour récupérer les fichiers de locale."""
    return get_locale_file(lang)


# Route de chat
@app.get("/api/rules")
async def rules(current_user: str = Depends(get_current_user)) -> list[dict[str, str]]:
    """Renvoie la liste des règles."""
    rules_list: list[Path] = recursively_get_file_path(gs.path.endpoints / 'ai_games' / '101_basic_computer_games' / 'ru' / 'rules' )
    rules_list = [rule.name for rule in rules_list]
    return rules_list

# Exécution du serveur local
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
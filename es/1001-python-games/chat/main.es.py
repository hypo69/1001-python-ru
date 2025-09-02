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
_html: Path = base_path / 'html'  # Ruta a la aplicación Angular


app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# Autenticación
# ============================================================================

# class User(BaseModel):
#     username: str
#     password: str

# En un caso real, esto debería comprobarse con una base de datos o similar
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
        logger.warning("Sesión caducada. Eliminar sesión")
        del SESSION_DATA[session_id]
        return None
    # extender la caducidad de la sesión
    data["expires"] = datetime.utcnow() + SESSION_TTL
    return data["user"]


@app.post("/api/login")
async def login(username: str = Form(), password: str = Form()) -> RedirectResponse:
    if username not in USERS or USERS[username] != password:
        logger.warning("Error de inicio de sesión: Nombre de usuario o contraseña no válidos")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales no válidas")

    session_id: str = str(uuid.uuid4())
    SESSION_DATA[session_id] = {
        "user": username,
        "expires": datetime.utcnow() + SESSION_TTL
    }
    logger.info(f"Inicio de sesión exitoso para el usuario {username}")
    response: RedirectResponse = RedirectResponse(url='/', status_code=303) # Redireccionar después del inicio de sesión
    response.set_cookie(key=SESSION_COOKIE_NAME, value=session_id, httponly=True, samesite="none", secure=True)
    return response


@app.post("/api/logout")
async def logout(session_id: Annotated[str | None, Cookie()] = None) -> JSONResponse:
    if session_id is None or session_id not in SESSION_DATA:
        logger.warning("Cierre de sesión fallido: session_id no es válido")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No autorizado")

    del SESSION_DATA[session_id]
    logger.info(f"Cierre de sesión exitoso para el usuario con session_id {session_id}")
    response: JSONResponse = JSONResponse(content={"message": "Cierre de sesión exitoso"})
    response.delete_cookie(SESSION_COOKIE_NAME)
    return response


# ============================================================================
# Aplicación principal
# ============================================================================

# Modelo de solicitud de chat
class ChatRequest(BaseModel):
    message: str


model: GoogleGenerativeAI | None = None
api_key: str = gs.credentials.gemini.games
system_instruction: str = ""


# Ruta raíz
@app.get("/", response_class=HTMLResponse)
async def root(request: Request, current_user: str | None = Depends(get_current_user)) -> HTMLResponse:
    """Sirve el archivo index.html principal para la aplicación."""
    try:
        if current_user:
            index_file: Path = _html / 'index.html'
            if not index_file.exists():
                raise FileNotFoundError(f"No se pudo encontrar index.html en la ruta: {index_file}")
            html_content: str = index_file.read_text(encoding="utf-8")
            return HTMLResponse(content=html_content)
        else:
             login_file: Path = _html / 'login.html'
             if not login_file.exists():
                raise FileNotFoundError(f"No se pudo encontrar login.html en la ruta: {login_file}")
             html_content: str = login_file.read_text(encoding="utf-8")
             return HTMLResponse(content=html_content)


    except FileNotFoundError as e:
      logger.error(f"Error en la raíz: Archivo no encontrado: {e}", exc_info=True)
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"index.html no encontrado: {e}")
    except Exception as e:
        logger.error(f"Error en la raíz: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error al leer las plantillas: {str(e)}")


# Ruta de chat
@app.post("/api/chat")
async def chat(request: ChatRequest, current_user: str = Depends(get_current_user)) -> dict[str, Any]:
    """Maneja las solicitudes de chat y devuelve una respuesta del bot."""
    global model
    try:
        if not model:
            model = GoogleGenerativeAI(api_key=api_key, model_name='gemini-2.0-flash-exp')
        response: str = await model.chat(request.message)
        return {"response": response}
    except Exception as ex:
        logger.error(f"Error en el chat: {ex}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex))


def get_locale_file(lang: str) -> dict[str, str]:
    """Lee un archivo de configuración regional basado en el idioma dado."""
    locale_file: Path = locales_path / f'{lang}.json'
    try:
        with open(locale_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError as ex:
        logger.error(f"Error al leer la configuración regional: {ex}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Configuración regional no encontrada")
    except json.JSONDecodeError as ex:
        logger.error(f"Error al decodificar json: {ex}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Archivo de configuración regional no válido")
    except Exception as ex:
        logger.error(f"Error al leer la configuración regional: {ex}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error al leer las configuraciones regionales")


@app.get("/locales/{lang}.json")
async def locales(lang: str, current_user: str = Depends(get_current_user)) -> dict[str, str]:
    """Punto final para recuperar archivos de configuración regional."""
    return get_locale_file(lang)


# Ruta de chat
@app.get("/api/rules")
async def rules(current_user: str = Depends(get_current_user)) -> list[dict[str, str]]:
    """Devuelve la lista de reglas."""
    rules_list: list[Path] = recursively_get_file_path(gs.path.endpoints / 'ai_games' / '101_basic_computer_games' / 'ru' / 'rules' )
    rules_list = [rule.name for rule in rules_list]
    return rules_list

# Ejecución del servidor local
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
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
_html: Path = base_path / 'html'  # Path to Angular App


app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# Аутентификация
# ============================================================================

# class User(BaseModel):
#     username: str
#     password: str

# In real case, this should check against db or similar
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
        logger.warning("Session expired. Remove session")
        del SESSION_DATA[session_id]
        return None
    # extend session expiration
    data["expires"] = datetime.utcnow() + SESSION_TTL
    return data["user"]


@app.post("/api/login")
async def login(username: str = Form(), password: str = Form()) -> RedirectResponse:
    if username not in USERS or USERS[username] != password:
        logger.warning("Login failed: Invalid username or password")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    session_id: str = str(uuid.uuid4())
    SESSION_DATA[session_id] = {
        "user": username,
        "expires": datetime.utcnow() + SESSION_TTL
    }
    logger.info(f"Login successful for user {username}")
    response: RedirectResponse = RedirectResponse(url='/', status_code=303) # Перенаправление после логина
    response.set_cookie(key=SESSION_COOKIE_NAME, value=session_id, httponly=True, samesite="none", secure=True)
    return response


@app.post("/api/logout")
async def logout(session_id: Annotated[str | None, Cookie()] = None) -> JSONResponse:
    if session_id is None or session_id not in SESSION_DATA:
        logger.warning("Logout failed: session_id is not valid")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

    del SESSION_DATA[session_id]
    logger.info(f"Logout successful for user with session_id {session_id}")
    response: JSONResponse = JSONResponse(content={"message": "Logout successful"})
    response.delete_cookie(SESSION_COOKIE_NAME)
    return response


# ============================================================================
# Основное приложение
# ============================================================================

# Chat request model
class ChatRequest(BaseModel):
    message: str


model: GoogleGenerativeAI | None = None
api_key: str = gs.credentials.gemini.games
system_instruction: str = ""


# Root route
@app.get("/", response_class=HTMLResponse)
async def root(request: Request, current_user: str | None = Depends(get_current_user)) -> HTMLResponse:
    """Serves the main index.html file for the application."""
    try:
        if current_user:
            index_file: Path = _html / 'index.html'
            if not index_file.exists():
                raise FileNotFoundError(f"Could not find index.html at path: {index_file}")
            html_content: str = index_file.read_text(encoding="utf-8")
            return HTMLResponse(content=html_content)
        else:
             login_file: Path = _html / 'login.html'
             if not login_file.exists():
                raise FileNotFoundError(f"Could not find login.html at path: {login_file}")
             html_content: str = login_file.read_text(encoding="utf-8")
             return HTMLResponse(content=html_content)


    except FileNotFoundError as e:
      logger.error(f"Error in root: File not found: {e}", exc_info=True)
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"index.html not found: {e}")
    except Exception as e:
        logger.error(f"Error in root: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error reading templates: {str(e)}")


# Chat route
@app.post("/api/chat")
async def chat(request: ChatRequest, current_user: str = Depends(get_current_user)) -> dict[str, Any]:
    """Handles chat requests and returns a bot response."""
    global model
    try:
        if not model:
            model = GoogleGenerativeAI(api_key=api_key, model_name='gemini-2.0-flash-exp')
        response: str = await model.chat(request.message)
        return {"response": response}
    except Exception as ex:
        logger.error(f"Error in chat: {ex}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex))


def get_locale_file(lang: str) -> dict[str, str]:
    """Reads a locale file based on the given language."""
    locale_file: Path = locales_path / f'{lang}.json'
    try:
        with open(locale_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError as ex:
        logger.error(f"Error reading locale: {ex}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Locale not found")
    except json.JSONDecodeError as ex:
        logger.error(f"Error decoding json: {ex}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Invalid locale file")
    except Exception as ex:
        logger.error(f"Error reading locale: {ex}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error reading locales")


@app.get("/locales/{lang}.json")
async def locales(lang: str, current_user: str = Depends(get_current_user)) -> dict[str, str]:
    """Endpoint to retrieve locale files."""
    return get_locale_file(lang)


# Chat route
@app.get("/api/rules")
async def rules(current_user: str = Depends(get_current_user)) -> list[dict[str, str]]:
    """Returns the list of rules."""
    rules_list: list[Path] = recursively_get_file_path(gs.path.endpoints / 'ai_games' / '101_basic_computer_games' / 'ru' / 'rules' )
    rules_list = [rule.name for rule in rules_list]
    return rules_list

# Local server execution
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")
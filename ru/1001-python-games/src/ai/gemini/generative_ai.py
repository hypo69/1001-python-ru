## \file /src/ai/gemini/generative_ai.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module::  src.ai.gemini
   :platform: Windows, Unix
   :synopsis: Google generative AI integration
   https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai.md
"""


import time
import json
from io import IOBase
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict
from types import SimpleNamespace
import base64

import google.generativeai as genai
import requests

from grpc import RpcError
from google.api_core.exceptions import (
    GatewayTimeout,
    ServiceUnavailable,
    ResourceExhausted,
    InvalidArgument,
)
from google.auth.exceptions import DefaultCredentialsError, RefreshError
from src.logger.logger import logger
from src import gs
from src.utils.printer import pprint
from src.utils.file import read_text_file, save_text_file
from src.utils.date_time import TimeoutCheck
from src.utils.convertors.unicode import decode_unicode_escape
from src.utils.jjson import j_loads, j_loads_ns, j_dumps

timeout_check = TimeoutCheck()

class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.

    Этот класс используется для настройки и работы с моделью Google Generative AI, включая отправку запросов,
    получение ответов и сохранение диалогов в текстовых и JSON файлах.

    Атрибуты:
        MODELS (List[str]): Список доступных моделей AI.
        api_key (str): Ключ API для доступа к генеративной модели.
        model_name (str): Название модели для использования.
        generation_config (Dict): Конфигурация для генерации.
        mode (str): Режим работы модели (например, 'debug' или 'production').
        dialogue_log_path (Optional[Path]): Путь для логирования диалогов.
        dialogue_txt_path (Optional[Path]): Путь для сохранения текстовых файлов диалогов.
        history_dir (Path): Директория для хранения истории.
        history_txt_file (Optional[Path]): Путь к файлу для хранения истории в формате текста.
        history_json_file (Optional[Path]): Путь к файлу для хранения истории в формате JSON.
        model (Optional[genai.GenerativeModel]): Объект модели Google Generative AI.
        system_instruction (Optional[str]): Инструкция для системы, которая задает параметры поведения модели.

    Пример использования:
        >>> ai = GoogleGenerativeAI(api_key="your_api_key", system_instruction="Instruction")
        >>> response = ai.ask("Как дела?")
        >>> print(response)
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, 
                 api_key: str, 
                 model_name: Optional[str] = None, 
                 generation_config: Optional[Dict] = None, 
                 system_instruction: Optional[str] = None, 
                 **kwargs):
        """
        Инициализация модели GoogleGenerativeAI с дополнительными настройками.

        Этот метод настраивает модель AI, а также определяет пути для логирования и истории.

        Аргументы:
            api_key (str): Ключ API для доступа к генеративной модели.
            model_name (Optional[str], optional): Название модели для использования. По умолчанию "gemini-1.5-flash-8b".
            generation_config (Optional[Dict], optional): Конфигурация для генерации. По умолчанию {"response_mime_type": "text/plain"}.
            system_instruction (Optional[str], optional): Инструкция для системы. По умолчанию None.
        """
        _now = gs.now
        self.api_key = api_key
        self.model_name = model_name or "gemini-1.5-flash-8b"
        self.generation_config = generation_config or {"response_mime_type": "text/plain"}
        self.system_instruction = system_instruction

        self.dialogue_log_path = gs.path.external_storage / 'AI' / 'log'
        self.dialogue_txt_path = self.dialogue_log_path / f"gemini_{_now}.txt"
        self.history_dir = gs.path.external_storage / 'AI' / 'history'
        self.history_txt_file = self.history_dir / f"gemini_{_now}.txt"
        self.history_json_file = self.history_dir / f"gemini_{_now}.json"

        # Инициализация модели
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            generation_config=self.generation_config
        )
        self._chat = self._start_chat()


    @property
    def config():
        """ Получаю конфигурацию из файла настроек"""
        return j_loads_ns(gs.path.src / 'ai' / 'gemini' / 'generative_ai.json')

    def _start_chat(self):
        """"""
        ...
        return self.model.start_chat(history=[])

    def _save_dialogue(self, dialogue: list):
        """
        Сохранить диалог в текстовый и JSON файл с управлением размером файлов.

        Этот метод сохраняет каждый диалог в текстовом и JSON формате для последующего анализа.

        Аргументы:
            dialogue (list): Список сообщений, представляющих диалог, который нужно сохранить.
        """
        save_text_file(dialogue, self.history_txt_file, mode='+a')
        for message in dialogue:
            j_dumps(data=message, file_path=self.history_json_file, mode='+a')


    async def ask(self, q: str, attempts: int = 15) -> Optional[str]:
        """
        метод отправляет текстовый запрос модели и возвращает ответ.

        Аргументы:
            q (str): Вопрос, который будет отправлен модели.
            attempts (int, optional): Количество попыток для получения ответа. По умолчанию 3.

        Возвращает:
            Optional[str]: Ответ от модели или None, если ответ не был получен.

        Пример:
            >>> ai = GoogleGenerativeAI(api_key="your_api_key")
            >>> response = ai.ask("Какая погода сегодня?")
            >>> print(response)
        TODO: 
            препарировать `response`
        """
        ### self.model.
        for attempt in range(attempts):
            try:
                response = self.model.generate_content(q)

                if not response:
                    logger.debug(f"No response from the model. Attempt: {attempt}\nSleeping for {2 ** attempt}")
                    time.sleep(2 ** attempt)
                    continue  # Повторить попытку

                messages = [
                    {"role": "user", "content": q},
                    {"role": "assistant", "content": response.text}
                ]

                # self._save_dialogue([messages])
                return response.text

            except requests.exceptions.RequestException as ex:
                timeout = 1200
                max_attempts = 5
                if attempt > max_attempts:
                    break
                logger.debug(f"Network error. Attempt: {attempt}\nSleeping for {timeout/60} min on {gs.now}",ex,None)
                time.sleep(timeout)
                continue  # Повторить попытку
            except (GatewayTimeout, ServiceUnavailable) as ex:
                logger.error("Service unavailable:", ex, None)
                # Экспоненциальный бэк-офф для повторных попыток
                max_attempts = 3
                if attempt > max_attempts:
                    break
                time.sleep(2 ** attempt)
                continue
            except ResourceExhausted as ex:
                timeout = 10800
                logger.debug(f"Quota exceeded. Attempt: {attempt}\nSleeping for {timeout/60} min on {gs.now}",ex,None)
                time.sleep(timeout)
                continue
            except (DefaultCredentialsError, RefreshError) as ex:
                logger.error("Authentication error:",ex,None)
                return  # Прекратить попытки, если ошибка аутентификации
            except (ValueError, TypeError) as ex:
                max_attempts = 3
                if attempt > max_attempts:
                    break
                timeout = 5
                logger.error(f"Invalid input: Attempt: {attempt}\nSleeping for {timeout/60} min on {gs.now}",ex,None)
                time.sleep(timeout)
                continue  
            except (InvalidArgument, RpcError) as ex:
                logger.error("API error:",ex,None)
                return
            except Exception as ex:
                logger.error("Unexpected error:",ex,None)
                return

        return

    def chat(self, q:str) -> str:
        """"""
        ...
        response = None
        try:
            response = self._chat.send_message(q)
            return response.text
        except Exception as ex:
            logger.error(f"Ошибка чата {response=}",ex)
            ...
            return

    def describe_image(self, image_path: Path) -> Optional[str]:
        """
        Генерирует описание изображения.

        Этот метод отправляет изображение в модель для анализа и получает текстовое описание изображения.

        Аргументы:
            image_path (Path): Путь к изображению, которое нужно описать.

        Возвращает:
            Optional[str]: Описание изображения или None, если произошла ошибка.

        Пример:
            >>> ai = GoogleGenerativeAI(api_key="your_api_key")
            >>> description = ai.describe_image(Path("path/to/image.jpg"))
            >>> print(description)
        """
        try:
            with image_path.open('rb') as f:
                encoded_image = base64.b64encode(f.read()).decode('utf-8')

            response = self.model.generate_content(encoded_image)
            return response.text

        except Exception as ex:
            logger.error(f"Error describing image:" , ex)
            return

    def upload_file(self, file: str | Path | IOBase, file_name:Optional[str] = None) -> bool:
        """
        https://github.com/google-gemini/generative-ai-python/blob/main/docs/api/google/generativeai/upload_file.md
        """
        
        response = None
        try:
            response =  genai.upload_file( 
                    path = file,
                    mime_type = None,
                    name = file_name,
                    display_name = file_name,
                    resumable = True
                )
            logger.debug(f"Файл {file_name} записан", None, False)
            return response
        except Exception as ex:
            logger.error(f"Ошибка записи файла {file_name=}", ex, False)
            try:
                response = genai.delete_file(file_name)
                logger.debug(f"Файл {file_name} удален", None, False)
                self.upload_file(file,file_name)
            except Exception as ex:
                logger.error(f"Общая ошибка модели: ", ex, False)   
                ...
                return





if __name__ == "__main__":
    ...

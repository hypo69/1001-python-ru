## \file /src/ai/gemini/generative_ai.py
# -*- coding: utf-8 -*-

"""
.. module::  src.ai.gemini
   :platform: Windows, Unix
   :synopsis: Google generative AI integration
"""

import google.generativeai as genai

class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, api_key: str, model_name: str = "gemini-1.5-flash-8b"):
        """
        Инициализация модели GoogleGenerativeAI.

        Аргументы:
            api_key (str): Ключ API для доступа к генеративной модели.
            model_name (str, optional): Название модели для использования. По умолчанию "gemini-1.5-flash-8b".
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name=self.model_name)

    def ask(self, q: str) -> str:
        """
        Отправляет текстовый запрос модели и возвращает ответ.

        Аргументы:
            q (str): Вопрос, который будет отправлен модели.

        Возвращает:
            str: Ответ от модели.
        """
        try:
            response = self.model.generate_content(q)
            return response.text
        except Exception as ex:
            return f"Error: {str(ex)}"

if __name__ == "__main__":
    ...
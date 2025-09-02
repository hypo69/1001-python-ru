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
    Clase para interactuar con los modelos de IA generativa de Google.
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, api_key: str, model_name: str = "gemini-1.5-flash-8b"):
        """
        Inicializa el modelo GoogleGenerativeAI.

        Argumentos:
            api_key (str): Clave API para acceder al modelo generativo.
            model_name (str, optional): Nombre del modelo a usar. Por defecto "gemini-1.5-flash-8b".
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name=self.model_name)

    def ask(self, q: str) -> str:
        """
        Envía una consulta de texto al modelo y devuelve la respuesta.

        Argumentos:
            q (str): La pregunta que se enviará al modelo.

        Devuelve:
            str: La respuesta del modelo.
        """
        try:
            response = self.model.generate_content(q)
            return response.text
        except Exception as ex:
            return f"Error: {str(ex)}"

if __name__ == "__main__":
    ...
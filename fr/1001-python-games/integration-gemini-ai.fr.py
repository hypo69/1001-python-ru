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
    Classe pour interagir avec les modèles d'IA générative de Google.
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, api_key: str, model_name: str = "gemini-1.5-flash-8b"):
        """
        Initialise le modèle GoogleGenerativeAI.

        Arguments:
            api_key (str): Clé API pour accéder au modèle génératif.
            model_name (str, optional): Nom du modèle à utiliser. Par défaut "gemini-1.5-flash-8b".
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name=self.model_name)

    def ask(self, q: str) -> str:
        """
        Envoie une requête textuelle au modèle et renvoie la réponse.

        Arguments:
            q (str): La question à envoyer au modèle.

        Renvoie:
            str: La réponse du modèle.
        """
        try:
            response = self.model.generate_content(q)
            return response.text
        except Exception as ex:
            return f"Error: {str(ex)}"

if __name__ == "__main__":
    ...
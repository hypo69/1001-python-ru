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
    Class for interacting with Google Generative AI models.
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, api_key: str, model_name: str = "gemini-1.5-flash-8b"):
        """
        Initializes the GoogleGenerativeAI model.

        Arguments:
            api_key (str): API key for accessing the generative model.
            model_name (str, optional): Name of the model to use. Defaults to "gemini-1.5-flash-8b".
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name=self.model_name)

    def ask(self, q: str) -> str:
        """
        Sends a text query to the model and returns the response.

        Arguments:
            q (str): The question to be sent to the model.

        Returns:
            str: The response from the model.
        """
        try:
            response = self.model.generate_content(q)
            return response.text
        except Exception as ex:
            return f"Error: {str(ex)}"

if __name__ == "__main__":
    ...
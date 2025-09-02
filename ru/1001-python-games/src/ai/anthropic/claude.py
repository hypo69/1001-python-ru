## \file /src/ai/anthropic/claude.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
module: src.ai.anthropic.claude
	:platform: Windows, Unix
	:synopsis: Модуль определяющий корневой путь к проекту. Все импорты строятся относительно этого пути.
    :TODO: В дальнейшем перенести в системную переменную"""


# test



import anthropic

class ClaudeClient:
    def __init__(self, api_key):
        self.client = anthropic.Client(api_key)

    def generate_text(self, prompt, max_tokens_to_sample=100):
        """
        Generates text based on the given prompt.

        :param prompt: The prompt to generate text from.
        :param max_tokens_to_sample: The maximum number of tokens to generate.
        :return: The generated text.
        """
        response = self.client.completion(
            prompt=prompt,
            model="claude-v1",
            max_tokens_to_sample=max_tokens_to_sample,
            stop_sequences=["\n\nHuman:"]
        )
        return response['completion']

    def analyze_sentiment(self, text):
        """
        Analyzes the sentiment of the given text.

        :param text: The text to analyze.
        :return: The sentiment analysis result.
        """
        response = self.client.completion(
            prompt=f"Analyze the sentiment of the following text: {text}",
            model="claude-v1",
            max_tokens_to_sample=50,
            stop_sequences=["\n\nHuman:"]
        )
        return response['completion']

    def translate_text(self, text, source_language, target_language):
        """
        Translates the given text from the source language to the target language.

        :param text: The text to translate.
        :param source_language: The source language code.
        :param target_language: The target language code.
        :return: The translated text.
        """
        response = self.client.completion(
            prompt=f"Translate the following text from {source_language} to {target_language}: {text}",
            model="claude-v1",
            max_tokens_to_sample=100,
            stop_sequences=["\n\nHuman:"]
        )
        return response['completion']

# Пример использования класса
if __name__ == "__main__":
    api_key = "your-api-key"
    claude_client = ClaudeClient(api_key)

    # Пример генерации текста
    prompt = "Write a short story about a robot learning to love."
    generated_text = claude_client.generate_text(prompt)
    print("Generated Text:", generated_text)

    # Пример анализа тональности
    text_to_analyze = "I am very happy today!"
    sentiment_analysis = claude_client.analyze_sentiment(text_to_analyze)
    print("Sentiment Analysis:", sentiment_analysis)

    # Пример перевода текста
    text_to_translate = "Hello, how are you?"
    source_language = "en"
    target_language = "es"
    translated_text = claude_client.translate_text(text_to_translate, source_language, target_language)
    print("Translated Text:", translated_text)
## \file /src/ai/openai/model/_experiments/kazarinov.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.ai.openai.model._experiments 
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""
  
""" module: src.ai.openai.model._experiments """


""" HERE SHOULD BE A DESCRIPTION OF THE MODULE OPERATION ! """

import header 
import openai
from src import gs
from src.utils.file import read_text_file
from src.logger.logger import logger
from pathlib import Path

# Загрузка системной инструкции
system_instruction_path = Path('../src/ai/openai/model/_experiments/system_instruction.txt')
system_instruction = read_text_file(system_instruction_path)

# Инициализация OpenAI модели
class OpenAIChat:
    def __init__(self, api_key: str, system_instruction: str = None):
        openai.api_key = gs.credentials
        self.system_instruction = system_instruction
        self.messages = []

        if self.system_instruction:
            self.messages.append({"role": "system", "content": self.system_instruction})

    def ask(self, prompt: str) -> str:
        """Отправка вопроса в модель OpenAI и получение ответа"""
        self.messages.append({"role": "user", "content": prompt})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.messages,
                max_tokens=150,
                temperature=0.7
            )
            answer = response['choices'][0]['message']['content']
            self.messages.append({"role": "assistant", "content": answer})
            return answer
        except Exception as e:
            logger.error(f"Ошибка: {e}")
            return "Произошла ошибка при обработке запроса."

def chat():
    print("Добро пожаловать в чат с OpenAI!")
    print("Чтобы завершить чат, напишите 'exit'.\n")
    
    # Ввод ключа API и инициализация модели
    api_key = input("Введите ваш OpenAI API ключ: ")
    ai = OpenAIChat(api_key=api_key, system_instruction=system_instruction)

    while True:
        # Получаем вопрос от пользователя
        user_input = input("> вопрос\n> ")
        
        if user_input.lower() == 'exit':
            print("Чат завершен.")
            break
        
        # Отправляем запрос модели и получаем ответ
        response = ai.ask(prompt=user_input)
        
        # Выводим ответ
        print(f">> ответ\n>> {response}\n")

if __name__ == "__main__":
    chat()

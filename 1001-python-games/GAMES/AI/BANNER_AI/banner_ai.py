import os
import re  # Импорт библиотеки для работы с регулярными выражениями
import json

from pathlib import Path
from dotenv import load_dotenv, set_key  # Импорт функции для сохранения переменной в .env

import google.generativeai as genai  # Импорт библиотеки для работы с Gemini
from header import __root__  # Импорт объекта __root__, содержащего абсолютный путь к корню проекта


# Загрузка переменных окружения из файла .env
load_dotenv()

class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.
    """

    MODELS = [
        'gemini-1.5-flash-8b',
        'gemini-2-13b',
        'gemini-3-20b'
    ]

    def __init__(self, api_key: str, system_instruction: str, model_name: str = 'gemini-2.0-flash-exp'):
        """
        Инициализация модели GoogleGenerativeAI.

        :param api_key: Ключ API для доступа к Gemini.
        :type api_key: str
        :param system_instruction: Инструкция для модели (системный промпт).
        :type system_instruction: str
        :param model_name: Название используемой модели Gemini. По умолчанию 'gemini-2.0-flash-exp'.
        :type model_name: str
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)  # Конфигурация библиотеки с API ключом
        self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction)  # Инициализация модели с инструкцией

    def ask(self, q: str) -> str:
        """
        Отправка запроса модели и получение ответа.

        :param q: Текст запроса.
        :type q: str
        :return: Ответ модели или сообщение об ошибке.
        :rtype: str
        """
        try:
            response = self.model.generate_content(q)  # Отправка запроса модели
            return response.text  # Получение текстового ответа
        except Exception as ex:
            return f'Error: {str(ex)}'  # Обработка и получение ошибки


# Основная часть программы
if __name__ == '__main__':
    relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # Относительный путь к директории
    base_path: Path = __root__ / relative_path  # Абсолютный путь к директории с использованием __root__


    # Чтение API ключа из переменных окружения или запрос у пользователя
    API_KEY: str = os.getenv('API_KEY')
    if not API_KEY:
        API_KEY = input('API ключ не найден. Введите API ключ от `gemini`: ')  # Запрос API ключа у пользователя
        # Сохранение введенного ключа в файл .env
        set_key('.env', 'API_KEY', API_KEY)

    instructions: dict = {
        '1': 'system_instruction_asterisk',
        '2': 'system_instruction_tilde',
        '3': 'system_instruction_hash',
    }

    # Приветствие пользователя
    print('Добро пожаловать в игру Banner!')
    print('Введите текст, и я создам для вас текстовый баннер.')

    while True:
        # Выбор стиля оформления баннера
        print('Выберите стиль оформления баннера:')
        print('1. Символ \'*\'')
        print('2. Символ \'~\'')
        print('3. Символ \'#\'')
        choice = input('Введите номер стиля (1, 2 или 3): ')

        if choice in ('1', '2', '3'):
            system_instruction: str = Path(base_path, 'instructions', f'{instructions[choice]}.md').read_text(encoding='UTF-8')  # Чтение инструкции из файла
        else:
            print('Неверный выбор. Используется стиль по умолчанию \'*\'')
            system_instruction: str = Path(base_path, 'instructions', 'system_instruction_asterisk.md').read_text(encoding='UTF-8')  # Чтение инструкции по умолчанию

        # Создание экземпляра класса с выбранной инструкцией
        model: GoogleGenerativeAI = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction)

        # Запрос текста у пользователя
        user_text: str = input('Введите текст для баннера: ')

        # Проверка, что текст не пустой
        if user_text.strip() == '':
            print('Вы не ввели текст. Попробуйте снова.')
        else:
            # Отправка текста модели и получение оформленного баннера
            response = model.ask(user_text)
            print('\nВаш баннер готов:')
            print(response)
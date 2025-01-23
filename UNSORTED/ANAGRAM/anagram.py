import google.generativeai as genai  # Импортируем библиотеку для работы с Gemini
import re  # Импортируем библиотеку для работы с регулярными выражениями

class GoogleGenerativeAI:
    """
    Класс для взаимодействия с моделями Google Generative AI.
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, api_key: str, system_instruction: str = "", model_name: str = "gemini-2.0-flash-exp"):
        """
        Инициализация модели GoogleGenerativeAI.

        Args:
            api_key: Ключ API для доступа к Gemini.
            system_instruction: Инструкция для модели (системный промпт).
            model_name: Название используемой модели Gemini.
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)  # Конфигурируем библиотеку с API ключом
        self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction) # Инициализируем модель с инструкцией

    def ask(self, q: str) -> str:
        """
        Отправляет запрос модели и возвращает ответ.

        Args:
            q: Текст запроса.

        Returns:
            Ответ модели или сообщение об ошибке.
        """
        try:
            response = self.model.generate_content(q)  # Отправляем запрос модели
            return response.text  # Возвращаем текстовый ответ
        except Exception as ex:
            return f"Error: {str(ex)}"  # Обрабатываем и возвращаем ошибку

# Инструкция для Gemini (системный промпт)
system_instruction = """
Ты — генератор анаграмм. Твоя задача — по заданному набору букв найти существующее слово русского языка, составленное из этих букв (используя все или часть из них).

Правила:

1. Игнорируй любые символы, кроме русских букв. Цифры и другие символы не учитываются.
2. Если из заданных букв можно составить несколько слов, верни одно из них.
3. Если из заданных букв невозможно составить ни одного слова русского языка, верни ответ "Нет анаграмм".
4. Не генерируй неологизмы или выдуманные слова. Используй только существующие слова русского языка.
5. Не объясняй процесс, просто возвращай слово или "Нет анаграмм".
"""

API_KEY: str = input("API ключ от `gemini`: ")  # Запрашиваем API ключ у пользователя
model = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction) # Создаем экземпляр класса, передавая API ключ и инструкцию

if __name__ == "__main__":
    while True:  # Бесконечный цикл для ввода запросов
        q = input("Введите буквы, по которым Gemini подберет анаграмму (для выхода нажмите Ctrl+C): ")
        # Очистка ввода от не кириллических символов
        q = re.sub(r"[^а-яА-ЯёЁ]", "", q) # Удаляем все символы, кроме русских букв
        if not q: # Проверяем, осталась ли строка пустой после очистки
            print("Введены некорректные символы. Введите русские буквы.")
            continue # Переходим к следующей итерации цикла
        response = model.ask(q) # Отправляем запрос модели
        print(response) # Выводим ответ модели
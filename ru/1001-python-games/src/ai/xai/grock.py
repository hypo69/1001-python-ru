import requests
import json

class XAI:
    def __init__(self, api_key):
        """
        Инициализация класса XAI.

        :param api_key: Ключ API для аутентификации.
        """
        self.api_key = api_key
        self.base_url = "https://api.x.ai/v1"  # Базовый URL API
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def _send_request(self, method, endpoint, data=None):
        """
        Отправка запроса к API x.ai.

        :param method: Метод HTTP (GET, POST, PUT, DELETE).
        :param endpoint: Конечная точка API.
        :param data: Данные для отправки в теле запроса (для POST и PUT).
        :return: Ответ от API.
        """
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, headers=self.headers, json=data)
        response.raise_for_status()  # Выбрасывает исключение, если статус ответа не 2xx
        return response.json()

    def chat_completion(self, messages, model="grok-beta", stream=False, temperature=0):
        """
        Запрос на завершение чата.

        :param messages: Список сообщений для чата.
        :param model: Модель для использования.
        :param stream: Флаг для включения потоковой передачи.
        :param temperature: Температура для генерации ответа.
        :return: Ответ от API.
        """
        endpoint = "chat/completions"
        data = {
            "messages": messages,
            "model": model,
            "stream": stream,
            "temperature": temperature
        }
        response = self._send_request("POST", endpoint, data)
        return response

    def stream_chat_completion(self, messages, model="grok-beta", temperature=0):
        """
        Запрос на завершение чата с потоковой передачей.

        :param messages: Список сообщений для чата.
        :param model: Модель для использования.
        :param temperature: Температура для генерации ответа.
        :return: Поток ответов от API.
        """
        endpoint = "chat/completions"
        data = {
            "messages": messages,
            "model": model,
            "stream": True,
            "temperature": temperature
        }
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, headers=self.headers, json=data, stream=True)
        response.raise_for_status()
        return response.iter_lines(decode_unicode=True)

# Пример использования класса XAI
if __name__ == "__main__":
    api_key = "your_api_key_here"  # Замените на ваш реальный API-ключ
    xai = XAI(api_key)

    messages = [
        {
            "role": "system",
            "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."
        },
        {
            "role": "user",
            "content": "What is the answer to life and universe?"
        }
    ]

    # Непотоковый запрос
    completion_response = xai.chat_completion(messages)
    print("Non-streaming response:", completion_response)

    # Потоковый запрос
    stream_response = xai.stream_chat_completion(messages)
    print("Streaming response:")
    for line in stream_response:
        if line.strip():
            print(json.loads(line))
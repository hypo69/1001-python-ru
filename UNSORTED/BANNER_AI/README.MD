# BANNER AI
Модель Gemini возвращает ответ, в виде ASCII баннера в зависимости от данной ей инструкции

 Программа взаимодействует с моделью Google Generative AI для создания текстовых баннеров. 
 Пользователь может выбирать стиль оформления баннера и отправить модели текст для обработки.

## Установка зависимостей
Для запуска кода на локальной машине потребуется установка бибилиотек google.

```python
pip install google
pip install google-generativeai
```

Все эксперименты я настоятельно рекомендую делать в виртуальном окружении.


## Особенности кода в этой программе
1. Инструкции хранятся в разных файлах и подружаются по мере необходимости
2. Начиная с этого примера ключ от модели я сохраняю в переменной окружения, что избавляет меня от необходимости вводить ключ раз за разом
3. Я использую абсолютные пути к файлам. 
    Для определения корневой директории проектаэ я рекурсивно ищу вверх маркерные файлы ('pyproject.toml', 'requirements.txt', '.git'). 
    Найденную директорию я храмю в переменной __root__. От нее я строю путь к системным инструкциям:
    ``python
    relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # Относительный путь к директории
    base_path: Path = __root__ / relative_path  # Абсолютный путь к директории с использованием __root__
    ```


### 1. **Импорт необходимых библиотек**
```python
import google.generativeai as genai  # Импорт библиотеки для работы с Gemini
import re  # Импорт библиотеки для работы с регулярными выражениями
from pathlib import Path  # Импорт для работы с путями файловой системы
from header import __root__  # Импорт объекта __root__, содержащего абсолютный путь к корню проекта
from dotenv import load_dotenv, set_key  # Импорт функций для работы с переменными окружения
import os  # Импорт для работы с переменными окружения
```

- **`google.generativeai`**: Используется для взаимодействия с API Google Generative AI.
- **`re`**: Библиотека для работы с регулярными выражениями (в данном коде не используется, но может быть полезна в будущем).
- **`Path`**: Позволяет работать с путями файловой системы.
- **`__root__`**: Объект, содержащий абсолютный путь к корню проекта.
- **`dotenv`**: Позволяет загружать переменные окружения из файла `.env` и сохранять их.
- **`os`**: Используется для работы с переменными окружения.

---

### 2. **Загрузка переменных окружения**
```python
load_dotenv()
```
- Функция `load_dotenv()` загружает переменные окружения из файла `.env`, если он существует.

---

### 3. **Класс `GoogleGenerativeAI`**
Класс предназначен для взаимодействия с моделью Google Generative AI.

#### 3.1. **Атрибуты класса**
```python
MODELS = [
    'gemini-1.5-flash-8b',
    'gemini-2-13b',
    'gemini-3-20b'
]
```
- Список доступных моделей Google Generative AI.

#### 3.2. **Метод `__init__`**
```python
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
```
- **`api_key`**: Ключ API для доступа к Google Generative AI.
- **`system_instruction`**: Инструкция для модели (например, стиль оформления текста).
- **`model_name`**: Название модели, по умолчанию используется `'gemini-2.0-flash-exp'`.
- **`genai.configure(api_key=self.api_key)`**: Настройка библиотеки с использованием API ключа.
- **`genai.GenerativeModel(...)`**: Инициализация модели с указанными параметрами.

#### 3.3. **Метод `ask`**
```python
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
```
- **`q`**: Текст запроса, который отправляется модели.
- **`self.model.generate_content(q)`**: Отправка запроса модели.
- **`response.text`**: Получение текстового ответа от модели.
- **`except Exception as ex`**: Обработка ошибок и возврат сообщения об ошибке.

---

### 4. **Основная часть программы**
```python
if __name__ == '__main__':
```
- Проверка, что программа запускается как самостоятельный скрипт.

#### 4.1. **Определение путей**
```python
relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # Относительный путь к директории
base_path: Path = __root__ / relative_path  # Абсолютный путь к директории с использованием __root__
```
- **`relative_path`**: Относительный путь к директории внутри проекта.
- **`base_path`**: Абсолютный путь, полученный путем объединения `__root__` и `relative_path`.

#### 4.2. **Чтение API ключа**
```python
API_KEY: str = os.getenv('API_KEY')
if not API_KEY:
    API_KEY = input('API ключ не найден. Введите API ключ от `gemini`: ')  # Запрос API ключа у пользователя
    set_key('.env', 'API_KEY', API_KEY)  # Сохранение ключа в файл .env
```
- **`os.getenv('API_KEY')`**: Пытаемся получить API ключ из переменных окружения.
- Если ключ не найден, запрашиваем его у пользователя через `input`.
- **`set_key('.env', 'API_KEY', API_KEY)`**: Сохраняем введенный ключ в файл `.env` для последующего использования.

#### 4.3. **Инструкции для модели**
```python
instructions: dict = {
    '1': 'system_instruction_asterisk',
    '2': 'system_instruction_tilde',
    '3': 'system_instruction_hash',
}
```
- Словарь, содержащий названия файлов с инструкциями для модели.

#### 4.4. **Приветствие пользователя**
```python
print('Добро пожаловать в игру Banner!')
print('Введите текст, и я создам для вас текстовый баннер.')
```
- Приветствие пользователя и объяснение функционала программы.

#### 4.5. **Цикл для выбора стиля баннера**
```python
while True:
    print('Выберите стиль оформления баннера:')
    print('1. Символ \'*\'')
    print('2. Символ \'~\'')
    print('3. Символ \'#\'')
    choice = input('Введите номер стиля (1, 2 или 3): ')
```
- Пользователь выбирает стиль оформления баннера.

#### 4.6. **Чтение инструкции для модели**
```python
if choice in ('1', '2', '3'):
    system_instruction: str = Path(base_path, 'instructions', f'{instructions[choice]}.md').read_text(encoding='UTF-8')  # Чтение инструкции из файла
else:
    print('Неверный выбор. Используется стиль по умолчанию \'*\'')
    system_instruction: str = Path(base_path, 'instructions', 'system_instruction_asterisk.md').read_text(encoding='UTF-8')  # Чтение инструкции по умолчанию
```
- Если выбор корректен, читаем соответствующую инструкцию из файла.
- Если выбор некорректен, используем инструкцию по умолчанию.

#### 4.7. **Создание экземпляра класса**
```python
model: GoogleGenerativeAI = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction)
```
- Создаем экземпляр класса `GoogleGenerativeAI` с указанными параметрами.

#### 4.8. **Запрос текста у пользователя**
```python
user_text: str = input('Введите текст для баннера: ')
```
- Пользователь вводит текст для баннера.

#### 4.9. **Проверка текста**
```python
if user_text.strip() == '':
    print('Вы не ввели текст. Попробуйте снова.')
else:
    response = model.ask(user_text)
    print('\nВаш баннер готов:')
    print(response)
```
- Если текст пустой, выводим сообщение об ошибке.
- Если текст введен, отправляем его модели и выводим результат.

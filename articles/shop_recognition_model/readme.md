# Обучение модели OpenAI для классификации веб-страниц

## Введение

Обучение модели OpenAI определять, является ли страница онлайн-магазином. 

- подготовка данных, 
- токенизация текста, 
- отправка данные для обучения
- тест модели. 

## Шаг 1: Регистрация и настройка OpenAI API

Для начала работы с OpenAI API необходимо зарегистрироваться на платформе OpenAI и получить ключ API. Этот ключ будет использоваться для аутентификации при вызове методов API.

```python
import openai

# Установка ключа API
openai.api_key = 'your-api-key'
```

## Шаг 2: Подготовка данных

Для обучения модели нужно подготовить набор данных, который будет содержать примеры веб-страниц, 
как магазинов, так и не магазинов. 
Каждая запись должна включать текст страницы и соответствующую метку (`positive` для магазинов и `negative` для не магазинов).

Пример JSON-файла:

```json
[
    {
        "text": "<html><body><h1>Welcome to Our Online Store</h1><p>We offer a wide range of products at competitive prices. Visit our store today!</p></body></html>",
        "label": "positive"
    },
    {
        "text": "<html><body><h1>About Us</h1><p>We are a leading provider of quality services. Contact us for more information.</p></body></html>",
        "label": "negative"
    }
]
```

## Шаг 3: Токенизация текста

Перед отправкой данных в модель OpenAI, текст необходимо токенизировать. 
Токенизация — это процесс разбиения текста на отдельные слова или токены. 
В Python можно использовать библиотеки, такие как NLTK, spaCy или tokenizers из библиотеки transformers.

Пример токенизации с использованием NLTK:

```python
import nltk
from nltk.tokenize import word_tokenize

# Пример текста
text = "Это пример текста для токенизации."

# Токенизация текста
tokens = word_tokenize(text)
tokenized_text = ' '.join(tokens)
print(tokenized_text)
```

## Шаг 4: Отправка данных для обучения

После токенизации текста можно отправить данные для обучения модели OpenAI. 
Вот пример кода для отправки данных:

```python
import openai

def train_model(data, positive=True):
    try:
        response = openai.Train.create(
            model="text-davinci-003",
            documents=[entry["text"] for entry in data],
            labels=["positive" if positive else "negative"] * len(data),
            show_progress=True
        )
        return response.id
    except Exception as ex:
        print("An error occurred during training:", ex)
        return None

# Пример использования
data = [
    {"text": "Текст первой веб-страницы...", "label": "positive"},
    {"text": "Текст второй веб-страницы...", "label": "negative"}
]

job_id = train_model(data, positive=True)
print("Job ID:", job_id)
```

## Шаг 5: Тестирование модели

После обучения модели необходимо протестировать её на тестовом наборе данных. 
Вот пример кода для тестирования:

```python
def test_model(test_data):
    try:
        predictions = []
        for entry in test_data:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=entry["text"],
                max_tokens=1
            )
            prediction = response.choices[0].text.strip()
            predictions.append(prediction)
        return predictions
    except Exception as ex:
        print("An error occurred during testing:", ex)
        return None

# Пример использования
test_data = [
    {"text": "Текст тестовой веб-страницы...", "label": "positive"},
    {"text": "Текст другой тестовой страницы...", "label": "negative"}
]

predictions = test_model(test_data)
print("Predictions:", predictions)
```

## Шаг 6: Обработка ошибок и улучшение модели

Если модель даёт неверные предсказания, можно улучшить её, 
добавив больше данных или изменив параметры обучения. Также можно использовать обратную связь для анализа ошибок.

Пример обработки ошибок:

```python
def handle_errors(predictions, test_data):
    for pred, entry in zip(predictions, test_data):
        if pred != entry["label"]:
            print(f"Incorrect prediction for page '{entry['name']}': Predicted {pred}, Actual {entry['label']}")

# Пример использования
handle_errors(predictions, test_data)
```
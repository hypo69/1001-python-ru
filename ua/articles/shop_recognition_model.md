# Навчання моделі OpenAI для класифікації веб-сторінок

## Вступ

Навчання моделі OpenAI визначати, чи є сторінка онлайн-магазином.

- підготовка даних,
- токенізація тексту,
- надсилання даних для навчання
- тест моделі.

## Крок 1: Реєстрація та налаштування OpenAI API

Для початку роботи з OpenAI API необхідно зареєструватися на платформі OpenAI та отримати ключ API. Цей ключ буде використовуватися для автентифікації при виклику методів API.

```python
import openai

# Встановлення ключа API
openai.api_key = 'your-api-key'
```

## Крок 2: Підготовка даних

Для навчання моделі потрібно підготувати набір даних, який міститиме приклади веб-сторінок,
як магазинів, так і не магазинів.
Кожен запис повинен включати текст сторінки та відповідну мітку (`positive` для магазинів та `negative` для не магазинів).

Приклад JSON-файлу:

```json
[
    {
        "text": "<html><body><h1>Ласкаво просимо до нашого онлайн-магазину</h1><p>Ми пропонуємо широкий асортимент товарів за конкурентними цінами. Завітайте до нашого магазину сьогодні!</p></body></html>",
        "label": "positive"
    },
    {
        "text": "<html><body><h1>Про нас</h1><p>Ми є провідним постачальником якісних послуг. Зв'яжіться з нами для отримання додаткової інформації.</p></body></html>",
        "label": "negative"
    }
]
```

## Крок 3: Токенізація тексту

Перед надсиланням даних до моделі OpenAI, текст необхідно токенізувати.
Токенізація — це процес розбиття тексту на окремі слова або токени.
У Python можна використовувати бібліотеки, такі як NLTK, spaCy або tokenizers з бібліотеки transformers.

Приклад токенізації з використанням NLTK:

```python
import nltk
from nltk.tokenize import word_tokenize

# Приклад тексту
text = "Це приклад тексту для токенізації."

# Токенізація тексту
tokens = word_tokenize(text)
tokenized_text = ' '.join(tokens)
print(tokenized_text)
```

## Крок 4: Надсилання даних для навчання

Після токенізації тексту можна надіслати дані для навчання моделі OpenAI.
Ось приклад коду для надсилання даних:

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
        print("Під час навчання сталася помилка:", ex)
        return None

# Приклад використання
data = [
    {"text": "Текст першої веб-сторінки...", "label": "positive"},
    {"text": "Текст другої веб-сторінки...", "label": "negative"}
]

job_id = train_model(data, positive=True)
print("ID завдання:", job_id)
```

## Крок 5: Тестування моделі

Після навчання моделі необхідно протестувати її на тестовому наборі даних.
Ось приклад коду для тестування:

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
        print("Під час тестування сталася помилка:", ex)
        return None

# Приклад використання
test_data = [
    {"text": "Текст тестової веб-сторінки...", "label": "positive"},
    {"text": "Текст іншої тестової сторінки...", "label": "negative"}
]

predictions = test_model(test_data)
print("Прогнози:", predictions)
```

## Крок 6: Обробка помилок та покращення моделі

Якщо модель дає невірні прогнози, можна покращити її,
додавши більше даних або змінивши параметри навчання. Також можна використовувати зворотний зв'язок для аналізу помилок.

Приклад обробки помилок:

```python
def handle_errors(predictions, test_data):
    for pred, entry in zip(predictions, test_data):
        if pred != entry["label"]:
            print(f"Невірний прогноз для сторінки '{entry['name']}': Прогнозовано {pred}, Фактично {entry['label']}")

# Приклад використання
handle_errors(predictions, test_data)
```
https://habr.com/ru/articles/667008/

Отлично! Вот подробный обучающий материал на основе твоей статьи. Я превратил её в структурированное пошаговое руководство с объяснениями и советами по каждому этапу разработки самообучающегося чат-бота на Python с возможностью поиска информации в Википедии.

---

# 🧠 Самообучающийся чат-бот на Python с поиском в Wikipedia и Telegram-интеграцией

## 🎯 Цель

Научиться создавать Telegram-бота на Python, который:

* Понимает вопросы пользователя и отвечает на них с помощью простого машинного обучения.
* Умеет искать информацию в русскоязычной Википедии.
* Самообучается: может запоминать правильные ответы, которые пользователь ему подсказывает.

---

## 🧰 Шаг 1. Установка необходимых библиотек

Нам понадобятся следующие библиотеки:

* **pyTelegramBotAPI** — для взаимодействия с Telegram.
* **scikit-learn** — для машинного обучения.
* **wikipedia** — для поиска информации в Википедии.

Установите их командой:

```bash
pip install pyTelegramBotAPI wikipedia scikit-learn
```

---

## 🛠 Шаг 2. Настройка окружения

Создайте файл Python (например `bot.py`) и вставьте следующий код:

```python
import telebot, wikipedia, re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
```

### Устанавливаем язык Википедии и создаём бота

```python
wikipedia.set_lang("ru")
bot = telebot.TeleBot('ВАШ_ТОКЕН_ОТ_BOTFATHER')
```

Замените `'ВАШ_ТОКЕН_ОТ_BOTFATHER'` на ваш токен, полученный от [BotFather](https://t.me/botfather) в Telegram.

---

## ✂️ Шаг 3. Очистка текста

Бот будет работать лучше, если мы удалим лишние символы из входного текста:

```python
alphabet = ' 1234567890-йцукенгшщзхъфывапролджэячсмитьбюёqwertyuiopasdfghjklzxcvbnm?%.,()!:;'

def clean_str(r):
    r = r.lower()
    r = [c for c in r if c in alphabet]
    return ''.join(r)
```

---

## 📁 Шаг 4. Подготовка обучающих данных

Создайте файл `dialogues.txt` рядом с `bot.py`. Пример содержимого:

```
привет\здравствуйте!
как дела\хорошо.
кто ты\я Джарвис.
```

Формат: **вопрос\ответ**

---

## 🤖 Шаг 5. Обучение модели

Добавим функцию, которая загружает `dialogues.txt`, обрабатывает данные и обучает модель:

```python
def update():
    with open('dialogues.txt', encoding='utf-8') as f:
        content = f.read()

    blocks = content.strip().split('\n')
    dataset = []

    for block in blocks:
        replicas = block.split('\\')[:2]
        if len(replicas) == 2:
            pair = [clean_str(replicas[0]), clean_str(replicas[1])]
            if pair[0] and pair[1]:
                dataset.append(pair)

    X_text = [q for q, _ in dataset]
    y = [a for _, a in dataset]

    global vectorizer, clf
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(X_text)

    clf = LogisticRegression()
    clf.fit(X, y)

update()
```

---

## 💬 Шаг 6. Генерация ответов

Функция, которая будет подбирать лучший ответ по обученной модели:

```python
def get_generative_replica(text):
    text_vector = vectorizer.transform([clean_str(text)]).toarray()[0]
    return clf.predict([text_vector])[0]
```

---

## 🌐 Шаг 7. Поиск в Википедии

Бот будет использовать Википедию, если не нашёл подходящий ответ:

```python
def getwiki(s):
    try:
        page = wikipedia.page(s)
        text = page.content[:1000]
        sentences = text.split('.')[:-1]

        summary = ''
        for sentence in sentences:
            if '==' not in sentence and len(sentence.strip()) > 3:
                summary += sentence.strip() + '.'
            else:
                break

        summary = re.sub(r'\([^()]*\)', '', summary)
        summary = re.sub(r'\{[^\{\}]*\}', '', summary)
        return summary
    except Exception:
        return 'В Википедии нет информации об этом'
```

---

## 🤝 Шаг 8. Работа с пользователями

Обработка команд и сообщений от пользователей:

```python
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Здравствуйте, Сэр.")

question = ""

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global question
    command = message.text.lower()

    if command == "не так":
        bot.send_message(message.from_user.id, "а как?")
        bot.register_next_step_handler(message, wrong)
    else:
        question = command
        reply = get_generative_replica(command)
        if reply.strip() == "вики":
            bot.send_message(message.from_user.id, getwiki(command))
        else:
            bot.send_message(message.from_user.id, reply)

def wrong(message):
    correction = message.text.lower()
    with open('dialogues.txt', "a", encoding='utf-8') as f:
        f.write(f"{question}\\{correction}\n")
    bot.send_message(message.from_user.id, "Готово, я запомнил.")
    update()
```

---

## ▶️ Шаг 9. Запуск бота

В конце файла добавьте:

```python
bot.polling(none_stop=True)
```

Запустите бота:

```bash
python bot.py
```

---

## 💡 Рекомендации по улучшению

* Используйте более мощные модели, например `transformers`, для продвинутого понимания текста.
* Добавьте логирование ошибок.
* Защитите токен бота через переменные окружения (`os.environ.get(...)`).
* Поддержка нескольких языков и языкового определения.

---

## ✅ Что вы узнали

* Как создать Telegram-бота на Python.
* Как реализовать простое машинное обучение с `scikit-learn`.
* Как подключить Wikipedia и фильтровать её контент.
* Как сделать бота, который самообучается на новых данных.

---

Если нужно, я могу оформить это как PDF, HTML-руководство или пост на блог. Хочешь продолжить?

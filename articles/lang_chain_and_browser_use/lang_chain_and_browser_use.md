# LangChain и Browser-Use: Создание ИИ-агентов для работы с веб-браузером. Быстрый старт

## Введение

В этой статье я покажу, как быстро настроить и запустить ИИ-агента, который сможет искать информацию в Google и анализировать веб-страницы.

---

## 1. Что такое LangChain и Browser-Use?

**LangChain** — это фреймворк для работы с языковыми моделями (LLM), который позволяет создавать интеллектуальные агенты с инструментами для поиска информации, выполнения вычислений и взаимодействия с внешними сервисами.

**Browser-Use** — это Python-библиотека, позволяющая языковым моделям управлять веб-браузером: посещать сайты, кликать по ссылкам, заполнять формы и анализировать страницы.

Комбинируя эти две технологии, можно создать мощного интеллектуального агента для автоматизированного взаимодействия с интернетом.

---

## 2. Установка необходимых библиотек

Перед началом работы установите зависимости с помощью pip:

```bash
pip install -U langchain langchain-openai langchain-community browser-use python-dotenv serpapi google-search-results numexpr
```

---

## 3. Настройка API-ключей

Для работы с OpenAI и SerpAPI необходимо получить API-ключи. Добавьте их в файл `.env`:

### SERPAPI_API_KEY: Для чего нужен и как получить?
1. Для чего используется SERPAPI_API_KEY?

SERPAPI — это сервис, который предоставляет API для парсинга результатов поисковых систем (Google, Bing, Yahoo и других). Ключ SERPAPI_API_KEY требуется для:


2. Где получить ключ?
Регистрация на SerpAPI:

Перейдите на сайт serpapi.com.

Нажмите Sign Up и создайте аккаунт (доступна бесплатная пробная версия).

Получение ключа:

После регистрации войдите в личный кабинет.

На странице Dashboard ваш ключ будет указан в разделе API Key.
Пример: abcd1234...5678xyz.

Бесплатный тариф:

Бесплатный план дает 100 запросов/месяц (достаточно для тестирования).
Для коммерческих проектов выберите подходящий тариф (от $50/месяц).


```
OPENAI_API_KEY=ваш_openai_ключ
SERPAPI_API_KEY=ваш_serpapi_ключ
```

---

## 4. Код агента

Создайте файл `browser_agent.py` и добавьте следующий код:

```python
from langchain_openai import ChatOpenAI
from browser_use import Agent
from langchain.tools import Tool
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from dotenv import load_dotenv
import os
import asyncio
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

# 1. Настройка API ключей
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

async def main():
    # 2. Инициализация LLM
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # 3. Загрузка инструментов
    search_tool = Tool(
        name="Google Search",
        func=lambda query: f"Ищу в Google: {query}",
        description="Ищет информацию в Google."
    )

    # 4. Определение задачи
    task = """
    Найди в Google последние новости о компании OpenAI.
    Затем посети один из найденных сайтов и найди имена основателей.
    """

    # 5. Создание агента
    agent = initialize_agent(
        tools=[search_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # 6. Запуск агента
    try:
        result = await agent.arun(task)  # Асинхронный вызов агента
        print(f"Результат: {result}")
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 5. Разбор кода

1. **Импортируем библиотеки**: `langchain_openai`, `browser_use`, `dotenv`, `asyncio` и другие.
2. **Загружаем API-ключи** из `.env`.
3. **Инициализируем языковую модель (`ChatOpenAI`)**.
4. **Определяем инструмент `Google Search`**.
5. **Формулируем задачу**: найти новости об OpenAI и затем основателей компании.
6. **Создаем агента с помощью `initialize_agent`**.
7. **Запускаем агента асинхронно** (`arun(task)`).
8. **Выводим результат** или логируем ошибки.

---

## 6. Запуск агента

Запустите скрипт с помощью Python:

```bash
python browser_agent.py
```

Ожидаемый результат:

1. Агент использует инструмент поиска для получения информации о последних новостях OpenAI.
2. Посещает один из найденных веб-сайтов.
3. Извлекает имена основателей OpenAI и выводит их в консоль.

---

## 7. Улучшение агента

### **Дополнительные возможности:**

- **Интеграция с векторными базами данных**: хранение и анализ информации.
- **Добавление памяти (`Memory`)**: сохранение истории запросов.
- **Расширение списка инструментов**: работа с API других сервисов.
- **Обработка сложных цепочек действий (`Chains`)**.

### **Использование `Browser-Use` для взаимодействия с веб-страницами**

Агент может не только искать информацию, но и управлять браузером. Например, можно добавить поддержку кликов и заполнения форм.

Пример:

```python
from browser_use import Agent

browser_agent = Agent()

async def navigate_and_extract():
    await browser_agent.go_to("https://example.com")
    text = await browser_agent.extract_text()
    print(f"Текст со страницы: {text}")

asyncio.run(navigate_and_extract())
```

Этот код позволяет агенту открыть веб-страницу и извлечь текст.

---

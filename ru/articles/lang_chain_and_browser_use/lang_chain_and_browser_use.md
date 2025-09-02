## Как создать ИИ-агента для работы с веб-браузером с помощью LangChain и Browser-Use: пошаговое руководство

Это пошаговое руководство покажет вам, как создать ИИ-агента, способного искать информацию в Google и анализировать веб-страницы, используя LangChain и Browser-Use.

**Шаг 1: Установка необходимых библиотек**

Сначала нужно установить необходимые библиотеки Python. Откройте терминал или командную строку и выполните следующую команду:

```bash
pip install -U langchain langchain-openai langchain-community browser-use python-dotenv serpapi google-search-results numexpr
```

**Шаг 2: Настройка API-ключей**

Для работы с OpenAI и SerpAPI необходимы API-ключи.

* **OpenAI API Key:** Получите ваш API-ключ на сайте OpenAI (openai.com).
* **SerpAPI API Key:**  SerpAPI предоставляет API для работы с результатами поиска.  Зарегистрируйтесь на сайте serpapi.com (доступна бесплатная пробная версия), войдите в свой аккаунт и найдите свой API-ключ на странице Dashboard.

Создайте файл `.env` в той же директории, где будет находиться ваш Python-скрипт, и добавьте туда ключи в следующем формате:

```
OPENAI_API_KEY=ваш_openai_ключ
SERPAPI_API_KEY=ваш_serpapi_ключ
```

**Шаг 3: Создание Python-скрипта (browser_agent.py)**

Создайте файл `browser_agent.py` и вставьте в него следующий код:

```python
import asyncio
import logging
import os
from dotenv import load_dotenv

from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI


# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

# Загрузка API ключей из .env файла
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

async def main():
    # Инициализация языковой модели
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0) # Можете попробовать другие модели

    # Определение инструмента поиска (простой пример, без фактического поиска в Google)
    search_tool = Tool(
        name="Google Search",
        func=lambda query: f"Ищу в Google: {query}",  # Замените на реальный поиск с SerpAPI при необходимости
        description="Ищет информацию в Google."
    )


    # Определение задачи для агента
    task = """
    Найди в Google последние новости о компании OpenAI.
    Затем посети один из найденных сайтов и найди имена основателей.
    """

    # Создание агента
    agent = initialize_agent(
        tools=[search_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # Запуск агента
    try:
        result = await agent.arun(task)
        print(f"Результат: {result}")
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

**Шаг 4: Запуск агента**

Откройте терминал или командную строку, перейдите в директорию с файлом `browser_agent.py` и запустите его:

```bash
python browser_agent.py
```

**Шаг 5: Улучшение агента (расширенные возможности)**

* **Реальный поиск в Google:** Замените `lambda` функцию в `search_tool` на код, использующий SerpAPI для реального поиска в Google.  Это потребует изучения документации SerpAPI.

* **Взаимодействие с веб-страницами (Browser-Use):**  Для добавления функциональности взаимодействия с веб-страницами (открытие ссылок, извлечение текста и т.д.) потребуется использовать библиотеку `browser-use`.  Документация по этой библиотеке поможет вам добавить соответствующие инструменты к вашему агенту.

* **Использование памяти:** Для сохранения контекста между запросами можно использовать механизмы памяти LangChain.

* **Более сложные цепочки действий:** LangChain позволяет создавать более сложные цепочки действий (Chains) для решения более комплексных задач.


Этот пример демонстрирует базовую структуру.  Для реализации полноценного агента, взаимодействующего с браузером и  Google Search, потребуется дополнительная работа с SerpAPI и `browser-use`.  Не забудьте обратиться к документации этих библиотек для получения более подробной информации.

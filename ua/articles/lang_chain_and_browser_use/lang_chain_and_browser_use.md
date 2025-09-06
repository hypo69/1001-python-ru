## Як створити ІІ-агента для роботи з веб-браузером за допомогою LangChain та Browser-Use: покроковий посібник

Цей покроковий посібник покаже вам, як створити ІІ-агента, здатного шукати інформацію в Google та аналізувати веб-сторінки, використовуючи LangChain та Browser-Use.

**Крок 1: Встановлення необхідних бібліотек**

Спочатку потрібно встановити необхідні бібліотеки Python. Відкрийте термінал або командний рядок і виконайте наступну команду:

```bash
pip install -U langchain langchain-openai langchain-community browser-use python-dotenv serpapi google-search-results numexpr
```

**Крок 2: Налаштування API-ключів**

Для роботи з OpenAI та SerpAPI необхідні API-ключі.

*   **OpenAI API Key:** Отримайте ваш API-ключ на сайті OpenAI (openai.com).
*   **SerpAPI API Key:** SerpAPI надає API для роботи з результатами пошуку. Зареєструйтесь на сайті serpapi.com (доступна безкоштовна пробна версія), увійдіть у свій обліковий запис та знайдіть свій API-ключ на сторінці Dashboard.

Створіть файл `.env` у тому ж каталозі, де буде знаходитися ваш Python-скрипт, і додайте туди ключі в наступному форматі:

```
OPENAI_API_KEY=ваш_openai_ключ
SERPAPI_API_KEY=ваш_serpapi_ключ
```

**Крок 3: Створення Python-скрипта (browser_agent.py)**

Створіть файл `browser_agent.py` і вставте в нього наступний код:

```python
import asyncio
import logging
import os
from dotenv import load_dotenv

from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI


# Налаштування логування
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

# Завантаження API ключів з .env файлу
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

async def main():
    # Ініціалізація мовної моделі
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0) # Можете спробувати інші моделі

    # Визначення інструменту пошуку (простий приклад, без фактичного пошуку в Google)
    search_tool = Tool(
        name="Google Search",
        func=lambda query: f"Шукаю в Google: {query}",  # Замініть на реальний пошук з SerpAPI за потреби
        description="Шукає інформацію в Google."
    )


    # Визначення завдання для агента
    task = """
    Знайди в Google останні новини про компанію OpenAI.
    Потім відвідай один із знайдених сайтів і знайди імена засновників.
    """

    # Створення агента
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
        logging.error(f"Сталася помилка: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

**Крок 4: Запуск агента**

Відкрийте термінал або командний рядок, перейдіть до каталогу, що містить `browser_agent.py`, і запустіть його:

```bash
python browser_agent.py
```

**Крок 5: Покращення агента (розширені можливості)**

*   **Реальний пошук у Google:** Замініть функцію `lambda` в `search_tool` на код, який використовує SerpAPI для реального пошуку в Google. Це вимагатиме вивчення документації SerpAPI.

*   **Взаємодія з веб-сторінками (Browser-Use):** Щоб додати функціональність для взаємодії з веб-сторінками (відкриття посилань, вилучення тексту тощо), вам потрібно буде використовувати бібліотеку `browser-use`. Документація цієї бібліотеки допоможе вам додати відповідні інструменти до вашого агента.

*   **Використання пам'яті:** Для збереження контексту між запитами можна використовувати механізми пам'яті LangChain.

*   **Складніші ланцюжки дій:** LangChain дозволяє створювати складніші ланцюжки дій (Chains) для вирішення більш комплексних завдань.


Цей приклад демонструє базову структуру. Для реалізації повноцінного агента, що взаємодіє з браузером та Google Search, знадобиться додаткова робота з SerpAPI та `browser-use`. Не забудьте звернутися до документації цих бібліотек для отримання більш детальної інформації.

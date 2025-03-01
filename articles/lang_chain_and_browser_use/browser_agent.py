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
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")  # Замените на свой API ключ
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


async def main():
    # 2. Инициализация LLM
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # 3. Загрузка инструментов
    search_tool = Tool(
        name="Google Search",
        func=lambda query: f"Ищу в Google: {query}",
        description="Ищет информацию в Google.",
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

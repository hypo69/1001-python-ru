
## Практическое руководство по созданию ИИ-агентов с LangGraph и MCP

Эта статья — практическое руководство для разработчиков по созданию автономных ИИ-агентов на Python. Мы не будем повторять теорию о том, что такое LangChain и LangGraph. Вместо этого мы сосредоточимся на коде, архитектуре и решении реальных задач.

**Цель:** С нуля создать два проекта:
1.  **Агент-классификатор:** многошаговый, с управляемым состоянием, но без внешних инструментов.
2.  **Агент-ассистент:** полноценный агент с доступом к файловой системе и веб-поиску через протокол MCP, построенный на циклической логике.

Мы рассмотрим лучшие практики: управление конфигурацией, выбор моделей и обработку ошибок для создания надежных систем.

### Кратко о концепции: Агент и мост MCP

Прежде чем перейти к коду, зафиксируем два понятия:
*   **ИИ-агент:** это программа, построенная вокруг цикла «рассуждение-действие». Она получает задачу, с помощью LLM решает, что делать дальше (например, вызвать инструмент), выполняет действие и повторяет цикл, пока задача не будет решена.
*   **MCP (Model Context Protocol):** это стандарт, который служит **мостом** между логикой агента и внешними инструментами. Он позволяет агенту унифицированно работать с файлами, API или поиском, не заботясь о деталях их реализации.

### Часть 1: Настройка надежного окружения

#### Шаг 1: Виртуальное окружение и зависимости

Создайте и активируйте виртуальное окружение. Затем создайте файл `requirements.txt`:
```
# Основные фреймворки
langchain
langgraph

# Адаптеры для моделей
langchain-openai
langchain-google-genai
langchain-mistralai
langchain-community # Для Ollama

# Инструменты и протоколы
langchain-mcp-adapters
mcp
ollama

# Вспомогательные
python-dotenv
tenacity # Для надежной обработки ошибок
```
Установите зависимости:
```bash
pip install -r requirements.txt```

#### Шаг 2: Конфигурация API-ключей

Создайте файл `.env` для хранения ключей:
```
OPENAI_API_KEY="sk-..."
GOOGLE_API_KEY="AIzaSy..."
MISTRAL_API_KEY="..."
BRAVE_API_KEY="..." # Для инструмента веб-поиска через MCP
```

#### Шаг 3: Паттерн «Фабрика моделей»

Чтобы гибко переключаться между облачными и локальными моделями, не меняя код агента, используем паттерн «фабрика».

```python
# llm_factory.py
import os
from enum import Enum
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai import ChatMistralAI
from langchain_community.chat_models import ChatOllama

load_dotenv()

class ModelProvider(Enum):
    OPENAI = "openai"
    GEMINI = "gemini"
    MISTRAL_API = "mistral_api"
    OLLAMA = "ollama"

def get_llm(provider: ModelProvider, model_name: str = None):
    """Фабрика для создания экземпляров LLM."""
    if provider == ModelProvider.OPENAI:
        return ChatOpenAI(model=model_name or "gpt-4o-mini", temperature=0)
    elif provider == ModelProvider.GEMINI:
        return ChatGoogleGenerativeAI(model=model_name or "gemini-1.5-flash", temperature=0)
    elif provider == ModelProvider.MISTRAL_API:
        return ChatMistralAI(model=model_name or "mistral-large-latest", temperature=0)
    elif provider == ModelProvider.OLLAMA:
        # Убедитесь, что у вас запущена Ollama с нужной моделью
        # docker exec -it ollama ollama pull mistral
        return ChatOllama(model=model_name or "mistral", temperature=0)
    raise ValueError(f"Неизвестный провайдер модели: {provider}")

# Пример использования
if __name__ == "__main__":
    # local_llm = get_llm(ModelProvider.OLLAMA)
    openai_llm = get_llm(ModelProvider.OPENAI)
    response = openai_llm.invoke("Объясни концепцию RAG в трех предложениях.")
    print(response.content)
```

### Часть 2: Проект 1 — Агент для классификации вакансий

Этот агент демонстрирует, как использовать LangGraph для создания **линейного графа** с управляемым состоянием. Он будет принимать описание вакансии и последовательно классифицировать его по трём параметрам.

#### Шаг 1: Определение состояния

Состояние — это «память» нашего графа, которая передается от узла к узлу.
```python
# vacancy_classifier.py
from typing import TypedDict, Dict

class ClassificationState(TypedDict):
    """Состояние агента-классификатора."""
    description: str          # Исходный текст
    job_type: str             # Тип работы (проектная/постоянная)
    category: str             # Профессия
    search_type: str          # Цель (ищу работу/исполнителя)
    classification_log: list  # Лог для отладки
```

#### Шаг 2: Реализация узлов графа

Каждый узел — это функция, которая принимает состояние, выполняет свою часть работы и возвращает обновленное состояние.

```python
import asyncio
import json
from langchain_core.prompts import ChatPromptTemplate
from llm_factory import get_llm, ModelProvider

class VacancyClassifierAgent:
    def __init__(self):
        self.llm = get_llm(ModelProvider.OPENAI, model_name="gpt-4o-mini")

    async def _classify_job_type(self, state: ClassificationState) -> ClassificationState:
        """Узел 1: Определяет тип работы."""
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Определи тип работы. Ответ должен быть 'проектная' или 'постоянная'."),
            ("human", "Текст вакансии:\n\n{description}")
        ])
        chain = prompt | self.llm
        result = await chain.ainvoke({"description": state["description"]})
        
        state["job_type"] = result.content.strip()
        state["classification_log"].append("Определен тип работы.")
        return state

    async def _classify_category(self, state: ClassificationState) -> ClassificationState:
        """Узел 2: Определяет категорию профессии."""
        # Категории можно загрузить из файла или базы данных
        categories = ["Python-разработчик", "Дизайнер", "Маркетолог", "3D-аниматор"]
        prompt = ChatPromptTemplate.from_messages([
            ("system", f"Выбери наиболее подходящую категорию из списка: {', '.join(categories)}."),
            ("human", "Текст вакансии:\n\n{description}")
        ])
        chain = prompt | self.llm
        result = await chain.ainvoke({"description": state["description"]})
        
        state["category"] = result.content.strip()
        state["classification_log"].append("Определена категория.")
        return state

    async def _classify_search_type(self, state: ClassificationState) -> ClassificationState:
        """Узел 3: Определяет цель поиска."""
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Определи цель автора. Ответ должен быть 'поиск работы' или 'поиск исполнителя'."),
            ("human", "Текст вакансии:\n\n{description}")
        ])
        chain = prompt | self.llm
        result = await chain.ainvoke({"description": state["description"]})
        
        state["search_type"] = result.content.strip()
        state["classification_log"].append("Определена цель поиска.")
        return state
```

#### Шаг 3: Сборка и запуск графа

Собираем узлы в единый рабочий процесс.

```python
# ... продолжение класса VacancyClassifierAgent ...
from langgraph.graph import StateGraph, END

    def build_graph(self):
        """Собирает граф состояний."""
        workflow = StateGraph(ClassificationState)
        
        workflow.add_node("job_type_classifier", self._classify_job_type)
        workflow.add_node("category_classifier", self._classify_category)
        workflow.add_node("search_type_classifier", self._classify_search_type)
        
        workflow.set_entry_point("job_type_classifier")
        workflow.add_edge("job_type_classifier", "category_classifier")
        workflow.add_edge("category_classifier", "search_type_classifier")
        workflow.add_edge("search_type_classifier", END)
        
        return workflow.compile()

async def main():
    agent = VacancyClassifierAgent()
    graph = agent.build_graph()
    
    description = "Ищем опытного Python-разработчика в команду на фултайм для работы над проектом в сфере финтех."
    
    initial_state = ClassificationState(
        description=description,
        job_type="", category="", search_type="",
        classification_log=[]
    )
    
    final_state = await graph.ainvoke(initial_state)
    
    print("--- Результат классификации ---")
    print(json.dumps(final_state, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    asyncio.run(main())
```

### Часть 3: Проект 2 — Агент-ассистент с инструментами (MCP)

Этот агент демонстрирует **циклическую логику**, где он может многократно обращаться к инструментам для решения задачи.

#### Шаг 1: Управление конфигурацией

Для агентов, взаимодействующих с внешним миром, важна надежная конфигурация.

```python
# mcp_agent_config.py
from dataclasses import dataclass, field
import os
from llm_factory import ModelProvider

@dataclass
class AgentConfig:
    workdir: str = "./agent_workdir"
    model_provider: ModelProvider = ModelProvider.OLLAMA
    
    def __post_init__(self):
        """Валидация после инициализации."""
        os.makedirs(self.workdir, exist_ok=True)
```

#### Шаг 2: Определение состояния для диалога

Состояние теперь будет хранить историю сообщений.

```python
# mcp_agent.py
from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage
import operator

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
```

#### Шаг 3: Реализация циклического графа

Граф будет состоять из двух основных узлов и условного перехода, который создает цикл «рассуждение-действие».

```python
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolExecutor
from langchain_mcp_adapters.langchain import V1ToolExecutor
from langchain_mcp_adapters.clients import MultiServerMCPClient
from llm_factory import get_llm
from mcp_agent_config import AgentConfig

class MCPAgent:
    def __init__(self, config: AgentConfig):
        self.config = config
        self.llm = get_llm(config.model_provider)
        self.tools = []
        self.tool_executor = None

    async def setup_tools(self):
        """Инициализация инструментов через MCP."""
        mcp_config = {
            "filesystem": {
                "command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", self.config.workdir],
                "transport": "stdio"
            },
            # Добавьте brave-search, если есть ключ BRAVE_API_KEY
        }
        mcp_client = MultiServerMCPClient(mcp_config)
        self.tools = await mcp_client.get_tools()
        self.tool_executor = ToolExecutor([V1ToolExecutor(tool) for tool in self.tools])
        
        # Привязываем инструменты к модели
        self.llm = self.llm.bind_tools(self.tools)

    def _should_continue(self, state: AgentState):
        """Условный переход: решаем, нужно ли вызывать инструмент."""
        last_message = state['messages'][-1]
        if not last_message.tool_calls:
            return "end"
        return "continue"

    def _call_model(self, state: AgentState):
        """Узел 1: Вызов LLM для принятия решения."""
        response = self.llm.invoke(state['messages'])
        return {"messages": [response]}

    def _call_tool(self, state: AgentState):
        """Узел 2: Выполнение вызова инструмента."""
        last_message = state['messages'][-1]
        tool_call = last_message.tool_calls[0]
        
        action = {"tool": tool_call["name"], "tool_input": tool_call["args"], "log": ""}
        response = self.tool_executor.invoke(action)
        
        return {"messages": [response]}

    def build_graph(self):
        workflow = StateGraph(AgentState)
        workflow.add_node("agent", self._call_model)
        workflow.add_node("action", self._call_tool)
        
        workflow.set_entry_point("agent")
        workflow.add_conditional_edges(
            "agent",
            self._should_continue,
            {"continue": "action", "end": END}
        )
        workflow.add_edge("action", "agent")
        
        return workflow.compile()
```

#### Шаг 4: Запуск и взаимодействие

```python
# ... продолжение mcp_agent.py ...
import asyncio
from langchain_core.messages import HumanMessage
from tenacity import retry, stop_after_attempt, wait_fixed

@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
async def run_agent_task(graph, task):
    """Запускает задачу с обработкой ошибок."""
    return await graph.ainvoke({"messages": [HumanMessage(content=task)]})

async def main():
    config = AgentConfig(model_provider=ModelProvider.OPENAI) # или OLLAMA
    agent = MCPAgent(config)
    await agent.setup_tools()
    graph = agent.build_graph()
    
    task = "Создай файл 'hello.txt' в рабочей директории и запиши в него 'Привет, мир!'."
    result = await run_agent_task(graph, task)
    
    print("\n--- Финальный ответ агента ---")
    print(result['messages'][-1].content)

if __name__ == "__main__":
    asyncio.run(main())
```
Здесь мы добавили декоратор `tenacity` для надежности — если вызов агента упадет из-за временной сетевой ошибки, он автоматически повторится.

### Заключение

Мы создали два типа агентов, используя современные практики:
*   **Линейный граф** отлично подходит для задач с четкой последовательностью шагов, таких как ETL-процессы или многоэтапный анализ.
*   **Циклический граф** является основой для создания интерактивных ассистентов и автономных агентов, способных решать сложные задачи с помощью инструментов.

Представленные архитектурные паттерны — фабрика моделей, управление конфигурацией, разделение логики на узлы и использование графов состояний — являются фундаментом для построения масштабируемых и надежных ИИ-систем.

Начав с простых примеров, вы можете постепенно наращивать сложность, создавая все более интеллектуальные и автономные системы для решения ваших уникальных задач.
![habr](https://habr.com/ru/companies/amvera/articles/929568/)





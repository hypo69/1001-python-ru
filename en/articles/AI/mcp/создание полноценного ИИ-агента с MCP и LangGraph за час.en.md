<!-- Translated to en -->
# How to teach a neural network to work with its hands: creating a full-fledged AI agent with MCP and LangGraph in an hour


Friends, greetings! I hope you've missed me.

Over the past couple of months, I've been deeply immersed in researching the integration of AI agents into my own Python projects. In the process, I've accumulated a lot of practical knowledge and observations that it would be a sin not to share. So today, I'm returning to Habr — with a new topic, a fresh perspective, and with the intention of writing more often.

On the agenda are LangGraph and MCP: tools with which you can create truly useful AI agents.

If before we argued about which neural network answers best in Russian, today the battlefield has shifted towards more practical tasks: who performs better as an AI agent? Which frameworks truly simplify development? And how to integrate all this good stuff into a real project?

But before diving into practice and code, let's understand the basic concepts. Especially the two key ones: **AI agents and MCP**. Without them, the conversation about LangGraph will be incomplete.

### AI agents in simple terms

AI agents are not just "pumped-up" chatbots. They represent more complex, autonomous entities that possess two crucial features:

1.  **Ability to interact and coordinate**

    Modern agents can break down tasks into subtasks, call other agents, request external data, work in a team. This is no longer a single assistant, but a distributed system where each component can contribute.

2.  **Access to external resources**

    An AI agent is no longer limited by the confines of a dialogue. It can access databases, make API calls, interact with local files, vector knowledge bases, and even run commands in the terminal. All this became possible thanks to the emergence of MCP — a new level of integration between the model and the environment.

---

Simply put: **MCP is a bridge between a neural network and its environment**. It allows the model to "understand" the context of the task, access data, make calls, and form reasoned actions, rather than just producing text responses.

**Let's imagine an analogy:**

*   You have a **neural network** — it can reason and generate texts.
*   There is **data and tools** — documents, APIs, knowledge bases, terminal, code.
*   And there is **MCP** — it is an interface that allows the model to interact with these external sources as if they were part of its inner world.

**Without MCP:**

The model is an isolated dialogue engine. You give it text — it responds. And that's it.

**With MCP:**

The model becomes a full-fledged **task executor**:

*   gains access to data structures and APIs;
*   calls external functions;
*   navigates the current state of the project or application;
*   can remember, track, and change context during a dialogue;
*   uses extensions such as search tools, code runners, vector embedding databases, etc.

In a technical sense, **MCP is a protocol for interaction between an LLM and its environment**, where context is provided as structured objects (instead of "raw" text), and calls are formatted as interactive operations (e.g., function calling, tool usage, or agent actions). This is what turns an ordinary model into a **real AI agent**, capable of doing more than just "talking."

### Now — to business!

Now that we've covered the basic concepts, it's logical to ask: "How do we implement all this in practice in Python?"

This is where **LangGraph** comes into play — a powerful framework for building state graphs, agent behavior, and thought chains. It allows you to "wire" the logic of interaction between agents, tools, and the user, creating a living AI architecture that adapts to tasks.

In the following sections, we will look at how to:

*   build an agent from scratch;
*   create states, transitions, and events;
*   integrate functions and tools;
*   and how this entire ecosystem works in a real project.

### A little theory: what is LangGraph

Before we get to practice, a few words about the framework itself.

**LangGraph** — is a project from the **LangChain** team, the same ones who first proposed the concept of "chains" (chains) of interaction with LLMs. If before the main emphasis was on linear or conditionally branching pipelines (langchain.chains), then now developers are betting on a **graph model**, and LangGraph is what they recommend as the new "core" for building complex AI systems.

**LangGraph** — is a framework for building finite state machines and state graphs, where each **node** represents a part of the agent's logic: a model call, an external tool, a condition, user input, etc.

### How it works: graphs and nodes

Conceptually, LangGraph is built on the following ideas:

*   **Graph** — is a structure that describes possible paths for logic execution. You can think of it as a map: from one point, you can move to another depending on conditions or the result of execution.
*   **Nodes** — are specific steps within the graph. Each node performs some function: calls a model, calls an external API, checks a condition, or simply updates the internal state.
*   **Transitions between nodes** — is the routing logic: if the result of the previous step is such and such, then go there.
*   **State** — is passed between nodes and accumulates everything needed: history, intermediate conclusions, user input, the result of tool operation, etc.

Thus, we get a **flexible mechanism for managing agent logic**, in which both simple and very complex scenarios can be described: loops, conditions, parallel actions, nested calls, and much more.

### Why is it convenient?

LangGraph allows you to build **transparent, reproducible, and extensible logic**:

*   easy to debug;
*   easy to visualize;
*   easy to scale for new tasks;
*   easy to integrate external tools and MCP protocols.

In essence, LangGraph is the **"brain" of the agent**, where each step is documented, controlled, and can be changed without chaos and "magic."

### But now — enough theory!

We could talk for a long time about graphs, states, logic composition, and the advantages of LangGraph over classic pipelines. But, as practice shows, it's better to see it once in code.

**It's time to move on to practice.** Next — a Python example: we will create a simple but useful AI agent based on LangGraph, which will use external tools, memory, and make decisions itself.

### Preparation: cloud and local neural networks

In order to start creating AI agents, we first need a **brain** — a language model. There are two approaches here:

*   **use cloud solutions**, where everything is ready "out of the box";
*   or **raise the model locally** — for complete autonomy and confidentiality.

Let's consider both options.

#### Cloud services: fast and convenient

The easiest way is to use the power of large providers: OpenAI, Anthropic, and use...

### Where to get keys and tokens:

*   **OpenAI** — ChatGPT and other products;
*   **Anthropic** — Claude;
*   **OpenRouter.ai** — dozens of models (one token — many models via OpenAI-compatible API);
*   **Amvera Cloud** — the ability to connect LLAMA with ruble payment and built-in proxying to OpenAI and Anthropic.

This path is convenient, especially if you:

*   do not want to configure the infrastructure;
*   develop with an emphasis on speed;
*   work with limited resources.

### Local models: full control

If **privacy, offline work** is important to you, or you want to build **fully autonomous agents**, then it makes sense to deploy the neural network locally.

**Main advantages:**

*   **Confidentiality** — data remains with you;
*   **Offline work** — useful in isolated networks;
*   **No subscriptions and tokens** — free after setup.

**Disadvantages are obvious:**

*   Resource requirements (especially video memory);
*   Setup can take time;
*   Some models are difficult to deploy without experience.

Nevertheless, there are tools that make local launch easier. One of the best today is **Ollama**.

### Deploying local LLM via Ollama + Docker

We will prepare a local launch of the Qwen 2.5 (qwen2.5:32b) model using a Docker container and the Ollama system. This will allow us to integrate the neural network with MCP and use it in our own agents based on LangGraph.

If the computing resources of your computer or server are insufficient to work with this version of the model, you can always choose a less "resource-hungry" neural network — the installation and launch process will remain similar.

**Quick installation (summary of steps)**

1.  **Install Docker + Docker Compose**
2.  **Create project structure:**
```bash
mkdir qwen-local && cd qwen-local
```
3.  **Create `docker-compose.yml`**
(universal option, GPU is determined automatically)

```yaml
services:
  ollama:
    image: ollama/ollama:latest
    container_name: ollama_qwen
    ports:
      - "11434:11434"
    volumes:
      - ./ollama_data:/root/.ollama
      - /tmp:/tmp
    environment:
      - OLLAMA_HOST=0.0.0.0
      - OLLAMA_ORIGINS=*
    restart: unless-stopped
```

4.  **Start container:**
```bash
docker compose up -d
```

5.  **Download model:**
```bash
docker exec -it ollama_qwen ollama pull qwen2.5:32b
```

6.  **Check operation via API:**
```bash
curl http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{"model": "qwen2.5:32b", "prompt": "Hello!", "stream": false}'
```
*(Image with curl command execution result)*

7.  **Integration with Python:**
```python
import requests

def query(prompt):
    res = requests.post("http://localhost:11434/api/generate", json={"model": "qwen2.5:32b", "prompt": prompt, "stream": False})
    return res.json()['response']

print(query("Explain quantum entanglement"))
```
Now you have a full-fledged local LLM, ready to work with MCP and LangGraph.

**What's next?**

We have a choice between cloud and local models, and we have learned how to connect both. The most interesting part is ahead — **creating AI agents on LangGraph**, which use the selected model, memory, tools, and their own logic.

**Let's move on to the most delicious part — code and practice!**

---

Before moving on to practice, it is important to prepare the working environment. I assume that you are already familiar with the basics of Python, know what libraries and dependencies are, and understand why to use a virtual environment.

If all this is new to you — I recommend first taking a short course or guide on Python basics, and then returning to the article.

#### Step 1: Creating a virtual environment

Create a new virtual environment in the project folder:
```bash
python -m venv venv
source venv/bin/activate  # for Linux/macOS
venc\Scripts\activate   # for Windows
```

#### Step 2: Installing dependencies

Create a `requirements.txt` file and add the following lines to it:
```
langchain==0.3.26
langchain-core==0.3.69
langchain-deepseek==0.1.3
langchain-mcp-adapters==0.1.9
langchain-ollama==0.3.5
langchain-openai==0.3.28
langgraph==0.5.3
langgraph-checkpoint==2.1.1
langgraph-prebuilt==0.5.2
langgraph-sdk==0.1.73
langsmith==0.4.8
mcp==1.12.0
ollama==0.5.1
openai==1.97.0
```

> ⚠️ **Current versions are indicated as of July 21, 2025.** Since publication, they may have changed — **check for relevance before installation.**

Then install the dependencies:
```bash
pip install -r requirements.txt```

#### Step 3: Configuring environment variables

Create a `.env` file in the project root and add the necessary API keys to it:
```
OPENAI_API_KEY=sk-proj-1234
DEEPSEEK_API_KEY=sk-123
OPENROUTER_API_KEY=sk-or-v1-123
BRAVE_API_KEY=BSAj123K1bvBGpH1344tLwc
```

**Purpose of variables:**

*   **OPENAI_API_KEY** — key for accessing GPT models from OpenAI;
*   **DEEPSEEK_API_KEY** — key for using Deepseek models;
*   **OPENROUTER_API_KEY** — single key for accessing many models via OpenRouter

---

Some MCP tools (e.g., `brave-web-search`) require a key to work. Without it, they simply won't activate.

**What if you don't have API keys?**

No problem. You can start development with a local model (e.g., via Ollama), without connecting any external services. In this case, the `.env` file can be omitted entirely.

Done! Now we have everything we need to get started — an isolated environment, dependencies, and, if necessary, access to cloud neural networks and MCP integrations.

Next - we will launch our LLM agent in different ways.

### Simple launch of LLM agents via LangGraph: basic integration

Let's start with the simplest: how to "connect the brain" to the future agent. We will analyze the basic ways to launch language models (LLM) with LangChain, so that in the next step we can move on to integration with LangGraph and building a full-fledged AI agent.

#### Imports
```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_deepseek import ChatDeepSeek
```
*   `os` and `load_dotenv()` — for loading variables from the `.env` file.
*   `ChatOpenAI`, `ChatOllama`, `ChatDeepSeek` — wrappers for connecting language models via LangChain.

> 💡 If you use alternative approaches to working with configurations (e.g., Pydantic Settings), you can replace `load_dotenv()` with your usual method.

#### Loading environment variables
```python
load_dotenv()
```
This will load all variables from `.env`, including keys for accessing OpenAI, DeepSeek, OpenRouter and other APIs.

#### Simple functions for getting LLM

**OpenAI**
```python
def get_openai_llm():
    return ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
```
If the `OPENAI_API_KEY` variable is correctly set, LangChain will substitute it automatically — explicit specification of `api_key=...` is optional here.

**DeepSeek**
```python
def get_deepseek_llm():
    # ...
```
Similarly, but we use the `ChatDeepSeek` wrapper.

**OpenRouter (and other compatible APIs)**
```python
def get_openrouter_llm(model="moonshotai/kimi-k2:free"):
    return ChatOpenAI(
        model=model,
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        temperature=0
    )
```
**Features:**

*   `ChatOpenAI` is used, even though the model is not from OpenAI — because OpenRouter uses the same protocol.
*   `base_url` is required: it points to the OpenRouter API.
*   The `moonshotai/kimi-k2:free` model was chosen as one of the most balanced options in terms of quality and speed at the time of writing.
*   The `OpenRouter` API key must be passed explicitly — automatic substitution does not work here.

#### Mini-test: checking model operation
```python
if __name__ == "__main__":
    llm = get_openrouter_llm(model="moonshotai/kimi-k2:free")
    response = llm.invoke("Who are you?")
    print(response.content)
```
*(Изображение с результатом выполнения: `Я - ИИ-ассистент, созданный компанией Moonshot AI...`)*

If everything is configured correctly, you will receive a meaningful response from the model. Congratulations — the first step is done!

### But this is not yet an agent

At this stage, we have connected the LLM and made a simple call. This is more like a console chatbot than an AI agent.

**Why?**

*   We are writing **synchronous, linear code** without state logic or goals.
*   Агент не принимает решений, не запоминает контекст и не использует инструменты.
*   МСР и LangGraph пока не задействованы.

**What's next?**

Далее мы реализуем **полноценного ИИ-агента** с использованием **LangGraph** — сначала без МСР, чтобы сфокусироваться на архитектуре, состояниях и логике самого агента.

Погружаемся в настоящую агентную механику. Поехали!

### Агент классификации вакансий: от теории к практике

...концепции LangGraph на практике и создать полезный инструмент для HR-платформ и бирж фриланса.

#### Задача агента

Наш агент принимает на вход текстовое описание вакансии или услуги и выполняет трёхуровневую классификацию:

1.  **Тип работы**: проектная работа или постоянная вакансия
2.  **Категория профессии**: из 45+ предопределённых специальностей
3.  **Тип поиска**: ищет ли человек работу или ищет исполнителя

Результат возвращается в структурированном JSON-формате с оценкой уверенности для каждой классификации.

#### 📈 Архитектура агента на LangGraph

Следуя принципам LangGraph, создаём **граф состояний** из четырёх узлов:

- Входное описание
- ↓
- Узел классификации типа работы
- ↓
- Узел классификации категории
- ↓
- Узел определения типа поиска
- ↓
- Узел расчёта уверенности
- ↓
- JSON-результат

Каждый узел — это **специализированная функция**, которая:

*   Получает текущее состояние агента
*   Выполняет свою часть анализа
*   Обновляет состояние и передаёт его дальше

#### Управление состоянием

Определяем **структуру памяти агента** через `TypedDict`:

```python
from typing import TypedDict, Dict

class State(TypedDict):
    """Состояние агента для хранения информации о процессе классификации"""
    description: str
    job_type: str
    category: str
    search_type: str
    confidence_scores: Dict[str, float]
    processed: bool
```

Это **рабочая память агента** — всё, что он помнит и накапливает в процессе анализа. Подобно тому, как человек-эксперт держит в уме контекст задачи при анализе документа.

Давайте рассмотрим полный код, а после сконцентрируемся на основных моментах.

```python
import asyncio
import json
from enum import Enum
from typing import TypedDict, Dict, Any, List

from langgraph.graph import StateGraph, END
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# Категории профессий
CATEGORIES = [
    "2D-аниматор", "3D-аниматор", "3D-моделлер",
    "Бизнес-аналитик", "Блокчейн-разработчик", ...
]

class JobType(Enum):
    PROJECT = "проектная работа"
    PERMANENT = "постоянная работа"

class SearchType(Enum):
    LOOKING_FOR_WORK = "поиск работы"
    LOOKING_FOR_PERFORMER = "поиск исполнителя"

class State(TypedDict):
    """Состояние агента для хранения информации о процессе классификации"""
    description: str
    job_type: str
    category: str
    search_type: str
    confidence_scores: Dict[str, float]
    processed: bool

class VacancyClassificationAgent:
    """Асинхронный агент для классификации вакансий и услуг"""

    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.1):
        """Инициализация агента"""
        self.llm = ChatOpenAI(model=model_name, temperature=temperature)
        self.workflow = self._create_workflow()

    def _create_workflow(self) -> StateGraph:
        """Создает рабочий процесс агента на основе LangGraph"""
        workflow = StateGraph(State)
        
        # Добавляем узлы в граф
        workflow.add_node("job_type_classification", self._classify_job_type)
        workflow.add_node("category_classification", self._classify_category)
        workflow.add_node("search_type_classification", self._classify_search_type)
        workflow.add_node("confidence_calculation", self._calculate_confidence)
        
        # Определяем последовательность выполнения узлов
        workflow.set_entry_point("job_type_classification")
        workflow.add_edge("job_type_classification", "category_classification")
        workflow.add_edge("category_classification", "search_type_classification")
        workflow.add_edge("search_type_classification", "confidence_calculation")
        workflow.add_edge("confidence_calculation", END)
        
        return workflow.compile()

    async def _classify_job_type(self, state: State) -> Dict[str, Any]:
        """Узел для определения типа работы: проектная или постоянная"""
        # ... (implementation follows)
        
    async def _classify_category(self, state: State) -> Dict[str, Any]:
        """Узел для определения категории профессии"""
        # ... (implementation follows)
        
    async def _classify_search_type(self, state: State) -> Dict[str, Any]:
        """Узел для определения типа поиска"""
        # ... (implementation follows)

    async def _calculate_confidence(self, state: State) -> Dict[str, Any]:
        """Узел для расчета уровня уверенности в классификации"""
        # ... (implementation follows)

    def _find_closest_category(self, predicted_category: str) -> str:
        """Находит наиболее похожую категорию из списка доступных"""
        # ... (implementation follows)

    async def classify(self, description: str) -> Dict[str, Any]:
        """Основной метод для классификации вакансии/услуги"""
        initial_state = {
            "description": description,
            "job_type": "",
            "category": "",
            "search_type": "",
            "confidence_scores": {},
            "processed": False
        }
        
        # Запускаем рабочий процесс
        result = await self.workflow.ainvoke(initial_state)
        
        # Формируем итоговый ответ в формате JSON
        classification_result = {
            "job_type": result["job_type"],
            "category": result["category"],
            "search_type": result["search_type"],
            "confidence_scores": result["confidence_scores"],
            "success": result["processed"]
        }
        return classification_result

async def main():
    """Демонстрация работы агента"""
    agent = VacancyClassificationAgent()
    
    test_cases = [
        "Требуется Python разработчик для создания веб-приложения на Django. Постоянная работа.",
        "Ищу заказы на создание логотипов и фирменного стиля. Работаю в Adobe Illustrator.",
        "Нужен 3D-аниматор для краткосрочного проекта создания рекламного ролика.",
        "Резюме: опытный маркетолог, ищу удаленную работу в сфере digital-маркетинга",
        "Ищем фронтенд-разработчика React в нашу команду на постоянную основе"
    ]
    
    print("🤖 Демонстрация работы агента классификации вакансий\n")
    for i, description in enumerate(test_cases, 1):
        print(f"--- Тест {i}: ---")
        print(f"Описание: {description}")
        try:
            result = await agent.classify(description)
            print("Результат классификации:")
            print(json.dumps(result, ensure_ascii=False, indent=2))
        except Exception as e:
            print(f"❌ Ошибка: {e}")
        print("-" * 80)

if __name__ == "__main__":
    asyncio.run(main())

```
*(...остальная часть кода с реализацией методов была представлена в статье...)*

### Ключевые преимущества архитектуры
1.  **Модульность** — каждый узел решает одну задачу, легко тестировать и улучшать отдельно
2.  **Расширяемость** — можно добавлять новые узлы анализа без изменения существующих
3.  **Прозрачность** — весь процесс принятия решений документирован и отслеживаем
4.  **Производительность** — асинхронная обработка множественных запросов
5.  **Надёжность** — fallback-механизмы и обработка ошибок

### Реальная польза
Такой агент может использоваться в:
*   **HR-платформах** для автоматической категоризации резюме и вакансий
*   **Биржах фриланса** для улучшения поиска и рекомендаций
*   **Внутренних системах** компаний для обработки заявок и проектов
*   **Аналитических решениях** для исследования рынка труда

### МСР в действии: создаём агента с файловой системой и веб-поиском
После того как мы разобрались с базовыми принципами LangGraph и создали простого агента-классификатора, давайте расширим его возможности, подключив к внешним পরমাণ через МСР.

Сейчас мы создадим полноценного ИИ-помощника, который сможет:
*   Работать с файловой системой (читать, создавать, изменять файлы)
*   Искать актуальную информацию в интернете
*   Запоминать контекст диалога
*   Обрабатывать ошибки и восстанавливаться после сбоев

#### От теории к реальным инструментам
Помните, как в начале статьи мы говорили о том, что **МСР — это мост между нейросетью и её окружением**? Сейчас вы увидите это на практике. Наш агент получит доступ к **реальным инструментам**:
```
# Инструменты файловой системы
- read_file — чтение файлов
- write_file — запись и создание файлов
- list_directory — просмотр содержимого папок
- create_directory — создание папок

# Инструменты веб-поиска
- brave_web_search — поиск в интернете
- get_web_content — получение содержимого страниц
```
Это уже не «игрушечный» агент — это **рабочий инструмент**, который может решать реальные задачи.

#### 📈 Архитектура: от простого к сложному

**1. Конфигурация как основа стабильности**
```python
from dataclasses import dataclass

@dataclass
class AgentConfig:
    """Упрощенная конфигурация АІ-агента"""
    filesystem_path: str = "/path/to/work/directory"
    model_provider: ModelProvider = ModelProvider.OLLAMA
    use_memory: bool = True
    enable_web_search: bool = True

    def validate(self) -> None:
        """Валидация конфигурации"""
        if not os.path.exists(self.filesystem_path):
            raise ValueError(f"Путь не существует: {self.filesystem_path}")
```
**Почему это важно?** В отличие от примера с классификацией, здесь агент взаимодействует с внешними системами. Одна ошибка в пути к файлам или отсутствующий АРІ-ключ — и весь агент перестаёт работать. **Валидация на старте** экономит часы отладки.

**2. Фабрика моделей: гибкость выбора**
```python
def create_model(config: AgentConfig):
    """Создает модель согласно конфигурации"""
    provider = config.model_provider.value
    if provider == "ollama":
        return ChatOllama(model="qwen2.5:32b", base_url="http://localhost:11434")
    elif provider == "openai":
        return ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
    # ... другие провайдеры
```
Один код — множество моделей. Хотите бесплатную локальную модель? Используйте Ollama. Нужна максимальная точность? Переключитесь на GPT-4. Важна скорость? Попробуйте DeepSeek. Код остаётся тем же.

**3. МСР-интеграция: подключение к реальному миру**
```python
async def _init_mcp_client(self):
    """Инициализация МСР клиента"""
    mcp_config = {
        "filesystem": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-filesystem", self.filesystem_path],
            "transport": "stdio"
        },
        "brave-search": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-brave-search@latest"],
            "transport": "stdio",
            "env": {"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")}
        }
    }
    self.mcp_client = MultiServerMCPClient(mcp_config)
    self.tools = await self.mcp_client.get_tools()
```
Здесь происходит ключевая работа МСР: мы подключаем к агенту внешние МСР-серверы, которые предоставляют набор инструментов и функций. Агент при этом получает не просто отдельные функции, а полноценное контекстное понимание того, как работать с файловой системой и интернетом.

#### Устойчивость к ошибкам
В реальном мире всё ломается: сеть недоступна, файлы заблокированы, АРІ-ключи просрочены. Наш агент готов к этому:
```python
@retry_on_failure(max_retries=2, delay=1.0)
async def process_message(self, user_input: str, thread_id: str = "default") -> str:
    # ...
```
Декоратор `@retry_on_failure` автоматически повторяет операции при временных сбоях. Пользователь даже не заметит, что что-то пошло не так.

### Итоги: от теории к практике ИИ-агентов

Сегодня мы прошли путь от базовых концепций до создания работающих ИИ-агентов. Давайте подведём итоги того, что мы изучили и чего достигли.

**Что мы освоили**

**1. Фундаментальные концепции**
*   Разобрались с различием между чат-ботами и настоящими ИИ-агентами
*   Поняли роль **МСР (Model Context Protocol)** как моста между моделью и внешним миром
*   Изучили архитектуру **LangGraph** для построения сложной логики агентов

**2. Практические навыки**
*   Настроили рабочее окружение с поддержкой облачных и локальных моделей
*   Создали **агента-классификатора** с асинхронной архитектурой и управлением состояниями
*   Построили **МСР-агента** с доступом к файловой системе и веб-поиску

**3. Архитектурные паттерны**
*   Освоили модульную конфигурацию и фабрики моделей
*   Внедрили обработку ошибок и **retry-механизмы** для продакшн-готовых решений

### Ключевые преимущества подхода
**LangGraph + МСР** дают нам:
*   **Прозрачность** — каждый шаг агента документирован и отслеживаем
*   **Расширяемость** — новые возможности добавляются декларативно
*   **Надёжность** — встроенная обработка ошибок и восстановление
*   **Гибкость** — поддержка множества моделей и провайдеров из коробки

### Заключение

ИИ-агенты — это не футуристическая фантастика, а **реальная технология сегодняшнего дня**. С помощью LangGraph и MCP мы можем создавать системы, которые решают конкретные бизнес-задачи, автоматизируют рутину и открывают новые возможности.

**Главное — начать.** Возьмите код из примеров, адаптируйте под свои задачи, экспериментируйте. Каждый проект — это новый опыт и шаг к мастерству в области ИИ-разработки.

Удачи в ваших проектах!

---
*Теги: python, ии, mcp, langchain, ии-ассистент, ollama, ии-агенты, local llm, langgraph, mcp-server*
*Хабы: Блог компании Amvera, Natural Language Processing, Искусственный интеллект, Python, Программирование*

![habr](https://habr.com/ru/companies/amvera/articles/929568/)
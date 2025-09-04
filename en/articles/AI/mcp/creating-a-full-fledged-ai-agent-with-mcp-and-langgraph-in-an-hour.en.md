# How to teach a neural network to work with its hands: creating a full-fledged AI agent with MCP and LangGraph in an hour


Friends, greetings! I hope you've missed me.

For the past couple of months, I've been deeply immersed in researching the integration of AI agents into my own Python projects. In the process, I've accumulated a lot of practical knowledge and observations that it would be a sin not to share. So today I'm returning to Habr - with a new topic, a fresh perspective, and with the intention of writing more often.

On the agenda are LangGraph and MCP: tools with which you can create truly useful AI agents.

If before we argued about which neural network answers better in Russian, today the battlefield has shifted towards more applied tasks: who better copes with the role of an AI agent? Which frameworks truly simplify development? And how to integrate all this good stuff into a real project?

But before diving into practice and code, let's understand the basic concepts. Especially two key ones: **AI agents and MCP**. Without them, the conversation about LangGraph will be incomplete.

### AI agents in simple terms

AI agents are not just "pumped-up" chatbots. They are more complex, autonomous entities that possess two crucial features:

1.  **Ability to interact and coordinate**

    Modern agents can break down tasks into subtasks, call other agents, request external data, and work in a team. This is no longer a solitary assistant, but a distributed system where each component can contribute.

2.  **Access to external resources**

    An AI agent is no longer limited by the confines of a dialogue. It can access databases, make API calls, interact with local files, vector knowledge bases, and even run commands in the terminal. All this became possible thanks to the emergence of MCP - a new level of integration between the model and the environment.

---

If to put it simply: **MCP is a bridge between a neural network and its environment**. It allows the model to "understand" the context of the task, access data, make calls, and form reasoned actions, rather than just issuing text responses.

**Let's imagine an analogy:**

*   You have a **neural network** - it can reason and generate texts.
*   There are **data and tools** - documents, APIs, knowledge bases, terminal, code.
*   And there is **MCP** - it is an interface that allows the model to interact with these external sources as if they were part of its internal world.

**Without MCP:**

Model is an isolated dialogue engine. You feed it text - it responds. And that's it.

**With MCP:**

Model becomes a full-fledged **task executor**:

*   gains access to data structures and APIs;
*   calls external functions;
*   navigates the current state of the project or application;
*   can remember, track, and change context as the dialogue progresses;
*   uses extensions such as search tools, code runners, vector embedding databases, etc.

In a technical sense, **MCP is a protocol for interaction between LLM and its environment**, where context is provided in the form of structured objects (instead of "raw" text), and calls are formalized as interactive operations (e.g., function calling, tool usage, or agent actions). This is what turns an ordinary model into a **real AI agent**, capable of doing more than just "talking".

### And now - to business!

Now that we've covered the basic concepts, it's logical to ask: "How do we implement all this in Python in practice?"

This is where **LangGraph** comes into play - a powerful framework for building state graphs, agent behavior, and thought chains. It allows you to "stitch together" the interaction logic between agents, tools, and the user, creating a living AI architecture that adapts to tasks.

In the following sections, we'll look at how to:

*   build an agent from scratch;
*   create states, transitions, and events;
*   integrate functions and tools;
*   and how this entire ecosystem works in a real project.

### A little theory: what is LangGraph

Before we dive into practice, a few words about the framework itself.

**LangGraph** is a project from the **LangChain** team, the very ones who first proposed the concept of "chains" for interacting with LLMs. If previously the main focus was on linear or conditionally branching pipelines (langchain.chains), now the developers are betting on a **graph model**, and LangGraph is what they recommend as the new "core" for building complex AI systems.

**LangGraph** is a framework for building finite state machines and state graphs, where each **node** represents a part of the agent's logic: a model call, an external tool, a condition, user input, etc.

### How it works: graphs and nodes

Conceptually, LangGraph is built on the following ideas:

*   **Graph** - is a structure that describes the possible paths of logic execution. You can think of it as a map: from one point you can move to another depending on conditions or the execution result.
*   **Nodes** - are specific steps within the graph. Each node performs some function: calls a model, calls an external API, checks a condition, or simply updates the internal state.
*   **Transitions between nodes** - is the routing logic: if the result of the previous step is such and such, then go there.
*   **State** - is passed between nodes and accumulates everything needed: history, intermediate conclusions, user input, tool operation results, etc.

Thus, we get a **flexible mechanism for controlling agent logic**, in which both simple and very complex scenarios can be described: loops, conditions, parallel actions, nested calls, and much more.

### Why is it convenient?

LangGraph allows you to build **transparent, reproducible, and extensible logic**:

*   easy to debug;
*   easy to visualize;
*   easy to scale for new tasks;
*   easy to integrate external tools and MCP protocols.

In essence, LangGraph is the **"brain" of the agent**, where each step is documented, controllable, and can be changed without chaos and "magic."

### Well, that's enough theory!

We could talk for a long time about graphs, states, logic composition, and the advantages of LangGraph over classic pipelines. But, as practice shows, it's better to see it once in code.

**It's time to move on to practice.** Next - a Python example: we'll create a simple but useful AI agent based on LangGraph that will use external tools, memory, and make decisions itself.

### Preparation: cloud and local neural networks

To start creating AI agents, we first need a **brain** - a language model. Here there are two approaches:

*   **use cloud solutions**, where everything is ready "out of the box";
*   or **raise the model locally** - for complete autonomy and confidentiality.

Let's consider both options.

#### Cloud services: fast and convenient

The simplest way is to use the power of large providers: OpenAI, Anthropic, and use...

### Where to get keys and tokens:

*   **OpenAI** - ChatGPT and other products;
*   **Anthropic** - Claude;
*   **OpenRouter.ai** - dozens of models (one token - many models via OpenAI-compatible API);
*   **Amvera Cloud** - the ability to connect LLAMA with ruble payment and built-in proxying to OpenAI and Anthropic.

This path is convenient, especially if you:

*   don't want to configure infrastructure;
*   develop with a focus on speed;
*   work with limited resources.

### Local models: full control

If **privacy, offline work** are important to you, or you want to build **fully autonomous agents**, then it makes sense to deploy the neural network locally.

**Main advantages:**

*   **Confidentiality** - data remains with you;
*   **Offline work** - useful in isolated networks;
*   **No subscriptions and tokens** - free after setup.

**Disadvantages are obvious:**

*   Resource requirements (especially for video memory);
*   Setup can take time;
*   Some models are difficult to deploy without experience.

Nevertheless, there are tools that make local launch easier. One of the best today is **Ollama**.

### Deploying local LLM via Ollama + Docker

We will prepare a local launch of the Qwen 2.5 model (qwen2.5:32b) using a Docker container and the Ollama system. This will allow integrating the neural network with MCP and using it in your own LangGraph-based agents.

If the computing resources of your computer or server are insufficient for working with this version of the model, you can always choose a less "resource-hungry" neural network - the installation and launch process will remain similar.

**Quick installation (summary of steps)**

1.  **Install Docker + Docker Compose**
2.  **Create project structure:**
```bash
mkdir qwen-local && cd qwen-local
```
3.  **Create `docker-compose.yml`**
(universal option, GPU is detected automatically)

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

4.  **Start the container:**
```bash
docker compose up -d
```

5.  **Download the model:**
```bash
docker exec -it ollama_qwen ollama pull qwen2.5:32b
```

6.  **Check operation via API:**
```bash
curl http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{"model": "qwen2.5:32b", "prompt": "Hello!", "stream": false}'
```
*(Image with the result of the curl command execution)*

7.  **Integration with Python:**
```python
import requests

def query(prompt):
    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "qwen2.5:32b",
        "prompt": prompt,
        "stream": False
    })
    return res.json()['response']

print(query("Explain quantum entanglement"))
```
Now you have a full-fledged local LLM, ready to work with MCP and LangGraph.

**What's next?**

We have a choice between cloud and local models, and we have learned how to connect both. The most interesting part is ahead - **creating AI agents on LangGraph**, which use the selected model, memory, tools, and their own logic.

**Let's move on to the most delicious part - code and practice!**

---

Before moving on to practice, it is important to prepare the working environment. I assume that you are already familiar with the basics of Python, know what libraries and dependencies are, and understand why to use a virtual environment.

If all this is new to you - I recommend first taking a short course or guide on Python basics, and then returning to the article.

#### Step 1: Creating a virtual environment

Create a new virtual environment in the project folder:
```bash
python -m venv venv
source venv/bin/activate  # for Linux/macOS
venv\Scripts\activate   # for Windows
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

> ⚠️ **Current versions are indicated as of July 21, 2025.** They may have changed since publication - **check for relevance before installation.**

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

*   **OPENAI_API_KEY** - key for accessing GPT models from OpenAI;
*   **DEEPSEEK_API_KEY** - key for using Deepseek models;
*   **OPENROUTER_API_KEY** - single key for accessing many models via OpenRouter

---
Some MCP tools (e.g., `brave-web-search`) require a key to work. Without it, they simply won't activate.

**What if you don't have API keys?**

No problem. You can start development with a local model (e.g., via Ollama), without connecting any external services. In this case, you don't need to create the `.env` file at all.

Done! Now we have everything we need to get started - an isolated environment, dependencies, and, if necessary, access to cloud neural networks and MCP integrations.

Next - we will launch our LLM agent in different ways.

### Simple launch of LLM agents via LangGraph: basic integration

Let's start with the simplest: how to "connect the brain" to a future agent. We will analyze the basic ways to launch language models (LLM) using LangChain, so that in the next step we can move on to integration with LangGraph and building a full-fledged AI agent.

#### Imports
```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_deepseek import ChatDeepSeek
```
*   `os` and `load_dotenv()` - for loading variables from the `.env` file.
*   `ChatOpenAI`, `ChatOllama`, `ChatDeepSeek` - wrappers for connecting language models via LangChain.

> 💡 If you use alternative approaches to working with configurations (e.g., Pydantic Settings), you can replace `load_dotenv()` with your usual method.

#### Loading environment variables
```python
load_dotenv()
```
This will load all variables from `.env`, including keys for accessing OpenAI, DeepSeek, OpenRouter, and other APIs.

#### Simple functions for getting LLM

**OpenAI**
```python
def get_openai_llm():
    return ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
```
If the `OPENAI_API_KEY` variable is correctly set, LangChain will substitute it automatically - explicit `api_key=...` here is optional.

**DeepSeek**
```python
def get_deepseek_llm():
    # ...
```
Similarly, but using the `ChatDeepSeek` wrapper.

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

*   `ChatOpenAI` is used, despite the model not being from OpenAI - because OpenRouter uses the same protocol.
*   `base_url` is mandatory: it points to the OpenRouter API.
*   The `moonshotai/kimi-k2:free` model was chosen as one of the most balanced options in terms of quality and speed at the time of writing.
*   The `OpenRouter` API key must be passed explicitly - automatic substitution does not work here.

#### Mini-test: checking model operation
```python
if __name__ == "__main__":
    llm = get_openrouter_llm(model="moonshotai/kimi-k2:free")
    response = llm.invoke("Who are you?")
    print(response.content)
```
*(Image with the execution result: `I am an AI assistant created by Moonshot AI...`)*

If everything is configured correctly, you will receive a meaningful response from the model. Congratulations - the first step is done!

### But this is not an agent yet

At the current stage, we have connected LLM and made a simple call. This is more like a console chatbot than an AI agent.

**Why?**

*   We write **synchronous, linear code** without state logic or goals.
*   The agent does not make decisions, does not remember context, and does not use tools.
*   MCP and LangGraph are not yet involved.

**What's next?**

Next, we will implement a **full-fledged AI agent** using **LangGraph** - first without MCP, to focus on the agent's architecture, states, and logic.

Let's dive into real agent mechanics. Let's go!

### Job classification agent: from theory to practice

...concepts of LangGraph in practice and create a useful tool for HR platforms and freelance exchanges.

#### Agent task

Our agent takes a text description of a vacancy or service as input and performs a three-level classification:

1.  **Job type**: project work or permanent vacancy
2.  **Profession category**: from 45+ predefined specialties
3.  **Search type**: whether a person is looking for a job or looking for a performer

The result is returned in a structured JSON format with a confidence score for each classification.

#### 📈 Agent architecture on LangGraph

Following the principles of LangGraph, we create a **state graph** of four nodes:

- Input description
- ↓
- Job type classification node
- ↓
- Category classification node
- ↓
- Search type determination node
- ↓
- Confidence calculation node
- ↓
- JSON result

Each node is a **specialized function** that:

*   Receives the current agent state
*   Performs its part of the analysis
*   Updates the state and passes it on

#### State management

We define the **agent's memory structure** via `TypedDict`:

```python
from typing import TypedDict, Dict

class State(TypedDict):
    """Agent state for storing information about the classification process"""
    description: str
    job_type: str
    category: str
    search_type: str
    confidence_scores: Dict[str, float]
    processed: bool
```

This is the **agent's working memory** - everything it remembers and accumulates during the analysis. Similar to how a human expert keeps the task context in mind when analyzing a document.

Let's look at the full code, and then focus on the main points.

```python
import asyncio
import json
from enum import Enum
from typing import TypedDict, Dict, Any, List

from langgraph.graph import StateGraph, END
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# Categories of professions
CATEGORIES = [
    "2D animator", "3D animator", "3D modeler",
    "Business analyst", "Blockchain developer", ...
]

class JobType(Enum):
    PROJECT = "project work"
    PERMANENT = "permanent work"

class SearchType(Enum):
    LOOKING_FOR_WORK = "looking for work"
    LOOKING_FOR_PERFORMER = "looking for performer"

class State(TypedDict):
    """Agent state for storing information about the classification process"""
    description: str
    job_type: str
    category: str
    search_type: str
    confidence_scores: Dict[str, float]
    processed: bool

class VacancyClassificationAgent:
    """Asynchronous agent for classifying vacancies and services"""

    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.1):
        """Agent initialization"""
        self.llm = ChatOpenAI(model=model_name, temperature=temperature)
        self.workflow = self._create_workflow()

    def _create_workflow(self) -> StateGraph:
        """Creates the agent's workflow based on LangGraph"""
        workflow = StateGraph(State)
        
        # Add nodes to the graph
        workflow.add_node("job_type_classification", self._classify_job_type)
        workflow.add_node("category_classification", self._classify_category)
        workflow.add_node("search_type_classification", self._classify_search_type)
        workflow.add_node("confidence_calculation", self._calculate_confidence)
        
        # Define the sequence of node execution
        workflow.set_entry_point("job_type_classification")
        workflow.add_edge("job_type_classification", "category_classification")
        workflow.add_edge("category_classification", "search_type_classification")
        workflow.add_edge("search_type_classification", "confidence_calculation")
        workflow.add_edge("confidence_calculation", END)
        
        return workflow.compile()

    async def _classify_job_type(self, state: State) -> Dict[str, Any]:
        """Node for determining job type: project or permanent"""
        # ... (implementation follows)
        
    async def _classify_category(self, state: State) -> Dict[str, Any]:
        """Node for determining profession category"""
        # ... (implementation follows)
        
    async def _classify_search_type(self, state: State) -> Dict[str, Any]:
        """Node for determining search type"""
        # ... (implementation follows)

    async def _calculate_confidence(self, state: State) -> Dict[str, Any]:
        """Node for calculating confidence level in classification"""
        # ... (implementation follows)

    def _find_closest_category(self, predicted_category: str) -> str:
        """Finds the closest category from the list of available ones"""
        # ... (implementation follows)

    async def classify(self, description: str) -> Dict[str, Any]:
        """Main method for classifying vacancy/service"""
        initial_state = {
            "description": description,
            "job_type": "",
            "category": "",
            "search_type": "",
            "confidence_scores": {},
            "processed": False
        }
        
        # Run the workflow
        result = await self.workflow.ainvoke(initial_state)
        
        # Form the final JSON response
        classification_result = {
            "job_type": result["job_type"],
            "category": result["category"],
            "search_type": result["search_type"],
            "confidence_scores": result["confidence_scores"],
            "success": result["processed"]
        }
        return classification_result

async def main():
    """Demonstration of agent operation"""
    agent = VacancyClassificationAgent()
    
    test_cases = [
        "Requires Python developer to create a web application in Django. Permanent job.",
        "Looking for orders to create logos and corporate identity. I work in Adobe Illustrator.",
        "Need a 3D animator for a short-term project to create a commercial.",
        "Resume: experienced marketer, looking for remote work in digital marketing",
        "Looking for a React frontend developer for our team on a permanent basis"
    ]
    
    print("🤖 Demonstration of vacancy classification agent operation\n")
    for i, description in enumerate(test_cases, 1):
        print(f"--- Test {i}: ---")
        print(f"Description: {description}")
        try:
            result = await agent.classify(description)
            print("Classification result:")
            print(json.dumps(result, ensure_ascii=False, indent=2))
        except Exception as e:
            print(f"❌ Error: {e}")
        print("-" * 80)

if __name__ == "__main__":
    asyncio.run(main())

```
*(...the rest of the code with method implementations was presented in the article...)*

### Key advantages of the architecture
1.  **Modularity** - each node solves one problem, easy to test and improve separately
2.  **Extensibility** - new features are added declaratively
3.  **Transparency** - the entire decision-making process is documented and traceable
4.  **Performance** - asynchronous processing of multiple requests
5.  **Reliability** - built-in error handling and recovery

### Real benefits
Such an agent can be used in:
*   **HR platforms** for automatic categorization of resumes and vacancies
*   **Freelance exchanges** for improving search and recommendations
*   **Internal systems** of companies for processing applications and projects
*   **Analytical solutions** for labor market research

### MCP in action: creating an agent with a file system and web search
After we have dealt with the basic principles of LangGraph and created a simple classifier agent, let's expand its capabilities by connecting it to the outside world via MCP.

Now we will create a full-fledged AI assistant that can:
*   Work with the file system (read, create, modify files)
*   Search for relevant information on the Internet
*   Remember the dialogue context
*   Handle errors and recover from failures

#### From theory to real tools
Remember how at the beginning of the article we talked about **MCP being a bridge between a neural network and its environment**? Now you will see this in practice. Our agent will gain access to **real tools**:
```
# File system tools
- read_file - reading files
- write_file - writing and creating files
- list_directory - viewing folder contents
- create_directory - creating folders

# Web search tools
- brave_web_search - searching the Internet
- get_web_content - getting page content
```
This is no longer a "toy" agent - it is a **working tool** that can solve real problems.

#### 📈 Architecture: from simple to complex

**1. Configuration as the basis of stability**
```python
from dataclasses import dataclass

@dataclass
class AgentConfig:
    """Simplified AI agent configuration"""
    filesystem_path: str = "/path/to/work/directory"
    model_provider: ModelProvider = ModelProvider.OLLAMA
    use_memory: bool = True
    enable_web_search: bool = True

    def validate(self) -> None:
        """Configuration validation"""
        if not os.path.exists(self.filesystem_path):
            raise ValueError(f"Path does not exist: {self.filesystem_path}")
```
**Why is this important?** Unlike the classification example, here the agent interacts with external systems. One error in the file path or a missing API key - and the entire agent stops working. **Validation at startup** saves hours of debugging.

**2. Model factory: flexibility of choice**
```python
def create_model(config: AgentConfig):
    """Creates a model according to the configuration"""
    provider = config.model_provider.value
    if provider == "ollama":
        return ChatOllama(model="qwen2.5:32b", base_url="http://localhost:11434")
    elif provider == "openai":
        return ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
    # ... other providers
```
One code - many models. Want a free local model? Use Ollama. Need maximum accuracy? Switch to GPT-4. Is speed important? Try DeepSeek. The code remains the same.

**3. MCP integration: connecting to the real world**
```python
async def _init_mcp_client(self):
    """MCP client initialization"""
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
Here the key work of MCP takes place: we connect external MCP servers to the agent, which provide a set of tools and functions. The agent, in turn, receives not just individual functions, but a full contextual understanding of how to work with the file system and the Internet.

#### Error resilience
In the real world, everything breaks: the network is unavailable, files are locked, API keys are expired. Our agent is ready for this:
```python
@retry_on_failure(max_retries=2, delay=1.0)
async def process_message(self, user_input: str, thread_id: str = "default") -> str:
    # ...
```
The `@retry_on_failure` decorator automatically retries operations on temporary failures. The user won't even notice that something went wrong.

### Summary: from theory to practice of AI agents

Today we have come a long way from basic concepts to creating working AI agents. Let's summarize what we have learned and achieved.

**What we have mastered**

**1. Fundamental concepts**
*   Understood the difference between chatbots and real AI agents
*   Understood the role of **MCP (Model Context Protocol)** as a bridge between the model and the outside world
*   Studied the architecture of **LangGraph** for building complex agent logic

**2. Practical skills**
*   Configured a working environment with support for cloud and local models
*   Created a **classifier agent** with an asynchronous architecture and state management
*   Built an **MCP agent** with access to the file system and web search

**3. Architectural patterns**
*   Mastered modular configuration and model factories
*   Implemented error handling and **retry mechanisms** for production-ready solutions

### Key advantages of the approach
**LangGraph + MCP** give us:
*   **Transparency** - every step of the agent is documented and traceable
*   **Extensibility** - new features are added declaratively
*   **Reliability** - built-in error handling and recovery
*   **Flexibility** - support for multiple models and providers out of the box

### Conclusion

AI agents are not futuristic fiction, but **real technology of today**. With LangGraph and MCP, we can create systems that solve specific business problems, automate routines, and open up new possibilities.

**The main thing is to start.** Take the code from the examples, adapt it to your tasks, experiment. Each project is a new experience and a step towards mastery in the field of AI development.

Good luck with your projects!

---
*Tags: python, ai, mcp, langchain, ai-assistant, ollama, ai-agents, local llm, langgraph, mcp-server*
*Hubs: Amvera company blog, Natural Language Processing, Artificial Intelligence, Python, Programming*

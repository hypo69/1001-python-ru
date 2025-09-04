## How to create an AI agent for web browsing with LangChain and Browser-Use: a step-by-step guide

This step-by-step guide will show you how to create an AI agent capable of searching for information on Google and analyzing web pages using LangChain and Browser-Use.

**Step 1: Install necessary libraries**

First, you need to install the necessary Python libraries. Open a terminal or command prompt and run the following command:

```bash
pip install -U langchain langchain-openai langchain-community browser-use python-dotenv serpapi google-search-results numexpr
```

**Step 2: Configure API keys**

API keys are required to work with OpenAI and SerpAPI.

* **OpenAI API Key:** Get your API key from the OpenAI website (openai.com).
* **SerpAPI API Key:** SerpAPI provides an API for working with search results. Register on the serpapi.com website (a free trial is available), log in to your account, and find your API key on the Dashboard page.

Create a `.env` file in the same directory where your Python script will be located, and add the keys there in the following format:

```
OPENAI_API_KEY=your_openai_key
SERPAPI_API_KEY=your_serpapi_key
```

**Step 3: Create a Python script (browser_agent.py)**

Create the `browser_agent.py` file and insert the following code into it:

```python
import asyncio
import logging
import os
from dotenv import load_dotenv

from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI


# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

# Load API keys from .env file
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

async def main():
    # Initialize the language model
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0) # You can try other models

    # Define the search tool (simple example, no actual Google search)
    search_tool = Tool(
        name="Google Search",
        func=lambda query: f"Searching Google: {query}",  # Replace with actual search using SerpAPI if needed
        description="Searches for information on Google."
    )


    # Define the task for the agent
    task = """
    Find the latest news about OpenAI on Google.
    Then visit one of the found websites and find the names of the founders.
    """

    # Create the agent
    agent = initialize_agent(
        tools=[search_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # Run the agent
    try:
        result = await agent.arun(task)
        print(f"Result: {result}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

**Step 4: Run the agent**

Open a terminal or command prompt, navigate to the directory with the `browser_agent.py` file, and run it:

```bash
python browser_agent.py
```

**Step 5: Improve the agent (advanced features)**

* **Real Google search:** Replace the `lambda` function in `search_tool` with code that uses SerpAPI for actual Google searches. This will require studying the SerpAPI documentation.

* **Web page interaction (Browser-Use):** To add web page interaction functionality (opening links, extracting text, etc.), you will need to use the `browser-use` library. The documentation for this library will help you add the appropriate tools to your agent.

* **Using memory:** LangChain's memory mechanisms can be used to preserve context between requests.

* **More complex action chains:** LangChain allows you to create more complex action chains to solve more complex tasks.


This example demonstrates the basic structure. To implement a full-fledged agent that interacts with a browser and Google Search, additional work with SerpAPI and `browser-use` will be required. Don't forget to refer to the documentation for these libraries for more detailed information.

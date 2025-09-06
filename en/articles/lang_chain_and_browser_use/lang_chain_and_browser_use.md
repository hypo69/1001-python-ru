## How to Create an AI Agent for Web Browser Interaction with LangChain and Browser-Use: A Step-by-Step Guide

This step-by-step guide will show you how to create an AI agent capable of searching for information on Google and analyzing web pages using LangChain and Browser-Use.

**Step 1: Install Necessary Libraries**

First, you need to install the required Python libraries. Open your terminal or command prompt and run the following command:

```bash
pip install -U langchain langchain-openai langchain-community browser-use python-dotenv serpapi google-search-results numexpr
```

**Step 2: Configure API Keys**

API keys are required to work with OpenAI and SerpAPI.

*   **OpenAI API Key:** Get your API key from the OpenAI website (openai.com).
*   **SerpAPI API Key:** SerpAPI provides an API for working with search results. Register on serpapi.com (a free trial is available), log in to your account, and find your API key on the Dashboard page.

Create a `.env` file in the same directory as your Python script and add the keys in the following format:

```
OPENAI_API_KEY=your_openai_key
SERPAPI_API_KEY=your_serpapi_key
```

**Step 3: Create the Python Script (browser_agent.py)**

Create a file named `browser_agent.py` and paste the following code into it:

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

    # Define the search tool (simple example, without actual Google search)
    search_tool = Tool(
        name="Google Search",
        func=lambda query: f"Searching Google for: {query}",  # Replace with actual SerpAPI search if needed
        description="Searches for information on Google."
    )


    # Define the agent's task
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

**Step 4: Run the Agent**

Open your terminal or command prompt, navigate to the directory containing `browser_agent.py`, and run it:

```bash
python browser_agent.py
```

**Step 5: Enhance the Agent (Advanced Features)**

*   **Real Google Search:** Replace the `lambda` function in `search_tool` with code that uses SerpAPI for actual Google searches. This will require studying the SerpAPI documentation.

*   **Web Page Interaction (Browser-Use):** To add functionality for interacting with web pages (opening links, extracting text, etc.), you will need to use the `browser-use` library. The documentation for this library will help you add the appropriate tools to your agent.

*   **Using Memory:** To maintain context between requests, you can use LangChain's memory mechanisms.

*   **More Complex Action Chains:** LangChain allows you to create more complex action chains (Chains) to solve more intricate tasks.


This example demonstrates the basic structure. To implement a full-fledged agent that interacts with a browser and Google Search, additional work with SerpAPI and `browser-use` will be required. Don't forget to refer to the documentation of these libraries for more detailed information.

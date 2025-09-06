### **"NOT Selenium" Cycle. Intro**

Those involved in web scraping, testing, and automation are familiar with Selenium, the more modern Playwright, and/or the Crawlee framework. They are powerful, they can do almost anything, and they... are not always needed. Moreover, in many cases, using these tools is like hammering nails with a microscope: the job will certainly be done, but at the cost of unjustified expenses – speed, system resources, and configuration complexity.

Welcome to the "NOT Selenium" article series. Here I will show other (not always obvious) ways to interact with internet content.

#### Paradigm #1: Direct Communication. HTTP Clients

*   **`Requests`** — Forms and sends a network request to the target address (URL), exactly as your browser does at the very first moment of page loading, but without the browser itself. In this request, it packages the method (e.g., `GET` to retrieve data), headers (`Headers`) that represent the site (e.g., `User-Agent: "I-am-a-browser"`), and other parameters. In response from the server, it receives raw data — most often, it's the original HTML code of the page or a string in JSON format, as well as a status code (e.g., `200 OK`).

*   **`HTTPX`** — is a modern successor to `Requests`. At a fundamental level, it does the same thing: sends the same HTTP requests with the same headers and receives the same responses. But there's a key difference: `Requests` works **synchronously** — it sends a request, sits and waits for a response, gets a response, sends the next one. `HTTPX` on the other hand, can work **asynchronously** — it can "fire off" a hundred requests at once without waiting for responses, and then efficiently process them as they arrive.

They are excellent for collecting data from static sites, working with APIs, parsing thousands of pages where JavaScript execution is not required.

*   **Advantages:** **Speed and efficiency.** Thanks to `HTTPX`'s asynchronous nature, where `Requests` would sequentially make 100 requests for several minutes, `HTTPX` will handle it in a few seconds.
*   **Disadvantages:** Not suitable for sites where content is generated using JavaScript.

#### Paradigm #2: Chrome DevTools Protocol (CDP)

What if the site is dynamic and content is generated using JavaScript? Modern browsers (Chrome, Chromium, Edge) have a built-in protocol for debugging and control — **Chrome DevTools Protocol (CDP)**. It allows you to send commands directly to the browser, bypassing the cumbersome WebDriver layer that Selenium uses.

*   **Tools:** The main representative of this approach today is `Pydoll`, which replaced the once popular but now unsupported `pyppeteer`.
*   **When to use:** When JavaScript rendering is needed, but you want to maintain high speed and avoid driver complexities.
*   **Advantages:** **Balance.** You get the power of a real browser, but with much lower overhead and often with built-in protection bypass mechanisms.
*   **Disadvantages:** Can be more difficult to debug than Playwright and requires a deeper understanding of browser operation.

#### Paradigm #3: Autonomous LLM Agents

This is the cutting edge. What if instead of writing code that says "click here, type this," we just give a task in natural language? "Find all suppliers on this site and collect their product categories."

This is exactly the problem that LLM agents solve. Using a "brain" in the form of a large language model (GPT, Gemini) and "hands" in the form of a set of tools (browser, Google search), these agents can independently plan and execute complex tasks on the web.

*   **Tools:** Bundles like `LangChain` + `Pydoll` or custom solutions, as in `simple_browser.py`, which we will analyze later.
*   **When to use:** For complex research tasks where steps are unknown in advance and real-time adaptation is required.
*   **Advantages:** **Intelligence.** The ability to solve unstructured problems and adapt to changes on the fly.
*   **Disadvantages:** "Non-determinism" (results may vary from run to run), cost of API calls to LLM, lower speed compared to direct code.

#### Paradigm #4: Code-Free Scraping

Sometimes the task is so simple that writing code is overkill. Need to quickly pull a table from one page? There are elegant solutions for this that don't require programming.

*   **Tools:** Google Sheets functions (`IMPORTXML`, `IMPORTHTML`), browser extensions.
*   **When to use:** For one-off tasks, rapid prototyping, or when you simply don't want to write code.
*   **Advantages:** **Simplicity.** Opened, specified what to collect — got the result.
*   **Disadvantages:** Limited functionality, not suitable for complex tasks or large volumes of data.

### What's next?

This article is just an introduction. In the next issues of our "NOT Selenium" series, we will move from theory to hard practice. We will delve deep into each of these paradigms and show how they work with real-world examples:

*   We will analyze **Pydoll** and see how it bypasses Cloudflare.
*   We will stage a battle between **JavaScript vs. Python** for the title of the best language for web scraping.
*   We will learn how to squeeze maximum speed out of parsing with **lxml**.
*   We will write a script that collects data from **Amazon** and saves it to **Excel**.
*   We will show how **Google Sheets** can become your first scraper.
*   And, of course, we will thoroughly analyze how to create and use an **autonomous LLM agent** to control the browser.

Get ready to change your view on automation and data collection on the web. It will be fast, efficient, and very interesting. Subscribe

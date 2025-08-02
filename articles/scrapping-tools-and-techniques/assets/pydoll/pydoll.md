# Pydoll: Asynchronous Web Automation in Python

Pydoll is a powerful Python library for automating Chromium-based browsers. It offers a modern, asynchronous approach to web scraping and automation, eliminating the need for traditional WebDrivers.

## Key Features

*   **WebDriver-less Architecture:** Pydoll communicates directly with browsers like Chrome and Edge using the DevTools Protocol. This means you don't need to manage WebDriver executables (like `chromedriver.exe`), which simplifies setup and avoids version compatibility issues.
*   **Asynchronous by Design:** Built on Python's `asyncio` library, Pydoll can perform multiple operations concurrently. This allows for significant performance gains, especially when working with multiple tabs or scraping data from numerous pages at once.
*   **Human-like Interactions:** To avoid being detected as a bot, Pydoll simulates realistic user behavior. It can mimic human-like mouse movements, typing speeds, and introduce random delays.
*   **Built-in Cloudflare Bypass:** Pydoll includes features to automatically handle and bypass Cloudflare's anti-bot protection, including Turnstile and reCAPTCHA v3.
*   **Advanced Element Selection:** You can find elements on a page using various strategies, including:
    *   Simple attributes (ID, class name, tag name)
    *   CSS selectors
    *   XPath queries
*   **Proxy Integration:** Easily configure Pydoll to use proxies for IP rotation, which is essential for large-scale scraping and avoiding IP-based blocking.
*   **Comprehensive Control:** Pydoll provides a rich API for fine-grained control over the browser, including:
    *   Taking screenshots and exporting pages to PDF
    *   Intercepting and modifying network requests
    *   Automating file uploads
    *   Executing custom JavaScript code

## Installation

To start using Pydoll, install it via pip:

```bash
pip install pydoll-python
```

## Getting Started: A Simple Example

Here's a basic script that opens Google, searches for "pydoll python," and waits for the results to load:

```python
import asyncio
from pydoll.browser.chrome import Chrome
from pydoll.constants import Key

async def main():
    async with Chrome() as browser:
        # Start the browser and get a new tab
        tab = await browser.start()

        # Navigate to Google
        await tab.go_to('https://www.google.com')

        # Find the search box by its attributes
        search_box = await tab.find(tag_name='textarea', name='q')

        # Type the search query and press Enter
        await search_box.insert_text('pydoll python')
        await search_box.press_keyboard_key(Key.ENTER)

        # Wait for the search results to appear
        await tab.wait_element(id='search')

        print("Search results are loaded!")

# Run the asynchronous main function
asyncio.run(main())
```

## Interacting with Web Elements

The `tab` object is your primary tool for interacting with a web page. It works similarly to Selenium's `WebDriver`, but with asynchronous methods.

### Finding Elements

*   **`tab.find(...)`:** Finds the first element matching the given criteria.
*   **`tab.find_elements(...)`:** Finds all elements matching the criteria.
*   **`tab.query(...)`:** Finds elements using CSS selectors or XPath queries.
*   **`tab.wait_element(...)`:** Waits for an element to become available on the page before returning it.

### Element Actions

Once you have an element, you can interact with it:

*   **`element.click()`:** Clicks the element.
*   **`element.insert_text('...')`:** Enters text into an input field.
*   **`element.text`:** Gets the text content of the element.
*   **`element.press_keyboard_key(...)`:** Simulates pressing a key on the keyboard.

## Handling Cloudflare

Pydoll provides two main approaches for dealing with Cloudflare's anti-bot measures:

### 1. Context Manager (Synchronous Handling)

This approach will pause your script's execution until the Cloudflare challenge is resolved.

```python
async with tab.expect_and_bypass_cloudflare_captcha():
    await tab.go_to('https://www.example.com')
```

### 2. Background Processing (Asynchronous Handling)

This method allows your script to continue with other tasks while Pydoll handles the Cloudflare challenge in the background.

```python
# Enable automatic Cloudflare solving
await tab.enable_auto_solve_cloudflare_captcha()

# Navigate to the page
await tab.go_to('https://www.example.com')

# Continue with other tasks...

# Disable the feature when no longer needed
await tab.disable_auto_solve_cloudflare_captcha()
```

## Limitations to Consider

*   **Rate Limiting:** While Pydoll can help you avoid detection, sending too many requests in a short period can still lead to your IP being blocked. It's important to implement delays and use proxies for large-scale scraping.
*   **CAPTCHA Complexity:** Pydoll's automated bypass works for many, but not all, types of CAPTCHAs. More complex challenges might require manual intervention or third-party solving services.
*   **Browser Compatibility:** Pydoll is specifically designed for Chromium-based browsers (like Chrome and Edge). It will not work with other browsers like Firefox or Safari.

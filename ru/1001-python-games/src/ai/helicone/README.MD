```rst
.. module:: src.ai.helicone
```
[Русский](https://github.com/hypo69/hypo/blob/master/src/ai/helicone/readme.ru.md)
[About `helicone.ai`](https://github.com/hypo69/hypo/blob/master/src/ai/helicone/about.ru.md)
# HeliconeAI: Integration with Helicone.ai and OpenAI

## Overview

The `HeliconeAI` class is designed to facilitate interaction with Helicone.ai and OpenAI's models. This class provides methods for generating poems, analyzing sentiment, summarizing text, and translating text. It also includes logging of completions using Helicone.ai.

## Key Features

1. **Poem Generation**:
   - Generates a poem based on a given prompt using the `gpt-3.5-turbo` model.

2. **Sentiment Analysis**:
   - Analyzes the sentiment of a given text using the `text-davinci-003` model.

3. **Text Summarization**:
   - Summarizes a given text using the `text-davinci-003` model.

4. **Text Translation**:
   - Translates a given text to a specified target language using the `text-davinci-003` model.

5. **Completion Logging**:
   - Logs all completions using Helicone.ai for monitoring and analysis.

## Installation

To use the `HeliconeAI` class, ensure you have the necessary dependencies installed. You can install them using pip:

```bash
pip install openai helicone
```

## Usage

### Initialization

Initialize the `HeliconeAI` class:

```python
from helicone import Helicone
from openai import OpenAI

class HeliconeAI:
    def __init__(self):
        self.helicone = Helicone()
        self.client = OpenAI()
```

### Methods

#### Generate Poem

Generate a poem based on a given prompt:

```python
def generate_poem(self, prompt: str) -> str:
    response = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    self.helicone.log_completion(response)
    return response.choices[0].message.content
```

#### Analyze Sentiment

Analyze the sentiment of a given text:

```python
def analyze_sentiment(self, text: str) -> str:
    response = self.client.completions.create(
        model="text-davinci-003",
        prompt=f"Analyze the sentiment of the following text: {text}",
        max_tokens=50
    )
    self.helicone.log_completion(response)
    return response.choices[0].text.strip()
```

#### Summarize Text

Summarize a given text:

```python
def summarize_text(self, text: str) -> str:
    response = self.client.completions.create(
        model="text-davinci-003",
        prompt=f"Summarize the following text: {text}",
        max_tokens=100
    )
    self.helicone.log_completion(response)
    return response.choices[0].text.strip()
```

#### Translate Text

Translate a given text to a specified target language:

```python
def translate_text(self, text: str, target_language: str) -> str:
    response = self.client.completions.create(
        model="text-davinci-003",
        prompt=f"Translate the following text to {target_language}: {text}",
        max_tokens=200
    )
    self.helicone.log_completion(response)
    return response.choices[0].text.strip()
```

### Example Usage

Here is an example of how to use the `HeliconeAI` class:

```python
def main():
    helicone_ai = HeliconeAI()

    poem = helicone_ai.generate_poem("Напиши мне стихотворение про кота.")
    print("Generated Poem:\n", poem)

    sentiment = helicone_ai.analyze_sentiment("Сегодня был отличный день!")
    print("Sentiment Analysis:\n", sentiment)

    summary = helicone_ai.summarize_text("Длинный текст для изложения...")
    print("Summary:\n", summary)

    translation = helicone_ai.translate_text("Hello, how are you?", "русский")
    print("Translation:\n", translation)

if __name__ == "__main__":
    main()
```

## Dependencies

- `helicone`
- `openai`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For more detailed information, refer to the source code and comments within the `HeliconeAI` class.
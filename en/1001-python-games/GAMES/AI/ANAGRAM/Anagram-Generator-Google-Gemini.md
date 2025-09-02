# Anagram Generator using Google Gemini

This is a simple code for generating anagrams using Google Gemini's large language model.

## Description

The program takes a set of Russian letters as input and tries to find an existing Russian word composed of these letters (using all or part of them).

## Anagram Rules

*   Only existing Russian words are used.
*   When searching for anagrams, only Russian letters are considered. Digits and other characters are ignored.
*   If multiple words can be formed, one of them is returned.
*   If no word can be formed from the given letters, the message "No anagrams" is returned.

## Usage

1.  **Google Gemini API Key.**

    API KEY FOR THE MODEL HERE: [https://aistudio.google.com/](https://aistudio.google.com/)

    Or you can use mine:

    AIzaSyCprZ9Tr-rB_xFau5zgWsKPM_6W-FmUntk

    I created the key for learning and understanding the code. Do not overload the model!

2.  **Install necessary libraries:**

    ```bash
    pip install google-generativeai
    ```

3.  **Run the script:**

    ```bash
    python anagram_generator.py
    ```

4.  The script will ask for the API key. Enter it.
5.  After that, enter the letters for which you want to find an anagram.

## Code Explanation

*   `import google.generativeai as genai`: Imports the library for interacting with Gemini.
*   `import re`: Imports the library for working with regular expressions (for cleaning input).
*   The `GoogleGenerativeAI` class encapsulates the logic for interacting with the Gemini model.
*   `system_instruction`: This is the system prompt (instruction) for Gemini, which explains what is required of it.
*   `re.sub(r"[^а-яА-ЯёЁ]", "", q)`: This line removes all characters from the input string `q` that are not Russian letters. `[^а-яА-ЯёЁ]` is a regular expression that means "any character *not* in the range a-z, A-Z, and ёЁ".
*   The `if not q:` check verifies if the string became empty after removing all non-Cyrillic characters.
*   `model.generate_content(q)`: Sends the query `q` to the Gemini model.
*   `try...except` exception handling prevents the program from crashing in case of API interaction errors.

## Usage Example

```
Enter letters for Gemini to find an anagram: сон
нос
Enter letters for Gemini to find an anagram: апельсин
спаниель
Enter letters for Gemini to find an anagram: 12345абвг
абвг
Enter letters for Gemini to find an anagram: 
```


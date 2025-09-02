# BANNER AI
Gemini model returns the response as an ASCII banner depending on the instruction given to it.

The program interacts with the Google Generative AI model to create text banners.
The user can choose the banner design style and send text to the model for processing.

## Installing dependencies
To run the code on a local machine, you will need to install the google libraries.

```python
pip install google
pip install google-generativeai
```

I strongly recommend doing all experiments in a virtual environment.


## Code features in this program
1. Instructions are stored in different files and loaded as needed.
2. Starting with this example, I save the model key in an environment variable, which saves me from having to enter the key repeatedly.
3. I use absolute paths to files.
    To determine the project's root directory, I recursively search upwards for marker files ('pyproject.toml', 'requirements.txt', '.git').
    I store the found directory in the __root__ variable. From it, I build the path to the system instructions:
    ``python
    relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # Relative path to the directory
    base_path: Path = __root__ / relative_path  # Absolute path to the directory using __root__
    ``


### 1. **Import necessary libraries**
```python
import google.generativeai as genai  # Import library for working with Gemini
import re  # Import library for working with regular expressions
from pathlib import Path  # Import for working with file system paths
from header import __root__  # Import __root__ object, containing the absolute path to the project root
from dotenv import load_dotenv, set_key  # Import functions for working with environment variables
import os  # Import for working with environment variables
```

- **`google.generativeai`**: Used for interacting with the Google Generative AI API.
- **`re`**: Library for working with regular expressions (not used in this code, but may be useful in the future).
- **`Path`**: Allows working with file system paths.
- **`__root__`**: Object containing the absolute path to the project root.
- **`dotenv`**: Allows loading environment variables from a `.env` file and saving them.
- **`os`**: Used for working with environment variables.

---


### 2. **Load environment variables**
```python
load_dotenv()
```
- The `load_dotenv()` function loads environment variables from the `.env` file, if it exists.

---


### 3. **`GoogleGenerativeAI` class**
The class is designed to interact with the Google Generative AI model.

#### 3.1. **Class attributes**
```python
MODELS = [
    'gemini-1.5-flash-8b',
    'gemini-2-13b',
    'gemini-3-20b'
]
```
- List of available Google Generative AI models.

#### 3.2. **`__init__` method**
```python
def __init__(self, api_key: str, system_instruction: str, model_name: str = 'gemini-2.0-flash-exp'):
    """
    Initializes the GoogleGenerativeAI model.

    :param api_key: API key for accessing Gemini.
    :type api_key: str
    :param system_instruction: Instruction for the model (system prompt).
    :type system_instruction: str
    :param model_name: Name of the Gemini model to use. Defaults to 'gemini-2.0-flash-exp'.
    :type model_name: str
    """
    self.api_key = api_key
    self.model_name = model_name
    genai.configure(api_key=self.api_key)  # Configure the library with the API key
    self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction)  # Initialize the model with the instruction
```
- **`api_key`**: API key for accessing Google Generative AI.
- **`system_instruction`**: Instruction for the model (e.g., text formatting style).
- **`model_name`**: Name of the model, defaults to `'gemini-2.0-flash-exp'`.
- **`genai.configure(api_key=self.api_key)`**: Configure the library using the API key.
- **`genai.GenerativeModel(...)`**: Initialize the model with the specified parameters.

#### 3.3. **`ask` method**
```python
def ask(self, q: str) -> str:
    """
    Sends a request to the model and receives a response.

    :param q: Request text.
    :type q: str
    :return: Model response or error message.
    :rtype: str
    """
    try:
        response = self.model.generate_content(q)  # Send request to the model
        return response.text  # Get text response
    except Exception as ex:
        return f'Error: {str(ex)}'  # Handle and get error
```
- **`q`**: The request text sent to the model.
- **`self.model.generate_content(q)`**: Sending the request to the model.
- **`response.text`**: Getting the text response from the model.
- **`except Exception as ex`**: Handling errors and returning an error message.

---


### 4. **Main part of the program**
```python
if __name__ == '__main__':
```
- Checks that the program is run as a standalone script.

#### 4.1. **Defining paths**
```python
relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # Relative path to the directory
base_path: Path = __root__ / relative_path  # Absolute path to the directory using __root__
```
- **`relative_path`**: Relative path to the directory within the project.
- **`base_path`**: Absolute path, obtained by combining `__root__` and `relative_path`.

#### 4.2. **Reading API key**
```python
API_KEY: str = os.getenv('API_KEY')
if not API_KEY:
    API_KEY = input('API key not found. Enter API key from `gemini`: ')  # Request API key from user
    set_key('.env', 'API_KEY', API_KEY)  # Save key to .env file
```
- **`os.getenv('API_KEY')`**: Attempts to get the API key from environment variables.
- If the key is not found, it prompts the user for it via `input`.
- **`set_key('.env', 'API_KEY', API_KEY)`**: Saves the entered key to the `.env` file for future use.

#### 4.3. **Instructions for the model**
```python
instructions: dict = {
    '1': 'system_instruction_asterisk',
    '2': 'system_instruction_tilde',
    '3': 'system_instruction_hash',
}
```
- Dictionary containing the names of files with instructions for the model.

#### 4.4. **Greeting the user**
```python
print('Welcome to the Banner game!')
print('Enter text, and I will create a text banner for you.')
```
- Greets the user and explains the program's functionality.

#### 4.5. **Loop for selecting banner style**
```python
while True:
    print('Select banner design style:')
    print('1. Symbol \'*\'')
    print('2. Symbol ~')
    print('3. Symbol #')
    choice = input('Enter style number (1, 2 or 3): ')
```
- The user selects the banner design style.

#### 4.6. **Reading instructions for the model**
```python
if choice in ('1', '2', '3'):
    system_instruction: str = Path(base_path, 'instructions', f'{instructions[choice]}.md').read_text(encoding='UTF-8')  # Read instruction from file
else:
    print('Invalid choice. Default style \'*\' is used')
    system_instruction: str = Path(base_path, 'instructions', 'system_instruction_asterisk.md').read_text(encoding='UTF-8')  # Read default instruction
```
- If the choice is valid, read the corresponding instruction from the file.
- If the choice is invalid, use the default instruction.

#### 4.7. **Creating a class instance**
```python
model: GoogleGenerativeAI = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction)
```
- Create an instance of the `GoogleGenerativeAI` class with the specified parameters.

#### 4.8. **Requesting text from the user**
```python
user_text: str = input('Enter text for banner: ')
```
- The user enters text for the banner.

#### 4.9. **Text validation**
```python
if user_text.strip() == '':
    print('You did not enter text. Please try again.')
else:
    response = model.ask(user_text)
    print('\nYour banner is ready:')
    print(response)
```
- If the text is empty, display an error message.
- If text is entered, send it to the model and display the result.

```
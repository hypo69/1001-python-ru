### Ask the Gemini Model

An API key is required to work.

API KEY FOR THE MODEL CAN BE OBTAINED HERE: [https://aistudio.google.com/](https://aistudio.google.com/)




```python
import google.generativeai as genai

class GoogleGenerativeAI:
    """
    Class for interacting with Google Generative AI models.
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, api_key: str, model_name: str = "gemini-2.0-flash-exp"):
        """
        Initializes the GoogleGenerativeAI model.

        Args:
            api_key (str): API key for accessing the generative model.
            model_name (str, optional): Name of the model to use. Defaults to "gemini-2.0-flash-exp".
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name=self.model_name)

    def ask(self, q: str) -> str:
        """
        Sends a text query to the model and returns the response.

        Args:
            q (str): The question to be sent to the model.

        Returns:
            str: Response from the model.
        """
        try:
            response = self.model.generate_content(q)
            return response.text
        except Exception as ex:
            return f"Error: {str(ex)}"
```

### How this code works

1. **Import library**: We import the `google.generativeai` library, which provides an interface for interacting with Google AI models.

2. **`GoogleGenerativeAI` class**: This class encapsulates all the logic for interacting with the Gemini model. It takes an API key and model name as parameters. The `gemini-2.0-flash-exp` model is used by default.

3. **`__init__` method**: This method configures the model. We pass the API key and model name, and then initialize the model object.

4. **`ask` method**: This method sends a text query to the model and returns the response. If something goes wrong, the method will return an error message.

### How to use?

```python
################################################################################
#                                                                              #
#             INSERT YOUR GEMINI API KEY                                       #
#                                                                              #
################################################################################

API_KEY: str = input("API key from `gemini`: ")
model = GoogleGenerativeAI(api_key=API_KEY)

q = input("Question: ")
response = model.ask(q)
print(response)
```

1. **Enter API key**: First, the program prompts the user for an API key to access the Gemini model. This key can be obtained from the [Google AI Studio](https://aistudio.google.com/) website.

2. **Create model object**: We create an object of the `GoogleGenerativeAI` class, passing it the API key.

3. **Enter question**: The user enters their question they want to ask the model.

4. **Get response**: The program sends the question to the model and displays the response on the screen.

### Usage example

You have an API key, and you want to ask the model: "How can I improve my code?". Here's how it will look:

```
API key from `gemini`: your_api_key
Question: How can I improve my code?
Response: To improve your code, it is recommended to follow clean code principles, such as naming variables and functions clearly and logically, using comments to explain complex logic, and applying SOLID principles for designing classes and modules.
```


Run the code [here](https://colab.research.google.com/github/hypo69/101_python_computer_games_ru/blob/master/GAMES/AI/ASK_GEMINI/ask_gemini_ru.ipynb)

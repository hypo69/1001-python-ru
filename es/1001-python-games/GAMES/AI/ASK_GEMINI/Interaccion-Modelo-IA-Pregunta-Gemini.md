### Pregunte al modelo Gemini

Se requiere una clave API para funcionar.

LA CLAVE API PARA EL MODELO SE PUEDE OBTENER AQUÍ: [https://aistudio.google.com/](https://aistudio.google.com/)




```python
import google.generativeai as genai

class GoogleGenerativeAI:
    """
    Clase para interactuar con los modelos de Google Generative AI.
    """

    MODELS = [
        "gemini-1.5-flash-8b",
        "gemini-2-13b",
        "gemini-3-20b"
    ]

    def __init__(self, api_key: str, model_name: str = "gemini-2.0-flash-exp"):
        """
        Inicializa el modelo GoogleGenerativeAI.

        Argumentos:
            api_key (str): Clave API para acceder al modelo generativo.
            model_name (str, optional): Nombre del modelo a usar. Por defecto "gemini-2.0-flash-exp".
        """
        self.api_key = api_key
        self.model_name = model_name
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name=self.model_name)

    def ask(self, q: str) -> str:
        """
        Envía una consulta de texto al modelo y devuelve la respuesta.

        Argumentos:
            q (str): La pregunta que se enviará al modelo.

        Devuelve:
            str: Respuesta del modelo.
        """
        try:
            response = self.model.generate_content(q)
            return response.text
        except Exception as ex:
            return f"Error: {str(ex)}"
```

### Cómo funciona este código

1. **Importar biblioteca**: Importamos la biblioteca `google.generativeai`, que proporciona una interfaz para interactuar con los modelos de Google AI.

2. **Clase `GoogleGenerativeAI`**: Esta clase encapsula toda la lógica para interactuar con el modelo Gemini. Toma una clave API y un nombre de modelo como parámetros. El modelo `gemini-2.0-flash-exp` se usa por defecto.

3. **Método `__init__`**: En este método, se configura el modelo. Pasamos la clave API y el nombre del modelo, y luego inicializamos el objeto del modelo.

4. **Método `ask`**: Este método envía una consulta de texto al modelo y devuelve la respuesta. Si algo sale mal, el método devolverá un mensaje de error.

### ¿Cómo usar?

```python
################################################################################
#                                                                              #
#             INSERTE SU CLAVE API DE GEMINI                                       #
#                                                                              #
################################################################################

API_KEY: str = input("Clave API de `gemini`: ")
model = GoogleGenerativeAI(api_key=API_KEY)

q = input("Pregunta: ")
response = model.ask(q)
print(response)
```

1. **Ingresar clave API**: Primero, el programa le pide al usuario una clave API para acceder al modelo Gemini. Esta clave se puede obtener en el sitio web de [Google AI Studio](https://aistudio.google.com/).

2. **Crear objeto del modelo**: Creamos un objeto de la clase `GoogleGenerativeAI`, pasándole la clave API.

3. **Ingresar pregunta**: El usuario ingresa su pregunta que desea hacerle al modelo.

4. **Obtener respuesta**: El programa envía la pregunta al modelo y muestra la respuesta en la pantalla.

### Ejemplo de uso

Tiene una clave API y quiere preguntarle al modelo: "¿Cómo puedo mejorar mi código?". Así es como se verá:

```
Clave API de `gemini`: su_clave_api
Pregunta: ¿Cómo puedo mejorar mi código?
Respuesta: Para mejorar su código, se recomienda seguir los principios de código limpio, como nombrar variables y funciones de forma clara y lógica, usar comentarios para explicar la lógica compleja y aplicar los principios SOLID para diseñar clases y módulos.
```


Ejecute el código [aquí](https://colab.research.google.com/github/hypo69/101_python_computer_games_ru/blob/master/GAMES/AI/ASK_GEMINI/ask_gemini_ru.ipynb)

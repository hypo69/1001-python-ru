# BANNER IA
El modelo Gemini devuelve la respuesta como un banner ASCII dependiendo de la instrucción que se le dé.

 El programa interactúa con el modelo de Google Generative AI para crear banners de texto.
 El usuario puede elegir el estilo de diseño del banner y enviar texto al modelo para su procesamiento.

## Instalación de dependencias
Para ejecutar el código en una máquina local, deberá instalar las bibliotecas de Google.

```python
pip install google
pip install google-generativeai
```

Recomiendo encarecidamente realizar todos los experimentos en un entorno virtual.


## Características del código en este programa
1. Las instrucciones se almacenan en diferentes archivos y se cargan según sea necesario.
2. A partir de este ejemplo, guardo la clave del modelo en una variable de entorno, lo que me evita tener que ingresar la clave repetidamente.
3. Utilizo rutas absolutas a los archivos.
    Para determinar el directorio raíz del proyecto, busco recursivamente hacia arriba los archivos marcadores ('pyproject.toml', 'requirements.txt', '.git').
    Almaceno el directorio encontrado en la variable __root__. A partir de ella, construyo la ruta a las instrucciones del sistema:
    ``python
    relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # Ruta relativa al directorio
    base_path: Path = __root__ / relative_path  # Ruta absoluta al directorio usando __root__
    ``


### 1. **Importar bibliotecas necesarias**
```python
import google.generativeai as genai  # Importar biblioteca para trabajar con Gemini
import re  # Importar biblioteca para trabajar con expresiones regulares
from pathlib import Path  # Importar para trabajar con rutas del sistema de archivos
from header import __root__  # Importar objeto __root__, que contiene la ruta absoluta a la raíz del proyecto
from dotenv import load_dotenv, set_key  # Importar funciones para trabajar con variables de entorno
import os  # Importar para trabajar con variables de entorno
```

- **`google.generativeai`**: Se utiliza para interactuar con la API de Google Generative AI.
- **`re`**: Biblioteca para trabajar con expresiones regulares (no utilizada en este código, pero puede ser útil en el futuro).
- **`Path`**: Permite trabajar con rutas del sistema de archivos.
- **`__root__`**: Objeto que contiene la ruta absoluta a la raíz del proyecto.
- **`dotenv`**: Permite cargar variables de entorno desde un archivo `.env` y guardarlas.
- **`os`**: Se utiliza para trabajar con variables de entorno.

---

### 2. **Cargar variables de entorno**
```python
load_dotenv()
```
- La función `load_dotenv()` carga las variables de entorno del archivo `.env`, si existe.

---

### 3. **Clase `GoogleGenerativeAI`**
La clase está diseñada para interactuar con el modelo de Google Generative AI.

#### 3.1. **Atributos de clase**
```python
MODELS = [
    'gemini-1.5-flash-8b',
    'gemini-2-13b',
    'gemini-3-20b'
]
```
- Lista de modelos de Google Generative AI disponibles.

#### 3.2. **Método `__init__`**
```python
def __init__(self, api_key: str, system_instruction: str, model_name: str = 'gemini-2.0-flash-exp'):
    """
    Inicializa el modelo GoogleGenerativeAI.

    :param api_key: Clave API para acceder a Gemini.
    :type api_key: str
    :param system_instruction: Instrucción para el modelo (prompt del sistema).
    :type system_instruction: str
    :param model_name: Nombre del modelo Gemini a usar. Por defecto 'gemini-2.0-flash-exp'.
    :type model_name: str
    """
    self.api_key = api_key
    self.model_name = model_name
    genai.configure(api_key=self.api_key)  # Configurar la biblioteca con la clave API
    self.model = genai.GenerativeModel(model_name=self.model_name, system_instruction=system_instruction)  # Inicializar el modelo con la instrucción
```
- **`api_key`**: Clave API para acceder a Google Generative AI.
- **`system_instruction`**: Instrucción para el modelo (por ejemplo, estilo de formato de texto).
- **`model_name`**: Nombre del modelo, por defecto `'gemini-2.0-flash-exp'`.
- **`genai.configure(api_key=self.api_key)`**: Configuración de la biblioteca usando la clave API.
- **`genai.GenerativeModel(...)`**: Inicialización del modelo con los parámetros especificados.

#### 3.3. **Método `ask`**
```python
def ask(self, q: str) -> str:
    """
    Envía una solicitud al modelo y recibe una respuesta.

    :param q: Texto de la solicitud.
    :type q: str
    :return: Respuesta del modelo o mensaje de error.
    :rtype: str
    """
    try:
        response = self.model.generate_content(q)  # Enviar solicitud al modelo
        return response.text  # Obtener respuesta de texto
    except Exception as ex:
        return f'Error: {str(ex)}'  # Manejar y obtener error
```
- **`q`**: El texto de la solicitud enviado al modelo.
- **`self.model.generate_content(q)`**: Envío de la solicitud al modelo.
- **`response.text`**: Obtención de la respuesta de texto del modelo.
- **`except Exception as ex`**: Manejo de errores y devolución de un mensaje de error.

---

### 4. **Parte principal del programa**
```python
if __name__ == '__main__':
```
- Comprueba que el programa se ejecuta como un script independiente.

#### 4.1. **Definición de rutas**
```python
relative_path: Path = Path('GAMES', 'AI', 'BANNER_AI')  # Ruta relativa al directorio
base_path: Path = __root__ / relative_path  # Ruta absoluta al directorio usando __root__
```
- **`relative_path`**: Ruta relativa al directorio dentro del proyecto.
- **`base_path`**: Ruta absoluta, obtenida combinando `__root__` y `relative_path`.

#### 4.2. **Lectura de la clave API**
```python
API_KEY: str = os.getenv('API_KEY')
if not API_KEY:
    API_KEY = input('Clave API no encontrada. Ingrese la clave API de `gemini`: ')  # Solicitar clave API al usuario
    set_key('.env', 'API_KEY', API_KEY)  # Guardar clave en el archivo .env
```
- **`os.getenv('API_KEY')`**: Intenta obtener la clave API de las variables de entorno.
- Si la clave no se encuentra, la solicita al usuario a través de `input`.
- **`set_key('.env', 'API_KEY', API_KEY)`**: Guarda la clave ingresada en el archivo `.env` para uso futuro.

#### 4.3. **Instrucciones para el modelo**
```python
instructions: dict = {
    '1': 'system_instruction_asterisk',
    '2': 'system_instruction_tilde',
    '3': 'system_instruction_hash',
}
```
- Diccionario que contiene los nombres de los archivos con instrucciones para el modelo.

#### 4.4. **Saludo al usuario**
```python
print('¡Bienvenido al juego Banner!')
print('Ingrese texto, y crearé un banner de texto para usted.')
```
- Saluda al usuario y explica la funcionalidad del programa.

#### 4.5. **Bucle para seleccionar el estilo del banner**
```python
while True:
    print('Seleccione el estilo de diseño del banner:')
    print('1. Símbolo 
*')
    print('2. Símbolo 
~')
    print('3. Símbolo 
#')
    choice = input('Ingrese el número de estilo (1, 2 o 3): ')
```
- El usuario selecciona el estilo de diseño del banner.

#### 4.6. **Lectura de instrucciones para el modelo**
```python
if choice in ('1', '2', '3'):
    system_instruction: str = Path(base_path, 'instructions', f'{instructions[choice]}.md').read_text(encoding='UTF-8')  # Leer instrucción del archivo
else:
    print('Elección inválida. Se usa el estilo predeterminado 
*
')
    system_instruction: str = Path(base_path, 'instructions', 'system_instruction_asterisk.md').read_text(encoding='UTF-8')  # Leer instrucción predeterminada
```
- Si la elección es válida, lee la instrucción correspondiente del archivo.
- Si la elección no es válida, usa la instrucción predeterminada.

#### 4.7. **Creación de una instancia de clase**
```python
model: GoogleGenerativeAI = GoogleGenerativeAI(api_key=API_KEY, system_instruction=system_instruction)
```
- Crea una instancia de la clase `GoogleGenerativeAI` con los parámetros especificados.

#### 4.8. **Solicitar texto al usuario**
```python
user_text: str = input('Ingrese texto para el banner: ')
```
- El usuario ingresa texto para el banner.

#### 4.9. **Validación de texto**
```python
if user_text.strip() == '':
    print('No ingresó texto. Intente de nuevo.')
else:
    response = model.ask(user_text)
    print('\nSu banner está listo:')
    print(response)
```
- Si el texto está vacío, muestra un mensaje de error.
- Si se ingresa texto, lo envía al modelo y muestra el resultado.

```
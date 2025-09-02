# Generador de anagramas usando Google Gemini

Este es un código simple para generar anagramas usando el modelo de lenguaje grande de Google Gemini.

## Descripción

El programa toma un conjunto de letras rusas como entrada e intenta encontrar una palabra rusa existente compuesta por estas letras (usando todas o parte de ellas).

## Reglas de anagramas

*   Solo se utilizan palabras rusas existentes.
*   Al buscar anagramas, solo se consideran las letras rusas. Los dígitos y otros caracteres se ignoran.
*   Si se pueden formar varias palabras, se devuelve una de ellas.
*   Si no se puede formar ninguna palabra a partir de las letras dadas, se devuelve el mensaje "No hay anagramas".

## Uso

1.  **Clave API de Google Gemini.**

    CLAVE API PARA EL MODELO AQUÍ: [https://aistudio.google.com/](https://aistudio.google.com/)

    O puede usar la mía:

    AIzaSyCprZ9Tr-rB_xFau5zgWsKPM_6W-FmUntk

    Creé la clave para aprender y comprender el código. ¡No sobrecargue el modelo!

2.  **Instale las bibliotecas necesarias:**

    ```bash
    pip install google-generativeai
    ```

3.  **Ejecute el script:**

    ```bash
    python anagram_generator.py
    ```

4.  El script le pedirá la clave API. Ingrésela.
5.  Después de eso, ingrese las letras para las que desea encontrar un anagrama.

## Explicación del código

*   `import google.generativeai as genai`: Importa la biblioteca para interactuar con Gemini.
*   `import re`: Importa la biblioteca para trabajar con expresiones regulares (para limpiar la entrada).
*   La clase `GoogleGenerativeAI` encapsula la lógica para interactuar con el modelo Gemini.
*   `system_instruction`: Este es el prompt del sistema (instrucción) para Gemini, que explica lo que se requiere de él.
*   `re.sub(r"[^а-яА-ЯёЁ]", "", q)`: Esta línea elimina de la cadena de entrada `q` todos los caracteres que no son letras rusas. `[^а-яА-ЯёЁ]` es una expresión regular que significa "cualquier carácter *que no esté* en el rango a-я, А-Я y ёЁ".
*   La verificación `if not q:` comprueba si la cadena quedó vacía después de eliminar todos los caracteres no cirílicos.
*   `model.generate_content(q)`: Envía la consulta `q` al modelo Gemini.
*   El manejo de excepciones `try...except` evita que el programa se bloquee en caso de errores de interacción con la API.

## Ejemplo de uso

```
Ingrese letras para que Gemini encuentre un anagrama: сон
нос
Ingrese letras para que Gemini encuentre un anagrama: апельсин
спаниель
Ingrese letras para que Gemini encuentre un anagrama: 12345абвг
абвг
Ingrese letras para que Gemini encuentre un anagrama: 
```


# Juego Banner: Creación de banner de texto

&nbsp;&nbsp;&nbsp;&nbsp;
El programa crea un banner de texto a partir del texto introducido por el usuario. Saluda al usuario, solicita el texto y lo muestra como un banner formateado.
El código demuestra los principios básicos de trabajo con funciones, entrada/salida y operadores condicionales en Python.

---

## **Cómo funciona el programa**

El programa consta de dos partes principales:
1. **Función `create_banner(text)`** – responsable de la creación y visualización del banner de texto.
2. **Parte principal del programa** – interacción con el usuario: saludo, solicitud de texto y validación de entrada.

---

## **Código del programa**

```python
# Juego Banner: Creación de banner de texto

# Función para crear un banner
def create_banner(text):
    """
    Crea un banner de texto a partir del texto introducido.
    :param text: La cadena a convertir en banner.
    :return: None
    """
    # Determinar el ancho del banner (longitud del texto + 4 caracteres para el marco)
    banner_width = len(text) + 4

    # Imprimir el borde superior del banner
    print("*" * banner_width)

    # Imprimir el texto con un marco
    print(f"* {text} *")

    # Imprimir el borde inferior del banner
    print("*" * banner_width)

# Parte principal del programa
if __name__ == "__main__":
    # Saludar al usuario
    print("¡Bienvenido al juego Banner!")
    print("Ingrese texto, y crearé un banner de texto para usted.")

    # Solicitar texto al usuario
    user_text = input("Ingrese texto: ")

    # Comprobar que el texto no esté vacío
    if user_text.strip() == "":
        print("No ingresó texto. Intente de nuevo.")
    else:
        # Crear y mostrar el banner
        print("\nSu banner está listo:")
        create_banner(user_text)
```

---

## **Descripción del funcionamiento del código**

### **1. Función `create_banner(text)`**
- **Acepta:** la cadena `text` – el texto a convertir en banner.
- **Realiza:**
  - Calcula el ancho del banner, agregando 4 caracteres para el marco (`*` y espacios).
  - Imprime los bordes superior e inferior del banner usando el carácter `*`.
  - Imprime el texto rodeado por un marco.

### **2. Parte principal del programa**
- **Saluda** al usuario y explica lo que hace el programa.
- **Solicita** al usuario texto para crear un banner.
- **Comprueba** que el texto no esté vacío:
  - Si el usuario ingresó una cadena vacía, el programa informa un error y pide que lo intente de nuevo.
  - Si se ingresa texto, el programa muestra el banner creado.

---

## **Ejemplo de programa**

Si el usuario ingresó el texto `"Hola"`, el programa mostrará:
```
*********
* Hola *
*********
```

---


## **Cómo el intérprete analiza el código**

### **Orden de ejecución de operadores en Python**
- Python lee el código línea por línea, comenzando desde arriba y moviéndose hacia abajo.
- Cada línea se ejecuta secuencialmente, a menos que sea parte de una función, condición o bucle.

### **Definición de funciones**
- Las funciones se definen usando la palabra clave `def`.
- La definición de una función no ejecuta su código, solo crea una "plantilla" para futuras llamadas.

### **Llamadas a funciones**
- Cuando se llama a una función, Python salta a su definición y ejecuta el código dentro de ella.
- Una vez que la función termina de ejecutarse, el control regresa al lugar desde donde fue llamada.

### **Sentencias condicionales (if, else)**
- Las sentencias condicionales verifican una condición y ejecutan el código dentro del bloque si la condición es verdadera.
- Si la condición es falsa, Python omite el bloque y pasa a la siguiente línea.

### **Bucles (for, while)**
- Los bucles permiten repetir la ejecución de un bloque de código varias veces.
- Python verifica la condición del bucle antes de cada iteración.

### **Operadores de asignación (=)**
- Los operadores de asignación almacenan un valor en una variable.
- Esto ocurre antes de que se ejecuten otras operaciones, como llamadas a funciones o sentencias condicionales.

### **Expresiones y cálculos**
- Las expresiones (por ejemplo, `len(text) + 4`) se evalúan antes de que su resultado se use en otras partes del código.

---

## **Resumen**

Este programa demuestra los principios básicos de trabajo con funciones, entrada/salida y sentencias condicionales en Python. Puede ser útil para principiantes que aprenden el lenguaje y para comprender cómo funciona el intérprete de Python.

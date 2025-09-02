# Funciones en Python

Las funciones en el lenguaje Python son bloques de código con nombre que realizan una tarea específica. Permiten organizar el código, hacerlo más estructurado y fácil de reutilizar.

# Tabla de contenido

1. [Declaración de función](#declaración-de-función)
2. [Parámetros de función](#parámetros-de-función)
   - [Tipos de parámetros](#tipos-de-parámetros)
3. [Retorno de valor](#retorno-de-valor)
4. [Variables locales y globales](#variables-locales-y-globales)
5. [Funciones anidadas](#funciones-anidadas)
6. [Recursividad](#recursividad)
7. [Manejo de excepciones con `try` y `except`](#manejo-de-excepciones-con-try-y-except)
8. [Ejemplo de uso de funciones](#ejemplo-de-uso-de-funciones)

## Declaración de función

Una función se declara con la palabra clave `def`, seguida del nombre de la función, una lista de parámetros entre paréntesis y dos puntos. El cuerpo de la función se escribe con una sangría.

```python
def nombre_funcion(parámetros):
    # acciones
    return resultado
```

### Ejemplo:
```python
def sumar(a: int, b: int) -> int:
    """Devuelve la suma de dos números."""
    return a + b
```

Aquí:
- `a: int` y `b: int` — parámetros de función con anotaciones de tipo.
- `-> int` — anotación de tipo del valor de retorno.

## Parámetros de función

Las funciones pueden aceptar parámetros, que representan datos de entrada. Se especifican entre paréntesis después del nombre de la función.

Ejemplo con un parámetro:
```python
def saludar(nombre: str) -> str:
    """Saluda al usuario por su nombre."""
    return f"¡Hola, {nombre}!"
```

### Tipos de parámetros:
1. **Parámetros obligatorios** — deben pasarse al llamar a la función.
2. **Parámetros opcionales** — pueden tener valores predeterminados.
   ```python
   def saludar(nombre: str, edad: int = 18) -> str:
       return f"¡Hola, {nombre}! Tienes {edad} años."
   ```

## Retorno de valor

Una función puede devolver un valor usando la palabra clave `return`. Si no se usa `return`, la función devuelve `None` por defecto.

Ejemplo:
```python
def multiplicar(a: int, b: int) -> int:
    """Devuelve el producto de dos números."""
    return a * b
```

## Variables locales y globales

- **Variable local** — es una variable que existe solo dentro de una función. Se crea y se destruye con cada llamada a la función.
- **Variable global** — es una variable que es accesible en todo el código, incluidas las funciones.

Ejemplo de uso de una variable global:
```python
x = 10  # Variable global

def mostrar_x() -> int:
    return x  # Acceso a la variable global
```

Si dentro de una función necesita cambiar una variable global, debe usar la palabra clave `global`:
```python
x = 10  # Variable global

def cambiar_x() -> None:
    global x
    x = 20
```

## Funciones anidadas

En Python, las funciones pueden estar anidadas, lo que significa que una función puede definirse dentro de otra. Una función anidada puede acceder a las variables de la función externa.

Ejemplo:
```python
def exterior(a: int, b: int) -> int:
    """Una función que usa una función anidada para calcular la diferencia."""
    
    def anidada(x: int, y: int) -> int:
        """Una función anidada que devuelve la diferencia."""
        return x - y
    
    return anidada(a, b)
```

## Recursividad

La recursividad es cuando una función se llama a sí misma. Esto es útil para tareas que se pueden dividir en tareas más pequeñas y similares (por ejemplo, factorial).

Ejemplo de recursividad:
```python
def factorial(n: int) -> int:
    """Calcula el factorial de un número usando recursividad."""
    if n == 0:
        return 1  # Caso base
    return n * factorial(n - 1)  # Llamada recursiva
```

## Manejo de excepciones con `try` y `except`

Python proporciona un mecanismo de manejo de errores usando bloques `try` y `except`. El código que puede causar un error se coloca en el bloque `try`, y los errores se manejan en el bloque `except`.

Ejemplo de manejo de errores:
```python
def dividir(a: int, b: int) -> float:
    """Divide un número por otro, manejando posibles errores."""
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: división por cero"
    except Exception as e:
        return f"Se produjo un error: {e}"
    return result
```

Aquí:
- El bloque `try` intenta realizar la operación de división.
- El bloque `except ZeroDivisionError` captura el error de división por cero.
- El bloque `except Exception as e` captura otras excepciones y muestra un mensaje de error.

## Ejemplo de uso de funciones

```python
# Suma de dos números
print(sumar(5, 3))  # 8

# Función anidada
print(exterior(10, 4))  # 6

# Recursividad para el cálculo del factorial
print(factorial(5))  # 120

# Manejo de excepciones en la división
print(dividir(10, 2))  # 5.0
print(dividir(10, 0))  # Error: división por cero
```
---

  [Al índice](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)

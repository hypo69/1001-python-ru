# Funciones en Python

Las funciones en Python son bloques de código con nombre que realizan una tarea específica. Permiten organizar el código, hacerlo más estructurado y facilitar su reutilización.

# Contenido

1. [Declaración de función](#declaración-de-función)
2. [Parámetros de función](#parámetros-de-función)
   - [Tipos de parámetros](#tipos-de-parámetros)
3. [Valor de retorno](#valor-de-retorno)
4. [Variables locales y globales](#variables-locales-y-globales)
5. [Funciones anidadas](#funciones-anidadas)
6. [Recursión](#recursión)
7. [Manejo de excepciones con `try` y `except`](#manejo-de-excepciones-con-try-y-except)
8. [Ejemplo de uso de funciones](#ejemplo-de-uso-de-funciones)

## Declaración de función

Una función se declara usando la palabra clave `def`, seguida del nombre de la función, una lista de parámetros entre paréntesis y dos puntos. El cuerpo de la función se escribe con una sangría.

```python
def nombre_funcion(parámetros):
    # acciones
    return resultado
```

### Ejemplo:
```python
def suma(a: int, b: int) -> int:
    """Devuelve la suma de dos números."""
    return a + b
```

Aquí:
- `a: int` y `b: int` — parámetros de función con anotaciones de tipo.
- `-> int` — anotación de tipo del valor de retorno.

## Parámetros de función

Las funciones pueden aceptar parámetros, que son datos de entrada. Se especifican entre paréntesis después del nombre de la función.

Ejemplo con un parámetro:
```python
def saludo(nombre: str) -> str:
    """Saluda al usuario por su nombre."""
    return f"Hola, {nombre}!"
```

### Tipos de parámetros:
1. **Parámetros obligatorios** — deben pasarse al llamar a la función.
2. **Parámetros opcionales** — pueden tener valores predeterminados.
   ```python
   def saludo(nombre: str, edad: int = 18) -> str:
       return f"Hola, {nombre}! Tienes {edad} años."
   ```

## Valor de retorno

Una función puede devolver un valor usando la palabra clave `return`. Si no se usa `return`, la función devuelve `None` por defecto.

Ejemplo:
```python
def multiplicacion(a: int, b: int) -> int:
    """Devuelve el producto de dos números."""
    return a * b
```

## Variables locales y globales

- **Variable local** — una variable que existe solo dentro de una función. Se crea y se destruye con cada llamada a la función.
- **Variable global** — una variable que es accesible en todo el código, incluidas las funciones.

Ejemplo de uso de una variable global:
```python
x = 10  # Variable global

def mostrar_x() -> int:
    return x  # Accediendo a la variable global
```

Si necesita cambiar una variable global dentro de una función, debe usar la palabra clave `global`:
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
def externa(a: int, b: int) -> int:
    """Función que usa una función anidada para calcular la diferencia."""
    
    def anidada(x: int, y: int) -> int:
        """Función anidada que devuelve la diferencia."""
        return x - y
    
    return anidada(a, b)
```

## Recursión

La recursión es cuando una función se llama a sí misma. Esto es útil para tareas que se pueden dividir en tareas más pequeñas y similares (por ejemplo, factorial).

Ejemplo de recursión:
```python
def factorial(n: int) -> int:
    """Calcula el factorial de un número usando recursión."""
    if n == 0:
        return 1  # Caso base
    return n * factorial(n - 1)  # Llamada recursiva
```

## Manejo de excepciones con `try` y `except`

Python proporciona un mecanismo de manejo de errores usando bloques `try` y `except`. El código que puede causar un error se coloca en el bloque `try`, y los errores se manejan en el bloque `except`.

Ejemplo de manejo de errores:
```python
def division(a: int, b: int) -> float:
    """Divide un número por otro, manejando posibles errores."""
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: división por cero"
    except Exception as e:
        return f"Ocurrió un error: {e}"
    return result
```

Aquí:
- El bloque `try` intenta realizar la operación de división.
- El bloque `except ZeroDivisionError` captura el error de división por cero.
- El bloque `except Exception as e` captura otras excepciones y muestra un mensaje de error.

## Ejemplo de uso de funciones

```python
# Suma de dos números
print(suma(5, 3))  # 8

# Función anidada
print(externa(10, 4))  # 6

# Recursión para el cálculo del factorial
print(factorial(5))  # 120

# Manejo de excepciones en la división
print(division(10, 2))  # 5.0
print(division(10, 0))  # Error: división por cero
```
---

  [Al índice](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)

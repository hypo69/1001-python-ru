## **¿Qué es una comprensión de lista?**

En su forma más simple, una comprensión de lista es una forma compacta de crear una nueva lista basada en una existente (o cualquier objeto iterable). En lugar de usar un bucle `for` tradicional y agregar elementos a la lista uno por uno, puede hacerlo en una sola línea de código.


*   **Concisión:** Le permiten escribir menos código.
*   **Legibilidad:** Una vez que se acostumbre a su sintaxis, le resultarán más fáciles de entender que los bucles `for` equivalentes.
*   **Rendimiento:** En algunos casos, las comprensiones de lista pueden ser más rápidas que los bucles `for`.


Aquí está la sintaxis básica de una comprensión de lista:

```python
new_list = [expression for item in iterable]
```

*   **`expression`**: Una expresión que define cómo se calculará cada elemento de la nueva lista. Esto puede ser cualquier cosa: un valor simple, una operación matemática, una llamada a función.
*   **`item`**: Una variable que toma el valor de cada elemento de `iterable` a su vez.
*   **`iterable`**: Un objeto iterable, por ejemplo, una lista, tupla, cadena o el resultado de `range()`.

**Ejemplo:**

Suponga que tiene una lista de números y desea crear una nueva lista que contenga los cuadrados de esos números.

**Sin comprensión de lista:**

```python
numbers = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
    squares.append(number**2)
print(squares)  # Salida: [1, 4, 9, 16, 25]
```

**Con comprensión de lista:**

```python
numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers]
print(squares) # Salida: [1, 4, 9, 16, 25]
```

¡La comprensión de lista hace que el código sea más corto y claro!

**Agregar una condición**

Las comprensiones de lista también le permiten agregar condiciones para seleccionar los elementos que se incluirán en la nueva lista.

```python
new_list = [expression for item in iterable if condition]
```

* **`condition`**: Una condición que debe cumplirse para que un elemento se incluya en la nueva lista.

**Ejemplo:**

Creemos una lista de cuadrados de solo números pares de nuestra lista `numbers` original.

**Sin comprensión de lista:**

```python
numbers = [1, 2, 3, 4, 5]
even_squares = []
for number in numbers:
    if number % 2 == 0:
        even_squares.append(number**2)
print(even_squares) # Salida: [4, 16]
```

**Con comprensión de lista:**

```python
numbers = [1, 2, 3, 4, 5]
even_squares = [number**2 for number in numbers if number % 2 == 0]
print(even_squares) # Salida: [4, 16]
```

Agregué `if number % 2 == 0` a la comprensión de lista para filtrar solo los números pares.

**Comprensiones de lista de varias líneas**

Cuando las comprensiones de lista se vuelven más complejas, se pueden dividir en varias líneas para una mejor legibilidad.

**Ejemplo:**

```python
numbers = [1, 2, 3, 4, 5]
squared_odds = [
    number**2
    for number in numbers
    if number % 2 != 0
]
print(squared_odds) # Salida: [1, 9, 25]
```
Esto hace que el código sea más claro, especialmente cuando tiene condiciones largas o expresiones complejas.





**Ejercicio 1: Conversión de temperaturas**

Tiene una lista de temperaturas en grados Celsius y necesita convertirlas a grados Fahrenheit. La fórmula de conversión es: `F = (C * 9/5) + 32`.

Aquí está su lista de temperaturas en Celsius:

```python
celsius_temperatures = [0, 10, 20, 30, 40]
```

**Tarea:**

1.  Usando una comprensión de lista, cree una nueva lista `fahrenheit_temperatures` que contenga las temperaturas de `celsius_temperatures`, convertidas a Fahrenheit.
2.  Imprima la lista `fahrenheit_temperatures` resultante en la pantalla.

**Sugerencia:**

*   Use la fórmula `(celsius * 9/5) + 32` como expresión en la comprensión de lista.
*   Piense en qué es el `iterable` y qué es el `item` en este caso.

Intente escribir el código.

Mi solución:
```python
# Lista original de temperaturas en Celsius
celsius_temperatures = [0, 10, 20, 30, 40]

# Usar comprensión de lista para la conversión a Fahrenheit
fahrenheit_temperatures = [
    (celsius * 9/5) + 32  # Expresión: fórmula de conversión
    for celsius in celsius_temperatures # Iterar sobre los elementos de la lista
]

# Imprimir el resultado
print(fahrenheit_temperatures) # Salida: [32.0, 50.0, 68.0, 86.0, 104.0]
```

**Desglose del código:**

1.  **`celsius_temperatures = [0, 10, 20, 30, 40]`**: Esta es la lista de origen con temperaturas en Celsius.
2.  **`fahrenheit_temperatures = [...]`**: Aquí creamos una nueva lista usando una comprensión de lista.
3.  **`(celsius * 9/5) + 32`**: Esta es la expresión que se ejecuta para cada elemento. Convierte la temperatura de Celsius a Fahrenheit.
4.  **`for celsius in celsius_temperatures`**: Esta es parte de la comprensión de lista que itera sobre cada elemento en la lista `celsius_temperatures`, asignando su valor a la variable `celsius` en cada iteración.
5.  **`print(fahrenheit_temperatures)`**: Imprime la lista resultante de temperaturas en Fahrenheit.

**Nota importante:**

*   En este caso, `celsius_temperatures` es el `iterable`, y `celsius` es el `item`.
*   Utilizo el formato de varias líneas para la comprensión de lista para mejorar la legibilidad del código.
*   Dentro de la expresión, aplico directamente la fórmula de conversión, usando el valor `celsius` actual.



**Ejercicio 2: Filtrado y transformación de cadenas**

Tiene una lista de palabras y necesita hacer lo siguiente:

1.  Filtrar las palabras que comienzan con la letra "a" (sin distinción entre mayúsculas y minúsculas).
2.  Convertir todas las palabras restantes a mayúsculas.

Aquí está su lista de palabras:

```python
words = ["apple", "banana", "apricot", "kiwi", "Avocado", "orange"]
```

**Tarea:**

1.  Usando una comprensión de lista, cree una nueva lista `transformed_words` que contenga solo aquellas palabras de la lista `words` que no comiencen con la letra "a" (o "A"), y que se conviertan a mayúsculas.
2.  Imprima la lista `transformed_words` resultante en la pantalla.

**Sugerencias:**

*   Use el método de cadena `startswith()` para verificar si una palabra comienza con una letra específica. ¡No olvide las mayúsculas y minúsculas! Convierta todo a minúsculas.
*   Use el método de cadena `upper()` para convertir una cadena a mayúsculas.
*   Piense en el orden de las operaciones. Primero filtre, luego transforme.

Mi solución:

```python
# Lista original de palabras
words = ["apple", "banana", "apricot", "kiwi", "Avocado", "orange"]

# Usar comprensión de lista para filtrar y transformar
transformed_words = [
    word.upper() # Convertir a mayúsculas
    for word in words # Iterar sobre las palabras de la lista
    if not word.lower().startswith("a") # Filtrar palabras que no comienzan con 'a'
]

# Imprimir el resultado
print(transformed_words) # Salida: ['BANANA', 'KIWI', 'ORANGE']
```

**Desglose del código:**

1.  **`words = ["apple", "banana", "apricot", "kiwi", "Avocado", "orange"]`**: Esta es la lista original de palabras.
2.  **`transformed_words = [...]`**: Crear una nueva lista usando una comprensión de lista.
3.  **`word.upper()`**: Esta es la expresión que se ejecuta para cada palabra que pasa el filtro. Convierte la palabra a mayúsculas.
4.  **`for word in words`**: Iterar sobre todas las palabras de la lista `words`.
5.  **`if not word.lower().startswith("a")`**: Esta es la condición de filtrado.
    *   `word.lower()`: Primero, convertimos la palabra a minúsculas, para que la comparación no distinga entre mayúsculas y minúsculas.
    *   `startswith("a")`: Luego comprobamos si la palabra comienza con la letra "a".
    *   `not`: Invertir el resultado para mantener solo aquellas palabras que *no* comienzan con la letra "a".
6.  **`print(transformed_words)`**: Imprime la lista de palabras transformadas.

**Puntos clave:**

*   Los métodos de cadena `lower()`, `upper()` y `startswith()` en la expresión y condición de la comprensión de lista.
*   La condición de filtrado `if not word.lower().startswith("a")` asegura que solo las palabras que no comienzan con "a" (independientemente de las mayúsculas y minúsculas) se incluyan en la nueva lista.
*   Primero se aplica el filtrado y luego la conversión a mayúsculas.
*   De nuevo, utilizo el formato de varias líneas para una mejor legibilidad.


**Ejercicio 3: Creación de un diccionario a partir de una lista de tuplas**

Tiene una lista de tuplas, donde cada tupla contiene dos elementos: el nombre y la edad de una persona.

```python
people_data = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35),
    ("David", 28),
]
```

**Tarea:**

1. Usando una comprensión de lista, cree un diccionario `people_dict`, donde las claves son los nombres de las personas y los valores son sus edades.
2. Imprima el diccionario `people_dict` en la pantalla.

**Sugerencias:**

*   Las comprensiones de lista crean listas, pero se pueden usar para crear listas de tuplas, que luego se pueden pasar al constructor `dict()`.
*   Piense en cómo extraer el nombre y la edad de cada tupla.
*   Recuerde que un diccionario es una estructura de datos que almacena pares clave-valor.

**Una pequeña explicación:**

En Python, puede crear un diccionario a partir de una lista de tuplas, donde cada tupla consta de dos elementos (clave, valor).
Para esto, uso el constructor `dict()`. Por ejemplo:
```python
my_list = [("a", 1), ("b", 2)]
my_dict = dict(my_list)
print(my_dict) # Salida {'a': 1, 'b': 2}
```
Su tarea es usar la comprensión de lista para crear esta lista de tuplas, que luego se usará para crear el diccionario.

Mi solución:

```python
# Lista original de tuplas con datos de personas
people_data = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35),
    ("David", 28),
]

# Uso la comprensión de lista para crear una lista de tuplas, que luego convierto a un diccionario
people_dict = dict(
    [
      (name, age) # Crear una tupla (nombre, edad)
      for name, age in people_data # Iterar sobre las tuplas en people_data
    ]
)

# Imprimir el diccionario resultante
print(people_dict) # Salida: {'Alice': 30, 'Bob': 25, 'Charlie': 35, 'David': 28}
```

**Desglose del código:**

1.  **`people_data = [...]`**: Esta es la lista original de tuplas, donde cada tupla contiene el nombre y la edad de una persona.
2.  **`people_dict = dict(...)`**: Usamos el constructor `dict()` para crear un diccionario a partir de una lista de tuplas.
3.  **`[ (name, age) for name, age in people_data ]`**: Esta es una comprensión de lista que crea una lista de tuplas.
    *   `(name, age)`: Esta expresión crea una tupla a partir de dos elementos: `name` y `age`.
    *   `for name, age in people_data`: Esta parte itera sobre todas las tuplas en la lista `people_data`. En cada iteración, la tupla se desempaqueta en dos variables: `name` y `age`.
4. **`print(people_dict)`**: Imprime el diccionario creado.

**Puntos clave:**

*   La comprensión de lista crea una lista de tuplas.
*   El constructor `dict()` convierte una lista de tuplas en un diccionario, usando el primer elemento de la tupla como clave y el segundo como valor.
*   El desempaquetado de tuplas en el bucle `for name, age in people_data` hace que el código sea más legible.
*  La comprensión de lista en este ejemplo se usa para preparar datos para un diccionario.


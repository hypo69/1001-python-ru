# Algoritmos de ordenación

En la vida cotidiana y en la programación, nos encontramos con la necesidad de ordenar datos.
Esto puede ser cualquier cosa: una lista de compras, libros en un estante o resultados de búsqueda.
Los algoritmos de ordenación son un conjunto de instrucciones que nos ayudan a organizar los elementos en un orden determinado, ya sea ascendente,
descendente o según algún otro criterio.

Por ejemplo, utilizo frutas de diferentes tamaños.

**Representación de frutas con tamaños:**

Asociaremos las frutas con los tamaños. Usaremos tuplas, donde:

*   El primer elemento es el tamaño de la fruta:
    *   🍎 (pequeña) – manzana
    *   🍐 (mediana) – pera
    *   🍉 (grande) – melón
    *   🧺 (muy grande) – cesta
*   El segundo elemento es un identificador único, para el funcionamiento del programa.

Ejemplo: `(🍎, 1)` – es una manzana pequeña con identificador 1.

```python
from typing import List, Tuple

def compare_fruits(fruit1: Tuple[str, int], fruit2: Tuple[str, int]) -> int:
    """
    Compara dos frutas por tamaño.

    Args:
        fruit1: Tupla (tamaño, identificador).
        fruit2: Tupla (tamaño, identificador).

    Returns:
        -1 si fruit1 es menor que fruit2, 1 si fruit1 es mayor que fruit2, 0 si son iguales.
    """
    order = {"🍎": 0, "🍐": 1, "🍉": 2, "🧺": 3}  # Definir el orden de las frutas por tamaño
    size1 = order.get(fruit1[0]) # Obtener el tamaño de la primera fruta
    size2 = order.get(fruit2[0]) # Obtener el tamaño de la segunda fruta
    if size1 < size2: # Si el tamaño de la primera fruta es menor, devolver -1
        return -1
    elif size1 > size2: # Si el tamaño de la primera fruta es mayor, devolver 1
        return 1
    else: # Si los tamaños son iguales, devolver 0
      return 0
```

**Algoritmos de ordenación (comparación por tamaño de fruta):**

1.  **Ordenación de burbuja (Bubble Sort):** (Las burbujas más ligeras suben antes)
    *   El algoritmo compara frutas adyacentes por tamaño. Si una fruta es más grande que la adyacente, intercambia posiciones con ella.
    *   Este proceso se repite hasta que toda la lista de frutas esté ordenada de menor a mayor.
    *   Analogía: Imagine que tiene un acuario con burbujas de aire de diferentes tamaños. Las burbujas más ligeras (correspondientes a frutas más pequeñas) subirán a la superficie antes que las más pesadas (correspondientes a frutas más grandes). Así, las frutas más ligeras "flotan" a la parte superior de la lista, y las más pesadas se hunden hasta el fondo.

    ```mermaid
    graph TD
        A[Inicio] --> B{¿Hay frutas sin ordenar?};
        B -- Sí --> C[Comparar dos frutas adyacentes];
        C -- La primera es más grande --> D[Intercambiar posiciones];
        D --> E[Ir al siguiente par];
        C -- La primera no es más grande --> E;
        E --> F{¿Se llegó al final de la lista?};
        F -- No --> C;
        F -- Sí --> G{¿Hubo un intercambio?};
        G -- Sí --> B;
        G -- No --> H[Fin];
        B -- No --> H;
        H[Fin]
    ```
    ```python
    def bubble_sort(fruits: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
        """
        Ordena una lista de frutas por tamaño, usando el algoritmo de "ordenación de burbuja".

        Args:
            fruits: Lista de tuplas (tamaño, identificador).

        Returns:
            Lista de tuplas ordenada.
        """
        n = len(fruits)  # Obtener el número de frutas
        for i in range(n):  # Recorrer la lista n veces
            for j in range(0, n - i - 1):  # Recorrer la parte sin ordenar de la lista
                if compare_fruits(fruits[j], fruits[j + 1]) == 1:  # Si la fruta de la izquierda es más grande que la de la derecha
                    fruits[j], fruits[j + 1] = fruits[j + 1], fruits[j]  # Intercambiar posiciones
        return fruits

    ```
2.  **Ordenación por inserción (Insertion Sort):**
    *   El algoritmo construye una lista ordenada, agregando frutas una por una. Una nueva fruta se inserta en la posición correcta para mantener el orden por tamaño.
    *   La ordenación por inserción es buena para listas pequeñas o para aquellas donde los datos ya están casi ordenados.

3.  **Ordenación por selección (Selection Sort):**
    *   El algoritmo encuentra la fruta más pequeña en la parte sin ordenar de la lista. Luego coloca esta fruta en la primera posición de la parte sin ordenar de la lista.
    *   Este proceso se repite hasta que todas las frutas estén ordenadas.
    *   La ordenación por selección es simple pero ineficiente para listas grandes.





```python
def insertion_sort(fruits: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """
    Ordena una lista de frutas por tamaño, usando el algoritmo de "ordenación por inserción".

    Args:
        fruits: Lista de tuplas (tamaño, identificador).

    Returns:
        Lista de tuplas ordenada.
    """
    for i in range(1, len(fruits)): # Comenzar desde la segunda fruta (la primera se considera ordenada)
        key = fruits[i] # Tomar la siguiente fruta
        j = i - 1 # Índice de la fruta anterior
        while j >= 0 and compare_fruits(fruits[j], key) == 1: # Encontrar la posición en la parte ordenada donde insertar la fruta
            fruits[j + 1] = fruits[j] # Desplazar frutas para hacer espacio para la nueva
            j -= 1
        fruits[j + 1] = key # Insertar la fruta en la posición correcta
    return fruits

def selection_sort(fruits: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """
    Ordena una lista de frutas por tamaño, usando el algoritmo de "ordenación por selección".

    Args:
        fruits: Lista de tuplas (tamaño, identificador).

    Returns:
        Lista de tuplas ordenada.
    """
    n = len(fruits) # Obtener el número de frutas en la lista
    for i in range(n): # Recorrer todas las frutas de la lista
        min_index = i # Índice de la fruta más pequeña
        for j in range(i + 1, n): # Encontrar la fruta más pequeña en la parte sin ordenar
            if compare_fruits(fruits[j], fruits[min_index]) == -1: # Si se encuentra una fruta más pequeña que el mínimo actual
                min_index = j # Recordar el índice del nuevo mínimo
        fruits[i], fruits[min_index] = fruits[min_index], fruits[i] # Intercambiar la fruta actual con la más pequeña de la parte sin ordenar
    return fruits

def display_fruits(fruits: List[Tuple[str, int]]) -> str:
    """
    Convierte una lista de frutas en una cadena para mostrar.

    Args:
        fruits: Lista de tuplas (tamaño, identificador).

    Returns:
        Cadena para mostrar la lista de frutas.
    """
    return ", ".join(f"{fruit[0]}{fruit[1]}" for fruit in fruits)  # Construir cadena para la salida


# Crear una lista de frutas para ordenar
fruits = [
    ("🍉", 1), ("🍎", 2), ("🍐", 3), ("🧺", 4), ("🍎", 5), ("🍉", 6), ("🍐", 7),
    ("🍎", 8), ("🧺", 9), ("🍉", 10), ("🍐", 11), ("🍎", 12)
]

print("Lista original de frutas: " + display_fruits(fruits))  # Imprimir la lista original
print("Ejemplos: Manzana (🍎) < Peras (🍐) < Melón (🍉) < Cestas (🧺)")  # Mostrar el orden de las frutas

# Ordenación de burbuja
sorted_fruits_bubble = bubble_sort(fruits.copy()) # Ordenar una copia de la lista
print("Ordenación de burbuja: " + display_fruits(sorted_fruits_bubble)) # Imprimir el resultado

# Ordenación por inserción
sorted_fruits_insertion = insertion_sort(fruits.copy()) # Ordenar una copia de la lista
print("Ordenación por inserción: " + display_fruits(sorted_fruits_insertion)) # Imprimir el resultado

# Ordenación por selección
sorted_fruits_selection = selection_sort(fruits.copy()) # Ordenar una copia de la lista
print("Ordenación por selección: " + display_fruits(sorted_fruits_selection)) # Imprimir el resultado
```

**Explicación del código:**

1.  **`compare_fruits(fruit1, fruit2)`:** Esta función compara dos frutas por tamaño y devuelve -1 si la primera fruta es más pequeña, 1 si es más grande y 0 si son iguales. Utilizo el diccionario `order` para definir el orden de los tamaños de las frutas.
2.  **`bubble_sort(fruits)`:** Implemento el algoritmo de ordenación de burbuja, donde las frutas adyacentes se comparan y se intercambian si están en el orden incorrecto.
3.  **`insertion_sort(fruits)`:** Implemento el algoritmo de ordenación por inserción, donde cada nueva fruta se inserta en la posición correcta en la parte ya ordenada de la lista.
4.  **`selection_sort(fruits)`:** Implemento el algoritmo de ordenación por selección, donde en cada pasada encuentro la fruta más pequeña y la coloco en la posición correcta.
5.  **`display_fruits(fruits)`:** Esta función convierte una lista de frutas en una cadena para una salida conveniente.
6.  **Ejemplos:** Al final, creo una lista de frutas y aplico los tres algoritmos de ordenación, imprimiendo los resultados de cada uno. También le muestro el orden en que se ordenan las frutas.

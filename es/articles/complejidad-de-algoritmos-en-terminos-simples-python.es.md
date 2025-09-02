## Complejidad de algoritmos en términos simples y ejemplos en Python

En programación, existen muchas formas de resolver un mismo problema. Sin embargo, no todas las soluciones son igualmente eficientes. Uno de los aspectos clave a tener en cuenta al desarrollar algoritmos es su complejidad. Comprender la complejidad de un algoritmo permite estimar qué tan rápido funcionará y cuántos recursos (por ejemplo, memoria) requerirá para su ejecución, especialmente a medida que aumenta el volumen de datos de entrada. Comprender la complejidad de los algoritmos es una habilidad fundamental que permite escribir código más eficiente.

### ¿Qué es la complejidad de un algoritmo?

Imagina que tienes una tarea: encontrar un nombre específico en una guía telefónica.

*   **La forma sencilla (búsqueda lineal):** Tomas el libro y comienzas a hojear página por página hasta que encuentras el nombre que necesitas. Si el nombre está al final del libro, ¡tendrás que hojear todo el libro!
*   **La forma inteligente (búsqueda binaria):** Abres el libro por la mitad. Si el nombre que buscas está antes del nombre de esta página, cierras la segunda mitad del libro y buscas en la primera mitad. Si el nombre está después, buscas en la segunda mitad. Y así repites hasta que encuentres el nombre que necesitas. ¡Con cada paso, descartas la mitad del libro!

**La complejidad de un algoritmo** es una forma de describir cuánto "tiempo" (o recursos, como la memoria) necesitará un algoritmo para completar su tarea, dependiendo de cuán "grande" sea esa tarea.

*   **Búsqueda lineal:** Si hay 10 páginas en el libro, es posible que necesites hojear 10 páginas. Si hay 100 páginas en el libro, es posible que necesites hojear 100 páginas. La cantidad de trabajo crece *linealmente* con el tamaño de la tarea. Esto se llama **O(n)**, donde 'n' es el tamaño de la tarea (el número de páginas del libro).

*   **Búsqueda binaria:** Si hay 16 páginas en el libro, necesitarás un máximo de 4 pasos para encontrar el nombre. Si hay 32 páginas en el libro, necesitarás un máximo de 5 pasos. La cantidad de trabajo crece mucho más lentamente que el tamaño de la tarea. Esto se llama **O(log n)** (se lee "O de log n").



*   Un algoritmo **O(n)** se vuelve más lento *directamente proporcional* al aumento del tamaño de la tarea.
*   Un algoritmo **O(log n)** se vuelve más lento *mucho más lentamente* de lo que crece el tamaño de la tarea.



Imagina que estás desarrollando un motor de búsqueda. Si usas un algoritmo O(n) para buscar en Internet (que contiene miles de millones de páginas web), ¡tardará una cantidad de tiempo increíble! Y un algoritmo O(log n) manejará esta tarea mucho más rápido.

### Principales tipos de complejidad de algoritmos

Estos son algunos de los tipos de complejidad más comunes:

*   **O(1) – Complejidad constante:** El tiempo de ejecución es siempre el mismo, independientemente del tamaño de la tarea. Por ejemplo, tomar el primer elemento de una lista.

    ```python
    def get_first_element(my_list):
        """O(1) - Obtener el primer elemento de una lista."""
        return my_list[0]
    ```

*   **O(log n) – Complejidad logarítmica:** El tiempo de ejecución crece muy lentamente a medida que aumenta el tamaño de la tarea. Un gran ejemplo es la búsqueda binaria.

    ```python
    def binary_search(my_list, target):
        """O(log n) - Búsqueda binaria en una lista ordenada."""
        low = 0
        high = len(my_list) - 1

        while low <= high:
            mid = (low + high) // 2
            if my_list[mid] == target:
                return mid
            elif my_list[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1  # Elemento no encontrado
    ```

*   **O(n) – Complejidad lineal:** El tiempo de ejecución crece de forma directamente proporcional al tamaño de la tarea. Por ejemplo, recorrer cada elemento de una lista.

    ```python
    def linear_search(my_list, target):
        """O(n) - Búsqueda lineal en una lista."""
        for i in range(len(my_list)):
            if my_list[i] == target:
                return i
        return -1  # Elemento no encontrado
    ```

*   **O(n log n) – Complejidad lineal-logarítmica:**  A menudo se encuentra en algoritmos de ordenación eficientes, como Merge Sort y Quick Sort.

    ```python
    def merge_sort(my_list):
        """O(n log n) - Ordenamiento por fusión."""
        if len(my_list) <= 1:
            return my_list

        mid = len(my_list) // 2
        left = merge_sort(my_list[:mid])
        right = merge_sort(my_list[mid:])

        return merge(left, right)

    def merge(left, right):
        """Función auxiliar para merge_sort."""
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
    ```

*   **O(n^2) – Complejidad cuadrática:** El tiempo de ejecución crece *cuadráticamente* con el tamaño de la tarea. Por ejemplo, comparar cada elemento de una lista con cada otro elemento de la misma lista.

    ```python
    def bubble_sort(my_list):
        """O(n^2) - Ordenamiento de burbuja."""
        n = len(my_list)
        for i in range(n):
            for j in range(0, n-i-1):
                if my_list[j] > my_list[j+1] :
                    my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    ```

*   **O(2^n) – Complejidad exponencial:** El tiempo de ejecución crece muy rápidamente a medida que aumenta el tamaño de la tarea.  Suele encontrarse en algoritmos que utilizan la fuerza bruta.

    ```python
    def fibonacci_recursive(n):
      """O(2^n) - Cálculo recursivo del número de Fibonacci."""
      if n <= 1:
          return n
      return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    ```

*   **O(n!) – Complejidad factorial:** El tipo de complejidad más lento. Se produce al iterar sobre todas las posibles permutaciones de elementos.

### Ejemplos de problemas y algoritmos con diferente complejidad

Veamos algunos ejemplos de problemas y diferentes algoritmos para resolverlos para ver
cómo la complejidad afecta al rendimiento.

**1. Ordenar una lista:**

*   **Tarea:** Ordenar una lista de elementos en un orden específico (por ejemplo, ascendente).
*   **Algoritmos:**
    *   **Ordenamiento de burbuja (Bubble Sort):**

        ```python
        def bubble_sort(my_list):
            n = len(my_list)
            for i in range(n):
                for j in range(0, n-i-1):
                    if my_list[j] > my_list[j+1] :
                        my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
        # Ejemplo de uso
        my_list = [64, 34, 25, 12, 22, 11, 90]
        bubble_sort(my_list)
        print("Array ordenado:", my_list) # Salida: [11, 12, 22, 25, 34, 64, 90]
        ```

    *   **Ordenamiento por fusión (Merge Sort):**

        ```python
        def merge_sort(my_list):
            if len(my_list) <= 1:
                return my_list

            mid = len(my_list) // 2
            left = merge_sort(my_list[:mid])
            right = merge_sort(my_list[mid:])

            return merge(left, right)

        def merge(left, right):
            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        # Ejemplo de uso
        my_list = [64, 34, 25, 12, 22, 11, 90]
        sorted_list = merge_sort(my_list)
        print("Array ordenado:", sorted_list) # Salida: [11, 12, 22, 25, 34, 64, 90]
        ```
*   **Conclusión:** Para listas grandes de elementos, los algoritmos con O(n log n) (Merge Sort) son preferibles a los algoritmos con O(n^2) (Bubble Sort).

**2. Encontrar el camino más corto en un grafo:**

*   **Tarea:** Encontrar el camino más corto entre dos vértices de un grafo (por ejemplo, entre dos ciudades en un mapa).
*   **Algoritmos:**
    *   **Algoritmo de Dijkstra:**

        ```python
        import heapq

        def dijkstra(graph, start):
            """Algoritmo de Dijkstra para encontrar los caminos más cortos."""
            distances = {node: float('inf') for node in graph}
            distances[start] = 0
            priority_queue = [(0, start)]  # (distance, node)

            while priority_queue:
                distance, node = heapq.heappop(priority_queue)

                if distance > distances[node]:
                    continue

                for neighbor, weight in graph[node].items():
                    new_distance = distance + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        heapq.heappush(priority_queue, (new_distance, neighbor))

            return distances

        # Ejemplo de uso
        graph = {
            'A': {'B': 5, 'C': 1},
            'B': {'A': 5, 'C': 2, 'D': 1},
            'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
            'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
            'E': {'C': 8, 'D': 3},
            'F': {'D': 6}
        }
        start_node = 'A'
        shortest_paths = dijkstra(graph, start_node)
        print(f"Caminos más cortos desde {start_node}: {shortest_paths}")
        ```

*   **Conclusión:** La elección del algoritmo depende del tipo de grafo (ponderado/no ponderado, presencia de pesos negativos) y del tamaño del grafo. El algoritmo de Dijkstra es eficaz para grafos con pesos no negativos.

**3. Encontrar una subcadena en una cadena:**

*   **Tarea:** Encontrar todas las apariciones de una subcadena específica en una cadena más grande.
*   **Algoritmos:**
    *   **Búsqueda de cadena ingenua (Naive String Search):**

        ```python
        def naive_string_search(text, pattern):
            """Algoritmo de búsqueda de cadena ingenuo."""
            occurrences = []
            for i in range(len(text) - len(pattern) + 1):
                if text[i:i+len(pattern)] == pattern:
                    occurrences.append(i)
            return occurrences

        # Ejemplo de uso
        text = "This is a simple example text."
        pattern = "example"
        occurrences = naive_string_search(text, pattern)
        print(f"Apariciones de '{pattern}' en el texto: {occurrences}")  # Salida: [17]
        ```

*   **Conclusión:** Para búsquedas frecuentes de subcadenas en cadenas grandes, existen algoritmos más eficientes, como KMP.

**4. Problema de la mochila (Knapsack Problem):**

*   **Tarea:** Tienes una mochila de una capacidad determinada y un conjunto de artículos con diferentes pesos y valores. Debes elegir los artículos que maximicen el valor total, sin exceder la capacidad de la mochila.
*   **Algoritmos:**
    *   **Programación dinámica (Dynamic Programming):**

        ```python
        def knapsack_dynamic_programming(capacity, weights, values, n):
            """Resolución del problema de la mochila mediante programación dinámica."""
            dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

            for i in range(n + 1):
                for w in range(capacity + 1):
                    if i == 0 or w == 0:
                        dp[i][w] = 0
                    elif weights[i-1] <= w:
                        dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]],  dp[i-1][w])
                    else:
                        dp[i][w] = dp[i-1][w]

            return dp[n][capacity]

        # Ejemplo de uso
        capacity = 50
        weights = [10, 20, 30]
        values = [60, 100, 120]
        n = len(values)
        max_value = knapsack_dynamic_programming(capacity, weights, values, n)
        print(f"Valor máximo: {max_value}")  # Salida: 220
        ```

*   **La elección del algoritmo depende del tamaño del problema y de los requisitos de precisión de la solución.**

###  Notación Big O: simplificación de la complejidad

Normalmente, la complejidad se describe usando la "O grande" (notación O). Muestra la rapidez con la que crece el tiempo de ejecución de un algoritmo con el tamaño de la tarea, *asintóticamente*, es decir, para valores muy grandes de `n`. Las constantes menores y los detalles de implementación suelen ignorarse. Por ejemplo, un algoritmo que realiza `2n + 5` operaciones se sigue considerando *O(n)*.

###  Peor de los casos, caso promedio, mejor de los casos

La complejidad de un algoritmo puede depender de los datos de entrada. Normalmente hablamos de complejidad en el *peor de los casos*: esta es la cantidad máxima de tiempo o recursos que un algoritmo puede requerir. A veces, también se analiza la complejidad en el caso promedio y en el mejor de los casos.

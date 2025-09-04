## Złożoność algorytmów w prostych słowach i przykłady w Pythonie

W programowaniu istnieje wiele sposobów rozwiązania tego samego problemu. Jednak nie wszystkie rozwiązania są równie skuteczne. Jednym z kluczowych aspektów, które należy wziąć pod uwagę podczas opracowywania algorytmów, jest ich złożoność. Zrozumienie złożoności algorytmu pozwala oszacować, jak szybko będzie działał i ile zasobów (np. pamięci) będzie wymagał do swojego wykonania, zwłaszcza gdy wzrasta objętość danych wejściowych. Zrozumienie złożoności algorytmów jest podstawową umiejętnością, która pozwala pisać bardziej efektywny kod.

### Co to jest złożoność algorytmu?

Wyobraź sobie, że masz zadanie: znaleźć konkretne nazwisko w książce telefonicznej.

*   **Prosty sposób (wyszukiwanie liniowe):** Bierzesz książkę i zaczynasz przewracać stronę po stronie, aż znajdziesz potrzebne nazwisko. Jeśli nazwisko znajduje się na samym końcu książki, będziesz musiał przewrócić całą książkę!
*   **Inteligentny sposób (wyszukiwanie binarne):** Otwierasz książkę na środku. Jeśli nazwisko, którego szukasz, znajduje się przed nazwiskiem na tej stronie, zamykasz drugą połowę książki i szukasz w pierwszej połowie. Jeśli nazwisko znajduje się później, szukasz w drugiej połowie. I tak powtarzasz, aż znajdziesz potrzebne nazwisko. Z każdym krokiem odrzucasz połowę książki!

**Złożoność algorytmu** to sposób opisania, ile "czasu" (lub zasobów, takich jak pamięć) algorytm będzie potrzebował do wykonania swojego zadania, w zależności od tego, jak "duże" jest to zadanie.

*   **Wyszukiwanie liniowe:** Jeśli w książce jest 10 stron, być może będziesz musiał przewrócić 10 stron. Jeśli w książce jest 100 stron, być może będziesz musiał przewrócić 100 stron. Ilość pracy rośnie *liniowo* wraz z rozmiarem zadania. Nazywa się to **O(n)**, gdzie 'n' to rozmiar zadania (liczba stron w książce).

*   **Wyszukiwanie binarne:** Jeśli w książce jest 16 stron, będziesz potrzebował maksymalnie 4 kroków, aby znaleźć nazwisko. Jeśli w książce jest 32 strony, będziesz potrzebował maksymalnie 5 kroków. Ilość pracy rośnie znacznie wolniej niż rozmiar zadania. Nazywa się to **O(log n)** (czytaj "O od log n").



*   Algorytm **O(n)** staje się wolniejszy *bezpośrednio proporcjonalnie* do wzrostu rozmiaru zadania.
*   Algorytm **O(log n)** staje się wolniejszy *znacznie wolniej* niż rozmiar zadania rośnie.



Wyobraź sobie, że rozwijasz wyszukiwarkę. Jeśli użyjesz algorytmu O(n) do przeszukiwania Internetu (który zawiera miliardy stron internetowych), zajmie to niewiarygodnie dużo czasu! A algorytm O(log n) poradzi sobie z tym zadaniem znacznie szybciej.

### Główne typy złożoności algorytmów

Oto niektóre z najczęstszych typów złożoności:

*   **O(1) – Złożoność stała:** Czas wykonania jest zawsze taki sam, niezależnie od rozmiaru zadania. Na przykład pobranie pierwszego elementu z listy.

    ```python
    def get_first_element(my_list):
        """O(1) - Pobieranie pierwszego elementu listy."""
        return my_list[0]
    ```

*   **O(log n) – Złożoność logarytmiczna:** Czas wykonania rośnie bardzo powoli wraz ze wzrostem rozmiaru zadania. Doskonałym przykładem jest wyszukiwanie binarne.

    ```python
    def binary_search(my_list, target):
        """O(log n) - Wyszukiwanie binarne w posortowanej liście."""
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
        return -1  # Element nie znaleziony
    ```

*   **O(n) – Złożoność liniowa:** Czas wykonania rośnie bezpośrednio proporcjonalnie do rozmiaru zadania. Na przykład iteracja po każdym elemencie listy.

    ```python
    def linear_search(my_list, target):
        """O(n) - Wyszukiwanie liniowe w liście."""
        for i in range(len(my_list)):
            if my_list[i] == target:
                return i
        return -1  # Element nie znaleziony
    ```

*   **O(n log n) – Złożoność liniowo-logarytmiczna:**  Często spotykana w efektywnych algorytmach sortowania, takich jak sortowanie przez scalanie i sortowanie szybkie.

    ```python
    def merge_sort(my_list):
        """O(n log n) - Sortowanie przez scalanie."""
        if len(my_list) <= 1:
            return my_list

        mid = len(my_list) // 2
        left = merge_sort(my_list[:mid])
        right = merge_sort(my_list[mid:])

        return merge(left, right)

    def merge(left, right):
        """Funkcja pomocnicza dla merge_sort."""
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

*   **O(n^2) – Złożoność kwadratowa:** Czas wykonania rośnie *kwadratowo* wraz z rozmiarem zadania. Na przykład porównywanie każdego elementu listy z każdym innym elementem tej samej listy.

    ```python
    def bubble_sort(my_list):
        """O(n^2) - Sortowanie bąbelkowe."""
        n = len(my_list)
        for i in range(n):
            for j in range(0, n-i-1):
                if my_list[j] > my_list[j+1] :
                    my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    ```

*   **O(2^n) – Złożoność wykładnicza:** Czas wykonania rośnie bardzo szybko wraz ze wzrostem rozmiaru zadania.  Zazwyczaj spotykana w algorytmach, które używają siły brutalnej.

    ```python
    def fibonacci_recursive(n):
      """O(2^n) - Rekurencyjne obliczanie liczby Fibonacciego."""
      if n <= 1:
          return n
      return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    ```

*   **O(n!) – Złożoność silni:** Najwolniejszy typ złożoności. Występuje podczas iteracji po wszystkich możliwych permutacjach elementów.

### Przykłady problemów i algorytmów o różnej złożoności

Przyjrzyjmy się kilku przykładom problemów i różnym algorytmom do ich rozwiązania, aby zobaczyć,
jak złożoność wpływa na wydajność.

**1. Sortowanie listy:**

*   **Zadanie:** Posortowanie listy elementów w określonej kolejności (np. rosnąco).
*   **Algorytmy:**
    *   **Sortowanie bąbelkowe (Bubble Sort):**

        ```python
        def bubble_sort(my_list):
            n = len(my_list)
            for i in range(n):
                for j in range(0, n-i-1):
                    if my_list[j] > my_list[j+1] :
                        my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
        # Przykład użycia
        my_list = [64, 34, 25, 12, 22, 11, 90]
        bubble_sort(my_list)
        print("Posortowana tablica:", my_list) # Wyjście: [11, 12, 22, 25, 34, 64, 90]
        ```

    *   **Sortowanie przez scalanie (Merge Sort):**

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

        # Przykład użycia
        my_list = [64, 34, 25, 12, 22, 11, 90]
        sorted_list = merge_sort(my_list)
        print("Posortowana tablica:", sorted_list) # Wyjście: [11, 12, 22, 25, 34, 64, 90]
        ```
*   **Wniosek:** Dla dużych list elementów algorytmy z O(n log n) (sortowanie przez scalanie) są preferowane w stosunku do algorytmów z O(n^2) (sortowanie bąbelkowe).

**2. Znajdowanie najkrótszej ścieżki w grafie:**

*   **Zadanie:** Znajdowanie najkrótszej ścieżki między dwoma wierzchołkami w grafie (np. między dwoma miastami na mapie).
*   **Algorytmy:**
    *   **Algorytm Dijkstry:**

        ```python
        import heapq

        def dijkstra(graph, start):
            """Algorytm Dijkstry do znajdowania najkrótszych ścieżek."""
            distances = {node: float('inf') for node in graph}
            distances[start] = 0
            priority_queue = [(0, start)]  # (odległość, węzeł)

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

        # Przykład użycia
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
        print(f"Najkrótsze ścieżki z {start_node}: {shortest_paths}")
        ```

*   **Wniosek:** Wybór algorytmu zależy od typu grafu (ważony/nieważony, obecność wag ujemnych) i rozmiaru grafu. Algorytm Dijkstry jest skuteczny dla grafów z wagami nieujemnymi.

**3. Znajdowanie podciągu w ciągu:**

*   **Zadanie:** Znajdowanie wszystkich wystąpień określonego podciągu w większym ciągu.
*   **Algorytmy:**
    *   **Naiwne wyszukiwanie ciągu (Naive String Search):**

        ```python
        def naive_string_search(text, pattern):
            """Naiwny algorytm wyszukiwania ciągu."""
            occurrences = []
            for i in range(len(text) - len(pattern) + 1):
                if text[i:i+len(pattern)] == pattern:
                    occurrences.append(i)
            return occurrences

        # Przykład użycia
        text = "To jest prosty tekst przykładowy."
        pattern = "przykładowy"
        occurrences = naive_string_search(text, pattern)
        print(f"Wystąpienia '{pattern}' w tekście: {occurrences}")  # Wyjście: [17]
        ```

*   **Wniosek:** Do częstego wyszukiwania podciągów w dużych ciągach istnieją bardziej efektywne algorytmy, takie jak KMP.

**4. Problem plecakowy (Knapsack Problem):**

*   **Zadanie:** Masz plecak o określonej pojemności i zestaw przedmiotów o różnych wagach i wartościach. Musisz wybrać przedmioty, które zmaksymalizują całkowitą wartość, nie przekraczając pojemności plecaka.
*   **Algorytmy:**
    *   **Programowanie dynamiczne (Dynamic Programming):**

        ```python
        def knapsack_dynamic_programming(capacity, weights, values, n):
            """Rozwiązywanie problemu plecakowego za pomocą programowania dynamicznego."""
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

        # Przykład użycia
        capacity = 50
        weights = [10, 20, 30]
        values = [60, 100, 120]
        n = len(values)
        max_value = knapsack_dynamic_programming(capacity, weights, values, n)
        print(f"Maksymalna wartość: {max_value}")  # Wyjście: 220
        ```

*   **Wybór algorytmu zależy od rozmiaru problemu i wymagań dotyczących dokładności rozwiązania.**

###  Notacja Big O: uproszczenie złożoności

Zazwyczaj złożoność opisuje się za pomocą "dużego O" (notacja O). Pokazuje ona, jak szybko czas wykonania algorytmu rośnie wraz z rozmiarem zadania, *asymptotycznie*, czyli dla bardzo dużych wartości `n`. Mniejsze stałe i szczegóły implementacji są zazwyczaj ignorowane. Na przykład algorytm, który wykonuje `2n + 5` operacji, nadal jest uważany za *O(n)*.

###  Najgorszy przypadek, średni przypadek, najlepszy przypadek

Złożoność algorytmu może zależeć od danych wejściowych. Zazwyczaj mówimy o złożoności w *najgorszym przypadku* – jest to maksymalna ilość czasu lub zasobów, jakich algorytm może wymagać. Czasami analizuje się również złożoność w przypadku średnim i najlepszym.

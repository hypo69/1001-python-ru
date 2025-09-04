## Algorithmuskomplexität in einfachen Worten und Python-Beispiele

In der Programmierung gibt es viele Wege, dasselbe Problem zu lösen. Allerdings sind nicht alle Lösungen gleich effektiv. Einer der wichtigsten Aspekte, die bei der Entwicklung von Algorithmen berücksichtigt werden müssen, ist ihre Komplexität. Das Verständnis der Komplexität eines Algorithmus ermöglicht es, abzuschätzen, wie schnell er arbeiten wird und wie viele Ressourcen (z.B. Speicher) er für seine Ausführung benötigt, insbesondere wenn das Volumen der Eingabedaten zunimmt. Das Verständnis der Algorithmuskomplexität ist eine grundlegende Fähigkeit, die es Ihnen ermöglicht, effizienteren Code zu schreiben.

### Was ist Algorithmuskomplexität?

Stellen Sie sich vor, Sie haben eine Aufgabe: einen bestimmten Namen in einem Telefonbuch zu finden.

*   **Der einfache Weg (lineare Suche):** Sie nehmen das Buch und blättern Seite für Seite durch, bis Sie den Namen finden, den Sie benötigen. Wenn der Name ganz am Ende des Buches steht, müssen Sie das gesamte Buch durchblättern!
*   **Der intelligente Weg (binäre Suche):** Sie öffnen das Buch in der Mitte. Wenn der gesuchte Name vor dem Namen auf dieser Seite steht, schließen Sie die zweite Hälfte des Buches und suchen in der ersten Hälfte. Wenn der Name später kommt, suchen Sie in der zweiten Hälfte. Und so wiederholen Sie, bis Sie den Namen finden, den Sie benötigen. Mit jedem Schritt verwerfen Sie die Hälfte des Buches!

**Algorithmuskomplexität** ist eine Möglichkeit zu beschreiben, wie viel "Zeit" (oder Ressourcen, wie Speicher) ein Algorithmus benötigt, um seine Aufgabe zu erfüllen, abhängig davon, wie "groß" diese Aufgabe ist.

*   **Lineare Suche:** Wenn das Buch 10 Seiten hat, müssen Sie möglicherweise 10 Seiten durchblättern. Wenn das Buch 100 Seiten hat, müssen Sie möglicherweise 100 Seiten durchblättern. Die Arbeitsmenge wächst *linear* mit der Größe der Aufgabe. Dies wird als **O(n)** bezeichnet, wobei 'n' die Größe der Aufgabe ist (die Anzahl der Seiten im Buch).

*   **Binäre Suche:** Wenn das Buch 16 Seiten hat, benötigen Sie maximal 4 Schritte, um den Namen zu finden. Wenn das Buch 32 Seiten hat, benötigen Sie maximal 5 Schritte. Die Arbeitsmenge wächst viel langsamer als die Größe der Aufgabe. Dies wird als **O(log n)** bezeichnet (gelesen "O von log n").



*   Ein **O(n)** Algorithmus wird langsamer *direkt proportional* zur Zunahme der Aufgabengröße.
*   Ein **O(log n)** Algorithmus wird *viel langsamer* langsamer, als die Aufgabengröße wächst.



Stellen Sie sich vor, Sie entwickeln eine Suchmaschine. Wenn Sie einen O(n)-Algorithmus verwenden, um das Internet zu durchsuchen (das Milliarden von Webseiten enthält), wird dies unglaublich lange dauern! Und ein O(log n)-Algorithmus wird diese Aufgabe viel schneller erledigen.

### Haupttypen der Algorithmuskomplexität

Hier sind einige der häufigsten Komplexitätstypen:

*   **O(1) – Konstante Komplexität:** Die Ausführungszeit ist immer gleich, unabhängig von der Größe der Aufgabe. Zum Beispiel das Entnehmen des ersten Elements aus einer Liste.

    ```python
    def get_first_element(my_list):
        """O(1) - Das erste Element einer Liste abrufen."""
        return my_list[0]
    ```

*   **O(log n) – Logarithmische Komplexität:** Die Ausführungszeit wächst sehr langsam, wenn die Größe der Aufgabe zunimmt. Ein großartiges Beispiel ist die binäre Suche.

    ```python
    def binary_search(my_list, target):
        """O(log n) - Binäre Suche in einer sortierten Liste."""
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
        return -1  # Element nicht gefunden
    ```

*   **O(n) – Lineare Komplexität:** Die Ausführungszeit wächst direkt proportional zur Größe der Aufgabe. Zum Beispiel das Durchlaufen jedes Elements in einer Liste.

    ```python
    def linear_search(my_list, target):
        """O(n) - Lineare Suche in einer Liste."""
        for i in range(len(my_list)):
            if my_list[i] == target:
                return i
        return -1  # Element nicht gefunden
    ```

*   **O(n log n) – Linear-logarithmische Komplexität:**  Oft in effizienten Sortieralgorithmen wie Mergesort und Quicksort zu finden.

    ```python
    def merge_sort(my_list):
        """O(n log n) - Mergesort."""
        if len(my_list) <= 1:
            return my_list

        mid = len(my_list) // 2
        left = merge_sort(my_list[:mid])
        right = merge_sort(my_list[mid:])

        return merge(left, right)

    def merge(left, right):
        """Hilfsfunktion für Mergesort."""
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

*   **O(n^2) – Quadratische Komplexität:** Die Ausführungszeit wächst *quadratisch* mit der Größe der Aufgabe. Zum Beispiel das Vergleichen jedes Elements in einer Liste mit jedem anderen Element in derselben Liste.

    ```python
    def bubble_sort(my_list):
        """O(n^2) - Bubblesort."""
        n = len(my_list)
        for i in range(n):
            for j in range(0, n-i-1):
                if my_list[j] > my_list[j+1] :
                    my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    ```

*   **O(2^n) – Exponentielle Komplexität:** Die Ausführungszeit wächst sehr schnell, wenn die Größe der Aufgabe zunimmt.  Normalerweise in Algorithmen zu finden, die Brute-Force verwenden.

    ```python
    def fibonacci_recursive(n):
      """O(2^n) - Rekursive Berechnung der Fibonacci-Zahl."""
      if n <= 1:
          return n
      return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    ```

*   **O(n!) – Fakultätskomplexität:** Der langsamste Komplexitätstyp. Tritt auf, wenn alle möglichen Permutationen von Elementen durchlaufen werden.

### Beispiele für Probleme und Algorithmen mit unterschiedlicher Komplexität

Betrachten wir einige Beispiele für Probleme und verschiedene Algorithmen zu deren Lösung, um zu sehen,
wie die Komplexität die Leistung beeinflusst.

**1. Sortieren einer Liste:**

*   **Aufgabe:** Eine Liste von Elementen in einer bestimmten Reihenfolge sortieren (z.B. aufsteigend).
*   **Algorithmen:**
    *   **Bubblesort:**

        ```python
        def bubble_sort(my_list):
            n = len(my_list)
            for i in range(n):
                for j in range(0, n-i-1):
                    if my_list[j] > my_list[j+1] :
                        my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
        # Anwendungsbeispiel
        my_list = [64, 34, 25, 12, 22, 11, 90]
        bubble_sort(my_list)
        print("Sortiertes Array:", my_list) # Ausgabe: [11, 12, 22, 25, 34, 64, 90]
        ```

    *   **Mergesort:**

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

        # Anwendungsbeispiel
        my_list = [64, 34, 25, 12, 22, 11, 90]
        sorted_list = merge_sort(my_list)
        print("Sortiertes Array:", sorted_list) # Ausgabe: [11, 12, 22, 25, 34, 64, 90]
        ```
*   **Fazit:** Für große Listen von Elementen sind Algorithmen mit O(n log n) (Mergesort) Algorithmen mit O(n^2) (Bubblesort) vorzuziehen.

**2. Finden des kürzesten Pfades in einem Graphen:**

*   **Aufgabe:** Den kürzesten Pfad zwischen zwei Knoten in einem Graphen finden (z.B. zwischen zwei Städten auf einer Karte).
*   **Algorithmen:**
    *   **Dijkstras Algorithmus:**

        ```python
        import heapq

        def dijkstra(graph, start):
            """Dijkstras Algorithmus zum Finden der kürzesten Pfade."""
            distances = {node: float('inf') for node in graph}
            distances[start] = 0
            priority_queue = [(0, start)]  # (Distanz, Knoten)

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

        # Anwendungsbeispiel
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
        print(f"Kürzeste Pfade von {start_node}: {shortest_paths}")
        ```

*   **Fazit:** Die Wahl des Algorithmus hängt vom Graphentyp (gewichtet/ungewichtet, Vorhandensein negativer Gewichte) und der Größe des Graphen ab. Dijkstras Algorithmus ist effektiv für Graphen mit nicht-negativen Gewichten.

**3. Finden eines Teilstrings in einem String:**

*   **Aufgabe:** Alle Vorkommen eines bestimmten Teilstrings in einem größeren String finden.
*   **Algorithmen:**
    *   **Naives String-Suchen (Naive String Search):**

        ```python
        def naive_string_search(text, pattern):
            """Naives String-Suchalgorithmus."""
            occurrences = []
            for i in range(len(text) - len(pattern) + 1):
                if text[i:i+len(pattern)] == pattern:
                    occurrences.append(i)
            return occurrences

        # Anwendungsbeispiel
        text = "Dies ist ein einfacher Beispieltext."
        pattern = "Beispiel"
        occurrences = naive_string_search(text, pattern)
        print(f"Vorkommen von '{pattern}' im Text: {occurrences}")  # Ausgabe: [17]
        ```

*   **Fazit:** Für häufige Teilstring-Suchen in großen Strings gibt es effizientere Algorithmen wie KMP.

**4. Rucksackproblem (Knapsack Problem):**

*   **Aufgabe:** Sie haben einen Rucksack mit einer bestimmten Kapazität und eine Reihe von Gegenständen mit unterschiedlichen Gewichten und Werten. Sie müssen Gegenstände auswählen, die den Gesamtwert maximieren, ohne die Kapazität des Rucksacks zu überschreiten.
*   **Algorithmen:**
    *   **Dynamische Programmierung (Dynamic Programming):**

        ```python
        def knapsack_dynamic_programming(capacity, weights, values, n):
            """Lösung des Rucksackproblems mittels dynamischer Programmierung."""
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

        # Anwendungsbeispiel
        capacity = 50
        weights = [10, 20, 30]
        values = [60, 100, 120]
        n = len(values)
        max_value = knapsack_dynamic_programming(capacity, weights, values, n)
        print(f"Maximalwert: {max_value}")  # Ausgabe: 220
        ```

*   **Die Wahl des Algorithmus hängt von der Problemgröße und den Anforderungen an die Genauigkeit der Lösung ab.**

###  Big O Notation: Vereinfachung der Komplexität

Normalerweise wird die Komplexität mit der "Big O"-Notation (O-Notation) beschrieben. Sie zeigt, wie schnell die Ausführungszeit eines Algorithmus mit der Größe der Aufgabe *asymptotisch* wächst, d.h. für sehr große Werte von `n`. Kleinere Konstanten und Implementierungsdetails werden normalerweise ignoriert. Zum Beispiel wird ein Algorithmus, der `2n + 5` Operationen ausführt, immer noch als *O(n)* betrachtet.

###  Worst Case, Average Case, Best Case

Die Komplexität eines Algorithmus kann von den Eingabedaten abhängen. Wir sprechen normalerweise von der Komplexität im *Worst Case* – dies ist die maximale Zeit- oder Ressourcenmenge, die ein Algorithmus benötigen kann. Manchmal wird auch die Komplexität im Average Case und Best Case analysiert.

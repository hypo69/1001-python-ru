## Complessità degli algoritmi in termini semplici ed esempi Python

Nella programmazione, ci sono molti modi per risolvere lo stesso problema. Tuttavia, non tutte le soluzioni sono ugualmente efficaci. Uno degli aspetti chiave da considerare quando si sviluppano algoritmi è la loro complessità. Comprendere la complessità di un algoritmo consente di stimare quanto velocemente funzionerà e quante risorse (ad esempio, memoria) richiederà per la sua esecuzione, soprattutto all'aumentare del volume dei dati di input. Comprendere la complessità degli algoritmi è un'abilità fondamentale che consente di scrivere codice più efficiente.

### Cos'è la complessità di un algoritmo?

Immagina di avere un compito: trovare un nome specifico in un elenco telefonico.

*   **Il modo semplice (ricerca lineare):** Prendi l'elenco e inizi a sfogliare pagina per pagina finché non trovi il nome che ti serve. Se il nome è alla fine dell'elenco, dovrai sfogliare l'intero elenco!
*   **Il modo intelligente (ricerca binaria):** Apri l'elenco a metà. Se il nome che cerchi è prima del nome su questa pagina, chiudi la seconda metà dell'elenco e cerchi nella prima metà. Se il nome è dopo, cerchi nella seconda metà. E così ripeti finché non trovi il nome che ti serve. Ad ogni passo, scarti metà dell'elenco!

**La complessità di un algoritmo** è un modo per descrivere quanto "tempo" (o risorse, come la memoria) un algoritmo avrà bisogno per completare il suo compito, a seconda di quanto "grande" è quel compito.

*   **Ricerca lineare:** Se ci sono 10 pagine nell'elenco, potresti dover sfogliare 10 pagine. Se ci sono 100 pagine nell'elenco, potresti dover sfogliare 100 pagine. La quantità di lavoro cresce *linearmente* con la dimensione del compito. Questo è chiamato **O(n)**, dove 'n' è la dimensione del compito (il numero di pagine nell'elenco).

*   **Ricerca binaria:** Se ci sono 16 pagine nell'elenco, avrai bisogno di un massimo di 4 passaggi per trovare il nome. Se ci sono 32 pagine nell'elenco, avrai bisogno di un massimo di 5 passaggi. La quantità di lavoro cresce molto più lentamente della dimensione del compito. Questo è chiamato **O(log n)** (si legge "O di log n").



*   Un algoritmo **O(n)** diventa più lento *direttamente proporzionale* all'aumento della dimensione del compito.
*   Un algoritmo **O(log n)** diventa più lento *molto più lentamente* di quanto cresca la dimensione del compito.



Immagina di sviluppare un motore di ricerca. Se usi un algoritmo O(n) per cercare su Internet (che contiene miliardi di pagine web), ci vorrà un tempo incredibilmente lungo! E un algoritmo O(log n) gestirà questo compito molto più velocemente.

### Principali tipi di complessità degli algoritmi

Ecco alcuni dei tipi di complessità più comuni:

*   **O(1) – Complessità costante:** Il tempo di esecuzione è sempre lo stesso, indipendentemente dalla dimensione del compito. Ad esempio, prendere il primo elemento da una lista.

    ```python
    def get_first_element(my_list):
        """O(1) - Ottenere il primo elemento di una lista."""
        return my_list[0]
    ```

*   **O(log n) – Complessità logaritmica:** Il tempo di esecuzione cresce molto lentamente all'aumentare della dimensione del compito. Un ottimo esempio è la ricerca binaria.

    ```python
    def binary_search(my_list, target):
        """O(log n) - Ricerca binaria in una lista ordinata."""
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
        return -1  # Elemento non trovato
    ```

*   **O(n) – Complessità lineare:** Il tempo di esecuzione cresce direttamente proporzionale alla dimensione del compito. Ad esempio, iterare su ogni elemento di una lista.

    ```python
    def linear_search(my_list, target):
        """O(n) - Ricerca lineare in una lista."""
        for i in range(len(my_list)):
            if my_list[i] == target:
                return i
        return -1  # Elemento non trovato
    ```

*   **O(n log n) – Complessità lineare-logaritmica:**  Spesso si trova in algoritmi di ordinamento efficienti, come Merge Sort e Quick Sort.

    ```python
    def merge_sort(my_list):
        """O(n log n) - Merge sort."""
        if len(my_list) <= 1:
            return my_list

        mid = len(my_list) // 2
        left = merge_sort(my_list[:mid])
        right = merge_sort(my_list[mid:])

        return merge(left, right)

    def merge(left, right):
        """Funzione di supporto per merge_sort."""
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

*   **O(n^2) – Complessità quadratica:** Il tempo di esecuzione cresce *quadraticamente* con la dimensione del compito. Ad esempio, confrontare ogni elemento di una lista con ogni altro elemento della stessa lista.

    ```python
    def bubble_sort(my_list):
        """O(n^2) - Bubble sort."""
        n = len(my_list)
        for i in range(n):
            for j in range(0, n-i-1):
                if my_list[j] > my_list[j+1] :
                    my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    ```

*   **O(2^n) – Complessità esponenziale:** Il tempo di esecuzione cresce molto rapidamente all'aumentare della dimensione del compito.  Di solito si trova in algoritmi che usano la forza bruta.

    ```python
    def fibonacci_recursive(n):
      """O(2^n) - Calcolo ricorsivo del numero di Fibonacci."""
      if n <= 1:
          return n
      return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    ```

*   **O(n!) – Complessità fattoriale:** Il tipo di complessità più lento. Si verifica quando si itera su tutte le possibili permutazioni di elementi.

### Esempi di problemi e algoritmi con complessità diversa

Vediamo alcuni esempi di problemi e diversi algoritmi per risolverli per vedere
come la complessità influisce sulle prestazioni.

**1. Ordinamento di una lista:**

*   **Compito:** Ordinare una lista di elementi in un ordine specifico (ad esempio, crescente).
*   **Algoritmi:**
    *   **Bubble Sort:**

        ```python
        def bubble_sort(my_list):
            n = len(my_list)
            for i in range(n):
                for j in range(0, n-i-1):
                    if my_list[j] > my_list[j+1] :
                        my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
        # Esempio di utilizzo
        my_list = [64, 34, 25, 12, 22, 11, 90]
        bubble_sort(my_list)
        print("Array ordinato:", my_list) # Output: [11, 12, 22, 25, 34, 64, 90]
        ```

    *   **Merge Sort:**

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

        # Esempio di utilizzo
        my_list = [64, 34, 25, 12, 22, 11, 90]
        sorted_list = merge_sort(my_list)
        print("Array ordinato:", sorted_list) # Output: [11, 12, 22, 25, 34, 64, 90]
        ```
*   **Conclusione:** Per liste di elementi di grandi dimensioni, gli algoritmi con O(n log n) (Merge Sort) sono preferibili agli algoritmi con O(n^2) (Bubble Sort).

**2. Ricerca del percorso più breve in un grafo:**

*   **Compito:** Trovare il percorso più breve tra due vertici in un grafo (ad esempio, tra due città su una mappa).
*   **Algoritmi:**
    *   **Algoritmo di Dijkstra:**

        ```python
        import heapq

        def dijkstra(graph, start):
            """Algoritmo di Dijkstra per la ricerca dei percorsi più brevi."""
            distances = {node: float('inf') for node in graph}
            distances[start] = 0
            priority_queue = [(0, start)]  # (distanza, nodo)

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

        # Esempio di utilizzo
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
        print(f"Percorsi più brevi da {start_node}: {shortest_paths}")
        ```

*   **Conclusione:** La scelta dell'algoritmo dipende dal tipo di grafo (pesato/non pesato, presenza di pesi negativi) e dalla dimensione del grafo. L'algoritmo di Dijkstra è efficace per grafi con pesi non negativi.

**3. Ricerca di una sottostringa in una stringa:**

*   **Compito:** Trovare tutte le occorrenze di una sottostringa specifica in una stringa più grande.
*   **Algoritmi:**
    *   **Ricerca di stringa ingenua (Naive String Search):**

        ```python
        def naive_string_search(text, pattern):
            """Algoritmo di ricerca di stringa ingenuo."""
            occurrences = []
            for i in range(len(text) - len(pattern) + 1):
                if text[i:i+len(pattern)] == pattern:
                    occurrences.append(i)
            return occurrences

        # Esempio di utilizzo
        text = "Questo è un semplice testo di esempio."
        pattern = "esempio"
        occurrences = naive_string_search(text, pattern)
        print(f"Occorrenze di '{pattern}' nel testo: {occurrences}")  # Output: [17]
        ```

*   **Conclusione:** Per ricerche frequenti di sottostringhe in stringhe di grandi dimensioni, esistono algoritmi più efficienti, come KMP.

**4. Problema dello zaino (Knapsack Problem):**

*   **Compito:** Hai uno zaino di una certa capacità e un set di oggetti con pesi e valori diversi. Devi scegliere gli oggetti che massimizzano il valore totale, senza superare la capacità dello zaino.
*   **Algoritmi:**
    *   **Programmazione dinamica (Dynamic Programming):**

        ```python
        def knapsack_dynamic_programming(capacity, weights, values, n):
            """Risoluzione del problema dello zaino tramite programmazione dinamica."""
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

        # Esempio di utilizzo
        capacity = 50
        weights = [10, 20, 30]
        values = [60, 100, 120]
        n = len(values)
        max_value = knapsack_dynamic_programming(capacity, weights, values, n)
        print(f"Valore massimo: {max_value}")  # Output: 220
        ```

*   **La scelta dell'algoritmo dipende dalla dimensione del problema e dai requisiti di precisione della soluzione.**

###  Notazione Big O: semplificazione della complessità

Di solito, la complessità viene descritta usando la "Big O" (notazione O). Mostra quanto velocemente il tempo di esecuzione di un algoritmo cresce con la dimensione del compito, *asintoticamente*, cioè per valori molto grandi di `n`. Costanti minori e dettagli di implementazione vengono solitamente ignorati. Ad esempio, un algoritmo che esegue `2n + 5` operazioni è ancora considerato *O(n)*.

###  Caso peggiore, caso medio, caso migliore

La complessità di un algoritmo può dipendere dai dati di input. Di solito parliamo di complessità nel *caso peggiore* – questa è la quantità massima di tempo o risorse che un algoritmo può richiedere. A volte, viene analizzata anche la complessità nel caso medio e nel caso migliore.

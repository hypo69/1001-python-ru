## La complexité des algorithmes en termes simples et exemples en Python

En programmation, il existe de nombreuses façons de résoudre un même problème. Cependant, toutes les solutions ne sont pas aussi efficaces. L'un des aspects clés à prendre en compte lors du développement d'algorithmes est leur complexité. Comprendre la complexité d'un algorithme permet d'estimer la rapidité avec laquelle il fonctionnera et la quantité de ressources (par exemple, la mémoire) qu'il nécessitera pour son exécution, en particulier lorsque le volume des données d'entrée augmente. Comprendre la complexité des algorithmes est une compétence fondamentale qui permet d'écrire du code plus efficace.

### Qu'est-ce que la complexité d'un algorithme ?

Imaginez que vous ayez une tâche : trouver un nom spécifique dans un annuaire téléphonique.

*   **La manière simple (recherche linéaire) :** Vous prenez le livre et commencez à feuilleter page par page jusqu'à ce que vous trouviez le nom que vous cherchez. Si le nom se trouve à la toute fin du livre, vous devrez feuilleter tout le livre !
*   **La manière intelligente (recherche binaire) :** Vous ouvrez le livre au milieu. Si le nom que vous cherchez se trouve avant le nom sur cette page, vous fermez la seconde moitié du livre et cherchez dans la première moitié. Si le nom vient après, vous cherchez dans la seconde moitié. Et ainsi de suite, jusqu'à ce que vous trouviez le nom que vous cherchez. À chaque étape, vous écartez la moitié du livre !

**La complexité d'un algorithme** est une façon de décrire le temps (ou les ressources, comme la mémoire) qu'il faudra à un algorithme pour accomplir sa tâche, en fonction de la "taille" de cette tâche.

*   **Recherche linéaire :** S'il y a 10 pages dans le livre, vous devrez peut-être feuilleter 10 pages. S'il y a 100 pages dans le livre, vous devrez peut-être feuilleter 100 pages. La quantité de travail augmente *linéairement* avec la taille de la tâche. C'est ce qu'on appelle **O(n)**, où 'n' est la taille de la tâche (le nombre de pages dans le livre).

*   **Recherche binaire :** S'il y a 16 pages dans le livre, il vous faudra au maximum 4 étapes pour trouver le nom. S'il y a 32 pages dans le livre, il vous faudra au maximum 5 étapes. La quantité de travail augmente beaucoup plus lentement que la taille de la tâche. C'est ce qu'on appelle **O(log n)** (lire "O de log n").



*   Un algorithme **O(n)** devient plus lent *directement proportionnellement* à l'augmentation de la taille de la tâche.
*   Un algorithme **O(log n)** devient plus lent *beaucoup plus lentement* que la taille de la tâche n'augmente.



Imaginez que vous développez un moteur de recherche. Si vous utilisez un algorithme O(n) pour rechercher sur Internet (qui contient des milliards de pages Web), cela prendra un temps incroyablement long ! Et un algorithme O(log n) s'acquittera de cette tâche beaucoup plus rapidement.

### Principaux types de complexité des algorithmes

Voici quelques-uns des types de complexité les plus courants :

*   **O(1) – Complexité constante :** Le temps d'exécution est toujours le même, quelle que soit la taille de la tâche. Par exemple, prendre le premier élément d'une liste.

    ```python
    def get_first_element(my_list):
        """O(1) - Obtention du premier élément d'une liste."""
        return my_list[0]
    ```

*   **O(log n) – Complexité logarithmique :** Le temps d'exécution augmente très lentement avec l'augmentation de la taille de la tâche. Un excellent exemple est la recherche binaire.

    ```python
    def binary_search(my_list, target):
        """O(log n) - Recherche binaire dans une liste triée."""
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
        return -1  # Élément non trouvé
    ```

*   **O(n) – Complexité linéaire :** Le temps d'exécution augmente de manière directement proportionnelle à la taille de la tâche. Par exemple, parcourir chaque élément d'une liste.

    ```python
    def linear_search(my_list, target):
        """O(n) - Recherche linéaire dans une liste."""
        for i in range(len(my_list)):
            if my_list[i] == target:
                return i
        return -1  # Élément non trouvé
    ```

*   **O(n log n) – Complexité quasi-linéaire :**  Souvent rencontrée dans les algorithmes de tri efficaces, tels que le tri par fusion et le tri rapide.

    ```python
    def merge_sort(my_list):
        """O(n log n) - Tri par fusion."""
        if len(my_list) <= 1:
            return my_list

        mid = len(my_list) // 2
        left = merge_sort(my_list[:mid])
        right = merge_sort(my_list[mid:])

        return merge(left, right)

    def merge(left, right):
        """Fonction auxiliaire pour merge_sort."""
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

*   **O(n^2) – Complexité quadratique :** Le temps d'exécution augmente *au carré* de la taille de la tâche. Par exemple, comparer chaque élément d'une liste avec chaque autre élément de la même liste.

    ```python
    def bubble_sort(my_list):
        """O(n^2) - Tri à bulles."""
        n = len(my_list)
        for i in range(n):
            for j in range(0, n-i-1):
                if my_list[j] > my_list[j+1] :
                    my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    ```

*   **O(2^n) – Complexité exponentielle :** Le temps d'exécution augmente très rapidement avec l'augmentation de la taille de la tâche.  Généralement rencontrée dans les algorithmes qui utilisent la force brute.

    ```python
    def fibonacci_recursive(n):
      """O(2^n) - Calcul récursif du nombre de Fibonacci."""
      if n <= 1:
          return n
      return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    ```

*   **O(n!) – Complexité factorielle :** Le type de complexité le plus lent. Se produit lors de l'itération sur toutes les permutations possibles d'éléments.

### Exemples de problèmes et d'algorithmes avec une complexité différente

Examinons quelques exemples de problèmes et différents algorithmes pour les résoudre afin de voir
comment la complexité affecte les performances.

**1. Tri d'une liste :**

*   **Tâche :** Trier une liste d'éléments dans un ordre spécifique (par exemple, croissant).
*   **Algorithmes :**
    *   **Tri à bulles (Bubble Sort) :**

        ```python
        def bubble_sort(my_list):
            n = len(my_list)
            for i in range(n):
                for j in range(0, n-i-1):
                    if my_list[j] > my_list[j+1] :
                        my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
        # Exemple d'utilisation
        my_list = [64, 34, 25, 12, 22, 11, 90]
        bubble_sort(my_list)
        print("Tableau trié :", my_list) # Sortie : [11, 12, 22, 25, 34, 64, 90]
        ```

    *   **Tri par fusion (Merge Sort) :**

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

        # Exemple d'utilisation
        my_list = [64, 34, 25, 12, 22, 11, 90]
        sorted_list = merge_sort(my_list)
        print("Tableau trié :", sorted_list) # Sortie : [11, 12, 22, 25, 34, 64, 90]
        ```
*   **Conclusion :** Pour les grandes listes d'éléments, les algorithmes en O(n log n) (Tri par fusion) sont préférables aux algorithmes en O(n^2) (Tri à bulles).

**2. Recherche du plus court chemin dans un graphe :**

*   **Tâche :** Trouver le plus court chemin entre deux sommets d'un graphe (par exemple, entre deux villes sur une carte).
*   **Algorithmes :**
    *   **Algorithme de Dijkstra :**

        ```python
        import heapq

        def dijkstra(graph, start):
            """Algorithme de Dijkstra pour trouver les plus courts chemins."""
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

        # Exemple d'utilisation
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
        print(f"Plus courts chemins depuis {start_node}: {shortest_paths}")
        ```

*   **Conclusion :** Le choix de l'algorithme dépend du type de graphe (pondéré/non pondéré, présence de poids négatifs) et de la taille du graphe. L'algorithme de Dijkstra est efficace pour les graphes avec des poids non négatifs.

**3. Recherche d'une sous-chaîne dans une chaîne :**

*   **Tâche :** Trouver toutes les occurrences d'une sous-chaîne spécifique dans une chaîne plus grande.
*   **Algorithmes :**
    *   **Recherche naïve de chaîne (Naive String Search) :**

        ```python
        def naive_string_search(text, pattern):
            """Algorithme de recherche de chaîne naïf."""
            occurrences = []
            for i in range(len(text) - len(pattern) + 1):
                if text[i:i+len(pattern)] == pattern:
                    occurrences.append(i)
            return occurrences

        # Exemple d'utilisation
        text = "This is a simple example text."
        pattern = "example"
        occurrences = naive_string_search(text, pattern)
        print(f"Occurrences de '{pattern}' dans le texte : {occurrences}")  # Sortie : [17]
        ```

*   **Conclusion :** Pour les recherches fréquentes de sous-chaînes dans de grandes chaînes, il existe des algorithmes plus efficaces, tels que KMP.

**4. Problème du sac à dos (Knapsack Problem) :**

*   **Tâche :** Vous avez un sac à dos d'une certaine capacité et un ensemble d'objets avec des poids et des valeurs différents. Vous devez choisir des objets qui maximisent la valeur totale, sans dépasser la capacité du sac à dos.
*   **Algorithmes :**
    *   **Programmation dynamique (Dynamic Programming) :**

        ```python
        def knapsack_dynamic_programming(capacity, weights, values, n):
            """Résolution du problème du sac à dos par programmation dynamique."""
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

        # Exemple d'utilisation
        capacity = 50
        weights = [10, 20, 30]
        values = [60, 100, 120]
        n = len(values)
        max_value = knapsack_dynamic_programming(capacity, weights, values, n)
        print(f"Valeur maximale : {max_value}")  # Sortie : 220
        ```

*   **Le choix de l'algorithme dépend de la taille du problème et des exigences de précision de la solution.**

###  Notation Big O : simplification de la complexité

Habituellement, la complexité est décrite à l'aide de la "notation Big O" (notation O). Elle montre à quelle vitesse le temps d'exécution d'un algorithme augmente avec la taille de la tâche, *asymptotiquement*, c'est-à-dire pour de très grandes valeurs de `n`. Les petites constantes et les détails d'implémentation sont généralement ignorés. Par exemple, un algorithme qui effectue `2n + 5` opérations est toujours considéré comme *O(n)*.

###  Pire des cas, cas moyen, meilleur des cas

La complexité d'un algorithme peut dépendre des données d'entrée. On parle généralement de complexité *dans le pire des cas* – c'est la quantité maximale de temps ou de ressources qu'un algorithme peut nécessiter. Parfois, on analyse également la complexité dans le cas moyen et dans le meilleur des cas.

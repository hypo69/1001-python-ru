# Algorithmes de tri

Dans la vie quotidienne et en programmation, nous sommes confrontés à la nécessité d'ordonner des données.
Cela peut être n'importe quoi : une liste de courses, des livres sur une étagère ou des résultats de recherche.
Les algorithmes de tri sont un ensemble d'instructions qui nous aident à organiser les éléments dans un ordre spécifique, qu'il soit croissant,
décroissant ou selon un autre critère.

À titre d'exemple, j'utilise des fruits de différentes tailles.

**Représentation des fruits avec des tailles :**

Associons les fruits à des tailles. Nous utiliserons des tuples, où :

*   Le premier élément est la taille du fruit :
    *   🍎 (petit) – pomme
    *   🍐 (moyen) – poire
    *   🍉 (grand) – melon
    *   🧺 (très grand) – panier
*   Le deuxième élément est un identifiant unique, pour le fonctionnement du programme.

Exemple : `(🍎, 1)` – est une petite pomme avec l'identifiant 1.

```python
from typing import List, Tuple

def compare_fruits(fruit1: Tuple[str, int], fruit2: Tuple[str, int]) -> int:
    """
    Compare deux fruits par leur taille.

    Args:
        fruit1: Tuple (taille, identifiant).
        fruit2: Tuple (taille, identifiant).

    Returns:
        -1 si fruit1 est plus petit que fruit2, 1 si fruit1 est plus grand que fruit2, 0 si égaux.
    """
    order = {"🍎": 0, "🍐": 1, "🍉": 2, "🧺": 3}  # Définir l'ordre des fruits par taille
    size1 = order.get(fruit1[0]) # Obtenir la taille du premier fruit
    size2 = order.get(fruit2[0]) # Obtenir la taille du deuxième fruit
    if size1 < size2: # Si la taille du premier fruit est plus petite, renvoyer -1
        return -1
    elif size1 > size2: # Si la taille du premier fruit est plus grande, renvoyer 1
        return 1
    else: # Si les tailles sont égales, renvoyer 0
      return 0
```

**Algorithmes de tri (comparaison par taille de fruit) :**

1.  **Tri à bulles (Bubble Sort) :** (Les bulles plus légères remontent plus tôt)
    *   L'algorithme compare les fruits adjacents par leur taille. Si un fruit est plus grand que son voisin, il échange sa place avec lui.
    *   Ce processus est répété jusqu'à ce que toute la liste de fruits soit triée du plus petit au plus grand.
    *   Analogie : Imaginez que vous avez un aquarium avec des bulles d'air de différentes tailles. Les bulles plus légères (correspondant aux fruits plus petits) remonteront à la surface plus tôt que les plus lourdes (correspondant aux fruits plus grands). Ainsi, les fruits plus légers "remontent" en haut de la liste, et les plus lourds descendent en bas.

    ```mermaid
    graph TD
        A[Début] --> B{Y a-t-il des fruits non triés ?};
        B -- Oui --> C[Comparer deux fruits adjacents];;
        C -- Le premier est plus grand --> D[Échanger les places];
        D --> E[Passer à la paire suivante];
        C -- Le premier n'est pas plus grand --> E;
        E --> F{Fin de la liste atteinte ?};
        F -- Non --> C;
        F -- Oui --> G{Y a-t-il eu un échange ?};
        G -- Oui --> B;
        G -- Non --> H[Fin];
        B -- Non --> H;
        H[Fin]
    ```
    ```python
    def bubble_sort(fruits: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
        """
        Trie une liste de fruits par taille, en utilisant l'algorithme de "tri à bulles".

        Args:
            fruits: Liste de tuples (taille, identifiant).

        Returns:
            Liste de tuples triée.
        """
        n = len(fruits)  # Obtenir le nombre de fruits
        for i in range(n):  # Parcourir la liste n fois
            for j in range(0, n - i - 1):  # Parcourir la partie non triée de la liste
                if compare_fruits(fruits[j], fruits[j + 1]) == 1:  # Si le fruit de gauche est plus grand que le fruit de droite
                    fruits[j], fruits[j + 1] = fruits[j + 1], fruits[j]  # Échanger les places
        return fruits

    ```
2.  **Tri par insertion (Insertion Sort) :**
    *   L'algorithme construit une liste triée en y ajoutant les fruits un par un. Un nouveau fruit est inséré à la bonne position pour maintenir l'ordre par taille.
    *   Le tri par insertion est bon pour les petites listes ou pour celles où les données sont déjà presque triées.

3.  **Tri par sélection (Selection Sort) :**
    *   L'algorithme trouve le plus petit fruit dans la partie non triée de la liste. Ensuite, il place ce fruit à la première position de la partie non triée de la liste.
    *   Ce processus est répété jusqu'à ce que tous les fruits soient triés.
    *   Le tri par sélection est simple mais inefficace pour les grandes listes.





```python
def insertion_sort(fruits: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """
    Trie une liste de fruits par taille, en utilisant l'algorithme de "tri par insertion".

    Args:
        fruits: Liste de tuples (taille, identifiant).

    Returns:
        Liste de tuples triée.
    """
    for i in range(1, len(fruits)): # Commencer par le deuxième fruit (le premier est considéré comme trié)
        key = fruits[i] # Prendre le fruit suivant
        j = i - 1 # Index du fruit précédent
        while j >= 0 and compare_fruits(fruits[j], key) == 1: # Trouver la position dans la partie triée où insérer le fruit
            fruits[j + 1] = fruits[j] # Décaler les fruits pour faire de la place au nouveau
            j -= 1
        fruits[j + 1] = key # Insérer le fruit à la bonne position
    return fruits

def selection_sort(fruits: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """
    Trie une liste de fruits par taille, en utilisant l'algorithme de "tri par sélection".

    Args:
        fruits: Liste de tuples (taille, identifiant).

    Returns:
        Liste de tuples triée.
    """
    n = len(fruits) # Obtenir le nombre de fruits dans la liste
    for i in range(n): # Parcourir tous les fruits de la liste
        min_index = i # Index du plus petit fruit
        for j in range(i + 1, n): # Trouver le plus petit fruit dans la partie non triée
            if compare_fruits(fruits[j], fruits[min_index]) == -1: # Si un fruit plus petit que le minimum actuel est trouvé
                min_index = j # Mémoriser l'index du nouveau minimum
        fruits[i], fruits[min_index] = fruits[min_index], fruits[i] # Échanger le fruit actuel avec le plus petit de la partie non triée
    return fruits

def display_fruits(fruits: List[Tuple[str, int]]) -> str:
    """
    Convertit une liste de fruits en une chaîne de caractères pour l'affichage.

    Args:
        fruits: Liste de tuples (taille, identifiant).

    Returns:
        Chaîne de caractères pour l'affichage de la liste de fruits.
    """
    return ", ".join(f"{fruit[0]}{fruit[1]}" for fruit in fruits)  # Assembler la chaîne pour la sortie


# Créer une liste de fruits à trier
fruits = [
    ("🍉", 1), ("🍎", 2), ("🍐", 3), ("🧺", 4), ("🍎", 5), ("🍉", 6), ("🍐", 7),
    ("🍎", 8), ("🧺", 9), ("🍉", 10), ("🍐", 11), ("🍎", 12)
]

print("Liste originale de fruits : " + display_fruits(fruits))  # Afficher la liste originale
print("Exemples : Pomme (🍎) < Poires (🍐) < Melon (🍉) < Paniers (🧺)")  # Afficher l'ordre des fruits

# Tri à bulles
sorted_fruits_bubble = bubble_sort(fruits.copy()) # Trier une copie de la liste
print("Tri à bulles : " + display_fruits(sorted_fruits_bubble)) # Afficher le résultat

# Tri par insertion
sorted_fruits_insertion = insertion_sort(fruits.copy()) # Trier une copie de la liste
print("Tri par insertion : " + display_fruits(sorted_fruits_insertion)) # Afficher le résultat

# Tri par sélection
sorted_fruits_selection = selection_sort(fruits.copy()) # Trier une copie de la liste
print("Tri par sélection : " + display_fruits(sorted_fruits_selection)) # Afficher le résultat
```

**Explication du code :**

1.  **`compare_fruits(fruit1, fruit2)` :** Cette fonction compare deux fruits par leur taille et renvoie -1 si le premier fruit est plus petit, 1 s'il est plus grand, et 0 s'ils sont égaux. J'utilise le dictionnaire `order` pour définir l'ordre des tailles de fruits.
2.  **`bubble_sort(fruits)` :** J'implémente l'algorithme de tri à bulles, où les fruits adjacents sont comparés et échangés s'ils sont dans le mauvais ordre.
3.  **`insertion_sort(fruits)` :** J'implémente l'algorithme de tri par insertion, où chaque nouveau fruit est inséré à la bonne position dans la partie déjà triée de la liste.
4.  **`selection_sort(fruits)` :** J'implémente l'algorithme de tri par sélection, où à chaque passage je trouve le plus petit fruit et le place à la bonne position.
5.  **`display_fruits(fruits)` :** Cette fonction convertit une liste de fruits en une chaîne de caractères pour une sortie pratique.
6.  **Exemples :** À la fin, je crée une liste de fruits et j'applique les trois algorithmes de tri, en affichant les résultats de chacun. Je vous montre également l'ordre dans lequel les fruits sont triés.

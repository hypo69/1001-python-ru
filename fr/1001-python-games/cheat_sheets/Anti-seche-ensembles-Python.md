# Ensembles en Python

**1. Introduction : Qu'est-ce qu'un ensemble ?**

En informatique et en mathématiques, les ensembles sont un moyen de représenter des collections d'éléments uniques. Il est important de comprendre que :

*   **Unicité :** Chaque élément d'un ensemble doit être unique. Les répétitions ne sont pas autorisées.
*   **Non ordonné :** L'ordre des éléments dans un ensemble n'a pas d'importance.


**2. Ensembles et fruits**

Imaginons que nous n'ayons que les fruits eux-mêmes :

*   🍎 (pomme)
*   🍐 (poire)
*   🍉 (melon)
*   🧺 (panier)

Il est important que :

1.  **Il n'y a *pas* de fruits identiques dans l'ensemble :** S'il y a une pomme dans l'ensemble, il n'y aura pas d'autre pomme identique. Chaque fruit est unique dans son ensemble.
2.  **L'ordre des fruits n'a pas d'importance :** S'il y a une pomme et une poire dans l'ensemble, c'est la même chose que s'il y avait une poire et une pomme. L'ordre n'a pas d'importance.

Par exemple, `{🍎, 🍐, 🍉}` est un ensemble contenant une pomme, une poire et un melon.

**3. Pourquoi les ensembles exigent-ils des éléments uniques ?**

*   Les ensembles sont conçus pour suivre la *présence* des éléments, et non leur *quantité*.
*   L'unicité des éléments simplifie l'exécution des opérations sur les ensembles.
*   Les ensembles sont utilisés pour éliminer la redondance des données.

**4. Opérations sur les ensembles (ensembles de fruits) :**

1.  **Union : "Rassembler tous les fruits en un seul ensemble"**
    *   Combiner deux ensembles de fruits, en rassemblant tous les fruits dans un nouvel ensemble. S'il y a des fruits identiques dans deux ensembles, le nouvel ensemble ne contiendra qu'un seul de ces fruits.
    *   Si l'ensemble A contient {🍎, 🍐}, et l'ensemble B contient {🍐, 🍉}, alors l'ensemble A ∪ B contiendra {🍎, 🍐, 🍉}.

2.  **Intersection : "Trouver les fruits communs"**
    *   Trouver *uniquement* les fruits qui sont présents à la fois dans l'ensemble A et dans l'ensemble B.
    *   Si l'ensemble A contient {🍎, 🍐}, et l'ensemble B contient {🍐, 🍉}, alors l'ensemble A ∩ B ne contiendra que {🍐}.

3.  **Différence : "Fruits qui sont dans un ensemble mais pas dans un autre"**
    *   Trouver *uniquement* les fruits qui sont présents dans l'ensemble A mais pas dans l'ensemble B.
    *   Si l'ensemble A contient {🍎, 🍐}, et l'ensemble B contient {🍐, 🍉}, alors l'ensemble A - B contiendra {🍎}, et l'ensemble B - A contiendra {🍉}.

4.  **Différence symétrique : "Fruits qui ne sont que dans l'un des ensembles"**
    *   Trouver *tous* les fruits qui sont présents soit dans l'ensemble A, soit dans l'ensemble B, mais pas dans les deux simultanément.
    *   Si l'ensemble A contient {🍎, 🍐}, et l'ensemble B contient {🍐, 🍉}, alors l'ensemble A ^ B contiendra {🍎, 🍉}.

5.  **Sous-ensemble : "Tous les fruits d'un ensemble sont-ils présents dans un autre ?"**
    *   Vérifier si l'ensemble A est un sous-ensemble de l'ensemble B. Cela signifie que tous les fruits de l'ensemble A sont également présents dans l'ensemble B.
    *   **Exemple :** Si l'ensemble A contient {🍎, 🍐}, et l'ensemble B contient {🍎, 🍐, 🍉}, alors A <= B.

6.  **Sur-ensemble : "Un ensemble contient-il tous les fruits d'un autre ?"**
    *   Vérifier si l'ensemble A est un sur-ensemble de l'ensemble B. Cela signifie que tous les fruits de l'ensemble B sont également présents dans l'ensemble A.
    *   Si l'ensemble A contient {🍎, 🍐, 🍉}, et l'ensemble B contient {🍎, 🍐}, alors A >= B.



```python
from typing import Set

def create_fruit_set(fruit_string: str) -> Set[str]:
    """
    Crée un ensemble de fruits à partir d'une chaîne de caractères.

    Args:
        fruit_string: Chaîne de fruits (🍎, 🍐, 🍉, 🧺).

    Returns:
        Ensemble de fruits uniques.
    """
    if not all(fruit in ["🍎", "🍐", "🍉", "🧺"] for fruit in fruit_string):
        raise ValueError("La chaîne ne peut contenir que les symboles 🍎, 🍐, 🍉, 🧺")
    return set(fruit_string)  # Utiliser set() pour créer un ensemble

def display_set(fruit_set: Set[str]) -> str:
  """
  Convertit un ensemble de fruits en une chaîne de caractères pour l'affichage.

    Args:
        fruit_set: Ensemble de fruits.

    Returns:
        Chaîne de caractères pour l'affichage.
  """
  return "{" + ", ".join(fruit_set) + "}"


# Créer des ensembles de fruits
fruits_set_A = create_fruit_set("🍎🍐")  # Ensemble A: {🍎, 🍐}
fruits_set_B = create_fruit_set("🍐🍉")  # Ensemble B: {🍐, 🍉}
fruits_set_C = create_fruit_set("🍎🍐🍉")  # Ensemble C: {🍎, 🍐, 🍉}
fruits_set_D = create_fruit_set("🧺")  # Ensemble D: {🧺}

# Afficher les ensembles
print(f"Ensemble A: {display_set(fruits_set_A)}")
print(f"Ensemble B: {display_set(fruits_set_B)}")
print(f"Ensemble C: {display_set(fruits_set_C)}")
print(f"Ensemble D: {display_set(fruits_set_D)}")

# Union des ensembles
union_result = fruits_set_A | fruits_set_B
print(f"A ∪ B: {display_set(union_result)}")  # Résultat: {🍎, 🍐, 🍉}

# Intersection des ensembles
intersection_result = fruits_set_A & fruits_set_B
print(f"A ∩ B: {display_set(intersection_result)}")  # Résultat: {🍐}

# Différence des ensembles
difference_result_AB = fruits_set_A - fruits_set_B
print(f"A - B: {display_set(difference_result_AB)}")  # Résultat: {🍎}
difference_result_BA = fruits_set_B - fruits_set_A
print(f"B - A: {display_set(difference_result_BA)}")  # Résultat: {🍉}

# Différence symétrique des ensembles
symmetric_difference_result = fruits_set_A ^ fruits_set_B
print(f"A ^ B: {display_set(symmetric_difference_result)}")  # Résultat: {🍎, 🍉}

# Sous-ensemble
subset_result1 = fruits_set_A <= fruits_set_C
print(f"A <= C: {subset_result1}")  # Résultat: True (A est un sous-ensemble de C)
subset_result2 = fruits_set_A <= fruits_set_B
print(f"A <= B: {subset_result2}") # Résultat: False (A n'est pas un sous-ensemble de B)

# Sur-ensemble
superset_result1 = fruits_set_C >= fruits_set_A
print(f"C >= A: {superset_result1}")  # Résultat: True (C est un sur-ensemble de A)
superset_result2 = fruits_set_B >= fruits_set_A
print(f"B >= A: {superset_result2}")  # Résultat: False (B n'est pas un sur-ensemble de A)

# Vérification de la présence d'un élément
print(f"🍎 dans A: {'🍎' in fruits_set_A}")  # Résultat: True
print(f"🍉 dans A: {'🍉' in fruits_set_A}")  # Résultat: False
```

*   **`create_fruit_set(fruit_string)` :** Cette fonction crée un ensemble à partir d'une chaîne de fruits.
    *   `set(fruit_string)` convertit la chaîne en un ensemble, en supprimant les doublons et en rendant l'ordre des éléments non pertinent.
    *   Nous vérifions que la chaîne ne contient que des caractères Unicode autorisés.
*   **`display_set(fruit_set)` :** Cette fonction est utilisée pour convertir un ensemble en une chaîne lisible pour l'affichage.
*   **Exemples :** Nous créons plusieurs ensembles et appliquons diverses opérations sur eux. Les résultats de chaque opération sont affichés à l'écran.



**5. Tâches pratiques :**

1.  Créez vos propres ensembles de fruits et essayez toutes les opérations sur eux.
2.  Implémentez la fonction `is_disjoint(set1, set2)`, qui vérifiera si deux ensembles sont disjoints (intersection = ensemble vide).
3.  Implémentez la fonction `power_set(fruit_set)`, qui renverra l'ensemble de tous les sous-ensembles d'un ensemble donné.
4.  Essayez d'appliquer les ensembles pour résoudre un problème réel. Par exemple, vous avez deux listes d'invités pour une fête, trouvez les invités qui sont dans les deux listes, les invités qui ne sont que dans la première liste, etc.

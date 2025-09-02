# 🧑‍💻 Utilisation de `array.array` en Python : Quand et pourquoi l'utiliser

Le module **`array`** fournit un type de données spécialisé `array.array` pour stocker des séquences de nombres du même type. Contrairement à la `list` générique, les tableaux `array.array` offrent une utilisation plus efficace de la mémoire et des performances accrues lors du traitement de données numériques.

---

## 📦 Principaux avantages de `array.array`

La principale différence entre `array.array` et `list` est le **stockage compact des données**. Au lieu d'une liste de pointeurs vers des objets Python, `array.array` stocke les valeurs sous la forme d'un bloc d'octets contigu, ce qui le rend idéal pour les tâches suivantes.

---

### 1. Économies de mémoire lors du traitement de grands ensembles de nombres

Lors du traitement de millions d'éléments numériques, les économies de mémoire deviennent critiques. `array.array` réduit considérablement la surcharge.

```python
import array
import sys

def compare_memory_usage(num_elements: int = 1_000_000) -> None:
    """
    Compare l'utilisation de la mémoire entre list et array.array.

    Args:
        num_elements (int, optional): Le nombre d'éléments à tester.
                                      La valeur par défaut est 1 000 000.
    """
    # Créer une liste avec des objets entiers Python
    list_numbers = list(range(num_elements))
    
    # Créer un tableau où les nombres sont stockés en tant qu'entiers de type C de 4 octets
    array_numbers = array.array('i', range(num_elements))

    list_size = sys.getsizeof(list_numbers)
    array_size = sys.getsizeof(array_numbers)

    print(f"Nombre d'éléments: {num_elements}")
    print(f"Taille de la liste:  {list_size / 1024 / 1024:.2f} Mo")
    print(f"Taille du tableau: {array_size / 1024 / 1024:.2f} Mo")
    if array_size > 0:
        print(f"Économies de mémoire: {list_size / array_size:.2f}x")

# Exemple d'utilisation
if __name__ == "__main__":
    compare_memory_usage()
```
**Sortie:**
```
Nombre d'éléments: 1000000
Taille de la liste:  7.63 Mo
Taille du tableau: 3.82 Mo
Économies de mémoire: 2.00x
```

---

### 2. Amélioration des performances des opérations numériques

Grâce à sa disposition en mémoire contiguë, les opérations mathématiques sur les éléments de `array.array` sont plus rapides car le processeur peut utiliser le cache plus efficacement.

```python
import array
import timeit

def compare_performance(num_elements: int = 10_000_000) -> None:
    """
    Compare les performances de la sommation des éléments dans une liste et un array.array.

    Args:
        num_elements (int, optional): Le nombre d'éléments à tester.
                                      La valeur par défaut est 10 000 000.
    """
    setup_code = f"""
import array
data = range({num_elements})
list_data = list(data)
array_data = array.array('i', data)
"""
    
    # Mesurer le temps pour la liste
    list_time = timeit.timeit("sum(list_data)", setup=setup_code, number=10)
    
    # Mesurer le temps pour le tableau
    array_time = timeit.timeit("sum(array_data)", setup=setup_code, number=10)
    
    print(f"Temps pour sommer {num_elements} éléments (10 fois):")
    print(f"liste:  {list_time:.4f} secondes")
    print(f"tableau: {array_time:.4f} secondes")

# Exemple d'utilisation
if __name__ == "__main__":
    compare_performance()
```
**Sortie:**
```
Temps pour sommer 10000000 éléments (10 fois):
liste:  2.1106 secondes
tableau: 1.1549 secondes
```

---

### 3. Travail direct avec les bibliothèques C (`ctypes`, `struct`)

`array.array` est idéal pour passer des données à des bibliothèques de bas niveau écrites en C, car sa structure interne est compatible avec les tableaux C.

#### Exemple avec `ctypes`:

```python
import array
from ctypes import c_double, CDLL

def demonstrate_ctypes_usage() -> None:
    """
    Montre comment passer un array.array à une fonction C via ctypes.
    """
    # Tableau avec des nombres à double précision (type 'd')
    py_array = array.array('d', [1.1, 2.2, 3.3, 4.4])
    
    # Créer un tableau compatible C à partir de py_array
    # La fonction (c_double * len(py_array)) crée un type "tableau de 4 c_double"
    # (*py_array) décompresse le tableau python dans les arguments de ce constructeur
    c_array = (c_double * len(py_array))(*py_array)

    # Ici pourrait se trouver un appel à une fonction C, par exemple:
    # my_c_library = CDLL("./libmath.so")
    # my_c_library.sum_doubles(c_array, len(c_array))
    
    print(f"Tableau Python: {py_array}")
    print(f"Tableau compatible C (ctypes): {[val for val in c_array]}")

# Exemple d'utilisation
if __name__ == "__main__":
    demonstrate_ctypes_usage()
```

#### Exemple avec `struct` pour l'empaquetage des données:

```python
import array
import struct

def demonstrate_struct_packing(data: list[int]) -> bytes:
    """
    Empaquette un tableau d'entiers dans une chaîne binaire.

    Args:
        data (list[int]): Une liste d'entiers à empaqueter.

    Returns:
        bytes: La représentation binaire des données.
    """
    arr = array.array('i', data)
    
    # Créer une chaîne de format comme '3i' pour 3 entiers
    format_string = f'{len(arr)}i'
    
    # Empaqueter les données dans un format binaire
    binary_data = struct.pack(format_string, *arr)
    
    print(f"Tableau original: {arr}")
    print(f"Données binaires: {binary_data}")
    
    # Vérification: décompression
    unpacked_data = struct.unpack(format_string, binary_data)
    print(f"Données décompressées: {unpacked_data}")
    
    return binary_data

# Exemple d'utilisation
if __name__ == "__main__":
    demonstrate_struct_packing([10, 20, 30])
```

---

### 4. Sérialisation et désérialisation efficaces

Les méthodes `.tobytes()` et `.frombytes()` vous permettent de convertir rapidement un tableau en octets et vice-versa, ce qui est idéal pour l'enregistrement dans des fichiers ou l'envoi sur un réseau.

```python
import array

def handle_binary_data() -> None:
    """
    Montre la sérialisation et la désérialisation d'un array.array en octets.
    """
    # Créer le tableau source
    source_array = array.array('i', [1, 2, 3, 4, 5])
    print(f"Tableau source: {source_array}")

    # Sérialiser le tableau en octets
    binary_data = source_array.tobytes()
    print(f"Données en octets: {binary_data}")

    # Désérialiser des octets vers un nouveau tableau
    new_array = array.array('i')
    new_array.frombytes(binary_data)
    print(f"Tableau restauré: {new_array}")

    # Vérifier l'intégrité
    assert source_array == new_array, "Les données ne correspondent pas!"
    print("Intégrité des données confirmée.")

# Exemple d'utilisation
if __name__ == "__main__":
    handle_binary_data()
```

---

### 5. Garantie de l'homogénéité des types

`array.array` impose qu'un seul type de données, spécifié lors de la création, soit stocké. Cela protège contre l'ajout accidentel d'éléments d'un type différent.

```python
import array

def demonstrate_type_safety() -> None:
    """
    Montre que array.array ne permet pas d'ajouter des éléments d'un type différent.
    """
    arr = array.array('i', [100, 200, 300])
    print(f"Tableau d\'entiers: {arr}")
    
    try:
        # Tentative d'ajout d'un élément de type chaîne de caractères
        arr.append('hello')
    except TypeError as e:
        # Exception attendue
        print(f"\nLa tentative d'ajout de 'hello' a provoqué une erreur: {e}")
        print("Cela confirme le typage strict du tableau.")

# Exemple d'utilisation
if __name__ == "__main__":
    demonstrate_type_safety()
```

---

### 6. Écriture et lecture directes dans des fichiers binaires

Les méthodes `.tofile()` et `.fromfile()` simplifient le travail avec les fichiers binaires, vous permettant d'éviter la sérialisation intermédiaire.

```python
import array
from pathlib import Path

def work_with_binary_files(file_path_str: str = "data.bin") -> None:
    """
    Écrit un tableau dans un fichier binaire et le relit.

    Args:
        file_path_str (str, optional): Le nom du fichier à enregistrer.
                                       La valeur par défaut est "data.bin".
    """
    file_path = Path(file_path_str)
    source_array = array.array('f', [1.5, 2.7, 3.14])

    try:
        # Écrire dans le fichier
        with file_path.open('wb') as f:
            source_array.tofile(f)
        print(f"Tableau {source_array} écrit dans le fichier '{file_path}'.")

        # Lire depuis le fichier
        new_array = array.array('f')
        with file_path.open('rb') as f:
            # Lire 3 éléments de type 'f' (float)
            new_array.fromfile(f, len(source_array))
        print(f"Tableau {new_array} lu depuis le fichier.")
        
        assert source_array == new_array

    finally:
        # Suppression garantie du fichier après exécution
        if file_path.exists():
            file_path.unlink()
            print(f"Fichier temporaire '{file_path}' supprimé.")

# Exemple d'utilisation
if __name__ == "__main__":
    work_with_binary_files()
```

---

## 🔹 Tableau comparatif : `array.array` vs `list`

| Caractéristique | `array.array` | `list` |
| :--- | :--- | :--- |
| **Type de données** | Primitifs homogènes (nombres, caractères) | Tous les objets Python |
| **Mémoire** | Faible consommation | Forte consommation |
| **Performance** | Élevée pour les opérations numériques | Inférieure pour les opérations numériques |
| **API** | Ensemble limité de méthodes | API riche et flexible |
| **Compatibilité C**| Élevée, passage direct des données | Nécessite des conversions |
| **Sérialisation binaire** | Méthodes intégrées (`.tobytes`, `.tofile`)| Nécessite `struct`, `pickle`, etc. |

---

**Conclusion:**

🚀 Utilisez `array.array` lorsque vous travaillez avec de grands volumes de **données numériques homogènes**, et lorsque les **performances** et l'**utilisation efficace de la mémoire** sont essentielles pour vous.

Pour la plupart des tâches quotidiennes où la flexibilité et le stockage de données hétérogènes sont nécessaires, `list` reste le meilleur choix.

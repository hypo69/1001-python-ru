# Importation de modules en Python

L'importation de bibliothèques en Python permet d'utiliser des modules et des fonctions externes ou propres, définis dans d'autres fichiers ou bibliothèques. Cela aide à organiser le code, à améliorer sa lisibilité et à éviter la duplication.

### Qu'est-ce qu'un module ?
Un module en Python est simplement un fichier avec l'extension `.py` qui contient du code (fonctions, classes, variables, etc.). Lorsque vous souhaitez utiliser du code d'un autre module, vous devez l'importer dans le fichier actuel.

### Modules externes et internes
1. **Modules externes** — ce sont des modules qui ne font pas partie de la bibliothèque standard de Python et qui doivent être installés séparément. Par exemple, les modules pour travailler avec des serveurs web, le traitement de données ou l'apprentissage automatique, tels que `numpy`, `requests` et autres.

2. **Modules internes** — ce sont des modules qui sont déjà inclus dans la bibliothèque standard de Python. Par exemple, les modules pour travailler avec des fichiers, le temps, les opérations mathématiques : `os`, `math`, `datetime`.

### Installation de modules externes avec pip
Pour installer un module externe, utilisez la commande `pip` — c'est un outil de gestion de paquets Python. Par exemple, pour installer la bibliothèque `requests`, vous devez exécuter la commande suivante dans le terminal :
```bash
pip install requests
```
Cette commande téléchargera et installera la bibliothèque dans votre projet.

### Importation de modules
Lorsque vous souhaitez utiliser un module en Python, vous devez l'importer :
1. **Importer le module entier** :
   ```python
   import os
   ```
   Après cela, vous pouvez utiliser toutes les fonctions et variables du module, par exemple :
   ```python
   os.listdir()  # liste les fichiers dans le répertoire
   ```

2. **Importer des éléments spécifiques d'un module** :
   ```python
   from math import sqrt
   ```
   Vous pouvez maintenant utiliser la fonction `sqrt` sans avoir besoin de faire référence au module `math`.

3. **Importer avec un alias** :
   ```python
   import pandas as pd
   ```
   Dans ce cas, pour utiliser les fonctions de la bibliothèque `pandas`, vous écrirez `pd` au lieu du nom complet `pandas`.

### Importation de vos propres modules
Si vous écrivez plusieurs fichiers dans un même projet, vous pouvez créer vos propres modules. Par exemple, si vous avez un fichier `utils.py` avec des fonctions utiles, vous pouvez l'importer dans d'autres fichiers comme ceci :
```python
import utils
```
Ou importer une fonction spécifique :
```python
from utils import my_function
```

### Pourquoi créer un module et l'importer dans d'autres parties du projet ?
1. **Organisation du code** : La séparation de la logique en différents modules aide à éviter le désordre dans un grand projet. Par exemple, vous pouvez créer un module pour la gestion des données, un autre pour le traitement des requêtes, et un troisième pour l'interface.
   
2. **Réutilisation du code** : Lorsque la logique est séparée en modules, elle peut être utilisée dans différentes parties du projet. Cela réduit la duplication du code et facilite la maintenance.

3. **Lisibilité et maintenabilité** : Lorsque le code est séparé en modules, d'autres développeurs (ou vous-même à l'avenir) pourront comprendre et maintenir le projet plus facilement.

Exemple :
```python
# utils.py
def greet(name):
    return f"Bonjour, {name}!"
    
# main.py
from utils import greet

print(greet("Alice"))
```

Dans cet exemple, la fonction `greet` est définie dans un module (`utils.py`), mais utilisée dans un autre (`main.py`), ce qui améliore la structure et rend le code plus modulaire et plus facile à modifier.

---

  [Vers la table des matières](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)

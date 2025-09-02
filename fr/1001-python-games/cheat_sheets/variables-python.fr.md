**Variables en Python : ce que c'est et pourquoi elles sont nécessaires**

Les variables sont des conteneurs nommés pour stocker des données en mémoire de l'ordinateur. Elles permettent d'accéder aux données par leur nom, au lieu de les utiliser directement.

Exemple :
```python
x = 10
y = 'Bonjour, le monde !'
```
Ici `x` et `y` sont des variables. `x` stocke le nombre 10, et `y` stocke la chaîne 'Bonjour, le monde !'.

### **Comment fonctionnent les variables en Python ?**
1. **Typage dynamique** :
   En Python, il n'est pas nécessaire de spécifier le type de la variable lors de sa création — cela se fait automatiquement. Par exemple :
   ```python
   a = 42      # Nombre entier (int)
   b = 3.14    # Nombre à virgule flottante (float)
   c = 'Texte' # Chaîne de caractères (str)
   ```

2. **Modèle de stockage de données par référence** :
   Les variables en Python sont des références à des objets en mémoire. Par exemple :
   ```python
   x = 5
   y = x  # y pointe maintenant aussi vers l'objet 5
   x = 10 # x pointe maintenant vers un autre objet 10, et y pointe toujours vers 5
   ```

---

### **Règles de nommage des variables**
1. **Règles obligatoires** :
   - Le nom d'une variable peut être composé de lettres, de chiffres et du symbole `_`, mais ne peut pas commencer par un chiffre.
     ✅ Exemples : `my_var`, `_data`, `var123`
     ❌ Incorrect : `123var`, `my-var`
   - Le nom d'une variable est sensible à la casse.
     Exemple : `age` et `Age` sont des variables différentes.

2. **Recommandations pour des noms significatifs** :
   - Utilisez des noms qui reflètent l'essence des données.
     ❌ Mauvais : `a = 100`, `b = 'Nom'`
     ✅ Bon : `salary = 100`, `username = 'Nom'`
   - Pour les noms composés de plusieurs mots, utilisez le style **snake_case** :
     Exemple : `user_age`, `total_cost`.

3. **Mots réservés** :
   Vous ne pouvez pas utiliser les mots-clés de Python (par exemple, `if`, `for`, `while`) comme noms de variables.

   Pour voir la liste des mots-clés, exécutez :
   ```python
   import keyword
   print(keyword.kwlist)
   ```

---

### **Caractéristiques du stockage des types de données**
1. **Types de données Python** :
   - **Nombres** : `int`, `float`, `complex`
   - **Chaînes** : `str`
   - **Listes** : `list`
   - **Tuples** : `tuple`
   - **Ensembles** : `set`
   - **Dictionnaires** : `dict`

2. **Types mutables et immuables** :
   - **Mutables** : `list`, `dict`, `set`.
     Exemple :
     ```python
     lst = [1, 2, 3]
     lst.append(4)  # La liste est modifiée
     ```
   - **Immuables** : `int`, `float`, `str`, `tuple`.
     Exemple :
     ```python
     name = 'Alice'
     name[0] = 'B'  # Erreur, les chaînes sont immuables
     ```

3. **Fonction `type` pour la vérification du type** :
   ```python
   x = 10
   print(type(x))  # <class 'int'>
   ```

---

### **Conseils pour les débutants**
1. Utilisez des noms de variables significatifs pour rendre votre code compréhensible.
2. N'oubliez pas que Python ne nécessite pas de déclaration de type de variable, mais soyez attentif à ne pas vous mélanger les pinceaux avec les types de données.
3. Apprenez les fonctions intégrées pour travailler avec les variables, telles que `type()`, `id()`, et les modules, tels que `sys`, pour mieux comprendre comment Python gère la mémoire.

---

  [Vers la table des matières](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)

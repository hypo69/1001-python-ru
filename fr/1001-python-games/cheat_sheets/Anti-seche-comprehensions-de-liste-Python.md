**Qu'est-ce que les compréhensions de liste ?**

Dans sa forme la plus simple, une compréhension de liste est un moyen compact de créer une nouvelle liste à partir d'une liste existante (ou de tout objet itérable). Au lieu d'utiliser une boucle `for` traditionnelle et d'ajouter des éléments à la liste un par un, vous pouvez le faire en une seule ligne de code.


*   **Concision :** Elles permettent d'écrire moins de code.
*   **Lisibilité :** Une fois que vous vous serez habitué à leur syntaxe, vous les trouverez plus faciles à comprendre que les boucles `for` équivalentes.
*   **Performance :** Dans certains cas, les compréhensions de liste peuvent être plus rapides que les boucles `for`.


Voici la syntaxe de base d'une compréhension de liste :

```python
new_list = [expression for item in iterable]
```

*   **`expression`** : Expression qui définit comment chaque élément de la nouvelle liste sera calculé. Cela peut être n'importe quoi : une valeur simple, une opération mathématique, un appel de fonction.
*   **`item`** : Variable qui prend la valeur de chaque élément de l'`iterable` tour à tour.
*   **`iterable`** : Objet itérable, par exemple, une liste, un tuple, une chaîne de caractères ou le résultat de `range()`.

**Exemple :**

Supposons que vous ayez une liste de nombres, et que vous vouliez créer une nouvelle liste contenant les carrés de ces nombres.

**Sans compréhension de liste :**

```python
numbers = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
    squares.append(number**2)
print(squares)  # Sortie : [1, 4, 9, 16, 25]
```

**Avec compréhension de liste :**

```python
numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers]
print(squares) # Sortie : [1, 4, 9, 16, 25]
```

La compréhension de liste rend le code plus court et plus clair !

**Ajout d'une condition**

Les compréhensions de liste vous permettent également d'ajouter des conditions pour sélectionner les éléments qui seront inclus dans la nouvelle liste.

```python
new_list = [expression for item in iterable if condition]
```

* **`condition`** : condition qui doit être remplie pour qu'un élément soit inclus dans la nouvelle liste.

**Exemple :**

Créons une liste de carrés des nombres pairs uniquement à partir de notre liste `numbers` originale.

**Sans compréhension de liste :**

```python
numbers = [1, 2, 3, 4, 5]
even_squares = []
for number in numbers:
    if number % 2 == 0:
        even_squares.append(number**2)
print(even_squares) # Sortie : [4, 16]
```

**Avec compréhension de liste :**

```python
numbers = [1, 2, 3, 4, 5]
even_squares = [number**2 for number in numbers if number % 2 == 0]
print(even_squares) # Sortie : [4, 16]
```

J'ai ajouté `if number % 2 == 0` à la compréhension de liste pour filtrer uniquement les nombres pairs.

**Compréhensions de liste multilignes**

Lorsque les compréhensions de liste deviennent plus complexes, elles peuvent être divisées en plusieurs lignes pour une meilleure lisibilité.

**Exemple :**

```python
numbers = [1, 2, 3, 4, 5]
squared_odds = [
    number**2
    for number in numbers
    if number % 2 != 0
]
print(squared_odds) # Sortie : [1, 9, 25]
```
Cela rend le code plus compréhensible, surtout lorsque vous avez de longues conditions ou des expressions complexes.





**Exercice 1 : Conversion de température**

Vous avez une liste de températures en degrés Celsius, et vous devez les convertir en degrés Fahrenheit. La formule de conversion est : `F = (C * 9/5) + 32`.

Voici votre liste de températures en Celsius :

```python
celsius_temperatures = [0, 10, 20, 30, 40]
```

**Tâche :**

1.  À l'aide d'une compréhension de liste, créez une nouvelle liste `fahrenheit_temperatures` contenant les températures de `celsius_temperatures`, converties en degrés Fahrenheit.
2.  Affichez la liste `fahrenheit_temperatures` résultante à l'écran.

**Indice :**

*   Utilisez la formule `(celsius * 9/5) + 32` comme expression dans la compréhension de liste.
*   Réfléchissez à ce qui est `iterable` et ce qui est `item` dans ce cas.

Essayez d'écrire le code.

Ma solution :
```python
# Liste originale des températures en Celsius
celsius_temperatures = [0, 10, 20, 30, 40]

# Utiliser la compréhension de liste pour convertir en Fahrenheit
fahrenheit_temperatures = [
    (celsius * 9/5) + 32  # Expression : formule de conversion
    for celsius in celsius_temperatures # Itérer sur les éléments de la liste
]

# Afficher le résultat
print(fahrenheit_temperatures) # Sortie : [32.0, 50.0, 68.0, 86.0, 104.0]
```

**Analyse du code :**

1.  **`celsius_temperatures = [0, 10, 20, 30, 40]`** : C'est la liste originale des températures en Celsius.
2.  **`fahrenheit_temperatures = [...]`** : Ici, nous créons une nouvelle liste à l'aide d'une compréhension de liste.
3.  **`(celsius * 9/5) + 32`** : C'est l'expression qui est exécutée pour chaque élément. Elle convertit la température de Celsius en Fahrenheit.
4.  **`for celsius in celsius_temperatures`** : Cette partie de la compréhension de liste itère sur chaque élément de la liste `celsius_temperatures`, en attribuant sa valeur à la variable `celsius` à chaque itération.
5.  **`print(fahrenheit_temperatures)`** : Affiche la liste résultante des températures en Fahrenheit.

**Remarques importantes :**

*   Dans ce cas, `celsius_temperatures` est l'`iterable`, et `celsius` est l'`item`.
*   J'utilise le formatage multiligne pour la compréhension de liste afin d'améliorer la lisibilité du code.
*   À l'intérieur de l'expression, j'applique directement la formule de conversion en utilisant la valeur `celsius` actuelle.



**Exercice 2 : Filtrage et transformation de chaînes de caractères**

Vous avez une liste de mots, et vous devez faire ce qui suit :

1.  Filtrer les mots qui commencent par la lettre "a" (insensible à la casse).
2.  Convertir tous les mots restants en majuscules.

Voici votre liste de mots :

```python
words = ["apple", "banana", "apricot", "kiwi", "Avocado", "orange"]
```

**Tâche :**

1.  À l'aide d'une compréhension de liste, créez une nouvelle liste `transformed_words` contenant uniquement les mots de la liste `words` qui ne commencent pas par la lettre "a" (ou "A"), et qui sont convertis en majuscules.
2.  Affichez la liste `transformed_words` résultante à l'écran.

**Indices :**

*   Utilisez la méthode de chaîne `startswith()` pour vérifier si un mot commence par une lettre spécifique. N'oubliez pas la casse ! Convertissez tout en minuscules.
*   Utilisez la méthode de chaîne `upper()` pour convertir une chaîne en majuscules.
*   Réfléchissez à l'ordre des opérations. D'abord filtrer, puis transformer.

Ma solution :

```python
# Liste originale de mots
words = ["apple", "banana", "apricot", "kiwi", "Avocado", "orange"]

# Utiliser la compréhension de liste pour le filtrage et la transformation
transformed_words = [
    word.upper() # Convertir en majuscules
    for word in words # Itérer sur les mots de la liste
    if not word.lower().startswith("a") # Filtrer les mots qui ne commencent pas par 'a'
]

# Afficher le résultat
print(transformed_words) # Sortie : ['BANANA', 'KIWI', 'ORANGE']
```

**Analyse du code :**

1.  **`words = ["apple", "banana", "apricot", "kiwi", "Avocado", "orange"]`** : C'est la liste originale de mots.
2.  **`transformed_words = [...]`** : Créons une nouvelle liste à l'aide d'une compréhension de liste.
3.  **`word.upper()`** : C'est l'expression qui est exécutée pour chaque mot filtré. Elle convertit le mot en majuscules.
4.  **`for word in words`** : Itérer sur tous les mots de la liste `words`.
5.  **`if not word.lower().startswith("a")`** : C'est la condition de filtrage.
    *   `word.lower()` : D'abord, nous convertissons le mot en minuscules afin que la comparaison soit insensible à la casse.
    *   `startswith("a")` : Ensuite, nous vérifions si le mot commence par la lettre "a".
    *   `not` : Inverser le résultat pour ne conserver que les mots qui *ne* commencent pas par la lettre "a".
6.  **`print(transformed_words)`** : Affiche la liste résultante des mots transformés.

**Points clés :**

*   Méthodes de chaîne `lower()`, `upper()`, et `startswith()` dans l'expression et la condition de la compréhension de liste.
*   La condition de filtrage `if not word.lower().startswith("a")` garantit que seuls les mots ne commençant pas par "a" (quelle que soit la casse) sont inclus dans la nouvelle liste.
*   Le filtrage est appliqué en premier, puis la conversion en majuscules.
*   Encore une fois, j'utilise le formatage multiligne pour la lisibilité.


**Exercice 3 : Création d'un dictionnaire à partir d'une liste de tuples**

Vous avez une liste de tuples, où chaque tuple contient deux éléments : le nom et l'âge d'une personne.

```python
people_data = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35),
    ("David", 28),
]
```

**Tâche :**

1. À l'aide d'une compréhension de liste, créez un dictionnaire `people_dict`, où les clés seront les noms des personnes, et les valeurs — leur âge.
2. Affichez le dictionnaire `people_dict` à l'écran.

**Indices :**

*   Les compréhensions de liste créent des listes, mais elles peuvent être utilisées pour créer des listes de tuples, qui peuvent ensuite être passées au constructeur `dict()`.
*   Réfléchissez à la façon d'extraire le nom et l'âge de chaque tuple.
*   N'oubliez pas qu'un dictionnaire est une structure de données qui stocke des paires clé-valeur.

**Petite explication :**

En Python, vous pouvez créer un dictionnaire à partir d'une liste de tuples, où chaque tuple est composé de deux éléments (clé, valeur).
Pour ce faire, j'utilise le constructeur `dict()`. Par exemple :
```python
my_list = [("a", 1), ("b", 2)]
my_dict = dict(my_list)
print(my_dict) # Sortie {'a': 1, 'b': 2}
```
Votre tâche consiste à utiliser une compréhension de liste pour créer cette liste de tuples, qui sera ensuite utilisée pour créer le dictionnaire.

Ma solution :

```python
# Liste originale de tuples avec les données des personnes
people_data = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35),
    ("David", 28),
]

# J'utilise une compréhension de liste pour créer une liste de tuples, que je convertis ensuite en dictionnaire
people_dict = dict(
    [
      (name, age) # Créer un tuple (nom, âge)
      for name, age in people_data # Itérer sur les tuples dans people_data
    ]
)

# Afficher le dictionnaire résultant
print(people_dict) # Sortie : {'Alice': 30, 'Bob': 25, 'Charlie': 35, 'David': 28}
```

**Analyse du code :**

1.  **`people_data = [...]`** : C'est la liste originale de tuples, où chaque tuple contient le nom et l'âge d'une personne.
2.  **`people_dict = dict(...)`** : Nous utilisons le constructeur `dict()` pour créer un dictionnaire à partir d'une liste de tuples.
3.  **`[ (name, age) for name, age in people_data ]`** : C'est une compréhension de liste qui crée une liste de tuples.
    *   `(name, age)` : Cette expression crée un tuple à partir de deux éléments : `name` et `age`.
    *   `for name, age in people_data` : Cette partie itère sur tous les tuples de la liste `people_data`. À chaque itération, le tuple est décompressé en deux variables : `name` et `age`.
4. **`print(people_dict)`** : Affiche le dictionnaire créé.

**Points clés :**

*   La compréhension de liste crée une liste de tuples.
*   Le constructeur `dict()` convertit une liste de tuples en un dictionnaire, en utilisant le premier élément du tuple comme clé et le second comme valeur.
*   Le déballage des tuples dans la boucle `for name, age in people_data` rend le code plus lisible.
*   La compréhension de liste dans cet exemple est utilisée pour préparer les données pour le dictionnaire.

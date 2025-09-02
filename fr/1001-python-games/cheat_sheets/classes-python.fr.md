# Classes en `python`

Les classes sont l'un des principaux mécanismes de la programmation orientée objet (POO) en Python. Une classe peut être considérée comme un "modèle" ou un "plan" pour créer des objets qui ont des attributs (données) et des méthodes (fonctions). Les objets créés à partir d'une classe sont appelés des instances de la classe. Les classes permettent de structurer le code, d'améliorer sa réutilisation et de faciliter sa maintenance.

### Structure d'une classe

```python
class ClassName:
    # Attributs de classe
    def __init__(self, param1, param2):
        # Constructeur (initialiseur) de la classe
        self.param1 = param1
        self.param2 = param2

    # Méthodes de classe
    def method(self):
        return f'{self.param1} et {self.param2}'
```

1. **Constructeur** (`__init__`) :
   Le constructeur `__init__` est une méthode spéciale qui est automatiquement appelée lors de la création d'un nouvel objet. Il est utilisé pour initialiser les attributs de l'objet.

   - `self` : un paramètre qui est une référence à l'instance actuelle de la classe. En Python, il doit obligatoirement être passé comme premier paramètre dans toutes les méthodes de classe (il n'est pas passé lors de l'appel de la méthode).
   - Les attributs, tels que `param1` et `param2`, sont affectés à l'objet via `self`. Ces attributs peuvent ensuite être utilisés par d'autres méthodes de la classe.

2. **Attributs de classe** :
   Les attributs sont des variables qui appartiennent aux objets de cette classe. Ils sont définis dans le constructeur (`__init__`) et peuvent être accessibles via une référence à l'objet.

3. **Méthodes de classe** :
   Les méthodes sont des fonctions qui peuvent manipuler les attributs de l'objet. Les méthodes peuvent utiliser les données de l'objet, les modifier ou effectuer d'autres opérations.

### Création d'un objet de classe

Une fois qu'une classe est définie, vous pouvez créer des objets de cette classe. Les objets sont des instances de la classe.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f'{self.year} {self.make} {self.model}'

# Création d'un objet
my_car = Car('Toyota', 'Corolla', 2020)
print(my_car.description())  # Sortie : 2020 Toyota Corolla
```

- Dans cet exemple, nous avons créé un objet `my_car` de la classe `Car`. Lors de la création de l'objet, les valeurs des attributs `make`, `model` et `year` sont passées, qui sont stockées dans l'objet.
- La méthode `description()` permet d'obtenir une représentation textuelle de la voiture.

### Types de méthodes

1. **Méthodes d'instance** : Ce sont des méthodes ordinaires qui opèrent sur des instances de la classe. Elles prennent une référence à l'objet comme premier paramètre (généralement `self`).

   Exemple :
   ```python
   def method(self):
       pass
   ```

2. **Méthodes de classe** : Méthodes qui prennent la classe elle-même comme premier paramètre. Le décorateur `@classmethod` est utilisé pour définir de telles méthodes. Elles peuvent modifier l'état de la classe elle-même, et non des instances individuelles de celle-ci.

   Exemple :
   ```python
   class MyClass:
       @classmethod
       def class_method(cls):
           pass
   ```

3. **Méthodes statiques** : Ce sont des méthodes qui n'utilisent ni `self` ni `cls` (c'est-à-dire qu'elles n'ont accès ni à l'instance ni à la classe). Les méthodes statiques sont déclarées à l'aide du décorateur `@staticmethod`. Elles peuvent être utiles lorsqu'une méthode ne dépend pas de l'état de l'objet ou de la classe, mais est liée à une logique appartenant à la classe.

   Exemple :
   ```python
   class MyClass:
       @staticmethod
       def static_method():
           pass
   ```

### Héritage

L'un des principes clés de la POO est l'**héritage**. Une classe peut hériter du comportement d'une autre classe, en étendant ou en modifiant ses fonctionnalités. Cela permet la réutilisation du code, évitant la duplication.

```python
class Animal:
    def speak(self):
        return 'Son d'animal'

class Dog(Animal):  # La classe Dog hérite de la classe Animal
    def speak(self):
        return 'Wouf'

# Création d'objets
dog = Dog()
print(dog.speak())  # Sortie : Wouf
```

- La classe `Dog` hérite de la méthode `speak` de la classe `Animal`, mais la surcharge pour renvoyer la chaîne `'Wouf'`.

### Polymorphisme

Le **polymorphisme** signifie la capacité des objets de différentes classes à utiliser les mêmes méthodes avec des implémentations différentes. En Python, cela est possible grâce à l'héritage et à la surcharge de méthodes.

```python
class Cat(Animal):
    def speak(self):
        return 'Miaou'

# Création d'objets
cat = Cat()
print(cat.speak())  # Sortie : Miaou
```

Ici, `Cat` surcharge également la méthode `speak`, mais renvoie une valeur différente. Cela permet d'appeler la méthode `speak` indépendamment du type d'objet.

### Encapsulation

L'**encapsulation** permet de masquer les détails d'implémentation internes et de fournir un accès aux données via des méthodes publiques. Cela aide à prévenir une mauvaise utilisation des données.

```python
class Car:
    def __init__(self, make, model):
        self._make = make  # Attribut protégé
        self._model = model

    def get_make(self):
        return self._make

    def set_make(self, make):
        self._make = make

# Création d'un objet
my_car = Car('Toyota', 'Corolla')
print(my_car.get_make())  # Sortie : Toyota
my_car.set_make('Honda')
print(my_car.get_make())  # Sortie : Honda
```

Ici, les attributs `_make` et `_model` sont protégés (généralement en Python, un underscore signifie que ces attributs ne doivent pas être utilisés directement en dehors de la classe), mais ils peuvent être accessibles et modifiés via les méthodes `get_make` et `set_make`.

### Autres caractéristiques des classes

1. **Destructeur** (`__del__`) :
   Une méthode spéciale qui est appelée lorsqu'un objet est détruit (par exemple, lorsqu'il sort de la portée). Elle peut être utilisée pour libérer des ressources.

   Exemple :
   ```python
   class MyClass:
       def __del__(self):
           print("Objet détruit")

   obj = MyClass()
   del obj  # L'objet sera détruit et la méthode __del__ sera appelée
   ```

2. **Méthodes magiques** :
   Ce sont des méthodes spéciales avec deux underscores (par exemple, `__init__`, `__str__`, `__repr__`, `__eq__`). Elles permettent de surcharger le comportement standard des opérations telles que la création d'objets, la comparaison, la représentation textuelle des objets, etc.

   Exemple :
   ```python
   class Point:
       def __init__(self, x, y):
           self.x = x
           self.y = y

       def __repr__(self):
           return f'Point({self.x}, {self.y})'

   p = Point(3, 4)
   print(p)  # Sortie : Point(3, 4)
   ```

 ---

  [Vers la table des matières](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)

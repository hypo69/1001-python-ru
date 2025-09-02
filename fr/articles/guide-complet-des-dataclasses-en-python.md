## Dataclasses : Quand Python rencontre les données structurées (avec de nouveaux exemples nommés)

En Python, lorsque vous avez besoin d'une classe pour stocker des données, vous devez généralement écrire du code répétitif pour `__init__`, `__repr__`, `__eq__` et d'autres méthodes magiques. Le module `dataclasses`, introduit dans Python 3.7, vise à résoudre ce problème en fournissant un décorateur `@dataclass` qui génère automatiquement ces méthodes pour vous.

### Qu'est-ce qu'un Dataclass ?

Un `dataclass` est une classe qui, comme son nom l'indique, est principalement destinée à stocker des données. Il offre les principaux avantages suivants :

1.  **Moins de code répétitif :** Génère automatiquement `__init__`, `__repr__`, `__eq__`, `__hash__` (sous certaines conditions) et d'autres méthodes en fonction des annotations de type de vos champs.
2.  **Lisibilité :** Le code devient plus concis et axé sur la définition de la structure des données.
3.  **Introspection :** Les champs de dataclass peuvent être facilement introspectés (vérifiés) à l'aide de fonctions du même module `dataclasses`.
4.  **Performance (avec `slots=True`) :** Peut consommer moins de mémoire et être plus rapide pour accéder aux attributs.

### Utilisation de base

Commençons par un exemple simple. Supposons que nous ayons besoin d'une classe pour représenter un point dans un espace 2D.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

# Création d'une instance
p1 = Point(10, 20)
print(p1) # Point(x=10, y=20) - __repr__ généré automatiquement

# Comparaison d'instances - __eq__ généré automatiquement
p2 = Point(10, 20)
p3 = Point(30, 40)
print(p1 == p2) # True
print(p1 == p3) # False
```

Comme vous pouvez le voir, nous n'avons pas eu à écrire `__init__` ou `__repr__`. Tout a fonctionné "d'emblée".

### Paramètres du décorateur `@dataclass`

Le décorateur `@dataclass` accepte plusieurs paramètres qui vous permettent de personnaliser le comportement généré.

```python
@dataclass(
    init=True,         # Faut-il générer __init__ (par défaut True)
    repr=True,         # Faut-il générer __repr__ (par défaut True)
    eq=True,           # Faut-il générer __eq__ (par défaut True)
    order=False,       # Faut-il générer __lt__, __le__, __gt__, __ge__ (par défaut False)
    unsafe_hash=False, # Faut-il générer __hash__ (par défaut False)
    frozen=False,      # Faut-il rendre les instances immuables (par défaut False)
    match_args=True,   # Faut-il inclure la classe dans le mécanisme de correspondance de formes structurelles (Python 3.10+, par défaut True)
    kw_only=False,     # Faut-il rendre tous les champs des arguments mot-clé uniquement dans __init__ (Python 3.10+, par défaut False)
    slots=False        # Faut-il utiliser __slots__ pour économiser de la mémoire (Python 3.10+, par défaut False)
)
class MyDataClass:
    # ...
```

Examinons les plus importants, y compris ceux de votre demande :

#### `init=True` (par défaut)

Si `True`, alors `dataclass` générera une méthode `__init__`. Si vous avez votre propre `__init__` et que vous laissez `init=True`, alors votre `__init__` sera appelé, mais les champs définis dans le dataclass ne seront pas initialisés automatiquement par son intermédiaire. Habituellement, si vous écrivez votre propre `__init__`, vous définissez `init=False` pour éviter les conflits et avoir un contrôle total sur l'initialisation.

```python
@dataclass(init=False)
class CustomPersonInit:
    name: str
    age: int

    def __init__(self, name: str, age: int, welcome_message: str = "Bonjour !"):
        self.name = name
        self.age = age
        print(welcome_message)

alice = CustomPersonInit("Alice", 30) # Affiche "Bonjour !"
print(alice) # CustomPersonInit(name='Alice', age=30) - repr fonctionne toujours
```

#### `repr=True` (par défaut)

Si `True`, il générera une méthode `__repr__` qui fournit une représentation de chaîne pratique de l'objet, utile pour le débogage.

#### `eq=True` (par défaut)

Si `True`, il générera une méthode `__eq__` qui vous permet de comparer deux instances de la classe pour l'égalité en vérifiant l'égalité de tous leurs champs.

#### `order=False`

Si `True`, alors `dataclass` générera les méthodes `__lt__`, `__le__`, `__gt__`, `__ge__`. Cela vous permet de comparer des instances pour "inférieur à", "supérieur à", etc. La comparaison se fait dans l'ordre de déclaration des champs. Pour que `order=True` fonctionne, `eq=True` doit également être défini.

```python
@dataclass(order=True)
class Person:
    name: str
    age: int

alice = Person("Alice", 30)
boris = Person("Boris", 25)
victor = Person("Victor", 35) # Ajoutons Victor
galina = Person("Galina", 30)
alice_older = Person("Alice", 35)


print(f"Alice ({alice.age}) > Boris ({boris.age})? {alice > boris}") # False (car 'Alice' < 'Boris' par nom). La comparaison se fait lexicographiquement sur le tuple (nom, âge). ('Alice', 30) < ('Boris', 25) est False. Donc `>` sera False.
# Explication : ('Alice', 30) > ('Boris', 25) -> False, car 'Alice' < 'Boris'.
print(f"Alice ({alice.age}) < Alice_older ({alice_older.age})? {alice < alice_older}") # True (car le nom est le même, et l'âge 30 < 35)
print(f"Galina ({galina.age}) == Alice ({alice.age})? {galina == alice}") # False (noms différents)
```

**Remarque importante :** L'ordre des champs est important pour `order=True`.

#### `unsafe_hash=False`

Si `True`, il générera une méthode `__hash__`. Les Dataclasses ne sont pas hachables par défaut s'ils sont modifiables (`frozen=False`), car les objets hachables doivent être immuables. Si vous êtes sûr que votre dataclass modifiable ne sera utilisé que dans des contextes où son hachage ne changera pas (ce qui est risqué !), vous pouvez définir `unsafe_hash=True`.
Beaucoup plus souvent, `__hash__` est généré automatiquement si :
1.  `frozen=True`.
2.  `frozen=False`, mais `eq=True` et tous les champs sont également hachables.

```python
@dataclass(frozen=True) # Les dataclasses gelés sont hachables
class ImmutablePoint:
    x: int
    y: int

p = ImmutablePoint(1, 2)
print(hash(p)) # Fonctionne

@dataclass(unsafe_hash=True) # Risqué si l'objet est modifiable
class MutableButHashable:
    value: int

m = MutableButHashable(5)
print(hash(m))
m.value = 10
print(hash(m)) # Le hachage a changé, ce qui peut entraîner des problèmes lors de l'utilisation dans un set/dict
```

#### `frozen=False`

Si `True`, les instances de la classe deviennent immuables. Après avoir créé un objet, vous ne pourrez pas modifier les valeurs de ses champs. Ceci est utile pour créer des objets immuables qui sont plus faciles à utiliser dans des applications multi-thread ou comme clés de dictionnaire (s'ils sont hachables).

```python
@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

c = Coordinate(10.0, 20.0)
# c.lat = 15.0 # AttributeError: cannot assign to field 'lat'
```

#### `kw_only=False` (Python 3.10+)

Si `True`, **tous** les champs de `__init__` deviennent des arguments **mot-clé uniquement**. Cela signifie que vous devez passer les valeurs des champs par leur nom, et non par leur position. Cela améliore la lisibilité et évite les erreurs, en particulier lorsque la classe a de nombreux champs ou qu'ils peuvent avoir les mêmes types.

```python
@dataclass(kw_only=True)
class UserConfig:
    username: str
    email: str
    is_active: bool = True
    theme: str = "dark"

# user1 = UserConfig("alice_ivanova", "alice@example.com") # TypeError: __init__() takes 0 positional arguments but 3 were given
user1 = UserConfig(username="alice_ivanova", email="alice@example.com")
print(user1)

# Vous pouvez remplacer ce comportement pour un champ spécifique avec field(kw_only=False)
@dataclass(kw_only=True)
class MixedConfig:
    # Positionnel obligatoire (pas de style dataclass)
    # Le champ `id` ne sera pas kw_only, bien que la classe soit spécifiée comme kw_only=True
    id: int = field(kw_only=False)
    name: str = field(kw_only=False)

    # Les champs restants sont kw_only
    email: str
    age: int = 0

# Notez que id et name sont passés positionnellement, et email est passé par nom
mixed_config = MixedConfig(123, "Boris", email="boris@example.com")
print(mixed_config)
# mixed_config_fail = MixedConfig(id=123, name="Victor", email="viktor@example.com") # Erreur, id et name seraient positionnels
# Ce scénario est moins typique, kw_only est généralement appliqué à toute la classe
```

**Remarque :** `field(kw_only=False)` sur un champ remplace `kw_only=True` au niveau de la classe, rendant ce champ spécifique positionnel. Cependant, le plus souvent, `kw_only=True` est utilisé pour toute la classe. L'utilisation principale de `field(kw_only=True)` est lorsque vous avez un dataclass normal (`kw_only=False` par défaut), mais que vous souhaitez rendre *certains* champs mot-clé uniquement.

#### `slots=False` (Python 3.10+)

Si `True`, `dataclass` générera `__slots__` pour votre classe. `__slots__` est un attribut spécial qui permet à Python d'allouer une quantité de mémoire fixe pour les instances de classe, au lieu d'utiliser un dictionnaire `__dict__` dynamique pour stocker les attributs.

**Avantages de `slots=True` :**
*   **Économies de mémoire :** Réduit considérablement la quantité de mémoire consommée par chaque instance. Ceci est particulièrement important pour les applications qui créent des millions d'objets.
*   **Accès plus rapide aux attributs :** L'accès aux attributs via `__slots__` peut être légèrement plus rapide, car Python n'a pas besoin de les rechercher dans un dictionnaire.

**Inconvénients de `slots=True` :**
*   **Impossible d'ajouter de nouveaux attributs à la volée :** Vous ne pourrez pas attribuer un attribut qui n'a pas été déclaré dans le dataclass (ou dans le `__slots__` d'une classe parente).
*   **Difficultés avec l'héritage multiple :** Il peut être difficile d'utiliser `__slots__` avec l'héritage multiple, surtout si certaines classes parentes n'utilisent pas `__slots__` ou les utilisent différemment.
*   **N'a pas de `__dict__` :** Les instances n'auront pas d'attribut `__dict__` à moins qu'il n'ait été explicitement ajouté à `__slots__` ou à une classe parente.

```python
import sys

@dataclass
class RegularPoint:
    x: int
    y: int

@dataclass(slots=True)
class SlottedPoint:
    x: int
    y: int

rp = RegularPoint(1, 2)
sp = SlottedPoint(1, 2)

print(f"Taille de RegularPoint : {sys.getsizeof(rp)} octets")
# Environ 56 octets sur Python 3.10+ (peut varier)
# print(rp.__dict__) # {'x': 1, 'y': 2} - a __dict__

print(f"Taille de SlottedPoint : {sys.getsizeof(sp)} octets")
# Environ 32 octets sur Python 3.10+ (peut varier) - nettement plus petit
# print(sp.__dict__) # AttributeError: 'SlottedPoint' object has no attribute '__dict__'

# Tentative d'ajout d'un nouvel attribut à un dataclass à slots
try:
    sp.z = 30
except AttributeError as e:
    print(f"Erreur lors de l'ajout d'un nouvel attribut : {e}")
```

**Quand utiliser `slots=True` ?**
Lorsque vous créez un très grand nombre d'instances de la même classe et que les économies de mémoire sont une priorité. C'est une excellente optimisation, mais elle a ses compromis.

### La fonction `field()` : Configuration détaillée des champs

En plus des paramètres au niveau de la classe, vous pouvez configurer chaque champ individuellement à l'aide de la fonction `field()` du module `dataclasses`. Ceci est particulièrement utile lorsque vous avez besoin d'une logique plus complexe pour les champs qu'une simple annotation de type.

```python
from dataclasses import dataclass, field
from typing import List, Dict, Any
import uuid # Pour générer des ID

@dataclass
class Product:
    id: str = field(default_factory=lambda: "prod-" + str(uuid.uuid4())[:8], init=False) # Non initialisé via __init__, généré automatiquement
    name: str
    price: float = field(compare=False, metadata={'unit': 'USD', 'min_value': 0.0}) # Non inclus dans la comparaison, a des métadonnées
    tags: List[str] = field(default_factory=list, repr=False) # Utilise une fabrique pour la liste, non affichée dans repr
    description: str = field(default="Description non disponible") # Valeur par défaut normale
    details: Dict[str, Any] = field(default_factory=dict, hash=False) # Non inclus dans le hachage

p = Product(name="Ordinateur portable", price=1200.0, tags=["électronique", "technologie"])
print(p)
# Product(id='prod-...', name='Ordinateur portable', price=1200.0, description='Description non disponible', details={})
# Notez que 'tags' n'est pas dans le repr, et 'id' a été généré automatiquement.

p2 = Product(name="Ordinateur portable", price=1500.0, tags=["électronique", "technologie"])
print(f"p == p2? {p == p2}") # True, car le prix n'est pas inclus dans la comparaison (compare=False)

# p3 = Product(name="PC de bureau", price=1000.0, details={"cpu": "Intel"})
# print(hash(p3)) # TypeError: unhashable type: 'dict' (à cause de details: hash=False)
# Si frozen=True, et que details n'était pas hash=False, alors le dict devrait être immuable.
```

Examinons les paramètres de `field()` :

*   **`default`** : Une valeur par défaut normale pour le champ.
    ```python
    value: int = field(default=0)
    ```

*   **`default_factory`** : Une fonction sans arguments qui sera appelée pour obtenir la valeur par défaut du champ. **Il est obligatoire d'utiliser `default_factory` pour les valeurs par défaut modifiables (listes, dictionnaires, objets) afin d'éviter les problèmes d'état partagé entre les instances !**
    ```python
    items: List[str] = field(default_factory=list)
    ```

*   **`init`** : Si `True` (par défaut), le champ sera inclus dans la méthode `__init__` générée. Si `False`, le champ ne sera pas un argument dans le constructeur, et vous devez soit lui fournir un `default` / `default_factory`, soit l'initialiser dans `__post_init__`.
    ```python
    import time
    timestamp: float = field(init=False, default_factory=time.time)
    ```

*   **`repr`** : Si `True` (par défaut), le champ sera inclus dans la méthode `__repr__` générée. Utile pour masquer des données volumineuses ou sensibles.
    ```python
    password: str = field(repr=False)
    ```

*   **`compare`** : Si `True` (par défaut), le champ sera inclus dans les méthodes `__eq__` et `__order__` générées. Si `False`, il n'affectera pas la comparaison des objets.
    ```python
    version: str = field(compare=False)
    ```

*   **`hash`** : Si `True` (par défaut), le champ sera inclus dans la méthode `__hash__` générée. Si `False`, il n'affectera pas le hachage de l'objet. Si la classe est `frozen=True`, mais qu'un champ a `hash=False`, alors la classe ne pourra pas générer son `__hash__` et deviendra non hachable.
    ```python
    config: Dict[str, Any] = field(hash=False, default_factory=dict)
    ```

*   **`metadata`** : Un dictionnaire pour stocker des données arbitraires associées au champ. `dataclasses` ignore ces données, mais elles peuvent être utilisées par des outils externes (par exemple, pour la validation, la sérialisation, la génération de documentation).
    ```python
    user_id: int = field(metadata={'help': 'Identifiant unique de l\'utilisateur', 'validator': 'positive_int'})
    ```

*   **`kw_only`** : (Python 3.10+) Si `True`, ce champ spécifique devient un argument mot-clé uniquement dans `__init__`. Si `False`, il devient positionnel. Cela vous permet de mélanger des arguments positionnels et des arguments mot-clé uniquement lorsque le `kw_only` de la classe est `False` par défaut.
    ```python
    @dataclass
    class FlexibleParams:
        mandatory_pos: str # Positionnel
        optional_kw: int = field(default=0, kw_only=True) # Mot-clé uniquement

    fp1 = FlexibleParams("obligatoire", optional_kw=100)
    # fp2 = FlexibleParams("obligatoire", 200) # TypeError: __init__() takes 1 positional argument but 2 were given (optional_kw)
    ```

### La fonction `fields()` : Introspection de Dataclass

La fonction `fields()` du module `dataclasses` vous permet d'obtenir des informations sur les champs d'un dataclass ou de son instance. Elle renvoie un tuple d'objets `Field`.

```python
from dataclasses import dataclass, field, fields
from typing import List

@dataclass
class Book:
    title: str
    author: str = field(metadata={'display_name': 'Auteur', 'max_length': 100})
    pages: int = field(default=0, metadata={'min_value': 1})
    tags: List[str] = field(default_factory=list, repr=False)

# Obtenir des informations sur les champs de la classe Book
book_fields = fields(Book)

for f in book_fields:
    print(f"Nom du champ : {f.name}")
    print(f"Type du champ : {f.type}")
    print(f"Valeur par défaut : {f.default}")
    print(f"Utilise default_factory : {f.default_factory is not None}")
    print(f"Inclus dans init : {f.init}")
    print(f"Inclus dans repr : {f.repr}")
    print(f"Inclus dans compare : {f.compare}")
    print(f"Inclus dans hash : {f.hash}")
    print(f"Métadonnées : {f.metadata}")
    print(f"Mot-clé uniquement : {f.kw_only}") # Pour Python 3.10+
    print("-" * 20)

# Accéder aux métadonnées d'un champ spécifique :
author_field_info = next(f for f in book_fields if f.name == 'author')
print(f"Nom d'affichage de l'auteur : {author_field_info.metadata.get('display_name')}")
```

L'objet `Field` a les attributs suivants : `name`, `type`, `default`, `default_factory`, `init`, `repr`, `hash`, `compare`, `metadata`, `kw_only`.

### La méthode `__post_init__`

Parfois, vous avez besoin d'une logique supplémentaire après que le `__init__` automatique du dataclass a fini d'initialiser les champs. Pour cela, vous pouvez définir une méthode `__post_init__`. Elle sera appelée immédiatement après `__init__`.

Ceci est utile pour :
*   La validation des données.
*   Le calcul de champs dérivés basés sur ceux déjà initialisés.
*   L'exécution de toute autre logique qui dépend de champs entièrement initialisés.

```python
import datetime

@dataclass
class User:
    first_name: str
    last_name: str
    email: str = field(init=False) # Ce champ ne sera pas inclus dans les paramètres de __init__
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now, init=False)

    def __post_init__(self):
        print(f"--- __post_init__ démarré pour {self.first_name} {self.last_name} ---")
        # Validation
        if not self.first_name or not self.last_name:
            raise ValueError("Le prénom et le nom de famille ne peuvent pas être vides.")
        # Calcul d'un champ dérivé
        self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@example.com"
        print(f"Utilisateur {self.first_name} {self.last_name} créé avec l\'email : {self.email}")
        print(f"Heure de création : {self.created_at}")
        print(f"--- __post_init__ terminé ---")

alice_ivanova = User("Alice", "Ivanova")
print("\nObjet créé :")
print(alice_ivanova)

print("\n")

try:
    victor_no_last_name = User("Victor", "")
except ValueError as e:
    print(f"Erreur lors de la création de l\'utilisateur : {e}")
```

### Héritage de Dataclass

Les Dataclasses prennent en charge l'héritage. Les champs des classes de base sont inclus dans les classes enfants.

```python
@dataclass
class Vehicle:
    make: str
    model: str

@dataclass
class Car(Vehicle):
    num_doors: int
    is_electric: bool = False

@dataclass
class ElectricCar(Car):
    battery_kwh: float

alices_car = Car("Toyota", "Camry", 4)
print(alices_car) # Car(make='Toyota', model='Camry', num_doors=4, is_electric=False)

boris_car = ElectricCar("Tesla", "Model 3", 4, True, 75.0)
print(boris_car) # ElectricCar(make='Tesla', model='Model 3', num_doors=4, is_electric=True, battery_kwh=75.0)
```

**Caractéristiques de l'héritage avec `slots=True` :**
*   Si la classe parente utilise `__slots__`, la classe enfant doit également utiliser `__slots__` pour bénéficier des économies de mémoire.
*   La classe enfant doit définir son propre `__slots__` pour ses nouveaux champs.
*   Si la classe enfant ne définit pas `__slots__`, elle aura un `__dict__` en plus des slots du parent.

### Quand utiliser les Dataclasses ?

*   **Classes conteneurs de données :** Lorsque l'objectif principal de la classe est de stocker des données, et que vous avez besoin de `__init__`, `__repr__`, `__eq__` automatiques.
*   **Objets immuables :** Lorsque vous avez besoin d'objets dont l'état ne doit pas changer après la création (`frozen=True`).
*   **Configurations :** Pour définir la structure des paramètres de configuration.
*   **Objets de transfert de données (DTO) :** Pour transférer des données structurées entre les parties d'une application.
*   **Logique métier simple :** Lorsque les méthodes de la classe opèrent principalement sur les données de la classe elle-même, n'ont pas d'état interne complexe ou d'effets secondaires.

### Quand NE PAS utiliser les Dataclasses ?

*   **Classes à comportement riche :** Lorsqu'une classe a une logique métier complexe, de nombreuses méthodes qui interagissent avec des systèmes externes, ou un état interne complexe, il est préférable d'utiliser une classe normale.
*   **Modèles de mappage OR (ORM) :** Bien que les dataclasses puissent faire partie d'un ORM, ils ne remplacent pas les modèles ORM complets, qui nécessitent souvent des méthodes spécifiques pour travailler avec une base de données, le chargement paresseux, etc.
*   **Polymorphisme et hiérarchie d'héritage profonde :** Si vous avez une hiérarchie de classes complexe avec un polymorphisme profond et une redéfinition de comportement, les classes normales peuvent être plus flexibles.

### Conclusion

Les `dataclasses` sont un ajout puissant et pratique à Python qui simplifie considérablement la création de classes axées sur les données. Ils aident à écrire un code plus propre, plus lisible et plus maintenable, et des options comme `slots=True` et `kw_only=True` offrent des possibilités supplémentaires d'optimisation des performances et d'amélioration de l'ergonomie de l'API de votre code. N'oubliez pas `field()` pour la configuration détaillée de chaque champ et `fields()` pour l'introspection !

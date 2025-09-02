## Théorie des groupes - Demi-groupe
La structure la plus simple de la théorie des groupes est un demi-groupe. Un demi-groupe est un ensemble pour lequel une opération binaire associative est définie, qui prend deux éléments de cet ensemble en entrée et en renvoie un troisième. À partir de maintenant, tous les exemples seront donnés dans le langage de programmation Python.

En Python, nous pouvons définir le concept de demi-groupe à l'aide de `typing.Protocol` (pour la vérification de type statique) ou simplement par convention (duck typing). Pour plus de clarté, nous utiliserons des dictionnaires qui stockent l'opération `combine`.

```python
from typing import TypeVar, Callable, Protocol, Generic
import functools # Pour reduce

T = TypeVar('T')

# Nous décrivons la structure d'un demi-groupe à l'aide de Protocol (pour le typage statique)
class Semigroup(Protocol[T]):
    # Callable[[T, T], T] signifie une fonction qui prend deux arguments de type T
    # et renvoie une valeur de type T
    combine: Callable[[T, T], T]

# Exemple : Un demi-groupe de nombres naturels (ou entiers/réels) avec addition
# Nous représentons un demi-groupe spécifique comme un dictionnaire avec la clé 'combine'
addition_semigroup: Semigroup[int] = {
    "combine": lambda a, b: a + b
}

# Exemple : Un demi-groupe de nombres avec multiplication
multiplication_semigroup: Semigroup[int] = {
    "combine": lambda a, b: a * b
}

# Exemple : Un demi-groupe de chaînes de caractères avec concaténation
concatenation_semigroup: Semigroup[str] = {
    "combine": lambda a, b: a + b
}
```

L'opération sur les éléments d'un demi-groupe doit avoir la propriété d'associativité. Testons cela avec la fonction intégrée `assert` :

```python
def check_associativity(semigroup: Semigroup[T], a: T, b: T, c: T) -> None:
    # Nous vérifions que (a * b) * c == a * (b * c)
    # Nous utilisons l'opération combine du demi-groupe passé
    left_side = semigroup["combine"](semigroup["combine"](a, b), c)
    right_side = semigroup["combine"](a, semigroup["combine"](b, c))
    assert left_side == right_side, f"L'associativité a échoué pour {semigroup}: ({a}, {b}, {c})"

check_associativity(addition_semigroup, 1, 2, 3)
check_associativity(multiplication_semigroup, 2, 3, 4) # 1*2*3 = 6, (1*2)*3 = 6, 1*(2*3)=6
check_associativity(concatenation_semigroup, 'a', 'b', 'c')
```

Un demi-groupe n'a pas de propriétés particulièrement intéressantes. Cependant, même avec leur exemple, nous voyons la commodité de la théorie des groupes - la capacité de travailler avec des ensembles et des opérations sur eux à l'aide d'une interface abstraite (dans notre cas, un dictionnaire avec une fonction `combine`).

Par exemple, nous pouvons écrire une fonction de réduction pour une liste de valeurs de demi-groupe en utilisant une valeur initiale. Cela fait déjà allusion à la structure suivante - un monoïde.

```python
from typing import List

# Cette fonction ressemble plus à un fold de la section suivante,
# car elle nécessite une valeur initiale. Une réduction de demi-groupe pure
# nécessiterait une liste non vide.
def reduce_semigroup_with_initial(
    values: List[T],
    semigroup: Semigroup[T],
    initial_value: T
) -> T:
    # Nous utilisons functools.reduce pour appliquer séquentiellement combine
    return functools.reduce(semigroup["combine"], values, initial_value)

# Nous pouvons maintenant utiliser cette fonction pour réduire une liste :
sum_val = reduce_semigroup_with_initial([1, 2, 3, 4], addition_semigroup, 0)
assert sum_val == 10

product_val = reduce_semigroup_with_initial([1, 2, 3, 4], multiplication_semigroup, 1)
assert product_val == 24

concat_val = reduce_semigroup_with_initial(['a', 'b', 'c'], concatenation_semigroup, '')
assert concat_val == 'abc'

```
L'utilisation de la fonction de réduction de demi-groupe nous amène en douceur à la structure suivante, beaucoup plus intéressante de la théorie des groupes - le monoïde.

**Théorie des groupes - Monoïde**
Un monoïde est un demi-groupe avec un élément neutre défini (`unit` ou `identity`).

```python
# Nous définissons un protocole pour un Monoïde, héritant de Semigroup
class Monoid(Semigroup[T], Protocol[T]):
    unit: T # Élément neutre

# Monoïde d'addition de nombres (élément neutre - 0)
addition_monoid: Monoid[int] = {
    "combine": lambda a, b: a + b,
    "unit": 0
}
```

L'élément neutre est un élément tel que sa combinaison avec tout autre élément ne modifie pas cet autre élément (`a + 0 = a`, `a * 1 = a`, `s + "" = s`). Pour l'addition de nombres, cet élément neutre est, bien sûr, zéro.

Testons cette propriété d'un monoïde avec `assert` :

```python
def check_unit_combination(monoid: Monoid[T], value: T) -> None:
    # Nous vérifions que combine(value, unit) == value
    # et combine(unit, value) == value (pour l'exhaustivité)
    assert monoid["combine"](value, monoid["unit"]) == value
    assert monoid["combine"](monoid["unit"], value) == value

check_unit_combination(addition_monoid, 10)
```

L'élément neutre du monoïde de multiplication de nombres est un.

```python
multiplication_monoid: Monoid[int] = {
    "combine": lambda a, b: a * b,
    "unit": 1
}

check_unit_combination(multiplication_monoid, 25)
```

En conséquence, l'élément neutre du monoïde de concaténation de chaînes de caractères est la chaîne vide.

```python
concatenation_monoid: Monoid[str] = {
    "combine": lambda a, b: a + b,
    "unit": ""
}

check_unit_combination(concatenation_monoid, 'a')
```

Et maintenant, nous arrivons à la propriété la plus intéressante des monoïdes - vous pouvez utiliser l'opération de pliage (fold) pour travailler avec eux. C'est essentiellement le même `reduce_semigroup_with_initial`, mais maintenant la valeur initiale est prise directement du monoïde (`unit`).

```python
def fold(monoid: Monoid[T], values: List[T]) -> T:
    # Nous utilisons functools.reduce, en commençant par l'élément neutre monoid['unit']
    return functools.reduce(monoid["combine"], values, monoid["unit"])

# Avec fold, nous avons des capacités complètement magiques :
sum_folded = fold(addition_monoid, [1, 2, 3, 4])
assert sum_folded == 10

product_folded = fold(multiplication_monoid, [1, 2, 3, 4])
assert product_folded == 24

concatenated_folded = fold(concatenation_monoid, ['a', 'b', 'c', 'd'])
assert concatenated_folded == 'abcd'
```

Nous pouvons également définir des monoïdes pour les opérations de comparaison de nombres. Pour `min`, l'élément neutre sera l'infini, et pour `max` - moins l'infini.

```python
import math # Pour float('inf')

min_monoid: Monoid[float] = { # Nous utilisons float pour l'infini
    "combine": lambda a, b: min(a, b),
    "unit": float('inf')
}

max_monoid: Monoid[float] = {
    "combine": lambda a, b: max(a, b),
    "unit": float('-inf')
}

min_fold_result = fold(min_monoid, [1, 9, 6, 4])
assert min_fold_result == 1

max_fold_result = fold(max_monoid, [1, 9, 6, 4])
assert max_fold_result == 9
```

Et de plus, nous pouvons définir, par exemple, un monoïde de fonctions. Par exemple, un monoïde de fonctions unaires (prenant un argument) sur les nombres, où l'opération `combine` sera la composition de fonctions, et l'élément neutre (`unit`) sera la fonction identité (`lambda x: x`).

```python
# Type pour une fonction unaire de int à int
IntUnaryFunc = Callable[[int], int]

# Monoïde pour la composition de fonctions (int -> int)
# IMPORTANT : L'ordre de composition est f(g(x))
function_monoid: Monoid[IntUnaryFunc] = {
    "combine": lambda f, g: lambda x: f(g(x)), # f après g
    "unit": lambda x: x # Fonction identité
}

add_one: IntUnaryFunc = lambda x: x + 1
double: IntUnaryFunc = lambda x: x * 2

# Pliage d'une liste de fonctions : [add_one, double]
# D'abord, l'unité sera appliquée, puis double, puis add_one.
# fold(monoid, [f, g]) est équivalent à combine(combine(unit, f), g) = combine(f, g)
# combine(f, g) = lambda x: f(g(x))
function_fold_result_func = fold(function_monoid, [add_one, double])

# Appliquer le résultat au nombre 1 : add_one(double(1)) = add_one(2) = 3
assert function_fold_result_func(1) == 3

# Si l'ordre des fonctions est important et que vous avez besoin de g(f(x)), vous devez modifier combine :
# "combine": lambda f, g: lambda x: g(f(x))
```

Sur l'exemple d'un monoïde, nous voyons que la théorie des groupes nous permet de travailler avec de nombreux ensembles et opérations différents sur eux de la même manière.

Vous souvenez-vous, à l'école, on nous a dit que tout nombre à la puissance zéro est égal à un, mais on ne nous a jamais expliqué pourquoi ?

Cette propriété devient évidente au premier coup d'œil sur le monoïde de multiplication. L'exponentiation est l'application répétée de l'opération `combine` du monoïde de multiplication. Par exemple, `2^3` est `combine(combine(unit, 2), 2), 2)` ou, ce qui est la même chose, `combine(combine(2, 2), 2)`.

```python
# 2^3 en utilisant le monoïde de multiplication
power_3 = multiplication_monoid["combine"](
    multiplication_monoid["combine"](2, 2), # 2*2
    2                                       # (2*2)*2
)
assert power_3 == 8
```

Mais qu'est-ce que la puissance zéro ? C'est l'application de l'opération `combine` zéro fois à l'élément initial. Quel résultat devrions-nous obtenir ? Si nous n'appliquons pas `combine` du tout, il ne nous reste que l'élément neutre `unit`, qui dans le cas du monoïde de multiplication est égal à un. C'est pourquoi `x^0 = 1`.

**Théorie des groupes - Groupe**
Un groupe est un monoïde pour lequel chaque élément a un élément inverse du même ensemble, de sorte que la combinaison d'un élément avec son inverse donne l'élément neutre.

```python
# Nous définissons un protocole pour un Groupe, héritant de Monoid
class Group(Monoid[T], Protocol[T]):
    inverse: Callable[[T], T] # Fonction pour obtenir l'élément inverse

# Un exemple classique de groupe est l'ensemble des entiers sous l'opération d'addition
addition_group: Group[int] = {
    "combine": lambda a, b: a + b,
    "unit": 0,
    "inverse": lambda a: -a # L'élément inverse pour l'addition est la négation
}
```

La propriété principale d'un groupe est que la combinaison d'un élément avec son élément inverse donne toujours l'élément neutre du groupe :

```python
def check_inversion_combination(group: Group[T], value: T) -> None:
    # Nous vérifions que combine(value, inverse(value)) == unit
    # et combine(inverse(value), value) == unit
    assert group["combine"](value, group["inverse"](value)) == group["unit"]
    assert group["combine"](group["inverse"](value), value) == group["unit"]

check_inversion_combination(addition_group, 5) # 5 + (-5) == 0
```

On peut dire qu'un groupe est une structure mathématique qui abstrait la notion de symétrie. C'est à l'aide de cette structure que les physiciens étudient les propriétés de l'espace, du temps, de l'énergie et des particules élémentaires - à la base de l'appareil mathématique de la théorie de la relativité et de la mécanique quantique se trouve la théorie des groupes. Avec son aide, en 1918, Emmy Noether a prouvé ses célèbres théorèmes selon lesquels toute loi de conservation, que ce soit la loi de conservation de l'énergie, de la quantité de mouvement ou de la charge, découle de symétries physiques fondamentales.

De plus, les monoïdes et les groupes sont souvent utilisés en programmation fonctionnelle. Si vous étudiez un peu la théorie des groupes, vous verrez que de nombreux problèmes et structures en programmation sont des cas particuliers d'une structure mathématique plus abstraite. L'exemple le plus simple d'un groupe en programmation est le système Annuler-Rétablir, implémenté dans de nombreuses applications (l'opération est l'action de l'utilisateur, l'opération inverse est l'annulation de l'action, l'élément neutre est l'absence de modifications).

**Monadologie**
La beauté des symétries fascine les gens depuis l'Antiquité. Dans l'école fondée par le légendaire philosophe et géomètre grec ancien Pythagore, ses élèves vénéraient la monade, représentée comme un cercle avec un point gras en son centre même :

*(Image de la monade de Pythagore)*

Le sens mystique de la monade résidait dans son point central - ce point personnifie le "rien" d'où naît l'Univers. Selon les pythagoriciens, il n'y a aucune restriction à l'émergence de toutes les choses possibles à partir de rien, mais en même temps que ces choses, leurs contraires apparaissent également. En dépliant le point de dimension zéro en un nombre infini de contraires, nous obtenons un cercle - une figure sur laquelle se trouve un nombre infini de points, pour chacun desquels, par rapport au centre du cercle, il existe un point opposé. En général, cette description correspond entièrement à la notion de groupe de la théorie des groupes.

Dans son magnum opus philosophique intitulé "Monadologie", le grand philosophe et mathématicien allemand Gottfried Wilhelm Leibniz a exposé sa vision du monde, selon laquelle toute notre réalité se compose d'un nombre infini de telles monades duales. En l'honneur de ce concept pythagoricien-leibnizien de la monade, la structure principale d'une autre théorie mathématique - la théorie des catégories - a été nommée.

Si la théorie des groupes abstrait les opérations algébriques et géométriques intuitives de base en structures générales, alors la théorie des catégories est comme l'étape suivante sur l'échelle des abstractions - une abstraction d'abstractions. La théorie des catégories étudie diverses structures mathématiques - groupes, graphes, ensembles - comme des catégories abstraites avec des objets (éléments) et des morphismes (opérations) entre eux. Les morphismes sont généralement représentés par des flèches et sont appelés "flèches". Un reflet de ce nom sont les fonctions lambda (`lambda`) ou les fonctions régulières (`def`) en programmation, que vous connaissez probablement, qui transforment certaines valeurs en d'autres.

Examinons les concepts de base de la théorie des catégories.

**Théorie des catégories - Flèche**
Une flèche (ou morphisme) en théorie des catégories est une application (fonction) entre deux catégories (ensembles d'objets) - une correspondance de chaque objet de la première catégorie à un objet de la seconde. Prenons, par exemple, deux des catégories les plus simples - les entiers non négatifs et les chaînes de la lettre "a".

```
0 -> ""
1 -> "a"
2 -> "aa"
3 -> "aaa"
4 -> "aaaa"
...
```

Ici, il est clairement visible que chaque élément de la catégorie des nombres est mappé à un élément de la catégorie des chaînes de caractères composées de la lettre 'a'. Toute application de ce type peut être décrite par une fonction. Dans ce cas, c'est :

```python
def map_number_to_a_string(num: int) -> str:
    # Nous nous assurons que le nombre est non négatif pour la répétition
    if num < 0:
        raise ValueError("Le nombre d'entrée doit être non négatif")
    return "a" * num # En Python, une chaîne est répétée par multiplication

assert map_number_to_a_string(3) == "aaa"
```

Il n'est pas nécessaire qu'un objet de la première catégorie corresponde à un objet unique de la seconde. Par exemple, pour la flèche suivante de la catégorie des nombres à la catégorie de la vérité (valeurs booléennes), il n'y a que deux objets dans la seconde catégorie (`True` et `False`), mais chaque objet de la première est mappé à l'un des objets de la seconde :

```
0 -> False
1 -> False
2 -> False
3 -> True
4 -> True
...
n -> True (pour n >= 3)
```

La fonction (flèche) dans ce cas peut être décrite comme :

```python
def map_number_to_boolean(number: int) -> bool:
    return number >= 3

assert map_number_to_boolean(2) == False
assert map_number_to_boolean(5) == True
```

**Théorie des catégories - Foncteur et Endofoncteur**
Nous pouvons envelopper des objets de n'importe quelle catégorie dans des conteneurs abstraits. Si nous avons des catégories (types) A et B, et que nous avons un conteneur F (par exemple, `list`, `Optional`, `Future`), qui peut contenir un ou plusieurs objets des catégories A ou B, alors nous obtenons deux nouvelles catégories (types) F(A) et F(B) (par exemple, `list[A]` et `list[B]`).

Par exemple, si nous avons une catégorie de nombres (`int`) et une catégorie de chaînes de caractères (`str`), et que nous avons un conteneur `list`, alors nous obtenons deux nouvelles catégories - une liste de nombres (`list[int]`) et une liste de chaînes de caractères (`list[str]`). En Python, ces relations se reflètent dans le système de types :

```python
number: int = 1
string_value: str = 'a'

numbers: list[int] = [1, 2, 3]
strings: list[str] = ['a', 'b', 'c']
```

En théorie des catégories, les applications entre les catégories d'objets et les catégories de conteneurs sont décrites, qui préservent la structure lors de la transformation. De telles applications sont appelées foncteurs. L'application elle-même est appelée `map` (ou `fmap`).

Il existe plusieurs types différents de foncteurs. Le plus utilisé d'entre eux est l'endofoncteur, dans lequel la transformation se produit au sein de la même catégorie de conteneur F(A) -> F(B) (par exemple, `list[A] -> list[B]`).

```python
# Type général pour les variables A et B
A = TypeVar('A')
B = TypeVar('B')

# Protocole pour un Foncteur
class Functor(Protocol[A]):
    # La méthode map prend une fonction (flèche) de A à B
    # et renvoie un nouveau Foncteur avec des éléments de type B.
    # Important : elle renvoie une instance du même type de foncteur (par exemple, list).
    def map(self, func: Callable[[A], B]) -> 'Functor[B]':
        ...

# Un exemple classique d'endofoncteur en Python est la liste.
# Bien que list n'ait pas de méthode .map par défaut, nous pouvons facilement l'implémenter
# ou utiliser des compréhensions de liste (ce qui est plus idiomatique).

# Exemple d'utilisation de la compréhension de liste comme analogue de map :
map_number_to_boolean_func = lambda number: number >= 3
numbers_list: list[int] = [1, 2, 3, 4]

# Appliquer la fonction à chaque élément de la liste, obtenir une nouvelle liste
booleans_list: list[bool] = [map_number_to_boolean_func(n) for n in numbers_list]
assert booleans_list == [False, False, True, True]

# Vous pouvez également utiliser la fonction intégrée map, qui renvoie un itérateur :
booleans_iterator = map(map_number_to_boolean_func, numbers_list)
assert list(booleans_iterator) == [False, False, True, True]
```

Ainsi, si nous avons une flèche (fonction) `A -> B`, alors à l'aide d'un foncteur (par exemple, `list` et son opération `map`/compréhension de liste), nous pouvons construire une flèche `F[A] -> F[B]`.

Plusieurs lois doivent être respectées pour les foncteurs.

La première loi est la loi de l'identité : `functor.map(id) == functor` (l'application de la fonction identité ne doit pas modifier le foncteur).

```python
def id_func(x: T) -> T:
    return x

# Vérification pour une liste :
numbers_list = [1, 2, 3]
assert [id_func(x) for x in numbers_list] == numbers_list
```

La deuxième loi est la loi de composition : `functor.map(g o f) == functor.map(f).map(g)` (où `g o f` est la composition de fonctions, `lambda x: g(f(x))`). Le mappage d'une composition de fonctions est équivalent au mappage séquentiel de ces fonctions.

```python
f: Callable[[int], str] = lambda x: str(x) # int -> str
g: Callable[[str], bool] = lambda x: len(x) > 1 # str -> bool
compose_gf: Callable[[int], bool] = lambda x: g(f(x)) # int -> bool

numbers_list = [5, 10, 15]

# Côté gauche : map(g o f)
left_side = [compose_gf(x) for x in numbers_list] # [False, True, True]

# Côté droit : map(f) puis map(g)
intermediate = [f(x) for x in numbers_list] # ['5', '10', '15']
right_side = [g(y) for y in intermediate] # [False, True, True]

assert left_side == right_side
```

**Théorie des catégories - Monade**
Une monade étend les capacités d'un foncteur en ajoutant une opération `flatMap` (parfois appelée `bind` ou `>>=`) et un moyen d'"envelopper" une valeur régulière dans un contexte monadique (souvent appelé `unit`, `return` ou `pure`, en Python pour les listes, il peut s'agir simplement de `lambda x: [x]`).

```python
# Protocole pour une Monade (hérite de Functor)
# IMPORTANT : Il s'agit d'une représentation simplifiée. Le typage correct des monades en Python est complexe.
class Monad(Functor[A], Protocol[A]):
    # flatMap prend une fonction qui renvoie elle-même une monade
    def flatMap(self, func: Callable[[A], 'Monad[B]']) -> 'Monad[B]':
        ...

    # Méthode statique ou de classe pour "envelopper" une valeur
    @classmethod
    def unit(cls, value: A) -> 'Monad[A]':
         ...

# Encore une fois, nous utilisons une liste comme exemple de monade en Python.
# Bien que list n'ait pas de méthodes flatMap/unit, nous pouvons les simuler.

# 'unit' pour une liste : envelopper une valeur dans une liste
list_unit = lambda x: [x]

# 'flatMap' pour une liste : appliquer une fonction à chaque élément,
# puis "aplatir" (flatten) le résultat (combiner les listes).
# C'est facile à faire avec une compréhension de liste avec deux boucles for.
def list_flat_map(data: list[A], func: Callable[[A], list[B]]) -> list[B]:
    # Pour chaque x dans data, appliquer func(x), qui renverra une liste.
    # Ensuite, pour chaque y dans cette liste interne, ajouter y au résultat.
    return [y for x in data for y in func(x)]

# Exemple d'utilisation
numbers = [1, 2, 3]
# Une fonction qui pour un nombre n renvoie une liste [n, n+1]
func_n_nplus1 = lambda number: [number, number + 1]

flat_mapped_numbers = list_flat_map(numbers, func_n_nplus1)
# Résultat attendu :
# Pour 1 -> [1, 2]
# Pour 2 -> [2, 3]
# Pour 3 -> [3, 4]
# Combiner : [1, 2, 2, 3, 3, 4]
assert flat_mapped_numbers == [1, 2, 2, 3, 3, 4]
```

D'autres exemples bien connus de monades (ou de structures de type monade) en Python peuvent être :
*   `asyncio.Future` (ou les `awaitables` en général) pour les opérations asynchrones (où `await` est similaire à `flatMap`).
*   Le type `Optional` (souvent implémenté comme `Union[T, None]`, bien qu'une monade correcte nécessite une structure `Maybe` ou `Option` plus stricte) pour travailler avec des valeurs qui peuvent être manquantes.
*   Diverses monades des bibliothèques de programmation fonctionnelle pour Python (par exemple, `pymonad`, `returns`).

Essentiellement, une monade est simplement une abstraction des calculs en tant que tels, permettant de construire des pipelines de traitement de données, de gérer les effets secondaires, de gérer les erreurs ou l'asynchronisme de manière uniforme.

*(Image/diagramme d'une monade)*

Plusieurs lois monadiques spéciales doivent être respectées pour les monades (identité gauche et droite, associativité de `flatMap`), que, cependant, je ne donnerai pas ici, car il est temps de terminer ce billet déjà long. Je veux juste noter que l'avantage le plus important des monades est qu'elles permettent d'ordonner l'exécution de calculs isolés. Un exemple d'un tel ordre en Python est l'utilisation de `await` pour l'exécution séquentielle d'opérations asynchrones (`asyncio.Future`), ce qui est conceptuellement similaire à la composition monadique.

**Conclusion**
En conclusion, je voudrais dire que la théorie des groupes et la théorie des catégories sont au cœur de toutes les mathématiques, de l'informatique et de la physique connues de l'homme. C'est littéralement le langage de l'univers - le plus expressif et le plus poétiquement beau. Je l'aurais appris juste pour le fait que Dieu l'a parlé !
## Teoría de grupos - Semigrupo
La estructura más simple en la teoría de grupos es un semigrupo. Un semigrupo es un conjunto para el cual se define una operación binaria asociativa, que toma dos elementos de este conjunto como entrada y devuelve un tercero. De ahora en adelante, todos los ejemplos se darán en el lenguaje de programación Python.

En Python, podemos definir el concepto de semigrupo usando `typing.Protocol` (para la verificación de tipos estáticos) o simplemente por convención (duck typing). Para mayor claridad, usaremos diccionarios que almacenan la operación `combine`.

```python
from typing import TypeVar, Callable, Protocol, Generic
import functools # Para reduce

T = TypeVar('T')

# Describimos la estructura de un semigrupo usando Protocol (para tipado estático)
class Semigroup(Protocol[T]):
    # Callable[[T, T], T] significa una función que toma dos argumentos de tipo T
    # y devuelve un valor de tipo T
    combine: Callable[[T, T], T]

# Ejemplo: Un semigrupo de números naturales (o enteros/reales) con adición
# Representamos un semigrupo específico como un diccionario con la clave 'combine'
addition_semigroup: Semigroup[int] = {
    "combine": lambda a, b: a + b
}

# Ejemplo: Un semigrupo de números con multiplicación
multiplication_semigroup: Semigroup[int] = {
    "combine": lambda a, b: a * b
}

# Ejemplo: Un semigrupo de cadenas con concatenación
concatenation_semigroup: Semigroup[str] = {
    "combine": lambda a, b: a + b
}
```

La operación sobre los elementos de un semigrupo debe tener la propiedad de asociatividad. Probemos esto con la función incorporada `assert`:

```python
def check_associativity(semigroup: Semigroup[T], a: T, b: T, c: T) -> None:
    # Comprobamos que (a * b) * c == a * (b * c)
    # Usamos la operación combine del semigrupo pasado
    left_side = semigroup["combine"](semigroup["combine"](a, b), c)
    right_side = semigroup["combine"](a, semigroup["combine"](b, c))
    assert left_side == right_side, f"La asociatividad falló para {semigroup}: ({a}, {b}, {c})"

check_associativity(addition_semigroup, 1, 2, 3)
check_associativity(multiplication_semigroup, 2, 3, 4) # 1*2*3 = 6, (1*2)*3 = 6, 1*(2*3)=6
check_associativity(concatenation_semigroup, 'a', 'b', 'c')
```

Un semigrupo no tiene propiedades particularmente interesantes. Sin embargo, incluso con su ejemplo, vemos la conveniencia de la teoría de grupos: la capacidad de trabajar con conjuntos y operaciones sobre ellos usando una interfaz abstracta (en nuestro caso, un diccionario con una función `combine`).

Por ejemplo, podemos escribir una función de reducción para una lista de valores de semigrupo usando un valor inicial. Esto ya insinúa la siguiente estructura: un monoide.

```python
from typing import List

# Esta función se parece más a un pliegue de la siguiente sección,
# ya que requiere un valor inicial. Una reducción de semigrupo pura
# requeriría una lista no vacía.
def reduce_semigroup_with_initial(
    values: List[T],
    semigroup: Semigroup[T],
    initial_value: T
) -> T:
    # Usamos functools.reduce para aplicar secuencialmente combine
    return functools.reduce(semigroup["combine"], values, initial_value)

# Ahora podemos usar esta función para reducir una lista:
sum_val = reduce_semigroup_with_initial([1, 2, 3, 4], addition_semigroup, 0)
assert sum_val == 10

product_val = reduce_semigroup_with_initial([1, 2, 3, 4], multiplication_semigroup, 1)
assert product_val == 24

concat_val = reduce_semigroup_with_initial(['a', 'b', 'c'], concatenation_semigroup, '')
assert concat_val == 'abc'

```
El uso de la función de reducción de semigrupos nos lleva sin problemas a la siguiente estructura, mucho más interesante de la teoría de grupos: el monoide.

**Teoría de grupos - Monoide**
Un monoide es un semigrupo con un elemento neutro definido (`unit` o `identity`).

```python
# Definimos un protocolo para un Monoide, que hereda de Semigroup
class Monoid(Semigroup[T], Protocol[T]):
    unit: T # Elemento neutro

# Monoide de la suma de números (elemento neutro - 0)
addition_monoid: Monoid[int] = {
    "combine": lambda a, b: a + b,
    "unit": 0
}
```

El elemento neutro es un elemento tal que su combinación con cualquier otro elemento no cambia ese otro elemento (`a + 0 = a`, `a * 1 = a`, `s + "" = s`). Para la suma de números, este elemento neutro es, por supuesto, cero.

Comprobemos esta propiedad de un monoide con `assert`:

```python
def check_unit_combination(monoid: Monoid[T], value: T) -> None:
    # Comprobamos que combine(value, unit) == value
    # y combine(unit, value) == value (para completar)
    assert monoid["combine"](value, monoid["unit"]) == value
    assert monoid["combine"](monoid["unit"], value) == value

check_unit_combination(addition_monoid, 10)
```

El elemento neutro del monoide de la multiplicación de números es uno.

```python
multiplication_monoid: Monoid[int] = {
    "combine": lambda a, b: a * b,
    "unit": 1
}

check_unit_combination(multiplication_monoid, 25)
```

En consecuencia, el elemento neutro del monoide de la concatenación de cadenas es la cadena vacía.

```python
concatenation_monoid: Monoid[str] = {
    "combine": lambda a, b: a + b,
    "unit": ""
}

check_unit_combination(concatenation_monoid, 'a')
```

Y ahora llegamos a la propiedad más interesante de los monoides: se puede usar la operación de plegado (fold) para trabajar con ellos. Es esencialmente el mismo `reduce_semigroup_with_initial`, pero ahora el valor inicial se toma directamente del monoide (`unit`).

```python
def fold(monoid: Monoid[T], values: List[T]) -> T:
    # Usamos functools.reduce, comenzando con el elemento neutro monoid['unit']
    return functools.reduce(monoid["combine"], values, monoid["unit"])

# Con fold, tenemos habilidades completamente mágicas:
sum_folded = fold(addition_monoid, [1, 2, 3, 4])
assert sum_folded == 10

product_folded = fold(multiplication_monoid, [1, 2, 3, 4])
assert product_folded == 24

concatenated_folded = fold(concatenation_monoid, ['a', 'b', 'c', 'd'])
assert concatenated_folded == 'abcd'
```

También podemos definir monoides para las operaciones de comparación de números. Para `min`, el elemento neutro será infinito, y para `max`, menos infinito.

```python
import math # Para float('inf')

min_monoid: Monoid[float] = { # Usamos float para el infinito
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

Y lo que es más, podemos definir, por ejemplo, un monoide de funciones. Por ejemplo, un monoide de funciones unarias (que toman un argumento) sobre números, donde la operación `combine` será la composición de funciones, y el elemento neutro (`unit`) será la función de identidad (`lambda x: x`).

```python
# Tipo para una función unaria de int a int
IntUnaryFunc = Callable[[int], int]

# Monoide para la composición de funciones (int -> int)
# IMPORTANTE: El orden de composición es f(g(x))
function_monoid: Monoid[IntUnaryFunc] = {
    "combine": lambda f, g: lambda x: f(g(x)), # f después de g
    "unit": lambda x: x # Función de identidad
}

add_one: IntUnaryFunc = lambda x: x + 1
double: IntUnaryFunc = lambda x: x * 2

# Plegado de una lista de funciones: [add_one, double]
# Primero se aplicará la unidad, luego el doble, luego add_one.
# fold(monoid, [f, g]) es equivalente a combine(combine(unit, f), g) = combine(f, g)
# combine(f, g) = lambda x: f(g(x))
function_fold_result_func = fold(function_monoid, [add_one, double])

# Aplicar el resultado al número 1: add_one(double(1)) = add_one(2) = 3
assert function_fold_result_func(1) == 3

# Si el orden de las funciones es importante y necesita g(f(x)), debe cambiar combine:
# "combine": lambda f, g: lambda x: g(f(x))
```

En el ejemplo de un monoide, vemos que la teoría de grupos nos permite trabajar con muchos conjuntos y operaciones diferentes sobre ellos de la misma manera.

¿Recuerdas que en la escuela nos decían que cualquier número elevado a la potencia de cero es igual a uno, pero nunca explicaron por qué?

Esta propiedad se vuelve obvia a primera vista en el monoide de la multiplicación. La exponenciación es la aplicación repetida de la operación `combine` del monoide de la multiplicación. Por ejemplo, `2^3` es `combine(combine(unit, 2), 2), 2)` o, lo que es lo mismo, `combine(combine(2, 2), 2)`.

```python
# 2^3 usando el monoide de la multiplicación
power_3 = multiplication_monoid["combine"](
    multiplication_monoid["combine"](2, 2), # 2*2
    2                                       # (2*2)*2
)
assert power_3 == 8
```

Pero, ¿qué es la potencia cero? Es la aplicación de la operación `combine` cero veces al elemento inicial. ¿Qué resultado deberíamos obtener? Si no aplicamos `combine` en absoluto, solo nos queda el elemento neutro `unit`, que en el caso del monoide de la multiplicación es igual a uno. Por eso `x^0 = 1`.

**Teoría de grupos - Grupo**
Un grupo es un monoide para el cual cada elemento tiene un elemento inverso del mismo conjunto, de modo que la combinación de un elemento con su inverso da el elemento neutro.

```python
# Definimos un protocolo para un Grupo, que hereda de Monoide
class Group(Monoid[T], Protocol[T]):
    inverse: Callable[[T], T] # Función para obtener el elemento inverso

# Un ejemplo clásico de un grupo es el conjunto de los números enteros bajo la operación de la suma
addition_group: Group[int] = {
    "combine": lambda a, b: a + b,
    "unit": 0,
    "inverse": lambda a: -a # El elemento inverso para la suma es la negación
}
```

La propiedad principal de un grupo es que la combinación de un elemento con su elemento inverso siempre da como resultado el elemento neutro del grupo:

```python
def check_inversion_combination(group: Group[T], value: T) -> None:
    # Comprobamos que combine(value, inverse(value)) == unit
    # y combine(inverse(value), value) == unit
    assert group["combine"](value, group["inverse"](value)) == group["unit"]
    assert group["combine"](group["inverse"](value), value) == group["unit"]

check_inversion_combination(addition_group, 5) # 5 + (-5) == 0
```

Se puede decir que un grupo es una estructura matemática que abstrae el concepto de simetría. Es con la ayuda de esta estructura que los físicos estudian las propiedades del espacio, el tiempo, la energía y las partículas elementales; en la base del aparato matemático de la teoría de la relatividad y la mecánica cuántica se encuentra la teoría de grupos. Con su ayuda, en 1918, Emmy Noether demostró sus famosos teoremas de que toda ley de conservación, ya sea la ley de conservación de la energía, el momento o la carga, proviene de simetrías físicas fundamentales.

Además, los monoides y los grupos se utilizan a menudo en la programación funcional. Si estudias un poco la teoría de grupos, verás que muchos problemas y estructuras en la programación son casos especiales de una estructura matemática más abstracta. El ejemplo más simple de un grupo en la programación es el sistema Deshacer-Rehacer, implementado en muchas aplicaciones (la operación es la acción del usuario, la operación inversa es la cancelación de la acción, el elemento neutro es la ausencia de cambios).

**Monadología**
La belleza de las simetrías ha fascinado a la gente desde la antigüedad. En la escuela fundada por el legendario filósofo y geómetra griego antiguo Pitágoras, sus alumnos adoraban la mónada, representada como un círculo con un punto grueso en su centro:

*(Imagen de la mónada de Pitágoras)*

El significado místico de la mónada residía en su punto central: este punto personifica la "nada" de la que surge el Universo. Según los pitagóricos, no hay restricciones para el surgimiento de todas las cosas posibles de la nada, pero al mismo tiempo que estas cosas, también surgen sus opuestos. Al desplegar el punto de dimensión cero en un número infinito de opuestos, obtenemos un círculo, una figura en la que se encuentra un número infinito de puntos, para cada uno de los cuales, en relación con el centro del círculo, hay un punto opuesto. En general, esta descripción se corresponde plenamente con el concepto de grupo de la teoría de grupos.

En su obra magna filosófica titulada "Monadología", el gran filósofo y matemático alemán Gottfried Wilhelm Leibniz expuso su visión del mundo, según la cual toda nuestra realidad consiste en un número infinito de tales mónadas duales. En honor a este concepto pitagórico-leibniziano de la mónada, se nombró la estructura principal de otra teoría matemática: la teoría de categorías.

Si la teoría de grupos abstrae las operaciones algebraicas y geométricas intuitivas básicas en estructuras generales, entonces la teoría de categorías es como el siguiente paso en la escalera de las abstracciones: una abstracción de abstracciones. La teoría de categorías estudia diversas estructuras matemáticas (grupos, grafos, conjuntos) como algunas categorías abstractas con objetos (elementos) y morfismos (operaciones) entre ellos. Los morfismos suelen representarse como flechas y se denominan "flechas". Un eco de este nombre son las funciones lambda (`lambda`) o las funciones regulares (`def`) en la programación, que probablemente conozcas, que transforman unos valores en otros.

Veamos los conceptos básicos de la teoría de categorías.

**Teoría de categorías - Flecha**
Una flecha (o morfismo) en la teoría de categorías se denomina una aplicación (función) entre dos categorías (conjuntos de objetos), una correspondencia de cada objeto de la primera categoría con algún objeto de la segunda. Tomemos, por ejemplo, dos de las categorías más simples: los números enteros no negativos y las cadenas de la letra "a".

```
0 -> ""
1 -> "a"
2 -> "aa"
3 -> "aaa"
4 -> "aaaa"
...
```

Aquí se ve claramente que cada elemento de la categoría de los números se corresponde con un elemento de la categoría de las cadenas que consisten en la letra 'a'. Cualquier correspondencia de este tipo puede describirse mediante una función. En este caso, es:

```python
def map_number_to_a_string(num: int) -> str:
    # Nos aseguramos de que el número no sea negativo para la repetición
    if num < 0:
        raise ValueError("El número de entrada debe ser no negativo")
    return "a" * num # En Python, una cadena se repite mediante la multiplicación

assert map_number_to_a_string(3) == "aaa"
```

No es necesario que un objeto de la primera categoría corresponda a un objeto único de la segunda. Por ejemplo, para la siguiente flecha de la categoría de los números a la categoría de la verdad (valores booleanos), solo hay dos objetos en la segunda categoría (`True` y `False`), pero cada objeto de la primera se corresponde con uno de los objetos de la segunda:

```
0 -> False
1 -> False
2 -> False
3 -> True
4 -> True
...
n -> True (para n >= 3)
```

La función (flecha) en este caso se puede describir como:

```python
def map_number_to_boolean(number: int) -> bool:
    return number >= 3

assert map_number_to_boolean(2) == False
assert map_number_to_boolean(5) == True
```

**Teoría de categorías - Funtor y Endofuntor**
Podemos envolver objetos de cualquier categoría en algunos contenedores abstractos. Si tenemos las categorías (tipos) A y B, y tenemos algún contenedor F (por ejemplo, `list`, `Optional`, `Future`), que puede contener uno o más objetos de las categorías A o B, entonces obtenemos dos nuevas categorías (tipos) F(A) y F(B) (por ejemplo, `list[A]` y `list[B]`).

Por ejemplo, si tenemos una categoría de números (`int`) y una categoría de cadenas (`str`), y tenemos un contenedor `list`, entonces obtenemos dos nuevas categorías: una lista de números (`list[int]`) y una lista de cadenas (`list[str]`). En Python, estas relaciones se reflejan en el sistema de tipos:

```python
number: int = 1
string_value: str = 'a'

numbers: list[int] = [1, 2, 3]
strings: list[str] = ['a', 'b', 'c']
```

En la teoría de categorías, se describen las aplicaciones entre las categorías de objetos y las categorías de contenedores, que conservan la estructura durante la transformación. Tales aplicaciones se denominan funtores. La aplicación en sí se denomina `map` (o `fmap`).

Existen varios tipos diferentes de funtores. El más utilizado de ellos es el endofuntor, en el que la transformación se produce dentro de la misma categoría de contenedor F(A) -> F(B) (por ejemplo, `list[A] -> list[B]`).

```python
# Tipo general para las variables A y B
A = TypeVar('A')
B = TypeVar('B')

# Protocolo para un Funtor
class Functor(Protocol[A]):
    # El método map toma una función (flecha) de A a B
    # y devuelve un nuevo Funtor con elementos de tipo B.
    # Importante: devuelve una instancia del mismo tipo de funtor (por ejemplo, list).
    def map(self, func: Callable[[A], B]) -> 'Functor[B]':
        ...

# Un ejemplo clásico de un endofuntor en Python es la lista.
# Aunque list no tiene un método .map por defecto, podemos implementarlo fácilmente
# o usar comprensiones de lista (que es más idiomático).

# Ejemplo de uso de la comprensión de lista como análogo de map:
map_number_to_boolean_func = lambda number: number >= 3
numbers_list: list[int] = [1, 2, 3, 4]

# Aplicar la función a cada elemento de la lista, obtener una nueva lista
booleans_list: list[bool] = [map_number_to_boolean_func(n) for n in numbers_list]
assert booleans_list == [False, False, True, True]

# También puede usar la función incorporada map, que devuelve un iterador:
booleans_iterator = map(map_number_to_boolean_func, numbers_list)
assert list(booleans_iterator) == [False, False, True, True]
```

Por lo tanto, si tenemos una flecha (función) `A -> B`, entonces con la ayuda de un funtor (por ejemplo, `list` y su operación `map`/comprensión de lista), podemos construir una flecha `F[A] -> F[B]`.

Se deben observar varias leyes para los funtores.

La primera ley es la Ley de la Identidad: `functor.map(id) == functor` (la aplicación de la función de identidad no debe cambiar el funtor).

```python
def id_func(x: T) -> T:
    return x

# Comprobación para una lista:
numbers_list = [1, 2, 3]
assert [id_func(x) for x in numbers_list] == numbers_list
```

La segunda ley es la Ley de Composición: `functor.map(g o f) == functor.map(f).map(g)` (donde `g o f` es la composición de funciones, `lambda x: g(f(x))`). Mapear una composición de funciones es equivalente a mapear secuencialmente estas funciones.

```python
f: Callable[[int], str] = lambda x: str(x) # int -> str
g: Callable[[str], bool] = lambda x: len(x) > 1 # str -> bool
compose_gf: Callable[[int], bool] = lambda x: g(f(x)) # int -> bool

numbers_list = [5, 10, 15]

# Lado izquierdo: map(g o f)
left_side = [compose_gf(x) for x in numbers_list] # [False, True, True]

# Lado derecho: map(f) y luego map(g)
intermediate = [f(x) for x in numbers_list] # ['5', '10', '15']
right_side = [g(y) for y in intermediate] # [False, True, True]

assert left_side == right_side
```

**Teoría de categorías - Mónada**
Una mónada amplía las capacidades de un funtor añadiendo una operación `flatMap` (a veces llamada `bind` o `>>=`) y una forma de "envolver" un valor regular en un contexto monádico (a menudo llamado `unit`, `return` o `pure`, en Python para las listas puede ser simplemente `lambda x: [x]`).

```python
# Protocolo para una Mónada (hereda de Funtor)
# IMPORTANTE: Esta es una representación simplificada. El tipado correcto de las mónadas en Python es complejo.
class Monad(Functor[A], Protocol[A]):
    # flatMap toma una función que a su vez devuelve una mónada
    def flatMap(self, func: Callable[[A], 'Monad[B]']) -> 'Monad[B]':
        ...

    # Método estático o de clase para "envolver" un valor
    @classmethod
    def unit(cls, value: A) -> 'Monad[A]':
         ...

# De nuevo, usamos una lista como ejemplo de una mónada en Python.
# Aunque list no tiene los métodos flatMap/unit, podemos simularlos.

# 'unit' para una lista: envolver un valor en una lista
list_unit = lambda x: [x]

# 'flatMap' para una lista: aplicar una función a cada elemento,
# y luego "aplanar" (flatten) el resultado (combinar las listas).
# Esto se hace fácilmente con una comprensión de lista con dos bucles for.
def list_flat_map(data: list[A], func: Callable[[A], list[B]]) -> list[B]:
    # Para cada x en data, aplicar func(x), que devolverá una lista.
    # Luego, para cada y en esta lista interna, añadir y al resultado.
    return [y for x in data for y in func(x)]

# Ejemplo de uso
numbers = [1, 2, 3]
# Una función que para un número n devuelve una lista [n, n+1]
func_n_nplus1 = lambda number: [number, number + 1]

flat_mapped_numbers = list_flat_map(numbers, func_n_nplus1)
# Resultado esperado:
# Para 1 -> [1, 2]
# Para 2 -> [2, 3]
# Para 3 -> [3, 4]
# Combinar: [1, 2, 2, 3, 3, 4]
assert flat_mapped_numbers == [1, 2, 2, 3, 3, 4]
```

Otros ejemplos bien conocidos de mónadas (o estructuras similares a las mónadas) en Python pueden ser:
*   `asyncio.Future` (o `awaitables` en general) para operaciones asíncronas (donde `await` es similar a `flatMap`).
*   El tipo `Optional` (a menudo implementado como `Union[T, None]`, aunque una mónada adecuada requiere una estructura `Maybe` u `Option` más estricta) para trabajar con valores que pueden faltar.
*   Varias mónadas de bibliotecas de programación funcional para Python (por ejemplo, `pymonad`, `returns`).

En esencia, una mónada es simplemente una abstracción de los cálculos como tales, que permite construir canalizaciones de procesamiento de datos, gestionar los efectos secundarios, manejar los errores o la asincronía de forma uniforme.

*(Imagen/diagrama de una mónada)*

Se deben observar varias leyes monádicas especiales para las mónadas (identidad izquierda y derecha, asociatividad de `flatMap`), que, sin embargo, no daré aquí, ya que es hora de terminar esta publicación ya larga. Solo quiero señalar que la ventaja más importante de las mónadas es que permiten ordenar la ejecución de cálculos aislados. Un ejemplo de tal ordenación en Python es el uso de `await` para la ejecución secuencial de operaciones asíncronas (`asyncio.Future`), que es conceptualmente similar a la composición monádica.

**Conclusión**
En conclusión, me gustaría decir que la teoría de grupos y la teoría de categorías están en el corazón de todas las matemáticas, la informática y la física conocidas por el hombre. Es literalmente el lenguaje del universo, el más expresivo y el más poéticamente bello. ¡Lo habría aprendido solo por el hecho de que Dios lo hablaba!
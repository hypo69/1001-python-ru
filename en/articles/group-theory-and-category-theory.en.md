## Group Theory - Semigroup
The simplest structure in group theory is a semigroup. A semigroup is a set for which an associative binary operation is defined, which takes two elements of this set as input and returns a third. From now on, all examples will be given in the Python programming language.

In Python, we can define the concept of a semigroup using `typing.Protocol` (for static type checking) or simply by convention (duck typing). For clarity, we will use dictionaries that store the `combine` operation.

```python
from typing import TypeVar, Callable, Protocol, Generic
import functools # For reduce

T = TypeVar('T')

# We describe the structure of a semigroup using Protocol (for static typing)
class Semigroup(Protocol[T]):
    # Callable[[T, T], T] means a function that takes two arguments of type T
    # and returns a value of type T
    combine: Callable[[T, T], T]

# Example: A semigroup of natural (or integer/real) numbers with addition
# We represent a specific semigroup as a dictionary with the key 'combine'
addition_semigroup: Semigroup[int] = {
    "combine": lambda a, b: a + b
}

# Example: A semigroup of numbers with multiplication
multiplication_semigroup: Semigroup[int] = {
    "combine": lambda a, b: a * b
}

# Example: A semigroup of strings with concatenation
concatenation_semigroup: Semigroup[str] = {
    "combine": lambda a, b: a + b
}
```

The operation on the elements of a semigroup must have the property of associativity. Let's test this with the built-in `assert` function:

```python
def check_associativity(semigroup: Semigroup[T], a: T, b: T, c: T) -> None:
    # We check that (a * b) * c == a * (b * c)
    # We use the combine operation from the passed semigroup
    left_side = semigroup["combine"](semigroup["combine"](a, b), c)
    right_side = semigroup["combine"](a, semigroup["combine"](b, c))
    assert left_side == right_side, f"Associativity failed for {semigroup}: ({a}, {b}, {c})"

check_associativity(addition_semigroup, 1, 2, 3)
check_associativity(multiplication_semigroup, 2, 3, 4) # 1*2*3 = 6, (1*2)*3 = 6, 1*(2*3)=6
check_associativity(concatenation_semigroup, 'a', 'b', 'c')
```

A semigroup does not have any particularly interesting properties. However, even with their example, we see the convenience of group theory - the ability to work with sets and operations on them using an abstract interface (in our case, a dictionary with a `combine` function).

For example, we can write a reduction function for a list of semigroup values using an initial value. This already hints at the next structure - a monoid.

```python
from typing import List

# This function is more like a fold from the next section,
# as it requires an initial value. A pure semigroup reduction
# would require a non-empty list.
def reduce_semigroup_with_initial(
    values: List[T],
    semigroup: Semigroup[T],
    initial_value: T
) -> T:
    # We use functools.reduce to sequentially apply combine
    return functools.reduce(semigroup["combine"], values, initial_value)

# Now we can use this function to reduce a list:
sum_val = reduce_semigroup_with_initial([1, 2, 3, 4], addition_semigroup, 0)
assert sum_val == 10

product_val = reduce_semigroup_with_initial([1, 2, 3, 4], multiplication_semigroup, 1)
assert product_val == 24

concat_val = reduce_semigroup_with_initial(['a', 'b', 'c'], concatenation_semigroup, '')
assert concat_val == 'abc'

```
The use of the semigroup reduction function smoothly leads us to the next, much more interesting structure from group theory - the monoid.

**Group Theory - Monoid**
A monoid is a semigroup with a defined neutral element (`unit` or `identity`).

```python
# We define a protocol for a Monoid, inheriting from Semigroup
class Monoid(Semigroup[T], Protocol[T]):
    unit: T # Neutral element

# Monoid of addition of numbers (neutral element - 0)
addition_monoid: Monoid[int] = {
    "combine": lambda a, b: a + b,
    "unit": 0
}
```

The neutral element is an element such that combining it with any other element does not change that other element (`a + 0 = a`, `a * 1 = a`, `s + "" = s`). For the addition of numbers, this neutral element is, of course, zero.

Let's check this property of a monoid with `assert`:

```python
def check_unit_combination(monoid: Monoid[T], value: T) -> None:
    # We check that combine(value, unit) == value
    # and combine(unit, value) == value (for completeness)
    assert monoid["combine"](value, monoid["unit"]) == value
    assert monoid["combine"](monoid["unit"], value) == value

check_unit_combination(addition_monoid, 10)
```

The neutral element of the monoid of multiplication of numbers is one.

```python
multiplication_monoid: Monoid[int] = {
    "combine": lambda a, b: a * b,
    "unit": 1
}

check_unit_combination(multiplication_monoid, 25)
```

Accordingly, the neutral element of the monoid of string concatenation is the empty string.

```python
concatenation_monoid: Monoid[str] = {
    "combine": lambda a, b: a + b,
    "unit": ""
}

check_unit_combination(concatenation_monoid, 'a')
```

And now we come to the most interesting property of monoids - you can use the fold operation to work with them. This is essentially the same `reduce_semigroup_with_initial`, but now the initial value is taken directly from the monoid (`unit`).

```python
def fold(monoid: Monoid[T], values: List[T]) -> T:
    # We use functools.reduce, starting with the neutral element monoid['unit']
    return functools.reduce(monoid["combine"], values, monoid["unit"])

# With fold, we have completely magical abilities:
sum_folded = fold(addition_monoid, [1, 2, 3, 4])
assert sum_folded == 10

product_folded = fold(multiplication_monoid, [1, 2, 3, 4])
assert product_folded == 24

concatenated_folded = fold(concatenation_monoid, ['a', 'b', 'c', 'd'])
assert concatenated_folded == 'abcd'
```

We can also define monoids for number comparison operations. For `min`, the neutral element will be infinity, and for `max` - minus infinity.

```python
import math # For float('inf')

min_monoid: Monoid[float] = { # We use float for infinity
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

And what's more, we can define, for example, a monoid of functions. For example, a monoid of unary functions (taking one argument) over numbers, where the `combine` operation will be function composition, and the neutral element (`unit`) will be the identity function (`lambda x: x`).

```python
# Type for a unary function from int to int
IntUnaryFunc = Callable[[int], int]

# Monoid for function composition (int -> int)
# IMPORTANT: The order of composition is f(g(x))
function_monoid: Monoid[IntUnaryFunc] = {
    "combine": lambda f, g: lambda x: f(g(x)), # f after g
    "unit": lambda x: x # Identity function
}

add_one: IntUnaryFunc = lambda x: x + 1
double: IntUnaryFunc = lambda x: x * 2

# Folding a list of functions: [add_one, double]
# First unit will be applied, then double, then add_one.
# fold(monoid, [f, g]) is equivalent to combine(combine(unit, f), g) = combine(f, g)
# combine(f, g) = lambda x: f(g(x))
function_fold_result_func = fold(function_monoid, [add_one, double])

# Apply the result to the number 1: add_one(double(1)) = add_one(2) = 3
assert function_fold_result_func(1) == 3

# If the order of functions is important and you need g(f(x)), you need to change combine:
# "combine": lambda f, g: lambda x: g(f(x))
```

On the example of a monoid, we see that group theory allows us to work with many different sets and operations on them in the same way.

Remember, in school we were told that any number to the power of zero is equal to one, but they never explained why?

This property becomes obvious at the first glance at the multiplication monoid. Exponentiation is the repeated application of the `combine` operation of the multiplication monoid. For example, `2^3` is `combine(combine(unit, 2), 2), 2)` or, which is the same, `combine(combine(2, 2), 2)`.

```python
# 2^3 using the multiplication monoid
power_3 = multiplication_monoid["combine"](
    multiplication_monoid["combine"](2, 2), # 2*2
    2                                       # (2*2)*2
)
assert power_3 == 8
```

But what is the zeroth power? It is the application of the `combine` operation zero times to the initial element. What result should we get? If we do not apply `combine` at all, we are left with only the neutral element `unit`, which in the case of the multiplication monoid is equal to one. That's why `x^0 = 1`.

**Group Theory - Group**
A group is a monoid for which every element has an inverse element from the same set, such that the combination of an element with its inverse gives the neutral element.

```python
# We define a protocol for a Group, inheriting from Monoid
class Group(Monoid[T], Protocol[T]):
    inverse: Callable[[T], T] # Function to get the inverse element

# A classic example of a group is the set of integers under the operation of addition
addition_group: Group[int] = {
    "combine": lambda a, b: a + b,
    "unit": 0,
    "inverse": lambda a: -a # The inverse element for addition is negation
}
```

The main property of a group is that combining an element with its inverse element always results in the neutral element of the group:

```python
def check_inversion_combination(group: Group[T], value: T) -> None:
    # We check that combine(value, inverse(value)) == unit
    # and combine(inverse(value), value) == unit
    assert group["combine"](value, group["inverse"](value)) == group["unit"]
    assert group["combine"](group["inverse"](value), value) == group["unit"]

check_inversion_combination(addition_group, 5) # 5 + (-5) == 0
```

It can be said that a group is a mathematical structure that abstracts the concept of symmetry. It is with the help of this structure that physicists study the properties of space, time, energy, and elementary particles - at the basis of the mathematical apparatus of the theory of relativity and quantum mechanics lies group theory. With its help, in 1918, Emmy Noether proved her famous theorems that any conservation law, be it the law of conservation of energy, momentum, or charge, comes from fundamental physical symmetries.

In addition, monoids and groups are often used in functional programming. If you study group theory even a little, you will see that many problems and structures in programming are special cases of a more abstract mathematical structure. The simplest example of a group in programming is the Undo-Redo system, implemented in many applications (the operation is the user's action, the inverse operation is the cancellation of the action, the neutral element is the absence of changes).

**Monadology**
The beauty of symmetries has fascinated people since ancient times. In the school founded by the legendary ancient Greek philosopher and geometer Pythagoras, his students worshiped the monad, depicted as a circle with a bold dot in its very center:

*(Image of the Pythagorean monad)*

The mystical meaning of the monad lay in its central point - this point personifies the "nothing" from which the Universe arises. According to the Pythagoreans, there are no restrictions on the emergence of all possible things from nothing, but at the same time as these things, their opposites also arise. By unfolding the zero-dimensional point into an infinite number of opposites, we get a circle - a figure on which an infinite number of points lie, for each of which, relative to the center of the circle, there is an opposite point. In general, this description fully corresponds to the concept of a group from group theory.

In his philosophical magnum opus entitled "Monadology", the great German philosopher and mathematician Gottfried Wilhelm Leibniz set forth his view of the world, according to which our entire reality consists of an infinite number of such dual monads. In honor of this Pythagorean-Leibnizian concept of the monad, the main structure from another mathematical theory - category theory - was named.

If group theory abstracts basic intuitive algebraic and geometric operations into general structures, then category theory is like the next step up the ladder of abstractions - an abstraction of abstractions. Category theory studies various mathematical structures - groups, graphs, sets - as some abstract categories with objects (elements) and morphisms (operations) between them. Morphisms are usually depicted as arrows and are called "arrows". A reflection of this name are the lambda functions (`lambda`) or regular functions (`def`) in programming, which you are probably familiar with, that transform some values into others.

Let's look at the basic concepts of category theory.

**Category Theory - Arrow**
An arrow (or morphism) in category theory is a mapping (function) between two categories (sets of objects) - a correspondence of each object of the first category to some object of the second. Let's take, for example, two of the simplest categories - non-negative integers and strings of the letter "a".

```
0 -> ""
1 -> "a"
2 -> "aa"
3 -> "aaa"
4 -> "aaaa"
...
```

Here it is clearly visible that each element of the category of numbers is mapped to an element from the category of strings consisting of the letter 'a'. Any such mapping can be described by a function. In this case, it is:

```python
def map_number_to_a_string(num: int) -> str:
    # We make sure that the number is non-negative for repeat
    if num < 0:
        raise ValueError("Input number must be non-negative")
    return "a" * num # In Python, a string is repeated by multiplication

assert map_number_to_a_string(3) == "aaa"
```

It is not necessary for an object from the first category to correspond to a unique object of the second. For example, for the next arrow from the category of numbers to the category of truth (boolean values), there are only two objects in the second category (`True` and `False`), but each object of the first is mapped to one of the objects of the second:

```
0 -> False
1 -> False
2 -> False
3 -> True
4 -> True
...
n -> True (for n >= 3)
```

The function (arrow) in this case can be described as:

```python
def map_number_to_boolean(number: int) -> bool:
    return number >= 3

assert map_number_to_boolean(2) == False
assert map_number_to_boolean(5) == True
```

**Category Theory - Functor and Endofunctor**
We can wrap objects of any category in some abstract containers. If we have categories (types) A and B, and we have some container F (for example, `list`, `Optional`, `Future`), which can contain one or more objects of categories A or B, then we get two new categories (types) F(A) and F(B) (for example, `list[A]` and `list[B]`).

For example, if we have a category of numbers (`int`) and a category of strings (`str`), and we have a container `list`, then we get two new categories - a list of numbers (`list[int]`) and a list of strings (`list[str]`). In Python, these relationships are reflected in the type system:

```python
number: int = 1
string_value: str = 'a'

numbers: list[int] = [1, 2, 3]
strings: list[str] = ['a', 'b', 'c']
```

In category theory, mappings between categories of objects and categories of containers are described, which preserve the structure during transformation. Such mappings are called functors. The mapping itself is called `map` (or `fmap`).

There are several different types of functors. The most used of them is the endofunctor, in which the transformation occurs within the same container category F(A) -> F(B) (for example, `list[A] -> list[B]`).

```python
# General type for variables A and B
A = TypeVar('A')
B = TypeVar('B')

# Protocol for a Functor
class Functor(Protocol[A]):
    # The map method takes a function (arrow) from A to B
    # and returns a new Functor with elements of type B.
    # Important: it returns an instance of the same functor type (e.g., list).
    def map(self, func: Callable[[A], B]) -> 'Functor[B]':
        ...

# A classic example of an endofunctor in Python is the list.
# Although list does not have a .map method by default, we can easily implement it
# or use list comprehensions (which is more idiomatic).

# Example of using list comprehension as an analogue of map:
map_number_to_boolean_func = lambda number: number >= 3
numbers_list: list[int] = [1, 2, 3, 4]

# Apply the function to each element of the list, get a new list
booleans_list: list[bool] = [map_number_to_boolean_func(n) for n in numbers_list]
assert booleans_list == [False, False, True, True]

# You can also use the built-in map function, which returns an iterator:
booleans_iterator = map(map_number_to_boolean_func, numbers_list)
assert list(booleans_iterator) == [False, False, True, True]
```

Thus, if we have an arrow (function) `A -> B`, then with the help of a functor (for example, `list` and its `map`/list comprehension operation), we can build an arrow `F[A] -> F[B]`.

Several laws must be observed for functors.

The first law is the Law of Identity: `functor.map(id) == functor` (applying the identity function should not change the functor).

```python
def id_func(x: T) -> T:
    return x

# Check for a list:
numbers_list = [1, 2, 3]
assert [id_func(x) for x in numbers_list] == numbers_list
```

The second law is the Law of Composition: `functor.map(g o f) == functor.map(f).map(g)` (where `g o f` is the composition of functions, `lambda x: g(f(x))`). Mapping a composition of functions is equivalent to sequentially mapping these functions.

```python
f: Callable[[int], str] = lambda x: str(x) # int -> str
g: Callable[[str], bool] = lambda x: len(x) > 1 # str -> bool
compose_gf: Callable[[int], bool] = lambda x: g(f(x)) # int -> bool

numbers_list = [5, 10, 15]

# Left side: map(g o f)
left_side = [compose_gf(x) for x in numbers_list] # [False, True, True]

# Right side: map(f) and then map(g)
intermediate = [f(x) for x in numbers_list] # ['5', '10', '15']
right_side = [g(y) for y in intermediate] # [False, True, True]

assert left_side == right_side
```

**Category Theory - Monad**
A monad extends the capabilities of a functor by adding a `flatMap` operation (sometimes called `bind` or `>>=`) and a way to "wrap" a regular value in a monadic context (often called `unit`, `return`, or `pure`, in Python for lists it can be simply `lambda x: [x]`).

```python
# Protocol for a Monad (inherits from Functor)
# IMPORTANT: This is a simplified representation. Correct typing of monads in Python is complex.
class Monad(Functor[A], Protocol[A]):
    # flatMap takes a function that itself returns a monad
    def flatMap(self, func: Callable[[A], 'Monad[B]']) -> 'Monad[B]':
        ...

    # Static or class method for "wrapping" a value
    @classmethod
    def unit(cls, value: A) -> 'Monad[A]':
         ...

# Again, we use a list as an example of a monad in Python.
# Although list does not have flatMap/unit methods, we can simulate them.

# 'unit' for a list: wrap a value in a list
list_unit = lambda x: [x]

# 'flatMap' for a list: apply a function to each element,
# and then "flatten" the result (combine the lists).
# This is easily done with a list comprehension with two for loops.
def list_flat_map(data: list[A], func: Callable[[A], list[B]]) -> list[B]:
    # For each x in data, apply func(x), which will return a list.
    # Then for each y in this inner list, add y to the result.
    return [y for x in data for y in func(x)]

# Example of use
numbers = [1, 2, 3]
# A function that for a number n returns a list [n, n+1]
func_n_nplus1 = lambda number: [number, number + 1]

flat_mapped_numbers = list_flat_map(numbers, func_n_nplus1)
# Expected result:
# For 1 -> [1, 2]
# For 2 -> [2, 3]
# For 3 -> [3, 4]
# Combine: [1, 2, 2, 3, 3, 4]
assert flat_mapped_numbers == [1, 2, 2, 3, 3, 4]
```

Other well-known examples of monads (or monad-like structures) in Python can be:
*   `asyncio.Future` (or `awaitables` in general) for asynchronous operations (where `await` is similar to `flatMap`).
*   The `Optional` type (often implemented as `Union[T, None]`, although a proper monad requires a stricter `Maybe` or `Option` structure) for working with values that may be missing.
*   Various monads from functional programming libraries for Python (e.g., `pymonad`, `returns`).

In essence, a monad is simply an abstraction of computations as such, allowing you to build data processing pipelines, manage side effects, handle errors, or asynchrony in a uniform way.

*(Image/diagram of a monad)*

Several special monadic laws must be observed for monads (left and right identity, associativity of `flatMap`), which, however, I will not give here, as it is time to finish this already long post. I just want to note that the most important advantage of monads is that they allow you to order the execution of isolated computations. An example of such ordering in Python is the use of `await` for sequential execution of asynchronous operations (`asyncio.Future`), which is conceptually similar to monadic composition.

**Conclusion**
In conclusion, I would like to say that group theory and category theory are at the heart of all known mathematics, computer science, and physics. It is literally the language of the universe - the most expressive and most poetically beautiful. I would have learned it just for the fact that God spoke it!
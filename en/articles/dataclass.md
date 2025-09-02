## Dataclasses: When Python Meets Structured Data (With New Named Examples)

In Python, when you need a class to store data, you usually have to write boilerplate code for `__init__`, `__repr__`, `__eq__`, and other magic methods. The `dataclasses` module, introduced in Python 3.7, aims to solve this problem by providing a `@dataclass` decorator that automatically generates these methods for you.

### What is a Dataclass?

A `dataclass` is a class that, as the name suggests, is primarily intended for storing data. It provides the following key benefits:

1.  **Less boilerplate code:** Automatically generates `__init__`, `__repr__`, `__eq__`, `__hash__` (under certain conditions), and other methods based on the type annotations of your fields.
2.  **Readability:** The code becomes more concise and focused on defining the data structure.
3.  **Introspection:** Dataclass fields are easy to introspect (check) using functions from the same `dataclasses` module.
4.  **Performance (with `slots=True`):** Can consume less memory and be faster in accessing attributes.

### Basic Usage

Let's start with a simple example. Suppose we need a class to represent a point in 2D space.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

# Creating an instance
p1 = Point(10, 20)
print(p1) # Point(x=10, y=20) - automatically generated __repr__

# Comparing instances - automatically generated __eq__
p2 = Point(10, 20)
p3 = Point(30, 40)
print(p1 == p2) # True
print(p1 == p3) # False
```

As you can see, we didn't have to write `__init__` or `__repr__`. Everything worked "out of the box".

### `@dataclass` Decorator Parameters

The `@dataclass` decorator accepts several parameters that allow you to customize the generated behavior.

```python
@dataclass(
    init=True,         # Whether to generate __init__ (default True)
    repr=True,         # Whether to generate __repr__ (default True)
    eq=True,           # Whether to generate __eq__ (default True)
    order=False,       # Whether to generate __lt__, __le__, __gt__, __ge__ (default False)
    unsafe_hash=False, # Whether to generate __hash__ (default False)
    frozen=False,      # Whether to make instances immutable (default False)
    match_args=True,   # Whether to include the class in the structural pattern matching mechanism (Python 3.10+, default True)
    kw_only=False,     # Whether to make all fields keyword-only arguments in __init__ (Python 3.10+, default False)
    slots=False        # Whether to use __slots__ to save memory (Python 3.10+, default False)
)
class MyDataClass:
    # ...
```

Let's consider the most important of them, including those that were in your request:

#### `init=True` (Default)

If `True`, then `dataclass` will generate the `__init__` method. If you have your own `__init__`, and you leave `init=True`, then your `__init__` will be called, but the fields defined in the dataclass will not be initialized through it automatically. Usually, if you write your own `__init__`, you set `init=False` to avoid conflicts and have full control over initialization.

```python
@dataclass(init=False)
class CustomPersonInit:
    name: str
    age: int

    def __init__(self, name: str, age: int, welcome_message: str = "Hello!"):
        self.name = name
        self.age = age
        print(welcome_message)

alice = CustomPersonInit("Alice", 30) # Prints "Hello!"
print(alice) # CustomPersonInit(name='Alice', age=30) - repr still works
```

#### `repr=True` (Default)

If `True`, it will generate a `__repr__` method that provides a convenient string representation of the object, useful for debugging.

#### `eq=True` (Default)

If `True`, it will generate an `__eq__` method that allows you to compare two instances of a class for equality by checking the equality of all their fields.

#### `order=False`

If `True`, then `dataclass` will generate the `__lt__`, `__le__`, `__gt__`, `__ge__` methods. This allows you to compare instances for "less than", "greater than", etc. The comparison is done in the order the fields are declared. For `order=True` to work, `eq=True` must also be set.

```python
@dataclass(order=True)
class Person:
    name: str
    age: int

alice = Person("Alice", 30)
boris = Person("Boris", 25)
victor = Person("Victor", 35) # Let's add Victor
galina = Person("Galina", 30)
alice_older = Person("Alice", 35)


print(f"Alice ({alice.age}) > Boris ({boris.age})? {alice > boris}") # False (since 'Alice' < 'Boris' by name) -> the comparison is done lexicographically on the tuple (name, age). ('Alice', 30) < ('Boris', 25) is True. So `>` will be False.
# Explanation: ('Alice', 30) > ('Boris', 25) -> False, because 'Alice' < 'Boris'.
print(f"Alice ({alice.age}) < Alice_older ({alice_older.age})? {alice < alice_older}") # True (because name is the same, but age 30 < 35)
print(f"Galina ({galina.age}) == Alice ({alice.age})? {galina == alice}") # False (different names)
```

**Important note:** The order of the fields matters for `order=True`.

#### `unsafe_hash=False`

If `True`, it will generate a `__hash__` method. Dataclasses are not hashable by default if they are mutable (`frozen=False`), because hashable objects must be immutable. If you are sure that your mutable dataclass will only be used in contexts where its hash will not change (which is risky!), you can set `unsafe_hash=True`.
Much more often, `__hash__` is generated automatically if:
1.  `frozen=True`.
2.  `frozen=False`, but `eq=True` and all fields are also hashable.

```python
@dataclass(frozen=True) # Frozen dataclasses are hashable
class ImmutablePoint:
    x: int
    y: int

p = ImmutablePoint(1, 2)
print(hash(p)) # Works

@dataclass(unsafe_hash=True) # Risky if the object is mutable
class MutableButHashable:
    value: int

m = MutableButHashable(5)
print(hash(m))
m.value = 10
print(hash(m)) # The hash has changed, which can lead to problems when used in a set/dict
```

#### `frozen=False`

If `True`, instances of the class become immutable. After creating an object, you will not be able to change the values of its fields. This is useful for creating immutable objects that are easier to use in multi-threaded applications or as dictionary keys (if they are hashable).

```python
@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

c = Coordinate(10.0, 20.0)
# c.lat = 15.0 # AttributeError: cannot assign to field 'lat'
```

#### `kw_only=False` (Python 3.10+)

If `True`, **all** fields in `__init__` become **keyword-only** arguments. This means that you must pass the values of the fields by name, not by position. This improves readability and prevents errors, especially when the class has many fields or they may have the same types.

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

# You can override this behavior for a specific field using field(kw_only=False)
@dataclass(kw_only=True)
class MixedConfig:
    # Mandatory positional-only (not dataclass-style)
    # The `id` field will not be kw_only, although the class is specified as kw_only=True
    id: int = field(kw_only=False)
    name: str = field(kw_only=False)

    # The remaining fields are kw_only
    email: str
    age: int = 0

# Note that id and name are passed positionally, and email is passed by name
mixed_config = MixedConfig(123, "Boris", email="boris@example.com")
print(mixed_config)
# mixed_config_fail = MixedConfig(id=123, name="Victor", email="viktor@example.com") # Error, id and name would be positional
# This scenario is less typical, kw_only is usually applied to the entire class
```

**Note:** `field(kw_only=False)` on a field overrides `kw_only=True` at the class level, making that specific field positional. However, most often, `kw_only=True` is used for the entire class. The main use of `field(kw_only=True)` is when you have a regular dataclass (`kw_only=False` by default), but you want to make *some* fields keyword-only.

#### `slots=False` (Python 3.10+)

If `True`, `dataclass` will generate `__slots__` for your class. `__slots__` is a special attribute that allows Python to allocate a fixed amount of memory for class instances, instead of using a dynamic `__dict__` to store attributes.

**Advantages of `slots=True`:**
*   **Memory savings:** Significantly reduces the amount of memory consumed by each instance. This is especially important for applications that create millions of objects.
*   **Faster attribute access:** Accessing attributes via `__slots__` can be slightly faster, as Python does not need to look them up in a dictionary.

**Disadvantages of `slots=True`:**
*   **Cannot add new attributes "on the fly":** You will not be able to assign an attribute that was not declared in the dataclass (or in the `__slots__` of a parent class).
*   **Difficulties with multiple inheritance:** It can be difficult to use `__slots__` with multiple inheritance, especially if some parent classes do not use `__slots__` or use them differently.
*   **Does not have `__dict__`:** Instances will not have a `__dict__` attribute unless it has been explicitly added to `__slots__` or a parent class.

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

print(f"Size of RegularPoint: {sys.getsizeof(rp)} bytes")
# Approximately 56 bytes on Python 3.10+ (may vary)
# print(rp.__dict__) # {'x': 1, 'y': 2} - has __dict__

print(f"Size of SlottedPoint: {sys.getsizeof(sp)} bytes")
# Approximately 32 bytes on Python 3.10+ (may vary) - significantly smaller
# print(sp.__dict__) # AttributeError: 'SlottedPoint' object has no attribute '__dict__'

# Attempt to add a new attribute to a slotted dataclass
try:
    sp.z = 30
except AttributeError as e:
    print(f"Error when adding a new attribute: {e}")
```

**When to use `slots=True`?**
When you are creating a very large number of instances of the same class, and memory saving is a priority. This is a great optimization, but it has its trade-offs.

### The `field()` Function: Detailed Field Configuration

In addition to class-level parameters, you can configure each field individually using the `field()` function from the `dataclasses` module. This is especially useful when you need more complex logic for fields than just a type annotation.

```python
from dataclasses import dataclass, field
from typing import List, Dict, Any
import uuid # For generating IDs

@dataclass
class Product:
    id: str = field(default_factory=lambda: "prod-" + str(uuid.uuid4())[:8], init=False) # Not initialized via __init__, generated automatically
    name: str
    price: float = field(compare=False, metadata={'unit': 'USD', 'min_value': 0.0}) # Does not participate in comparison, has metadata
    tags: List[str] = field(default_factory=list, repr=False) # Uses a factory for a list, not displayed in repr
    description: str = field(default="No description available") # Regular default value
    details: Dict[str, Any] = field(default_factory=dict, hash=False) # Does not participate in hashing

p = Product(name="Laptop", price=1200.0, tags=["electronics", "tech"])
print(p)
# Product(id='prod-...', name='Laptop', price=1200.0, description='No description available', details={})
# Note that 'tags' is not in the repr, and 'id' was generated automatically.

p2 = Product(name="Laptop", price=1500.0, tags=["electronics", "tech"])
print(f"p == p2? {p == p2}") # True, because price does not participate in comparison (compare=False)

# p3 = Product(name="Desktop PC", price=1000.0, details={"cpu": "Intel"})
# print(hash(p3)) # TypeError: unhashable type: 'dict' (due to details: hash=False)
# If frozen=True, and details were not hash=False, then the dict would need to be immutable.
```

Let's consider the `field()` parameters:

*   **`default`**: A regular default value for the field.
    ```python
    value: int = field(default=0)
    ```

*   **`default_factory`**: A function with no arguments that will be called to get the default value for the field. **Be sure to use `default_factory` for mutable default values (lists, dictionaries, objects) to avoid problems with shared state between instances!**
    ```python
    items: List[str] = field(default_factory=list)
    ```

*   **`init`**: If `True` (default), the field will be included in the generated `__init__` method. If `False`, the field will not be an argument in the constructor, and you must either provide a `default` / `default_factory` for it, or initialize it in `__post_init__`.
    ```python
    import time
    timestamp: float = field(init=False, default_factory=time.time)
    ```

*   **`repr`**: If `True` (default), the field will be included in the generated `__repr__` method. Useful for hiding large or sensitive data.
    ```python
    password: str = field(repr=False)
    ```

*   **`compare`**: If `True` (default), the field will be included in the generated `__eq__` and `__order__` methods. If `False`, it will not affect the comparison of objects.
    ```python
    version: str = field(compare=False)
    ```

*   **`hash`**: If `True` (default), the field will be included in the generated `__hash__` method. If `False`, it will not affect the hash of the object. If the class is `frozen=True`, but any field has `hash=False`, then the class will not be able to generate its `__hash__` and will become unhashable.
    ```python
    config: Dict[str, Any] = field(hash=False, default_factory=dict)
    ```

*   **`metadata`**: A dictionary for storing arbitrary data associated with the field. `dataclasses` ignore this data, but it can be used by external tools (e.g., for validation, serialization, documentation generation).
    ```python
    user_id: int = field(metadata={'help': 'Unique user identifier', 'validator': 'positive_int'})
    ```

*   **`kw_only`**: (Python 3.10+) If `True`, this specific field becomes a keyword-only argument in `__init__`. If `False`, it becomes positional. This allows you to mix positional and keyword-only arguments when the class's `kw_only` is `False` by default.
    ```python
    @dataclass
    class FlexibleParams:
        mandatory_pos: str # Positional
        optional_kw: int = field(default=0, kw_only=True) # Keyword-only

    fp1 = FlexibleParams("mandatory", optional_kw=100)
    # fp2 = FlexibleParams("mandatory", 200) # TypeError: __init__() takes 1 positional argument but 2 were given (optional_kw)
    ```

### The `fields()` Function: Dataclass Introspection

The `fields()` function from the `dataclasses` module allows you to get information about the fields of a dataclass or its instance. It returns a tuple of `Field` objects.

```python
from dataclasses import dataclass, field, fields
from typing import List

@dataclass
class Book:
    title: str
    author: str = field(metadata={'display_name': 'Author', 'max_length': 100})
    pages: int = field(default=0, metadata={'min_value': 1})
    tags: List[str] = field(default_factory=list, repr=False)

# Get information about the fields of the Book class
book_fields = fields(Book)

for f in book_fields:
    print(f"Field name: {f.name}")
    print(f"Field type: {f.type}")
    print(f"Default value: {f.default}")
    print(f"Uses default_factory: {f.default_factory is not None}")
    print(f"Included in init: {f.init}")
    print(f"Included in repr: {f.repr}")
    print(f"Included in compare: {f.compare}")
    print(f"Included in hash: {f.hash}")
    print(f"Metadata: {f.metadata}")
    print(f"Keyword-only: {f.kw_only}") # For Python 3.10+
    print("-" * 20)

# Access the metadata of a specific field:
author_field_info = next(f for f in book_fields if f.name == 'author')
print(f"Display name for author: {author_field_info.metadata.get('display_name')}")
```

The `Field` object has the following attributes: `name`, `type`, `default`, `default_factory`, `init`, `repr`, `hash`, `compare`, `metadata`, `kw_only`.

### The `__post_init__` Method

Sometimes you need additional logic after the automatic `__init__` of a dataclass has finished initializing the fields. For this, you can define a `__post_init__` method. It will be called immediately after `__init__`.

This is useful for:
*   Data validation.
*   Calculating derived fields based on already initialized ones.
*   Executing any other logic that depends on fully initialized fields.

```python
import datetime

@dataclass
class User:
    first_name: str
    last_name: str
    email: str = field(init=False) # This field will not be included in the __init__ parameters
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now, init=False)

    def __post_init__(self):
        print(f"--- __post_init__ started for {self.first_name} {self.last_name} ---")
        # Validation
        if not self.first_name or not self.last_name:
            raise ValueError("First name and last name cannot be empty.")
        # Calculation of a derived field
        self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@example.com"
        print(f"User {self.first_name} {self.last_name} created with email: {self.email}")
        print(f"Creation time: {self.created_at}")
        print(f"--- __post_init__ finished ---")

alice_ivanova = User("Alice", "Ivanova")
print("
Object created:")
print(alice_ivanova)

print("
")

try:
    victor_no_last_name = User("Victor", "")
except ValueError as e:
    print(f"Error creating user: {e}")
```

### Dataclass Inheritance

Dataclasses support inheritance. Fields from base classes are included in child classes.

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

**Features of inheritance with `slots=True`:**
*   If the parent class uses `__slots__`, the child class must also use `__slots__` to get the memory savings.
*   The child class must define its own `__slots__` for its new fields.
*   If the child class does not define `__slots__`, it will have a `__dict__` in addition to the parent's slots.

### When to use Dataclasses?

*   **Data container classes:** When the main purpose of the class is to store data, and you need automatic `__init__`, `__repr__`, `__eq__`.
*   **Immutable objects:** When you need objects whose state should not change after creation (`frozen=True`).
*   **Configurations:** To define the structure of configuration parameters.
*   **Data Transfer Objects (DTOs):** To transfer structured data between parts of an application.
*   **Simple business logic:** When the class methods mainly operate on the data of the class itself, do not have complex internal state or side effects.

### When NOT to use Dataclasses?

*   **Classes with rich behavior:** When a class has complex business logic, many methods that interact with external systems, or complex internal state, it is better to use a regular class.
*   **OR-mapping (ORM) models:** Although dataclasses can be part of an ORM, they do not replace full-fledged ORM models, which often require specific methods for working with a database, lazy loading, etc.
*   **Polymorphism and deep inheritance hierarchy:** If you have a complex class hierarchy with deep polymorphism and behavior overriding, regular classes may be more flexible.

### Conclusion

`dataclasses` are a powerful and convenient addition to Python that greatly simplifies the creation of data-oriented classes. They help to write cleaner, more readable, and maintainable code, and options like `slots=True` and `kw_only=True` provide additional opportunities for performance optimization and improving the ergonomics of your code's API. Don't forget about `field()` for detailed configuration of each field and `fields()` for introspection!
## Dataclasses: Cuando Python se encuentra con datos estructurados (con nuevos ejemplos con nombre)

En Python, cuando necesitas una clase para almacenar datos, normalmente tienes que escribir código repetitivo para `__init__`, `__repr__`, `__eq__` y otros métodos mágicos. El módulo `dataclasses`, introducido en Python 3.7, tiene como objetivo resolver este problema proporcionando un decorador `@dataclass` que genera automáticamente estos métodos por ti.

### ¿Qué es un Dataclass?

Un `dataclass` es una clase que, como su nombre indica, está destinada principalmente a almacenar datos. Proporciona los siguientes beneficios clave:

1.  **Menos código repetitivo:** Genera automáticamente `__init__`, `__repr__`, `__eq__`, `__hash__` (bajo ciertas condiciones) y otros métodos basados en las anotaciones de tipo de tus campos.
2.  **Legibilidad:** El código se vuelve más conciso y centrado en la definición de la estructura de datos.
3.  **Introspección:** Los campos de dataclass se pueden introspeccionar (comprobar) fácilmente utilizando funciones del mismo módulo `dataclasses`.
4.  **Rendimiento (con `slots=True`):** Puede consumir menos memoria y ser más rápido para acceder a los atributos.

### Uso básico

Empecemos con un ejemplo sencillo. Supongamos que necesitamos una clase para representar un punto en un espacio 2D.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

# Creando una instancia
p1 = Point(10, 20)
print(p1) # Point(x=10, y=20) - __repr__ generado automáticamente

# Comparando instancias - __eq__ generado automáticamente
p2 = Point(10, 20)
p3 = Point(30, 40)
print(p1 == p2) # True
print(p1 == p3) # False
```

Como puedes ver, no tuvimos que escribir `__init__` o `__repr__`. Todo funcionó "de fábrica".

### Parámetros del decorador `@dataclass`

El decorador `@dataclass` acepta varios parámetros que te permiten personalizar el comportamiento generado.

```python
@dataclass(
    init=True,         # Si se debe generar __init__ (predeterminado True)
    repr=True,         # Si se debe generar __repr__ (predeterminado True)
    eq=True,           # Si se debe generar __eq__ (predeterminado True)
    order=False,       # Si se deben generar __lt__, __le__, __gt__, __ge__ (predeterminado False)
    unsafe_hash=False, # Si se debe generar __hash__ (predeterminado False)
    frozen=False,      # Si se deben hacer las instancias inmutables (predeterminado False)
    match_args=True,   # Si se debe incluir la clase en el mecanismo de coincidencia de patrones estructurales (Python 3.10+, predeterminado True)
    kw_only=False,     # Si se deben hacer todos los campos argumentos de solo palabra clave en __init__ (Python 3.10+, predeterminado False)
    slots=False        # Si se debe usar __slots__ para ahorrar memoria (Python 3.10+, predeterminado False)
)
class MyDataClass:
    # ...
```

Consideremos los más importantes, incluidos los de tu solicitud:

#### `init=True` (predeterminado)

Si es `True`, entonces `dataclass` generará un método `__init__`. Si tienes tu propio `__init__` y dejas `init=True`, entonces se llamará a tu `__init__`, pero los campos definidos en el dataclass no se inicializarán a través de él automáticamente. Por lo general, si escribes tu propio `__init__`, estableces `init=False` para evitar conflictos y tener un control total sobre la inicialización.

```python
@dataclass(init=False)
class CustomPersonInit:
    name: str
    age: int

    def __init__(self, name: str, age: int, welcome_message: str = "¡Hola!"):
        self.name = name
        self.age = age
        print(welcome_message)

alice = CustomPersonInit("Alice", 30) # Imprime "¡Hola!"
print(alice) # CustomPersonInit(name='Alice', age=30) - repr sigue funcionando
```

#### `repr=True` (predeterminado)

Si es `True`, generará un método `__repr__` que proporciona una representación de cadena conveniente del objeto, útil para la depuración.

#### `eq=True` (predeterminado)

Si es `True`, generará un método `__eq__` que te permite comparar dos instancias de la clase por igualdad comprobando la igualdad de todos sus campos.

#### `order=False`

Si es `True`, entonces `dataclass` generará los métodos `__lt__`, `__le__`, `__gt__`, `__ge__`. Esto te permite comparar instancias por "menor que", "mayor que", etc. La comparación se realiza en el orden en que se declaran los campos. Para que `order=True` funcione, `eq=True` también debe estar establecido.

```python
@dataclass(order=True)
class Person:
    name: str
    age: int

alice = Person("Alice", 30)
boris = Person("Boris", 25)
victor = Person("Victor", 35) # Añadamos a Victor
galina = Person("Galina", 30)
alice_older = Person("Alice", 35)


print(f"Alice ({alice.age}) > Boris ({boris.age})? {alice > boris}") # False (ya que 'Alice' < 'Boris' por nombre). La comparación se realiza lexicográficamente en la tupla (nombre, edad). ('Alice', 30) < ('Boris', 25) es False. Por lo tanto, `>` será False.
# Explicación: ('Alice', 30) > ('Boris', 25) -> False, porque 'Alice' < 'Boris'.
print(f"Alice ({alice.age}) < Alice_older ({alice_older.age})? {alice < alice_older}") # True (porque el nombre es el mismo, y la edad 30 < 35)
print(f"Galina ({galina.age}) == Alice ({alice.age})? {galina == alice}") # False (nombres diferentes)
```

**Nota importante:** El orden de los campos es importante para `order=True`.

#### `unsafe_hash=False`

Si es `True`, generará un método `__hash__`. Los Dataclasses no son hashables por defecto si son mutables (`frozen=False`), porque los objetos hashables deben ser inmutables. Si estás seguro de que tu dataclass mutable solo se usará en contextos donde su hash no cambiará (¡lo cual es arriesgado!), puedes establecer `unsafe_hash=True`.
Mucho más a menudo, `__hash__` se genera automáticamente si:
1.  `frozen=True`.
2.  `frozen=False`, pero `eq=True` y todos los campos también son hashables.

```python
@dataclass(frozen=True) # Los dataclasses congelados son hashables
class ImmutablePoint:
    x: int
    y: int

p = ImmutablePoint(1, 2)
print(hash(p)) # Funciona

@dataclass(unsafe_hash=True) # Arriesgado si el objeto es mutable
class MutableButHashable:
    value: int

m = MutableButHashable(5)
print(hash(m))
m.value = 10
print(hash(m)) # El hash ha cambiado, lo que puede provocar problemas cuando se usa en un set/dict
```

#### `frozen=False`

Si es `True`, las instancias de la clase se vuelven inmutables. Después de crear un objeto, no podrás cambiar los valores de sus campos. Esto es útil para crear objetos inmutables que son más fáciles de usar en aplicaciones multiproceso o como claves de diccionario (si son hashables).

```python
@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

c = Coordinate(10.0, 20.0)
# c.lat = 15.0 # AttributeError: cannot assign to field 'lat'
```

#### `kw_only=False` (Python 3.10+)

Si es `True`, **todos** los campos en `__init__` se convierten en argumentos de **solo palabra clave**. Esto significa que debes pasar los valores de los campos por su nombre, no por su posición. Esto mejora la legibilidad y evita errores, especialmente cuando la clase tiene muchos campos o pueden tener los mismos tipos.

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

# Puedes anular este comportamiento para un campo específico con field(kw_only=False)
@dataclass(kw_only=True)
class MixedConfig:
    # Posicional obligatorio (no estilo dataclass)
    # El campo `id` no será kw_only, aunque la clase se especifica como kw_only=True
    id: int = field(kw_only=False)
    name: str = field(kw_only=False)

    # Los campos restantes son kw_only
    email: str
    age: int = 0

# Ten en cuenta que id y name se pasan posicionalmente, y email se pasa por nombre
mixed_config = MixedConfig(123, "Boris", email="boris@example.com")
print(mixed_config)
# mixed_config_fail = MixedConfig(id=123, name="Victor", email="viktor@example.com") # Error, id y name serían posicionales
# Este escenario es menos típico, kw_only se aplica generalmente a toda la clase
```

**Nota:** `field(kw_only=False)` en un campo anula `kw_only=True` a nivel de clase, haciendo que ese campo específico sea posicional. Sin embargo, la mayoría de las veces, `kw_only=True` se usa para toda la clase. El uso principal de `field(kw_only=True)` es cuando tienes un dataclass normal (`kw_only=False` por defecto), pero quieres que *algunos* campos sean de solo palabra clave.

#### `slots=False` (Python 3.10+)

Si es `True`, `dataclass` generará `__slots__` para tu clase. `__slots__` es un atributo especial que permite a Python asignar una cantidad fija de memoria para las instancias de la clase, en lugar de usar un diccionario dinámico `__dict__` para almacenar atributos.

**Ventajas de `slots=True`:**
*   **Ahorro de memoria:** Reduce significativamente la cantidad de memoria consumida por cada instancia. Esto es especialmente importante para las aplicaciones que crean millones de objetos.
*   **Acceso más rápido a los atributos:** El acceso a los atributos a través de `__slots__` puede ser ligeramente más rápido, ya que Python no necesita buscarlos en un diccionario.

**Desventajas de `slots=True`:**
*   **No se pueden añadir nuevos atributos sobre la marcha:** No podrás asignar un atributo que no se haya declarado en el dataclass (o en el `__slots__` de una clase padre).
*   **Dificultades con la herencia múltiple:** Puede ser difícil usar `__slots__` con la herencia múltiple, especialmente si algunas clases padre no usan `__slots__` o los usan de manera diferente.
*   **No tiene `__dict__`:** Las instancias no tendrán un atributo `__dict__` a menos que se haya añadido explícitamente a `__slots__` o a una clase padre.

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

print(f"Tamaño de RegularPoint: {sys.getsizeof(rp)} bytes")
# Aproximadamente 56 bytes en Python 3.10+ (puede variar)
# print(rp.__dict__) # {'x': 1, 'y': 2} - tiene __dict__

print(f"Tamaño de SlottedPoint: {sys.getsizeof(sp)} bytes")
# Aproximadamente 32 bytes en Python 3.10+ (puede variar) - significativamente más pequeño
# print(sp.__dict__) # AttributeError: 'SlottedPoint' object has no attribute '__dict__'

# Intento de añadir un nuevo atributo a un dataclass con slots
try:
    sp.z = 30
except AttributeError as e:
    print(f"Error al añadir un nuevo atributo: {e}")
```

**¿Cuándo usar `slots=True`?**
Cuando estás creando un número muy grande de instancias de la misma clase y el ahorro de memoria es una prioridad. Es una gran optimización, but it has its trade-offs.

### La función `field()`: Configuración detallada de los campos

Además de los parámetros a nivel de clase, puedes configurar cada campo individualmente usando la función `field()` del módulo `dataclasses`. Esto es especialmente útil cuando necesitas una lógica más compleja para los campos que una simple anotación de tipo.

```python
from dataclasses import dataclass, field
from typing import List, Dict, Any
import uuid # Para generar IDs

@dataclass
class Product:
    id: str = field(default_factory=lambda: "prod-" + str(uuid.uuid4())[:8], init=False) # No se inicializa a través de __init__, se genera automáticamente
    name: str
    price: float = field(compare=False, metadata={'unit': 'USD', 'min_value': 0.0}) # No se incluye en la comparación, tiene metadatos
    tags: List[str] = field(default_factory=list, repr=False) # Usa una fábrica para la lista, no se muestra en repr
    description: str = field(default="Descripción no disponible") # Valor por defecto normal
    details: Dict[str, Any] = field(default_factory=dict, hash=False) # No se incluye en el hash

p = Product(name="Portátil", price=1200.0, tags=["electrónica", "tecnología"])
print(p)
# Product(id='prod-...', name='Portátil', price=1200.0, description='Descripción no disponible', details={})
# Ten en cuenta que 'tags' no está en el repr, y 'id' se generó automáticamente.

p2 = Product(name="Portátil", price=1500.0, tags=["electrónica", "tecnología"])
print(f"p == p2? {p == p2}") # True, porque el precio no se incluye en la comparación (compare=False)

# p3 = Product(name="PC de sobremesa", price=1000.0, details={"cpu": "Intel"})
# print(hash(p3)) # TypeError: unhashable type: 'dict' (debido a details: hash=False)
# Si frozen=True, y details no fuera hash=False, entonces el dict tendría que ser inmutable.
```

Consideremos los parámetros de `field()`:

*   **`default`**: Un valor por defecto normal para el campo.
    ```python
    value: int = field(default=0)
    ```

*   **`default_factory`**: Una función sin argumentos que se llamará para obtener el valor por defecto del campo. **¡Es obligatorio usar `default_factory` para los valores por defecto mutables (listas, diccionarios, objetos) para evitar problemas de estado compartido entre instancias!**
    ```python
    items: List[str] = field(default_factory=list)
    ```

*   **`init`**: Si es `True` (predeterminado), el campo se incluirá en el método `__init__` generado. Si es `False`, el campo no será un argumento en el constructor, y debes proporcionarle un `default` / `default_factory`, o inicializarlo en `__post_init__`.
    ```python
    import time
    timestamp: float = field(init=False, default_factory=time.time)
    ```

*   **`repr`**: Si es `True` (predeterminado), el campo se incluirá en el método `__repr__` generado. Útil para ocultar datos grandes o sensibles.
    ```python
    password: str = field(repr=False)
    ```

*   **`compare`**: Si es `True` (predeterminado), el campo se incluirá en los métodos `__eq__` y `__order__` generados. Si es `False`, no afectará a la comparación de objetos.
    ```python
    version: str = field(compare=False)
    ```

*   **`hash`**: Si es `True` (predeterminado), el campo se incluirá en el método `__hash__` generado. Si es `False`, no afectará al hash del objeto. Si la clase es `frozen=True`, pero algún campo tiene `hash=False`, entonces la clase no podrá generar su `__hash__` y se volverá no hashable.
    ```python
    config: Dict[str, Any] = field(hash=False, default_factory=dict)
    ```

*   **`metadata`**: Un diccionario para almacenar datos arbitrarios asociados con el campo. `dataclasses` ignora estos datos, pero pueden ser utilizados por herramientas externas (por ejemplo, para validación, serialización, generación de documentación).
    ```python
    user_id: int = field(metadata={'help': 'Identificador único de usuario', 'validator': 'positive_int'})
    ```

*   **`kw_only`**: (Python 3.10+) Si es `True`, este campo específico se convierte en un argumento de solo palabra clave en `__init__`. Si es `False`, se convierte en posicional. Esto te permite mezclar argumentos posicionales y de solo palabra clave cuando el `kw_only` de la clase es `False` por defecto.
    ```python
    @dataclass
    class FlexibleParams:
        mandatory_pos: str # Posicional
        optional_kw: int = field(default=0, kw_only=True) # Solo palabra clave

    fp1 = FlexibleParams("obligatorio", optional_kw=100)
    # fp2 = FlexibleParams("obligatorio", 200) # TypeError: __init__() takes 1 positional argument but 2 were given (optional_kw)
    ```

### La función `fields()`: Introspección de Dataclass

La función `fields()` del módulo `dataclasses` te permite obtener información sobre los campos de un dataclass o su instancia. Devuelve una tupla de objetos `Field`.

```python
from dataclasses import dataclass, field, fields
from typing import List

@dataclass
class Book:
    title: str
    author: str = field(metadata={'display_name': 'Autor', 'max_length': 100})
    pages: int = field(default=0, metadata={'min_value': 1})
    tags: List[str] = field(default_factory=list, repr=False)

# Obtener información sobre los campos de la clase Book
book_fields = fields(Book)

for f in book_fields:
    print(f"Nombre del campo: {f.name}")
    print(f"Tipo del campo: {f.type}")
    print(f"Valor por defecto: {f.default}")
    print(f"Usa default_factory: {f.default_factory is not None}")
    print(f"Incluido en init: {f.init}")
    print(f"Incluido en repr: {f.repr}")
    print(f"Incluido en compare: {f.compare}")
    print(f"Incluido en hash: {f.hash}")
    print(f"Metadatos: {f.metadata}")
    print(f"Solo palabra clave: {f.kw_only}") # Para Python 3.10+
    print("-" * 20)

# Accediendo a los metadatos de un campo específico:
author_field_info = next(f for f in book_fields if f.name == 'author')
print(f"Nombre para mostrar del autor: {author_field_info.metadata.get('display_name')}")
```

El objeto `Field` tiene los siguientes atributos: `name`, `type`, `default`, `default_factory`, `init`, `repr`, `hash`, `compare`, `metadata`, `kw_only`.

### El método `__post_init__`

A veces necesitas lógica adicional después de que el `__init__` automático del dataclass haya terminado de inicializar los campos. Para ello, puedes definir un método `__post_init__`. Se llamará inmediatamente después de `__init__`.

Esto es útil para:
*   Validación de datos.
*   Cálculo de campos derivados basados en los ya inicializados.
*   Ejecución de cualquier otra lógica que dependa de campos completamente inicializados.

```python
import datetime

@dataclass
class User:
    first_name: str
    last_name: str
    email: str = field(init=False) # Este campo no se incluirá en los parámetros de __init__
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now, init=False)

    def __post_init__(self):
        print(f"--- __post_init__ iniciado para {self.first_name} {self.last_name} ---")
        # Validación
        if not self.first_name or not self.last_name:
            raise ValueError("El nombre y el apellido no pueden estar vacíos.")
        # Cálculo de un campo derivado
        self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@example.com"
        print(f"Usuario {self.first_name} {self.last_name} creado con el correo electrónico: {self.email}")
        print(f"Hora de creación: {self.created_at}")
        print(f"--- __post_init__ finalizado ---")

alice_ivanova = User("Alice", "Ivanova")
print("\nObjeto creado:")
print(alice_ivanova)

print("\n")

try:
    victor_no_last_name = User("Victor", "")
except ValueError as e:
    print(f"Error al crear el usuario: {e}")
```

### Herencia de Dataclass

Los Dataclasses admiten la herencia. Los campos de las clases base se incluyen en las clases hijas.

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

**Características de la herencia con `slots=True`:**
*   Si la clase padre usa `__slots__`, la clase hija también debe usar `__slots__` para obtener el ahorro de memoria.
*   La clase hija debe definir su propio `__slots__` para sus nuevos campos.
*   Si la clase hija no define `__slots__`, tendrá un `__dict__` además de los slots del padre.

### ¿Cuándo usar Dataclasses?

*   **Clases contenedoras de datos:** Cuando el propósito principal de la clase es almacenar datos, y necesitas `__init__`, `__repr__`, `__eq__` automáticos.
*   **Objetos inmutables:** Cuando necesitas objetos cuyo estado no debe cambiar después de la creación (`frozen=True`).
*   **Configuraciones:** Para definir la estructura de los parámetros de configuración.
*   **Objetos de transferencia de datos (DTO):** Para transferir datos estructurados entre partes de una aplicación.
*   **Lógica de negocio simple:** Cuando los métodos de la clase operan principalmente sobre los datos de la propia clase, no tienen un estado interno complejo o efectos secundarios.

### ¿Cuándo NO usar Dataclasses?

*   **Clases con un comportamiento rico:** Cuando una clase tiene una lógica de negocio compleja, muchos métodos que interactúan con sistemas externos o un estado interno complejo, es mejor usar una clase normal.
*   **Modelos de mapeo OR (ORM):** Aunque los dataclasses pueden ser parte de un ORM, no reemplazan a los modelos ORM completos, que a menudo requieren métodos específicos para trabajar con una base de datos, carga diferida, etc.
*   **Polimorfismo y jerarquía de herencia profunda:** Si tienes una jerarquía de clases compleja con un polimorfismo profundo y anulación de comportamiento, las clases normales pueden ser más flexibles.

### Conclusión

Los `dataclasses` son una adición potente y conveniente a Python que simplifica significativamente la creación de clases orientadas a datos. Ayudan a escribir un código más limpio, legible y mantenible, y opciones como `slots=True` y `kw_only=True` brindan oportunidades adicionales para la optimización del rendimiento y la mejora de la ergonomía de la API de tu código. ¡No te olvides de `field()` para la configuración detallada de cada campo y `fields()` para la introspección!

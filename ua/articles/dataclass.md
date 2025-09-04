## Dataclasses: Коли Python зустрічає структуровані дані (з новими іменованими прикладами)

У Python, коли вам потрібен клас для зберігання даних, зазвичай доводиться писати шаблонний код для `__init__`, `__repr__`, `__eq__` та інших магічних методів. Модуль `dataclasses`, представлений у Python 3.7, має на меті вирішити цю проблему, надаючи декоратор `@dataclass`, який автоматично генерує ці методи для вас.

### Що таке Dataclass?

`dataclass` — це клас, який, як випливає з назви, в першу чергу призначений для зберігання даних. Він надає такі ключові переваги:

1.  **Менше шаблонного коду:** Автоматично генерує `__init__`, `__repr__`, `__eq__`, `__hash__` (за певних умов) та інші методи на основі анотацій типів ваших полів.
2.  **Читабельність:** Код стає більш лаконічним і зосередженим на визначенні структури даних.
3.  **Інтроспекція:** Поля Dataclass легко інтроспектувати (перевіряти) за допомогою функцій з того ж модуля `dataclasses`.
4.  **Продуктивність (з `slots=True`):** Може споживати менше пам'яті та бути швидшим у доступі до атрибутів.

### Базове використання

Почнемо з простого прикладу. Припустимо, нам потрібен клас для представлення точки в 2D-просторі.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

# Створення екземпляра
p1 = Point(10, 20)
print(p1) # Point(x=10, y=20) - автоматично згенерований __repr__

# Порівняння екземплярів - автоматично згенерований __eq__
p2 = Point(10, 20)
p3 = Point(30, 40)
print(p1 == p2) # True
print(p1 == p3) # False
```

Як бачите, нам не довелося писати `__init__` або `__repr__`. Все працювало "з коробки".

### Параметри декоратора `@dataclass`

Декоратор `@dataclass` приймає кілька параметрів, які дозволяють налаштувати згенеровану поведінку.

```python
@dataclass(
    init=True,         # Чи генерувати __init__ (за замовчуванням True)
    repr=True,         # Чи генерувати __repr__ (за замовчуванням True)
    eq=True,           # Чи генерувати __eq__ (за замовчуванням True)
    order=False,       # Чи генерувати __lt__, __le__, __gt__, __ge__ (за замовчуванням False)
    unsafe_hash=False, # Чи генерувати __hash__ (за замовчуванням False)
    frozen=False,      # Чи робити екземпляри незмінними (за замовчуванням False)
    match_args=True,   # Чи включати клас у механізм структурного зіставлення шаблонів (Python 3.10+, за замовчуванням True)
    kw_only=False,     # Чи робити всі поля аргументами лише за ключовими словами в __init__ (Python 3.10+, за замовчуванням False)
    slots=False        # Чи використовувати __slots__ для економії пам'яті (Python 3.10+, за замовчуванням False)
)
class MyDataClass:
    # ...
```

Розглянемо найважливіші з них, включаючи ті, що були у вашому запиті:

#### `init=True` (За замовчуванням)

Якщо `True`, то `dataclass` згенерує метод `__init__`. Якщо у вас є власний `__init__`, і ви залишите `init=True`, то ваш `__init__` буде викликаний, але поля, визначені в dataclass, не будуть ініціалізовані через нього автоматично. Зазвичай, якщо ви пишете власний `__init__`, ви встановлюєте `init=False`, щоб уникнути конфліктів і мати повний контроль над ініціалізацією.

```python
@dataclass(init=False)
class CustomPersonInit:
    name: str
    age: int

    def __init__(self, name: str, age: int, welcome_message: str = "Привіт!"):
        self.name = name
        self.age = age
        print(welcome_message)

alice = CustomPersonInit("Alice", 30) # Виводить "Привіт!"
print(alice) # CustomPersonInit(name='Alice', age=30) - repr все ще працює
```

#### `repr=True` (За замовчуванням)

Якщо `True`, він згенерує метод `__repr__`, який надає зручне рядкове представлення об'єкта, корисне для налагодження.

#### `eq=True` (За замовчуванням)

Якщо `True`, він згенерує метод `__eq__`, який дозволяє порівнювати два екземпляри класу на рівність, перевіряючи рівність усіх їхніх полів.

#### `order=False`

Якщо `True`, то `dataclass` згенерує методи `__lt__`, `__le__`, `__gt__`, `__ge__`. Це дозволяє порівнювати екземпляри на "менше ніж", "більше ніж" тощо. Порівняння виконується в порядку оголошення полів. Щоб `order=True` працював, `eq=True` також має бути встановлено.

```python
@dataclass(order=True)
class Person:
    name: str
    age: int

alice = Person("Alice", 30)
boris = Person("Boris", 25)
victor = Person("Victor", 35) # Додамо Віктора
galina = Person("Galina", 30)
alice_older = Person("Alice", 35)


print(f"Alice ({alice.age}) > Boris ({boris.age})? {alice > boris}") # False (оскільки 'Alice' < 'Boris' за іменем) -> порівняння виконується лексикографічно за кортежем (ім'я, вік). ('Alice', 30) < ('Boris', 25) є True. Отже, `>` буде False.
# Пояснення: ('Alice', 30) > ('Boris', 25) -> False, тому що 'Alice' < 'Boris'.
print(f"Alice ({alice.age}) < Alice_older ({alice_older.age})? {alice < alice_older}") # True (тому що ім'я те саме, але вік 30 < 35)
print(f"Galina ({galina.age}) == Alice ({alice.age})? {galina == alice}") # False (різні імена)
```

**Важлива примітка:** Порядок полів має значення для `order=True`.

#### `unsafe_hash=False`

Якщо `True`, він згенерує метод `__hash__`. Dataclasses за замовчуванням не хешуються, якщо вони змінювані (`frozen=False`), оскільки хешовані об'єкти повинні бути незмінними. Якщо ви впевнені, що ваша змінювана dataclass буде використовуватися лише в контекстах, де її хеш не зміниться (що ризиковано!), ви можете встановити `unsafe_hash=True`.
Набагато частіше `__hash__` генерується автоматично, якщо:
1.  `frozen=True`.
2.  `frozen=False`, але `eq=True` і всі поля також хешуються.

```python
@dataclass(frozen=True) # Заморожені dataclasses хешуються
class ImmutablePoint:
    x: int
    y: int

p = ImmutablePoint(1, 2)
print(hash(p)) # Працює

@dataclass(unsafe_hash=True) # Ризиковано, якщо об'єкт змінюваний
class MutableButHashable:
    value: int

m = MutableButHashable(5)
print(hash(m))
m.value = 10
print(hash(m)) # Хеш змінився, що може призвести до проблем при використанні в set/dict
```

#### `frozen=False`

Якщо `True`, екземпляри класу стають незмінними. Після створення об'єкта ви не зможете змінити значення його полів. Це корисно для створення незмінних об'єктів, які легше використовувати в багатопотокових програмах або як ключі словника (якщо вони хешуються).

```python
@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

c = Coordinate(10.0, 20.0)
# c.lat = 15.0 # AttributeError: cannot assign to field 'lat'
```

#### `kw_only=False` (Python 3.10+)

Якщо `True`, **всі** поля в `__init__` стають аргументами **лише за ключовими словами**. Це означає, що ви повинні передавати значення полів за іменем, а не за позицією. Це покращує читабельність і запобігає помилкам, особливо коли клас має багато полів або вони можуть мати однакові типи.

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

# Ви можете перевизначити цю поведінку для конкретного поля за допомогою field(kw_only=False)
@dataclass(kw_only=True)
class MixedConfig:
    # Обов'язковий позиційний (не в стилі dataclass)
    # Поле `id` не буде kw_only, хоча клас вказано як kw_only=True
    id: int = field(kw_only=False)
    name: str = field(kw_only=False)

    # Решта полів є kw_only
    email: str
    age: int = 0

# Зверніть увагу, що id та name передаються позиційно, а email - за іменем
mixed_config = MixedConfig(123, "Boris", email="boris@example.com")
print(mixed_config)
# mixed_config_fail = MixedConfig(id=123, name="Victor", email="viktor@example.com") # Помилка, id та name були б позиційними
# Цей сценарій менш типовий, kw_only зазвичай застосовується до всього класу
```

**Примітка:** `field(kw_only=False)` для поля перевизначає `kw_only=True` на рівні класу, роблячи це конкретне поле позиційним. Однак, найчастіше `kw_only=True` використовується для всього класу. Основне використання `field(kw_only=True)` полягає в тому, коли у вас є звичайна dataclass (за замовчуванням `kw_only=False`), але ви хочете зробити *деякі* поля лише за ключовими словами.

#### `slots=False` (Python 3.10+)

Якщо `True`, `dataclass` згенерує `__slots__` для вашого класу. `__slots__` — це спеціальний атрибут, який дозволяє Python виділяти фіксовану кількість пам'яті для екземплярів класу, замість використання динамічного `__dict__` для зберігання атрибутів.

**Переваги `slots=True`:**
*   **Економія пам'яті:** Значно зменшує обсяг пам'яті, споживаної кожним екземпляром. Це особливо важливо для програм, які створюють мільйони об'єктів.
*   **Швидший доступ до атрибутів:** Доступ до атрибутів через `__slots__` може бути трохи швидшим, оскільки Python не потрібно шукати їх у словнику.

**Недоліки `slots=True`:**
*   **Не можна додавати нові атрибути "на льоту":** Ви не зможете призначити атрибут, який не був оголошений у dataclass (або в `__slots__` батьківського класу).
*   **Труднощі з множинним успадкуванням:** Може бути важко використовувати `__slots__` з множинним успадкуванням, особливо якщо деякі батьківські класи не використовують `__slots__` або використовують їх по-різному.
*   **Не має `__dict__`:** Екземпляри не матимуть атрибута `__dict__`, якщо він не був явно доданий до `__slots__` або батьківського класу.

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

print(f"Розмір RegularPoint: {sys.getsizeof(rp)} байт")
# Приблизно 56 байт на Python 3.10+ (може відрізнятися)
# print(rp.__dict__) # {'x': 1, 'y': 2} - має __dict__

print(f"Розмір SlottedPoint: {sys.getsizeof(sp)} байт")
# Приблизно 32 байт на Python 3.10+ (може відрізнятися) - значно менший
# print(sp.__dict__) # AttributeError: 'SlottedPoint' object has no attribute '__dict__'

# Спроба додати новий атрибут до slotted dataclass
try:
    sp.z = 30
except AttributeError as e:
    print(f"Помилка при додаванні нового атрибута: {e}")
```

**Коли використовувати `slots=True`?**
Коли ви створюєте дуже велику кількість екземплярів одного класу, і економія пам'яті є пріоритетом. Це чудова оптимізація, але вона має свої компроміси.

### Функція `field()`: Детальна конфігурація поля

Окрім параметрів на рівні класу, ви можете налаштувати кожне поле окремо за допомогою функції `field()` з модуля `dataclasses`. Це особливо корисно, коли вам потрібна складніша логіка для полів, ніж просто анотація типу.

```python
from dataclasses import dataclass, field
from typing import List, Dict, Any
import uuid # Для генерації ID

@dataclass
class Product:
    id: str = field(default_factory=lambda: "prod-" + str(uuid.uuid4())[:8], init=False) # Не ініціалізується через __init__, генерується автоматично
    name: str
    price: float = field(compare=False, metadata={'unit': 'USD', 'min_value': 0.0}) # Не бере участі в порівнянні, має метадані
    tags: List[str] = field(default_factory=list, repr=False) # Використовує фабрику для списку, не відображається в repr
    description: str = field(default="Опис відсутній") # Звичайне значення за замовчуванням
    details: Dict[str, Any] = field(default_factory=dict, hash=False) # Не бере участі в хешуванні

p = Product(name="Ноутбук", price=1200.0, tags=["електроніка", "техніка"])
print(p)
# Product(id='prod-...', name='Ноутбук', price=1200.0, description='Опис відсутній', details={})
# Зверніть увагу, що 'tags' немає в repr, а 'id' було згенеровано автоматично.

p2 = Product(name="Ноутбук", price=1500.0, tags=["електроніка", "техніка"])
print(f"p == p2? {p == p2}") # True, тому що ціна не бере участі в порівнянні (compare=False)

# p3 = Product(name="Настільний ПК", price=1000.0, details={"cpu": "Intel"})
# print(hash(p3)) # TypeError: unhashable type: 'dict' (через details: hash=False)
# Якщо frozen=True, і details не були hash=False, то dict мав би бути незмінним.
```

Розглянемо параметри `field()`:

*   **`default`**: Звичайне значення за замовчуванням для поля.
    ```python
    value: int = field(default=0)
    ```

*   **`default_factory`**: Функція без аргументів, яка буде викликана для отримання значення за замовчуванням для поля. **Обов'язково використовуйте `default_factory` для змінюваних значень за замовчуванням (списки, словники, об'єкти), щоб уникнути проблем зі спільним станом між екземплярами!**
    ```python
    items: List[str] = field(default_factory=list)
    ```

*   **`init`**: Якщо `True` (за замовчуванням), поле буде включено до згенерованого методу `__init__`. Якщо `False`, поле не буде аргументом у конструкторі, і ви повинні або надати для нього `default` / `default_factory`, або ініціалізувати його в `__post_init__`.
    ```python
    import time
    timestamp: float = field(init=False, default_factory=time.time)
    ```

*   **`repr`**: Якщо `True` (за замовчуванням), поле буде включено до згенерованого методу `__repr__`. Корисно для приховування великих або конфіденційних даних.
    ```python
    password: str = field(repr=False)
    ```

*   **`compare`**: Якщо `True` (за замовчуванням), поле буде включено до згенерованих методів `__eq__` та `__order__`. Якщо `False`, воно не впливатиме на порівняння об'єктів.
    ```python
    version: str = field(compare=False)
    ```

*   **`hash`**: Якщо `True` (за замовчуванням), поле буде включено до згенерованого методу `__hash__`. Якщо `False`, воно не впливатиме на хеш об'єкта. Якщо клас є `frozen=True`, але будь-яке поле має `hash=False`, то клас не зможе згенерувати свій `__hash__` і стане нехешованим.
    ```python
    config: Dict[str, Any] = field(hash=False, default_factory=dict)
    ```

*   **`metadata`**: Словник для зберігання довільних даних, пов'язаних з полем. `dataclasses` ігнорують ці дані, але вони можуть використовуватися зовнішніми інструментами (наприклад, для валідації, серіалізації, генерації документації).
    ```python
    user_id: int = field(metadata={'help': 'Унікальний ідентифікатор користувача', 'validator': 'positive_int'})
    ```

*   **`kw_only`**: (Python 3.10+) Якщо `True`, це конкретне поле стає аргументом лише за ключовим словом у `__init__`. Якщо `False`, воно стає позиційним. Це дозволяє змішувати позиційні та ключові аргументи, коли `kw_only` класу за замовчуванням є `False`.
    ```python
    @dataclass
    class FlexibleParams:
        mandatory_pos: str # Позиційний
        optional_kw: int = field(default=0, kw_only=True) # Лише за ключовим словом

    fp1 = FlexibleParams("обов'язковий", optional_kw=100)
    # fp2 = FlexibleParams("обов'язковий", 200) # TypeError: __init__() takes 1 positional argument but 2 were given (optional_kw)
    ```

### Функція `fields()`: Інтроспекція Dataclass

Функція `fields()` з модуля `dataclasses` дозволяє отримати інформацію про поля dataclass або її екземпляра. Вона повертає кортеж об'єктів `Field`.

```python
from dataclasses import dataclass, field, fields
from typing import List

@dataclass
class Book:
    title: str
    author: str = field(metadata={'display_name': 'Автор', 'max_length': 100})
    pages: int = field(default=0, metadata={'min_value': 1})
    tags: List[str] = field(default_factory=list, repr=False)

# Отримати інформацію про поля класу Book
book_fields = fields(Book)

for f in book_fields:
    print(f"Назва поля: {f.name}")
    print(f"Тип поля: {f.type}")
    print(f"Значення за замовчуванням: {f.default}")
    print(f"Використовує default_factory: {f.default_factory is not None}")
    print(f"Включено в init: {f.init}")
    print(f"Включено в repr: {f.repr}")
    print(f"Включено в compare: {f.compare}")
    print(f"Включено в hash: {f.hash}")
    print(f"Метадані: {f.metadata}")
    print(f"Лише за ключовим словом: {f.kw_only}") # Для Python 3.10+
    print("-" * 20)

# Доступ до метаданих конкретного поля:
author_field_info = next(f for f in book_fields if f.name == 'author')
print(f"Відображуване ім'я для автора: {author_field_info.metadata.get('display_name')}")
```

Об'єкт `Field` має такі атрибути: `name`, `type`, `default`, `default_factory`, `init`, `repr`, `hash`, `compare`, `metadata`, `kw_only`.

### Метод `__post_init__`

Іноді вам потрібна додаткова логіка після того, як автоматичний `__init__` dataclass завершив ініціалізацію полів. Для цього ви можете визначити метод `__post_init__`. Він буде викликаний відразу після `__init__`.

Це корисно для:
*   Валідації даних.
*   Обчислення похідних полів на основі вже ініціалізованих.
*   Виконання будь-якої іншої логіки, яка залежить від повністю ініціалізованих полів.

```python
import datetime

@dataclass
class User:
    first_name: str
    last_name: str
    email: str = field(init=False) # Це поле не буде включено в параметри __init__
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now, init=False)

    def __post_init__(self):
        print(f"--- __post_init__ розпочато для {self.first_name} {self.last_name} ---")
        # Валідація
        if not self.first_name or not self.last_name:
            raise ValueError("Ім'я та прізвище не можуть бути порожніми.")
        # Обчислення похідного поля
        self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@example.com"
        print(f"Користувач {self.first_name} {self.last_name} створений з електронною поштою: {self.email}")
        print(f"Час створення: {self.created_at}")
        print(f"--- __post_init__ завершено ---")

alice_ivanova = User("Alice", "Ivanova")
print("
Об'єкт створено:")
print(alice_ivanova)

print("
")

try:
    victor_no_last_name = User("Victor", "")
except ValueError as e:
    print(f"Помилка при створенні користувача: {e}")
```

### Успадкування Dataclass

Dataclasses підтримують успадкування. Поля з базових класів включаються в дочірні класи.

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

**Особливості успадкування з `slots=True`:**
*   Якщо батьківський клас використовує `__slots__`, дочірній клас також повинен використовувати `__slots__`, щоб отримати економію пам'яті.
*   Дочірній клас повинен визначити власні `__slots__` для своїх нових полів.
*   Якщо дочірній клас не визначає `__slots__`, він матиме `__dict__` на додаток до слотів батьківського класу.

### Коли використовувати Dataclasses?

*   **Класи-контейнери даних:** Коли основною метою класу є зберігання даних, і вам потрібні автоматичні `__init__`, `__repr__`, `__eq__`.
*   **Незмінні об'єкти:** Коли вам потрібні об'єкти, стан яких не повинен змінюватися після створення (`frozen=True`).
*   **Конфігурації:** Для визначення структури параметрів конфігурації.
*   **Об'єкти передачі даних (DTO):** Для передачі структурованих даних між частинами програми.
*   **Проста бізнес-логіка:** Коли методи класу в основному оперують даними самого класу, не мають складної внутрішньої стану або побічних ефектів.

### Коли НЕ використовувати Dataclasses?

*   **Класи з багатою поведінкою:** Коли клас має складну бізнес-логіку, багато методів, які взаємодіють із зовнішніми системами, або складний внутрішній стан, краще використовувати звичайний клас.
*   **Моделі OR-мапінгу (ORM):** Хоча dataclasses можуть бути частиною ORM, вони не замінюють повноцінні моделі ORM, які часто вимагають специфічних методів для роботи з базою даних, лінивого завантаження тощо.
*   **Поліморфізм та глибока ієрархія успадкування:** Якщо у вас складна ієрархія класів з глибоким поліморфізмом та перевизначенням поведінки, звичайні класи можуть бути гнучкішими.

### Висновок

`dataclasses` — це потужне та зручне доповнення до Python, яке значно спрощує створення класів, орієнтованих на дані. Вони допомагають писати чистіший, читабельніший та легший у підтримці код, а такі опції, як `slots=True` та `kw_only=True`, надають додаткові можливості для оптимізації продуктивності та покращення ергономіки API вашого коду. Не забувайте про `field()` для детальної конфігурації кожного поля та `fields()` для інтроспекції!
## Dataclasses: Gdy Python spotyka dane strukturalne (z nowymi nazwanymi przykładami)

W Pythonie, gdy potrzebujesz klasy do przechowywania danych, zazwyczaj musisz pisać powtarzalny kod dla `__init__`, `__repr__`, `__eq__` i innych magicznych metod. Moduł `dataclasses`, wprowadzony w Pythonie 3.7, ma na celu rozwiązanie tego problemu, dostarczając dekorator `@dataclass`, który automatycznie generuje te metody.

### Co to jest Dataclass?

`dataclass` to klasa, która, jak sama nazwa wskazuje, jest przeznaczona głównie do przechowywania danych. Zapewnia następujące kluczowe korzyści:

1.  **Mniej kodu boilerplate:** Automatycznie generuje `__init__`, `__repr__`, `__eq__`, `__hash__` (w pewnych warunkach) i inne metody na podstawie adnotacji typów twoich pól.
2.  **Czytelność:** Kod staje się bardziej zwięzły i skupiony na definiowaniu struktury danych.
3.  **Introspekcja:** Pola Dataclass są łatwe do introspekcji (sprawdzania) za pomocą funkcji z tego samego modułu `dataclasses`.
4.  **Wydajność (z `slots=True`):** Może zużywać mniej pamięci i być szybsza w dostępie do atrybutów.

### Podstawowe użycie

Zacznijmy od prostego przykładu. Załóżmy, że potrzebujemy klasy do reprezentowania punktu w przestrzeni 2D.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

# Tworzenie instancji
p1 = Point(10, 20)
print(p1) # Point(x=10, y=20) - automatycznie wygenerowany __repr__

# Porównywanie instancji - automatycznie wygenerowany __eq__
p2 = Point(10, 20)
p3 = Point(30, 40)
print(p1 == p2) # True
print(p1 == p3) # False
```

Jak widać, nie musieliśmy pisać `__init__` ani `__repr__`. Wszystko działało "od razu".

### Parametry dekoratora `@dataclass`

Dekorator `@dataclass` akceptuje kilka parametrów, które pozwalają dostosować generowane zachowanie.

```python
@dataclass(
    init=True,         # Czy generować __init__ (domyślnie True)
    repr=True,         # Czy generować __repr__ (domyślnie True)
    eq=True,           # Czy generować __eq__ (domyślnie True)
    order=False,       # Czy generować __lt__, __le__, __gt__, __ge__ (domyślnie False)
    unsafe_hash=False, # Czy generować __hash__ (domyślnie False)
    frozen=False,      # Czy uczynić instancje niezmiennymi (domyślnie False)
    match_args=True,   # Czy uwzględnić klasę w mechanizmie strukturalnego dopasowywania wzorców (Python 3.10+, domyślnie True)
    kw_only=False,     # Czy uczynić wszystkie pola argumentami tylko-słownikowymi w __init__ (Python 3.10+, domyślnie False)
    slots=False        # Czy używać __slots__ do oszczędzania pamięci (Python 3.10+, domyślnie False)
)
class MyDataClass:
    # ...
```

Rozważmy najważniejsze z nich, w tym te, które były w Twoim zapytaniu:

#### `init=True` (domyślnie)

Jeśli `True`, to `dataclass` wygeneruje metodę `__init__`. Jeśli masz własny `__init__` i pozostawisz `init=True`, to Twój `__init__` zostanie wywołany, ale pola zdefiniowane w dataclass nie zostaną przez niego automatycznie zainicjalizowane. Zazwyczaj, jeśli piszesz własny `__init__`, ustawiasz `init=False`, aby uniknąć konfliktów i mieć pełną kontrolę nad inicjalizacją.

```python
@dataclass(init=False)
class CustomPersonInit:
    name: str
    age: int

    def __init__(self, name: str, age: int, welcome_message: str = "Witaj!"):
        self.name = name
        self.age = age
        print(welcome_message)

alice = CustomPersonInit("Alice", 30) # Wyświetla "Witaj!"
print(alice) # CustomPersonInit(name='Alice', age=30) - repr nadal działa
```

#### `repr=True` (domyślnie)

Jeśli `True`, wygeneruje metodę `__repr__`, która zapewnia wygodną reprezentację ciągu znaków obiektu, przydatną do debugowania.

#### `eq=True` (domyślnie)

Jeśli `True`, wygeneruje metodę `__eq__`, która pozwala porównywać dwie instancje klasy pod kątem równości, sprawdzając równość wszystkich ich pól.

#### `order=False`

Jeśli `True`, to `dataclass` wygeneruje metody `__lt__`, `__le__`, `__gt__`, `__ge__`. Pozwala to porównywać instancje pod kątem "mniejsze niż", "większe niż" itp. Porównanie odbywa się w kolejności deklaracji pól. Aby `order=True` działało, `eq=True` również musi być ustawione.

```python
@dataclass(order=True)
class Person:
    name: str
    age: int

alice = Person("Alice", 30)
boris = Person("Boris", 25)
victor = Person("Victor", 35) # Dodajmy Victora
galina = Person("Galina", 30)
alice_older = Person("Alice", 35)


print(f"Alice ({alice.age}) > Boris ({boris.age})? {alice > boris}") # False (ponieważ 'Alice' < 'Boris' według nazwy) -> porównanie odbywa się leksykograficznie na krotce (nazwa, wiek). ('Alice', 30) < ('Boris', 25) jest True. Zatem `>` będzie False.
# Wyjaśnienie: ('Alice', 30) > ('Boris', 25) -> False, ponieważ 'Alice' < 'Boris'.
print(f"Alice ({alice.age}) < Alice_older ({alice_older.age})? {alice < alice_older}") # True (ponieważ nazwa jest taka sama, ale wiek 30 < 35)
print(f"Galina ({galina.age}) == Alice ({alice.age})? {galina == alice}") # False (różne nazwy)
```

**Ważna uwaga:** Kolejność pól ma znaczenie dla `order=True`.

#### `unsafe_hash=False`

Jeśli `True`, wygeneruje metodę `__hash__`. Dataclassy nie są domyślnie haszowalne, jeśli są zmienne (`frozen=False`), ponieważ obiekty haszowalne muszą być niezmienne. Jeśli masz pewność, że Twoja zmienna dataclass będzie używana tylko w kontekstach, w których jej hash się nie zmieni (co jest ryzykowne!), możesz ustawić `unsafe_hash=True`.
Znacznie częściej `__hash__` jest generowany automatycznie, jeśli:
1.  `frozen=True`.
2.  `frozen=False`, ale `eq=True` i wszystkie pola są również haszowalne.

```python
@dataclass(frozen=True) # Zamrożone dataclassy są haszowalne
class ImmutablePoint:
    x: int
    y: int

p = ImmutablePoint(1, 2)
print(hash(p)) # Działa

@dataclass(unsafe_hash=True) # Ryzykowne, jeśli obiekt jest zmienny
class MutableButHashable:
    value: int

m = MutableButHashable(5)
print(hash(m))
m.value = 10
print(hash(m)) # Hash się zmienił, co może prowadzić do problemów przy użyciu w zbiorze/słowniku
```

#### `frozen=False`

Jeśli `True`, instancje klasy stają się niezmienne. Po utworzeniu obiektu nie będziesz mógł zmienić wartości jego pól. Jest to przydatne do tworzenia niezmiennych obiektów, które są łatwiejsze w użyciu w aplikacjach wielowątkowych lub jako klucze słownika (jeśli są haszowalne).

```python
@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

c = Coordinate(10.0, 20.0)
# c.lat = 15.0 # AttributeError: cannot assign to field 'lat'
```

#### `kw_only=False` (Python 3.10+)

Jeśli `True`, **wszystkie** pola w `__init__` stają się argumentami **tylko-słownikowymi**. Oznacza to, że musisz przekazywać wartości pól po nazwie, a nie po pozycji. Poprawia to czytelność i zapobiega błędom, zwłaszcza gdy klasa ma wiele pól lub mogą mieć te same typy.

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

# Możesz nadpisać to zachowanie dla konkretnego pola, używając field(kw_only=False)
@dataclass(kw_only=True)
class MixedConfig:
    # Obowiązkowe tylko pozycyjne (nie w stylu dataclass)
    # Pole `id` nie będzie kw_only, chociaż klasa jest określona jako kw_only=True
    id: int = field(kw_only=False)
    name: str = field(kw_only=False)

    # Pozostałe pola są kw_only
    email: str
    age: int = 0

# Zauważ, że id i name są przekazywane pozycyjnie, a email po nazwie
mixed_config = MixedConfig(123, "Boris", email="boris@example.com")
print(mixed_config)
# mixed_config_fail = MixedConfig(id=123, name="Victor", email="viktor@example.com") # Błąd, id i name byłyby pozycyjne
# Ten scenariusz jest mniej typowy, kw_only jest zazwyczaj stosowane do całej klasy
```

**Uwaga:** `field(kw_only=False)` w polu nadpisuje `kw_only=True` na poziomie klasy, czyniąc to konkretne pole pozycyjnym. Jednak najczęściej `kw_only=True` jest używane dla całej klasy. Główne zastosowanie `field(kw_only=True)` jest wtedy, gdy masz zwykłą dataclass (domyślnie `kw_only=False`), ale chcesz, aby *niektóre* pola były tylko-słownikowe.

#### `slots=False` (Python 3.10+)

Jeśli `True`, `dataclass` wygeneruje `__slots__` dla Twojej klasy. `__slots__` to specjalny atrybut, który pozwala Pythonowi przydzielić stałą ilość pamięci dla instancji klasy, zamiast używać dynamicznego `__dict__` do przechowywania atrybutów.

**Zalety `slots=True`:**
*   **Oszczędność pamięci:** Znacząco zmniejsza ilość pamięci zużywanej przez każdą instancję. Jest to szczególnie ważne w aplikacjach, które tworzą miliony obiektów.
*   **Szybszy dostęp do atrybutów:** Dostęp do atrybutów za pośrednictwem `__slots__` może być nieco szybszy, ponieważ Python nie musi ich szukać w słowniku.

**Wady `slots=True`:**
*   **Nie można dodawać nowych atrybutów "w locie":** Nie będziesz mógł przypisać atrybutu, który nie został zadeklarowany w dataclass (lub w `__slots__` klasy nadrzędnej).
*   **Trudności z dziedziczeniem wielokrotnym:** Może być trudno używać `__slots__` z dziedziczeniem wielokrotnym, zwłaszcza jeśli niektóre klasy nadrzędne nie używają `__slots__` lub używają ich inaczej.
*   **Nie ma `__dict__`:** Instancje nie będą miały atrybutu `__dict__`, chyba że został on jawnie dodany do `__slots__` lub klasy nadrzędnej.

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

print(f"Rozmiar RegularPoint: {sys.getsizeof(rp)} bajtów")
# Około 56 bajtów w Pythonie 3.10+ (może się różnić)
# print(rp.__dict__) # {'x': 1, 'y': 2} - ma __dict__

print(f"Rozmiar SlottedPoint: {sys.getsizeof(sp)} bajtów")
# Około 32 bajtów w Pythonie 3.10+ (może się różnić) - znacznie mniejszy
# print(sp.__dict__) # AttributeError: 'SlottedPoint' object has no attribute '__dict__'

# Próba dodania nowego atrybutu do slotted dataclass
try:
    sp.z = 30
except AttributeError as e:
    print(f"Błąd podczas dodawania nowego atrybutu: {e}")
```

**Kiedy używać `slots=True`?**
Kiedy tworzysz bardzo dużą liczbę instancji tej samej klasy, a oszczędność pamięci jest priorytetem. Jest to świetna optymalizacja, ale ma swoje kompromisy.

### Funkcja `field()`: Szczegółowa konfiguracja pola

Oprócz parametrów na poziomie klasy, możesz skonfigurować każde pole indywidualnie, używając funkcji `field()` z modułu `dataclasses`. Jest to szczególnie przydatne, gdy potrzebujesz bardziej złożonej logiki dla pól niż tylko adnotacja typu.

```python
from dataclasses import dataclass, field
from typing import List, Dict, Any
import uuid # Do generowania ID

@dataclass
class Product:
    id: str = field(default_factory=lambda: "prod-" + str(uuid.uuid4())[:8], init=False) # Nie inicjalizowane przez __init__, generowane automatycznie
    name: str
    price: float = field(compare=False, metadata={'unit': 'USD', 'min_value': 0.0}) # Nie uczestniczy w porównaniu, ma metadane
    tags: List[str] = field(default_factory=list, repr=False) # Używa fabryki dla listy, nie wyświetlane w repr
    description: str = field(default="Brak opisu") # Zwykła wartość domyślna
    details: Dict[str, Any] = field(default_factory=dict, hash=False) # Nie uczestniczy w haszowaniu

p = Product(name="Laptop", price=1200.0, tags=["electronics", "tech"])
print(p)
# Product(id='prod-...', name='Laptop', price=1200.0, description='Brak opisu', details={})
# Zauważ, że 'tags' nie ma w repr, a 'id' zostało wygenerowane automatycznie.

p2 = Product(name="Laptop", price=1500.0, tags=["electronics", "tech"])
print(f"p == p2? {p == p2}") # True, ponieważ cena nie uczestniczy w porównaniu (compare=False)

# p3 = Product(name="Komputer stacjonarny", price=1000.0, details={"cpu": "Intel"})
# print(hash(p3)) # TypeError: unhashable type: 'dict' (z powodu details: hash=False)
# Jeśli frozen=True, a details nie były hash=False, to słownik musiałby być niezmienny.
```

Rozważmy parametry `field()`:

*   **`default`**: Zwykła wartość domyślna dla pola.
    ```python
    value: int = field(default=0)
    ```

*   **`default_factory`**: Funkcja bez argumentów, która zostanie wywołana w celu uzyskania wartości domyślnej dla pola. **Pamiętaj, aby używać `default_factory` dla zmiennych wartości domyślnych (listy, słowniki, obiekty), aby uniknąć problemów ze współdzielonym stanem między instancjami!**
    ```python
    items: List[str] = field(default_factory=list)
    ```

*   **`init`**: Jeśli `True` (domyślnie), pole zostanie uwzględnione w wygenerowanej metodzie `__init__`. Jeśli `False`, pole nie będzie argumentem w konstruktorze, a musisz albo podać dla niego `default` / `default_factory`, albo zainicjalizować je w `__post_init__`.
    ```python
    import time
    timestamp: float = field(init=False, default_factory=time.time)
    ```

*   **`repr`**: Jeśli `True` (domyślnie), pole zostanie uwzględnione w wygenerowanej metodzie `__repr__`. Przydatne do ukrywania dużych lub wrażliwych danych.
    ```python
    password: str = field(repr=False)
    ```

*   **`compare`**: Jeśli `True` (domyślnie), pole zostanie uwzględnione w wygenerowanych metodach `__eq__` i `__order__`. Jeśli `False`, nie wpłynie na porównanie obiektów.
    ```python
    version: str = field(compare=False)
    ```

*   **`hash`**: Jeśli `True` (domyślnie), pole zostanie uwzględnione w wygenerowanej metodzie `__hash__`. Jeśli `False`, nie wpłynie na hash obiektu. Jeśli klasa jest `frozen=True`, ale jakiekolwiek pole ma `hash=False`, to klasa nie będzie w stanie wygenerować swojego `__hash__` i stanie się niehaszowalna.
    ```python
    config: Dict[str, Any] = field(hash=False, default_factory=dict)
    ```

*   **`metadata`**: Słownik do przechowywania dowolnych danych związanych z polem. `dataclasses` ignorują te dane, ale mogą być używane przez zewnętrzne narzędzia (np. do walidacji, serializacji, generowania dokumentacji).
    ```python
    user_id: int = field(metadata={'help': 'Unikalny identyfikator użytkownika', 'validator': 'positive_int'})
    ```

*   **`kw_only`**: (Python 3.10+) Jeśli `True`, to konkretne pole staje się argumentem tylko-słownikowym w `__init__`. Jeśli `False`, staje się pozycyjne. Pozwala to mieszać argumenty pozycyjne i tylko-słownikowe, gdy `kw_only` klasy jest domyślnie `False`.
    ```python
    @dataclass
    class FlexibleParams:
        mandatory_pos: str # Pozycyjne
        optional_kw: int = field(default=0, kw_only=True) # Tylko-słownikowe

    fp1 = FlexibleParams("obowiązkowe", optional_kw=100)
    # fp2 = FlexibleParams("obowiązkowe", 200) # TypeError: __init__() takes 1 positional argument but 2 were given (optional_kw)
    ```

### Funkcja `fields()`: Introspekcja Dataclass

Funkcja `fields()` z modułu `dataclasses` pozwala uzyskać informacje o polach dataclass lub jej instancji. Zwraca krotkę obiektów `Field`.

```python
from dataclasses import dataclass, field, fields
from typing import List

@dataclass
class Book:
    title: str
    author: str = field(metadata={'display_name': 'Autor', 'max_length': 100})
    pages: int = field(default=0, metadata={'min_value': 1})
    tags: List[str] = field(default_factory=list, repr=False)

# Uzyskaj informacje o polach klasy Book
book_fields = fields(Book)

for f in book_fields:
    print(f"Nazwa pola: {f.name}")
    print(f"Typ pola: {f.type}")
    print(f"Wartość domyślna: {f.default}")
    print(f"Używa default_factory: {f.default_factory is not None}")
    print(f"Uwzględnione w init: {f.init}")
    print(f"Uwzględnione w repr: {f.repr}")
    print(f"Uwzględnione w compare: {f.compare}")
    print(f"Uwzględnione w hash: {f.hash}")
    print(f"Metadane: {f.metadata}")
    print(f"Tylko-słownikowe: {f.kw_only}") # Dla Pythona 3.10+
    print("-" * 20)

# Dostęp do metadanych konkretnego pola:
author_field_info = next(f for f in book_fields if f.name == 'author')
print(f"Nazwa wyświetlana dla autora: {author_field_info.metadata.get('display_name')}")
```

Obiekt `Field` ma następujące atrybuty: `name`, `type`, `default`, `default_factory`, `init`, `repr`, `hash`, `compare`, `metadata`, `kw_only`.

### Metoda `__post_init__`

Czasami potrzebujesz dodatkowej logiki po zakończeniu automatycznej inicjalizacji pól przez `__init__` dataclass. W tym celu możesz zdefiniować metodę `__post_init__`. Zostanie ona wywołana natychmiast po `__init__`.

Jest to przydatne do:
*   Walidacji danych.
*   Obliczania pól pochodnych na podstawie już zainicjalizowanych.
*   Wykonywania dowolnej innej logiki, która zależy od w pełni zainicjalizowanych pól.

```python
import datetime

@dataclass
class User:
    first_name: str
    last_name: str
    email: str = field(init=False) # To pole nie zostanie uwzględnione w parametrach __init__
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now, init=False)

    def __post_init__(self):
        print(f"--- __post_init__ rozpoczęte dla {self.first_name} {self.last_name} ---")
        # Walidacja
        if not self.first_name or not self.last_name:
            raise ValueError("Imię i nazwisko nie mogą być puste.")
        # Obliczanie pola pochodnego
        self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@example.com"
        print(f"Użytkownik {self.first_name} {self.last_name} utworzony z adresem e-mail: {self.email}")
        print(f"Czas utworzenia: {self.created_at}")
        print(f"--- __post_init__ zakończone ---")

alice_ivanova = User("Alice", "Ivanova")
print("
Obiekt utworzony:")
print(alice_ivanova)

print("
")

try:
    victor_no_last_name = User("Victor", "")
except ValueError as e:
    print(f"Błąd podczas tworzenia użytkownika: {e}")
```

### Dziedziczenie Dataclass

Dataclassy obsługują dziedziczenie. Pola z klas bazowych są uwzględniane w klasach potomnych.

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

**Cechy dziedziczenia z `slots=True`:**
*   Jeśli klasa nadrzędna używa `__slots__`, klasa potomna również musi używać `__slots__`, aby uzyskać oszczędność pamięci.
*   Klasa potomna musi zdefiniować własne `__slots__` dla swoich nowych pól.
*   Jeśli klasa potomna nie definiuje `__slots__`, będzie miała `__dict__` oprócz slotów rodzica.

### Kiedy używać Dataclass?

*   **Klasy kontenerów danych:** Gdy głównym celem klasy jest przechowywanie danych i potrzebujesz automatycznych `__init__`, `__repr__`, `__eq__`.
*   **Obiekty niezmienne:** Gdy potrzebujesz obiektów, których stan nie powinien zmieniać się po utworzeniu (`frozen=True`).
*   **Konfiguracje:** Do definiowania struktury parametrów konfiguracyjnych.
*   **Obiekty transferu danych (DTO):** Do transferu danych strukturalnych między częściami aplikacji.
*   **Prosta logika biznesowa:** Gdy metody klasy głównie operują na danych samej klasy, nie mają złożonego stanu wewnętrznego ani efektów ubocznych.

### Kiedy NIE używać Dataclass?

*   **Klasy z bogatym zachowaniem:** Gdy klasa ma złożoną logikę biznesową, wiele metod, które wchodzą w interakcje z systemami zewnętrznymi, lub złożony stan wewnętrzny, lepiej jest użyć zwykłej klasy.
*   **Modele mapowania OR (ORM):** Chociaż dataclassy mogą być częścią ORM, nie zastępują pełnoprawnych modeli ORM, które często wymagają specyficznych metod do pracy z bazą danych, leniwego ładowania itp.
*   **Polimorfizm i głęboka hierarchia dziedziczenia:** Jeśli masz złożoną hierarchię klas z głębokim polimorfizmem i nadpisywaniem zachowania, zwykłe klasy mogą być bardziej elastyczne.

### Wniosek

`dataclasses` to potężny i wygodny dodatek do Pythona, który znacznie upraszcza tworzenie klas zorientowanych na dane. Pomagają pisać czystszy, bardziej czytelny i łatwiejszy w utrzymaniu kod, a opcje takie jak `slots=True` i `kw_only=True` zapewniają dodatkowe możliwości optymalizacji wydajności i poprawy ergonomii API Twojego kodu. Nie zapomnij o `field()` do szczegółowej konfiguracji każdego pola i `fields()` do introspekcji!
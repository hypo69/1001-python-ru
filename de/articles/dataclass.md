## Dataclasses: Wenn Python auf strukturierte Daten trifft (mit neuen benannten Beispielen)

In Python müssen Sie, wenn Sie eine Klasse zum Speichern von Daten benötigen, normalerweise Boilerplate-Code für `__init__`, `__repr__`, `__eq__` und andere magische Methoden schreiben. Das Modul `dataclasses`, das in Python 3.7 eingeführt wurde, soll dieses Problem lösen, indem es einen `@dataclass`-Decorator bereitstellt, der diese Methoden automatisch für Sie generiert.

### Was ist eine Dataclass?

Eine `dataclass` ist eine Klasse, die, wie der Name schon sagt, hauptsächlich zum Speichern von Daten gedacht ist. Sie bietet die folgenden Hauptvorteile:

1.  **Weniger Boilerplate-Code:** Generiert automatisch `__init__`, `__repr__`, `__eq__`, `__hash__` (unter bestimmten Bedingungen) und andere Methoden basierend auf den Typannotationen Ihrer Felder.
2.  **Lesbarkeit:** Der Code wird prägnanter und konzentriert sich auf die Definition der Datenstruktur.
3.  **Introspektion:** Dataclass-Felder lassen sich leicht mit Funktionen aus demselben `dataclasses`-Modul introspektieren (überprüfen).
4.  **Leistung (mit `slots=True`):** Kann weniger Speicher verbrauchen und schneller auf Attribute zugreifen.

### Grundlegende Verwendung

Beginnen wir mit einem einfachen Beispiel. Angenommen, wir benötigen eine Klasse, um einen Punkt im 2D-Raum darzustellen.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

# Erstellen einer Instanz
p1 = Point(10, 20)
print(p1) # Point(x=10, y=20) - automatisch generierter __repr__

# Vergleichen von Instanzen - automatisch generierter __eq__
p2 = Point(10, 20)
p3 = Point(30, 40)
print(p1 == p2) # True
print(p1 == p3) # False
```

Wie Sie sehen, mussten wir `__init__` oder `__repr__` nicht schreiben. Alles funktionierte "out of the box".

### Parameter des `@dataclass`-Decorators

Der `@dataclass`-Decorator akzeptiert mehrere Parameter, mit denen Sie das generierte Verhalten anpassen können.

```python
@dataclass(
    init=True,         # Ob __init__ generiert werden soll (Standard True)
    repr=True,         # Ob __repr__ generiert werden soll (Standard True)
    eq=True,           # Ob __eq__ generiert werden soll (Standard True)
    order=False,       # Ob __lt__, __le__, __gt__, __ge__ generiert werden sollen (Standard False)
    unsafe_hash=False, # Ob __hash__ generiert werden soll (Standard False)
    frozen=False,      # Ob Instanzen unveränderlich gemacht werden sollen (Standard False)
    match_args=True,   # Ob die Klasse in den strukturellen Mustervergleichsmechanismus aufgenommen werden soll (Python 3.10+, Standard True)
    kw_only=False,     # Ob alle Felder nur-Schlüsselwort-Argumente in __init__ sein sollen (Python 3.10+, Standard False)
    slots=False        # Ob __slots__ zur Speichereinsparung verwendet werden sollen (Python 3.10+, Standard False)
)
class MyDataClass:
    # ...
```

Betrachten wir die wichtigsten davon, einschließlich derer, die in Ihrer Anfrage enthalten waren:

#### `init=True` (Standard)

Wenn `True`, generiert `dataclass` die `__init__`-Methode. Wenn Sie Ihre eigene `__init__` haben und `init=True` belassen, wird Ihre `__init__` aufgerufen, aber die in der Dataclass definierten Felder werden nicht automatisch darüber initialisiert. Normalerweise, wenn Sie Ihre eigene `__init__` schreiben, setzen Sie `init=False`, um Konflikte zu vermeiden und die volle Kontrolle über die Initialisierung zu haben.

```python
@dataclass(init=False)
class CustomPersonInit:
    name: str
    age: int

    def __init__(self, name: str, age: int, welcome_message: str = "Hallo!"):
        self.name = name
        self.age = age
        print(welcome_message)

alice = CustomPersonInit("Alice", 30) # Gibt "Hallo!" aus
print(alice) # CustomPersonInit(name='Alice', age=30) - repr funktioniert immer noch
```

#### `repr=True` (Standard)

Wenn `True`, generiert es eine `__repr__`-Methode, die eine bequeme Zeichenfolgendarstellung des Objekts liefert, nützlich zum Debuggen.

#### `eq=True` (Standard)

Wenn `True`, generiert es eine `__eq__`-Methode, die es Ihnen ermöglicht, zwei Instanzen einer Klasse auf Gleichheit zu vergleichen, indem die Gleichheit aller ihrer Felder überprüft wird.

#### `order=False`

Wenn `True`, generiert `dataclass` die Methoden `__lt__`, `__le__`, `__gt__`, `__ge__`. Dies ermöglicht es Ihnen, Instanzen auf "kleiner als", "größer als" usw. zu vergleichen. Der Vergleich erfolgt in der Reihenfolge, in der die Felder deklariert sind. Damit `order=True` funktioniert, muss auch `eq=True` gesetzt sein.

```python
@dataclass(order=True)
class Person:
    name: str
    age: int

alice = Person("Alice", 30)
boris = Person("Boris", 25)
victor = Person("Victor", 35) # Fügen wir Victor hinzu
galina = Person("Galina", 30)
alice_older = Person("Alice", 35)


print(f"Alice ({alice.age}) > Boris ({boris.age})? {alice > boris}") # False (da 'Alice' < 'Boris' nach Namen) -> der Vergleich erfolgt lexikographisch auf dem Tupel (Name, Alter). ('Alice', 30) < ('Boris', 25) ist True. Also wird `>` False sein.
# Erklärung: ('Alice', 30) > ('Boris', 25) -> False, weil 'Alice' < 'Boris'.
print(f"Alice ({alice.age}) < Alice_older ({alice_older.age})? {alice < alice_older}") # True (weil der Name derselbe ist, aber das Alter 30 < 35)
print(f"Galina ({galina.age}) == Alice ({alice.age})? {galina == alice}") # False (unterschiedliche Namen)
```

**Wichtiger Hinweis:** Die Reihenfolge der Felder ist wichtig für `order=True`.

#### `unsafe_hash=False`

Wenn `True`, generiert es eine `__hash__`-Methode. Dataclasses sind standardmäßig nicht hashbar, wenn sie veränderlich sind (`frozen=False`), da hashbare Objekte unveränderlich sein müssen. Wenn Sie sicher sind, dass Ihre veränderliche Dataclass nur in Kontexten verwendet wird, in denen ihr Hash nicht geändert wird (was riskant ist!), können Sie `unsafe_hash=True` setzen.
Viel häufiger wird `__hash__` automatisch generiert, wenn:
1.  `frozen=True`.
2.  `frozen=False`, aber `eq=True` und alle Felder ebenfalls hashbar sind.

```python
@dataclass(frozen=True) # Gefrorene Dataclasses sind hashbar
class ImmutablePoint:
    x: int
    y: int

p = ImmutablePoint(1, 2)
print(hash(p)) # Funktioniert

@dataclass(unsafe_hash=True) # Riskant, wenn das Objekt veränderlich ist
class MutableButHashable:
    value: int

m = MutableButHashable(5)
print(hash(m))
m.value = 10
print(hash(m)) # Der Hash hat sich geändert, was zu Problemen bei der Verwendung in einem Set/Dict führen kann
```

#### `frozen=False`

Wenn `True`, werden Instanzen der Klasse unveränderlich. Nach dem Erstellen eines Objekts können Sie die Werte seiner Felder nicht mehr ändern. Dies ist nützlich, um unveränderliche Objekte zu erstellen, die in Multithread-Anwendungen oder als Wörterbuchschlüssel (wenn sie hashbar sind) einfacher zu verwenden sind.

```python
@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

c = Coordinate(10.0, 20.0)
# c.lat = 15.0 # AttributeError: cannot assign to field 'lat'
```

#### `kw_only=False` (Python 3.10+)

Wenn `True`, werden **alle** Felder in `__init__` zu **nur-Schlüsselwort-Argumenten**. Das bedeutet, dass Sie die Werte der Felder nach Namen und nicht nach Position übergeben müssen. Dies verbessert die Lesbarkeit und verhindert Fehler, insbesondere wenn die Klasse viele Felder hat oder diese die gleichen Typen haben können.

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

# Sie können dieses Verhalten für ein bestimmtes Feld mit field(kw_only=False) überschreiben
@dataclass(kw_only=True)
class MixedConfig:
    # Obligatorisch nur-positional (nicht im Dataclass-Stil)
    # Das Feld `id` wird nicht kw_only sein, obwohl die Klasse als kw_only=True angegeben ist
    id: int = field(kw_only=False)
    name: str = field(kw_only=False)

    # Die restlichen Felder sind kw_only
    email: str
    age: int = 0

# Beachten Sie, dass id und name positional übergeben werden und email nach Namen
mixed_config = MixedConfig(123, "Boris", email="boris@example.com")
print(mixed_config)
# mixed_config_fail = MixedConfig(id=123, name="Victor", email="viktor@example.com") # Fehler, id und name wären positional
# Dieses Szenario ist weniger typisch, kw_only wird normalerweise auf die gesamte Klasse angewendet
```

**Hinweis:** `field(kw_only=False)` bei einem Feld überschreibt `kw_only=True` auf Klassenebene und macht dieses spezifische Feld positional. Am häufigsten wird jedoch `kw_only=True` für die gesamte Klasse verwendet. Der Hauptzweck von `field(kw_only=True)` ist, wenn Sie eine normale Dataclass haben (standardmäßig `kw_only=False`), aber *einige* Felder nur-Schlüsselwort-Argumente sein sollen.

#### `slots=False` (Python 3.10+)

Wenn `True`, generiert `dataclass` `__slots__` für Ihre Klasse. `__slots__` ist ein spezielles Attribut, das Python ermöglicht, eine feste Menge an Speicher für Klasseninstanzen zuzuweisen, anstatt ein dynamisches `__dict__` zum Speichern von Attributen zu verwenden.

**Vorteile von `slots=True`:**
*   **Speichereinsparungen:** Reduziert die von jeder Instanz verbrauchte Speichermenge erheblich. Dies ist besonders wichtig für Anwendungen, die Millionen von Objekten erstellen.
*   **Schnellerer Attributzugriff:** Der Zugriff auf Attribute über `__slots__` kann etwas schneller sein, da Python sie nicht in einem Wörterbuch nachschlagen muss.

**Nachteile von `slots=True`:**
*   **Kann keine neuen Attribute "on the fly" hinzufügen:** Sie können kein Attribut zuweisen, das nicht in der Dataclass (oder in den `__slots__` einer übergeordneten Klasse) deklariert wurde.
*   **Schwierigkeiten bei Mehrfachvererbung:** Es kann schwierig sein, `__slots__` mit Mehrfachvererbung zu verwenden, insbesondere wenn einige übergeordnete Klassen `__slots__` nicht verwenden oder sie anders verwenden.
*   **Hat kein `__dict__`:** Instanzen haben kein `__dict__`-Attribut, es sei denn, es wurde explizit zu `__slots__` oder einer übergeordneten Klasse hinzugefügt.

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

print(f"Größe von RegularPoint: {sys.getsizeof(rp)} Bytes")
# Ungefähr 56 Bytes unter Python 3.10+ (kann variieren)
# print(rp.__dict__) # {'x': 1, 'y': 2} - hat __dict__

print(f"Größe von SlottedPoint: {sys.getsizeof(sp)} Bytes")
# Ungefähr 32 Bytes unter Python 3.10+ (kann variieren) - deutlich kleiner
# print(sp.__dict__) # AttributeError: 'SlottedPoint' object has no attribute '__dict__'

# Versuch, ein neues Attribut zu einer slotted Dataclass hinzuzufügen
try:
    sp.z = 30
except AttributeError as e:
    print(f"Fehler beim Hinzufügen eines neuen Attributs: {e}")
```

**Wann sollte man `slots=True` verwenden?**
Wenn Sie eine sehr große Anzahl von Instanzen derselben Klasse erstellen und die Speichereinsparung Priorität hat. Dies ist eine großartige Optimierung, hat aber ihre Kompromisse.

### Die Funktion `field()`: Detaillierte Feldkonfiguration

Zusätzlich zu den Parametern auf Klassenebene können Sie jedes Feld einzeln mit der Funktion `field()` aus dem `dataclasses`-Modul konfigurieren. Dies ist besonders nützlich, wenn Sie eine komplexere Logik für Felder benötigen als nur eine Typannotation.

```python
from dataclasses import dataclass, field
from typing import List, Dict, Any
import uuid # Zum Generieren von IDs

@dataclass
class Product:
    id: str = field(default_factory=lambda: "prod-" + str(uuid.uuid4())[:8], init=False) # Nicht über __init__ initialisiert, automatisch generiert
    name: str
    price: float = field(compare=False, metadata={'unit': 'USD', 'min_value': 0.0}) # Nimmt nicht am Vergleich teil, hat Metadaten
    tags: List[str] = field(default_factory=list, repr=False) # Verwendet eine Factory für eine Liste, wird nicht in repr angezeigt
    description: str = field(default="Keine Beschreibung verfügbar") # Regulärer Standardwert
    details: Dict[str, Any] = field(default_factory=dict, hash=False) # Nimmt nicht am Hashing teil

p = Product(name="Laptop", price=1200.0, tags=["Elektronik", "Technik"])
print(p)
# Product(id='prod-...', name='Laptop', price=1200.0, description='Keine Beschreibung verfügbar', details={})
# Beachten Sie, dass 'tags' nicht in repr ist und 'id' automatisch generiert wurde.

p2 = Product(name="Laptop", price=1500.0, tags=["Elektronik", "Technik"])
print(f"p == p2? {p == p2}") # True, weil der Preis nicht am Vergleich teilnimmt (compare=False)

# p3 = Product(name="Desktop-PC", price=1000.0, details={"cpu": "Intel"})
# print(hash(p3)) # TypeError: unhashable type: 'dict' (aufgrund von details: hash=False)
# Wenn frozen=True und details nicht hash=False wären, müsste das Dict unveränderlich sein.
```

Betrachten wir die `field()`-Parameter:

*   **`default`**: Ein regulärer Standardwert für das Feld.
    ```python
    value: int = field(default=0)
    ```

*   **`default_factory`**: Eine Funktion ohne Argumente, die aufgerufen wird, um den Standardwert für das Feld zu erhalten. **Stellen Sie sicher, dass Sie `default_factory` für veränderliche Standardwerte (Listen, Wörterbücher, Objekte) verwenden, um Probleme mit gemeinsam genutztem Zustand zwischen Instanzen zu vermeiden!**
    ```python
    items: List[str] = field(default_factory=list)
    ```

*   **`init`**: Wenn `True` (Standard), wird das Feld in die generierte `__init__`-Methode aufgenommen. Wenn `False`, ist das Feld kein Argument im Konstruktor, und Sie müssen entweder einen `default` / `default_factory` dafür bereitstellen oder es in `__post_init__` initialisieren.
    ```python
    import time
    timestamp: float = field(init=False, default_factory=time.time)
    ```

*   **`repr`**: Wenn `True` (Standard), wird das Feld in die generierte `__repr__`-Methode aufgenommen. Nützlich zum Ausblenden großer oder sensibler Daten.
    ```python
    password: str = field(repr=False)
    ```

*   **`compare`**: Wenn `True` (Standard), wird das Feld in die generierten `__eq__`- und `__order__`-Methoden aufgenommen. Wenn `False`, hat es keinen Einfluss auf den Vergleich von Objekten.
    ```python
    version: str = field(compare=False)
    ```

*   **`hash`**: Wenn `True` (Standard), wird das Feld in die generierte `__hash__`-Methode aufgenommen. Wenn `False`, hat es keinen Einfluss auf den Hash des Objekts. Wenn die Klasse `frozen=True` ist, aber ein Feld `hash=False` hat, kann die Klasse ihren `__hash__` nicht generieren und wird unhashbar.
    ```python
    config: Dict[str, Any] = field(hash=False, default_factory=dict)
    ```

*   **`metadata`**: Ein Wörterbuch zum Speichern beliebiger Daten, die mit dem Feld verknüpft sind. `dataclasses` ignorieren diese Daten, aber sie können von externen Tools verwendet werden (z. B. zur Validierung, Serialisierung, Dokumentationsgenerierung).
    ```python
    user_id: int = field(metadata={'help': 'Eindeutige Benutzerkennung', 'validator': 'positive_int'})
    ```

*   **`kw_only`**: (Python 3.10+) Wenn `True`, wird dieses spezifische Feld zu einem nur-Schlüsselwort-Argument in `__init__`. Wenn `False`, wird es positional. Dies ermöglicht es Ihnen, positional und nur-Schlüsselwort-Argumente zu mischen, wenn das `kw_only` der Klasse standardmäßig `False` ist.
    ```python
    @dataclass
    class FlexibleParams:
        mandatory_pos: str # Positional
        optional_kw: int = field(default=0, kw_only=True) # Nur-Schlüsselwort

    fp1 = FlexibleParams("obligatorisch", optional_kw=100)
    # fp2 = FlexibleParams("obligatorisch", 200) # TypeError: __init__() takes 1 positional argument but 2 were given (optional_kw)
    ```

### Die Funktion `fields()`: Dataclass-Introspektion

Die Funktion `fields()` aus dem `dataclasses`-Modul ermöglicht es Ihnen, Informationen über die Felder einer Dataclass oder ihrer Instanz zu erhalten. Sie gibt ein Tupel von `Field`-Objekten zurück.

```python
from dataclasses import dataclass, field, fields
from typing import List

@dataclass
class Book:
    title: str
    author: str = field(metadata={'display_name': 'Autor', 'max_length': 100})
    pages: int = field(default=0, metadata={'min_value': 1})
    tags: List[str] = field(default_factory=list, repr=False)

# Informationen über die Felder der Book-Klasse abrufen
book_fields = fields(Book)

for f in book_fields:
    print(f"Feldname: {f.name}")
    print(f"Feldtyp: {f.type}")
    print(f"Standardwert: {f.default}")
    print(f"Verwendet default_factory: {f.default_factory is not None}")
    print(f"In init enthalten: {f.init}")
    print(f"In repr enthalten: {f.repr}")
    print(f"In compare enthalten: {f.compare}")
    print(f"In hash enthalten: {f.hash}")
    print(f"Metadaten: {f.metadata}")
    print(f"Nur-Schlüsselwort: {f.kw_only}") # Für Python 3.10+
    print("-" * 20)

# Zugriff auf die Metadaten eines bestimmten Feldes:
author_field_info = next(f for f in book_fields if f.name == 'author')
print(f"Anzeigename für Autor: {author_field_info.metadata.get('display_name')}")
```

Das `Field`-Objekt hat die folgenden Attribute: `name`, `type`, `default`, `default_factory`, `init`, `repr`, `hash`, `compare`, `metadata`, `kw_only`.

### Die `__post_init__`-Methode

Manchmal benötigen Sie zusätzliche Logik, nachdem die automatische `__init__` einer Dataclass die Felder initialisiert hat. Dafür können Sie eine `__post_init__`-Methode definieren. Sie wird sofort nach `__init__` aufgerufen.

Dies ist nützlich für:
*   Datenvalidierung.
*   Berechnung abgeleiteter Felder basierend auf bereits initialisierten.
*   Ausführung jeder anderen Logik, die von vollständig initialisierten Feldern abhängt.

```python
import datetime

@dataclass
class User:
    first_name: str
    last_name: str
    email: str = field(init=False) # Dieses Feld wird nicht in die __init__-Parameter aufgenommen
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now, init=False)

    def __post_init__(self):
        print(f"--- __post_init__ gestartet für {self.first_name} {self.last_name} ---")
        # Validierung
        if not self.first_name or not self.last_name:
            raise ValueError("Vorname und Nachname dürfen nicht leer sein.")
        # Berechnung eines abgeleiteten Feldes
        self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@example.com"
        print(f"Benutzer {self.first_name} {self.last_name} erstellt mit E-Mail: {self.email}")
        print(f"Erstellungszeit: {self.created_at}")
        print(f"--- __post_init__ beendet ---")

alice_ivanova = User("Alice", "Ivanova")
print("
Objekt erstellt:")
print(alice_ivanova)

print("
")

try:
    victor_no_last_name = User("Victor", "")
except ValueError as e:
    print(f"Fehler beim Erstellen des Benutzers: {e}")
```

### Dataclass-Vererbung

Dataclasses unterstützen Vererbung. Felder aus Basisklassen werden in Kindklassen aufgenommen.

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

**Merkmale der Vererbung mit `slots=True`:**
*   Wenn die übergeordnete Klasse `__slots__` verwendet, muss die untergeordnete Klasse ebenfalls `__slots__` verwenden, um die Speichereinsparungen zu erzielen.
*   Die untergeordnete Klasse muss ihre eigenen `__slots__` für ihre neuen Felder definieren.
*   Wenn die untergeordnete Klasse keine `__slots__` definiert, hat sie zusätzlich zu den Slots des übergeordneten Elements ein `__dict__`.

### Wann sollte man Dataclasses verwenden?

*   **Datencontainer-Klassen:** Wenn der Hauptzweck der Klasse darin besteht, Daten zu speichern, und Sie automatische `__init__`, `__repr__`, `__eq__` benötigen.
*   **Unveränderliche Objekte:** Wenn Sie Objekte benötigen, deren Zustand sich nach der Erstellung nicht ändern sollte (`frozen=True`).
*   **Konfigurationen:** Zum Definieren der Struktur von Konfigurationsparametern.
*   **Datenübertragungsobjekte (DTOs):** Zum Übertragen strukturierter Daten zwischen Teilen einer Anwendung.
*   **Einfache Geschäftslogik:** Wenn die Klassenmethoden hauptsächlich mit den Daten der Klasse selbst arbeiten, keinen komplexen internen Zustand oder Nebenwirkungen haben.

### Wann sollte man Dataclasses NICHT verwenden?

*   **Klassen mit reichem Verhalten:** Wenn eine Klasse eine komplexe Geschäftslogik, viele Methoden, die mit externen Systemen interagieren, oder einen komplexen internen Zustand hat, ist es besser, eine normale Klasse zu verwenden.
*   **OR-Mapping (ORM)-Modelle:** Obwohl Dataclasses Teil eines ORM sein können, ersetzen sie keine vollwertigen ORM-Modelle, die oft spezifische Methoden für die Arbeit mit einer Datenbank, Lazy Loading usw. erfordern.
*   **Polymorphie und tiefe Vererbungshierarchie:** Wenn Sie eine komplexe Klassenhierarchie mit tiefer Polymorphie und Verhaltensüberschreibung haben, können normale Klassen flexibler sein.

### Fazit

`dataclasses` sind eine leistungsstarke und bequeme Ergänzung zu Python, die die Erstellung datenorientierter Klassen erheblich vereinfacht. Sie helfen dabei, saubereren, lesbareren und wartbareren Code zu schreiben, und Optionen wie `slots=True` und `kw_only=True` bieten zusätzliche Möglichkeiten zur Leistungsoptimierung und Verbesserung der Ergonomie der API Ihres Codes. Vergessen Sie nicht `field()` für die detaillierte Konfiguration jedes Feldes und `fields()` für die Introspektion!
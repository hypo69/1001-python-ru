## Dataclasses: Quando Python incontra i dati strutturati (con nuovi esempi nominati)

In Python, quando hai bisogno di una classe per memorizzare dati, di solito devi scrivere codice boilerplate per `__init__`, `__repr__`, `__eq__` e altri metodi magici. Il modulo `dataclasses`, introdotto in Python 3.7, mira a risolvere questo problema fornendo un decoratore `@dataclass` che genera automaticamente questi metodi per te.

### Cos'è una Dataclass?

Una `dataclass` è una classe che, come suggerisce il nome, è principalmente destinata a memorizzare dati. Offre i seguenti vantaggi chiave:

1.  **Meno codice boilerplate:** Genera automaticamente `__init__`, `__repr__`, `__eq__`, `__hash__` (in determinate condizioni) e altri metodi basati sulle annotazioni di tipo dei tuoi campi.
2.  **Leggibilità:** Il codice diventa più conciso e focalizzato sulla definizione della struttura dei dati.
3.  **Introspezione:** I campi Dataclass sono facili da introspezionare (controllare) usando le funzioni dello stesso modulo `dataclasses`.
4.  **Prestazioni (con `slots=True`):** Può consumare meno memoria ed essere più veloce nell'accesso agli attributi.

### Utilizzo di base

Cominciamo con un semplice esempio. Supponiamo di aver bisogno di una classe per rappresentare un punto nello spazio 2D.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

# Creazione di un'istanza
p1 = Point(10, 20)
print(p1) # Point(x=10, y=20) - __repr__ generato automaticamente

# Confronto di istanze - __eq__ generato automaticamente
p2 = Point(10, 20)
p3 = Point(30, 40)
print(p1 == p2) # True
print(p1 == p3) # False
```

Come puoi vedere, non abbiamo dovuto scrivere `__init__` o `__repr__`. Tutto ha funzionato "out of the box".

### Parametri del decoratore `@dataclass`

Il decoratore `@dataclass` accetta diversi parametri che ti consentono di personalizzare il comportamento generato.

```python
@dataclass(
    init=True,         # Se generare __init__ (predefinito True)
    repr=True,         # Se generare __repr__ (predefinito True)
    eq=True,           # Se generare __eq__ (predefinito True)
    order=False,       # Se generare __lt__, __le__, __gt__, __ge__ (predefinito False)
    unsafe_hash=False, # Se generare __hash__ (predefinito False)
    frozen=False,      # Se rendere le istanze immutabili (predefinito False)
    match_args=True,   # Se includere la classe nel meccanismo di corrispondenza di pattern strutturali (Python 3.10+, predefinito True)
    kw_only=False,     # Se rendere tutti i campi argomenti solo-keyword in __init__ (Python 3.10+, predefinito False)
    slots=False        # Se usare __slots__ per risparmiare memoria (Python 3.10+, predefinito False)
)
class MyDataClass:
    # ...
```

Consideriamo i più importanti, inclusi quelli che erano nella tua richiesta:

#### `init=True` (Predefinito)

Se `True`, allora `dataclass` genererà il metodo `__init__`. Se hai il tuo `__init__`, e lasci `init=True`, allora il tuo `__init__` verrà chiamato, ma i campi definiti nella dataclass non verranno inizializzati automaticamente tramite esso. Di solito, se scrivi il tuo `__init__`, imposti `init=False` per evitare conflitti e avere il controllo completo sull'inizializzazione.

```python
@dataclass(init=False)
class CustomPersonInit:
    name: str
    age: int

    def __init__(self, name: str, age: int, welcome_message: str = "Ciao!"):
        self.name = name
        self.age = age
        print(welcome_message)

alice = CustomPersonInit("Alice", 30) # Stampa "Ciao!"
print(alice) # CustomPersonInit(name='Alice', age=30) - repr funziona ancora
```

#### `repr=True` (Predefinito)

Se `True`, genererà un metodo `__repr__` che fornisce una comoda rappresentazione stringa dell'oggetto, utile per il debug.

#### `eq=True` (Predefinito)

Se `True`, genererà un metodo `__eq__` che ti consente di confrontare due istanze di una classe per l'uguaglianza controllando l'uguaglianza di tutti i loro campi.

#### `order=False`

Se `True`, allora `dataclass` genererà i metodi `__lt__`, `__le__`, `__gt__`, `__ge__`. Questo ti consente di confrontare le istanze per "minore di", "maggiore di", ecc. Il confronto viene eseguito nell'ordine in cui i campi sono dichiarati. Affinché `order=True` funzioni, `eq=True` deve essere impostato.

```python
@dataclass(order=True)
class Person:
    name: str
    age: int

alice = Person("Alice", 30)
boris = Person("Boris", 25)
victor = Person("Victor", 35) # Aggiungiamo Victor
galina = Person("Galina", 30)
alice_older = Person("Alice", 35)


print(f"Alice ({alice.age}) > Boris ({boris.age})? {alice > boris}") # False (poiché 'Alice' < 'Boris' per nome) -> il confronto viene eseguito lessicograficamente sulla tupla (nome, età). ('Alice', 30) < ('Boris', 25) è True. Quindi `>` sarà False.
# Spiegazione: ('Alice', 30) > ('Boris', 25) -> False, perché 'Alice' < 'Boris'.
print(f"Alice ({alice.age}) < Alice_older ({alice_older.age})? {alice < alice_older}") # True (perché il nome è lo stesso, ma l'età 30 < 35)
print(f"Galina ({galina.age}) == Alice ({alice.age})? {galina == alice}") # False (nomi diversi)
```

**Nota importante:** L'ordine dei campi è importante per `order=True`.

#### `unsafe_hash=False`

Se `True`, genererà un metodo `__hash__`. Le dataclass non sono hashable per impostazione predefinita se sono mutabili (`frozen=False`), perché gli oggetti hashable devono essere immutabili. Se sei sicuro che la tua dataclass mutabile verrà utilizzata solo in contesti in cui il suo hash non cambierà (il che è rischioso!), puoi impostare `unsafe_hash=True`.
Molto più spesso, `__hash__` viene generato automaticamente se:
1.  `frozen=True`.
2.  `frozen=False`, ma `eq=True` e tutti i campi sono anche hashable.

```python
@dataclass(frozen=True) # Le dataclass congelate sono hashable
class ImmutablePoint:
    x: int
    y: int

p = ImmutablePoint(1, 2)
print(hash(p)) # Funziona

@dataclass(unsafe_hash=True) # Rischioso se l'oggetto è mutabile
class MutableButHashable:
    value: int

m = MutableButHashable(5)
print(hash(m))
m.value = 10
print(hash(m)) # L'hash è cambiato, il che può portare a problemi quando usato in un set/dict
```

#### `frozen=False`

Se `True`, le istanze della classe diventano immutabili. Dopo aver creato un oggetto, non sarai in grado di modificare i valori dei suoi campi. Questo è utile per creare oggetti immutabili che sono più facili da usare in applicazioni multi-thread o come chiavi di dizionario (se sono hashable).

```python
@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

c = Coordinate(10.0, 20.0)
# c.lat = 15.0 # AttributeError: cannot assign to field 'lat'
```

#### `kw_only=False` (Python 3.10+)

Se `True`, **tutti** i campi in `__init__` diventano argomenti **solo-keyword**. Ciò significa che devi passare i valori dei campi per nome, non per posizione. Questo migliora la leggibilità e previene errori, soprattutto quando la classe ha molti campi o possono avere gli stessi tipi.

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

# Puoi sovrascrivere questo comportamento per un campo specifico usando field(kw_only=False)
@dataclass(kw_only=True)
class MixedConfig:
    # Obbligatorio solo posizionale (non stile dataclass)
    # Il campo `id` non sarà kw_only, anche se la classe è specificata come kw_only=True
    id: int = field(kw_only=False)
    name: str = field(kw_only=False)

    # I campi rimanenti sono kw_only
    email: str
    age: int = 0

# Nota che id e name vengono passati posizionalmente, e l'email viene passata per nome
mixed_config = MixedConfig(123, "Boris", email="boris@example.com")
print(mixed_config)
# mixed_config_fail = MixedConfig(id=123, name="Victor", email="viktor@example.com") # Errore, id e name sarebbero posizionali
# Questo scenario è meno tipico, kw_only è solitamente applicato all'intera classe
```

**Nota:** `field(kw_only=False)` su un campo sovrascrive `kw_only=True` a livello di classe, rendendo quel campo specifico posizionale. Tuttavia, il più delle volte, `kw_only=True` viene utilizzato per l'intera classe. L'uso principale di `field(kw_only=True)` è quando hai una dataclass normale (`kw_only=False` per impostazione predefinita), ma vuoi rendere *alcuni* campi solo-keyword.

#### `slots=False` (Python 3.10+)

Se `True`, `dataclass` genererà `__slots__` per la tua classe. `__slots__` è un attributo speciale che consente a Python di allocare una quantità fissa di memoria per le istanze di classe, invece di utilizzare un `__dict__` dinamico per memorizzare gli attributi.

**Vantaggi di `slots=True`:**
*   **Risparmio di memoria:** Riduce significativamente la quantità di memoria consumata da ogni istanza. Questo è particolarmente importante per le applicazioni che creano milioni di oggetti.
*   **Accesso più rapido agli attributi:** L'accesso agli attributi tramite `__slots__` può essere leggermente più veloce, poiché Python non ha bisogno di cercarli in un dizionario.

**Svantaggi di `slots=True`:**
*   **Impossibile aggiungere nuovi attributi "al volo":** Non sarai in grado di assegnare un attributo che non è stato dichiarato nella dataclass (o negli `__slots__` di una classe padre).
*   **Difficoltà con l'ereditarietà multipla:** Può essere difficile usare `__slots__` con l'ereditarietà multipla, soprattutto se alcune classi padre non usano `__slots__` o li usano in modo diverso.
*   **Non ha `__dict__`:** Le istanze non avranno un attributo `__dict__` a meno che non sia stato esplicitamente aggiunto a `__slots__` o a una classe padre.

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

print(f"Dimensione di RegularPoint: {sys.getsizeof(rp)} byte")
# Circa 56 byte su Python 3.10+ (può variare)
# print(rp.__dict__) # {'x': 1, 'y': 2} - ha __dict__

print(f"Dimensione di SlottedPoint: {sys.getsizeof(sp)} byte")
# Circa 32 byte su Python 3.10+ (può variare) - significativamente più piccolo
# print(sp.__dict__) # AttributeError: 'SlottedPoint' object has no attribute '__dict__'

# Tentativo di aggiungere un nuovo attributo a una dataclass con slot
try:
    sp.z = 30
except AttributeError as e:
    print(f"Errore durante l'aggiunta di un nuovo attributo: {e}")
```

**Quando usare `slots=True`?**
Quando stai creando un numero molto elevato di istanze della stessa classe, e il risparmio di memoria è una priorità. Questa è un'ottima ottimizzazione, ma ha i suoi compromessi.

### La funzione `field()`: Configurazione dettagliata del campo

Oltre ai parametri a livello di classe, puoi configurare ogni campo individualmente usando la funzione `field()` del modulo `dataclasses`. Questo è particolarmente utile quando hai bisogno di una logica più complessa per i campi rispetto a una semplice annotazione di tipo.

```python
from dataclasses import dataclass, field
from typing import List, Dict, Any
import uuid # Per generare ID

@dataclass
class Product:
    id: str = field(default_factory=lambda: "prod-" + str(uuid.uuid4())[:8], init=False) # Non inizializzato tramite __init__, generato automaticamente
    name: str
    price: float = field(compare=False, metadata={'unit': 'USD', 'min_value': 0.0}) # Non partecipa al confronto, ha metadati
    tags: List[str] = field(default_factory=list, repr=False) # Usa una factory per una lista, non visualizzata in repr
    description: str = field(default="Nessuna descrizione disponibile") # Valore predefinito normale
    details: Dict[str, Any] = field(default_factory=dict, hash=False) # Non partecipa all'hashing

p = Product(name="Laptop", price=1200.0, tags=["elettronica", "tech"])
print(p)
# Product(id='prod-...', name='Laptop', price=1200.0, description='Nessuna descrizione disponibile', details={})
# Nota che 'tags' non è in repr, e 'id' è stato generato automaticamente.

p2 = Product(name="Laptop", price=1500.0, tags=["elettronica", "tech"])
print(f"p == p2? {p == p2}") # True, perché il prezzo non partecipa al confronto (compare=False)

# p3 = Product(name="Desktop PC", price=1000.0, details={"cpu": "Intel"})
# print(hash(p3)) # TypeError: unhashable type: 'dict' (a causa di details: hash=False)
# Se frozen=True, e details non fossero hash=False, allora il dict dovrebbe essere immutabile.
```

Consideriamo i parametri di `field()`:

*   **`default`**: Un valore predefinito normale per il campo.
    ```python
    value: int = field(default=0)
    ```

*   **`default_factory`**: Una funzione senza argomenti che verrà chiamata per ottenere il valore predefinito per il campo. **Assicurati di usare `default_factory` per i valori predefiniti mutabili (liste, dizionari, oggetti) per evitare problemi di stato condiviso tra le istanze!**
    ```python
    items: List[str] = field(default_factory=list)
    ```

*   **`init`**: Se `True` (predefinito), il campo verrà incluso nel metodo `__init__` generato. Se `False`, il campo non sarà un argomento nel costruttore, e devi fornire un `default` / `default_factory` per esso, o inizializzarlo in `__post_init__`.
    ```python
    import time
    timestamp: float = field(init=False, default_factory=time.time)
    ```

*   **`repr`**: Se `True` (predefinito), il campo verrà incluso nel metodo `__repr__` generato. Utile per nascondere dati grandi o sensibili.
    ```python
    password: str = field(repr=False)
    ```

*   **`compare`**: Se `True` (predefinito), il campo verrà incluso nei metodi `__eq__` e `__order__` generati. Se `False`, non influirà sul confronto degli oggetti.
    ```python
    version: str = field(compare=False)
    ```

*   **`hash`**: Se `True` (predefinito), il campo verrà incluso nel metodo `__hash__` generato. Se `False`, non influirà sull'hash dell'oggetto. Se la classe è `frozen=True`, ma un campo ha `hash=False`, allora la classe non sarà in grado di generare il suo `__hash__` e diventerà non hashable.
    ```python
    config: Dict[str, Any] = field(hash=False, default_factory=dict)
    ```

*   **`metadata`**: Un dizionario per memorizzare dati arbitrari associati al campo. `dataclasses` ignorano questi dati, ma possono essere utilizzati da strumenti esterni (ad esempio, per la validazione, la serializzazione, la generazione di documentazione).
    ```python
    user_id: int = field(metadata={'help': 'Identificatore utente unico', 'validator': 'positive_int'})
    ```

*   **`kw_only`**: (Python 3.10+) Se `True`, questo campo specifico diventa un argomento solo-keyword in `__init__`. Se `False`, diventa posizionale. Questo ti consente di mescolare argomenti posizionali e solo-keyword quando il `kw_only` della classe è `False` per impostazione predefinita.
    ```python
    @dataclass
    class FlexibleParams:
        mandatory_pos: str # Posizionale
        optional_kw: int = field(default=0, kw_only=True) # Solo-keyword

    fp1 = FlexibleParams("obbligatorio", optional_kw=100)
    # fp2 = FlexibleParams("obbligatorio", 200) # TypeError: __init__() takes 1 positional argument but 2 were given (optional_kw)
    ```

### La funzione `fields()`: Introspezione Dataclass

La funzione `fields()` del modulo `dataclasses` ti consente di ottenere informazioni sui campi di una dataclass o della sua istanza. Restituisce una tupla di oggetti `Field`.

```python
from dataclasses import dataclass, field, fields
from typing import List

@dataclass
class Book:
    title: str
    author: str = field(metadata={'display_name': 'Autore', 'max_length': 100})
    pages: int = field(default=0, metadata={'min_value': 1})
    tags: List[str] = field(default_factory=list, repr=False)

# Ottieni informazioni sui campi della classe Book
book_fields = fields(Book)

for f in book_fields:
    print(f"Nome del campo: {f.name}")
    print(f"Tipo del campo: {f.type}")
    print(f"Valore predefinito: {f.default}")
    print(f"Usa default_factory: {f.default_factory is not None}")
    print(f"Incluso in init: {f.init}")
    print(f"Incluso in repr: {f.repr}")
    print(f"Incluso in compare: {f.compare}")
    print(f"Incluso in hash: {f.hash}")
    print(f"Metadati: {f.metadata}")
    print(f"Solo-keyword: {f.kw_only}") # Per Python 3.10+
    print("-" * 20)

# Accedi ai metadati di un campo specifico:
author_field_info = next(f for f in book_fields if f.name == 'author')
print(f"Nome visualizzato per l'autore: {author_field_info.metadata.get('display_name')}")
```

L'oggetto `Field` ha i seguenti attributi: `name`, `type`, `default`, `default_factory`, `init`, `repr`, `hash`, `compare`, `metadata`, `kw_only`.

### Il metodo `__post_init__`

A volte hai bisogno di logica aggiuntiva dopo che l'`__init__` automatico di una dataclass ha finito di inizializzare i campi. Per questo, puoi definire un metodo `__post_init__`. Verrà chiamato immediatamente dopo `__init__`.

Questo è utile per:
*   Validazione dei dati.
*   Calcolo di campi derivati basati su quelli già inizializzati.
*   Esecuzione di qualsiasi altra logica che dipende da campi completamente inizializzati.

```python
import datetime

@dataclass
class User:
    first_name: str
    last_name: str
    email: str = field(init=False) # Questo campo non sarà incluso nei parametri __init__
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now, init=False)

    def __post_init__(self):
        print(f"--- __post_init__ avviato per {self.first_name} {self.last_name} ---")
        # Validazione
        if not self.first_name or not self.last_name:
            raise ValueError("Nome e cognome non possono essere vuoti.")
        # Calcolo di un campo derivato
        self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@example.com"
        print(f"Utente {self.first_name} {self.last_name} creato con email: {self.email}")
        print(f"Ora di creazione: {self.created_at}")
        print(f"--- __post_init__ terminato ---")

alice_ivanova = User("Alice", "Ivanova")
print("
Oggetto creato:")
print(alice_ivanova)

print("
")

try:
    victor_no_last_name = User("Victor", "")
except ValueError as e:
    print(f"Errore durante la creazione dell'utente: {e}")
```

### Ereditarietà Dataclass

Le dataclass supportano l'ereditarietà. I campi delle classi base sono inclusi nelle classi figlie.

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

**Caratteristiche dell'ereditarietà con `slots=True`:**
*   Se la classe padre usa `__slots__`, la classe figlia deve anche usare `__slots__` per ottenere il risparmio di memoria.
*   La classe figlia deve definire i propri `__slots__` per i suoi nuovi campi.
*   Se la classe figlia non definisce `__slots__`, avrà un `__dict__` oltre agli slot del padre.

### Quando usare le Dataclass?

*   **Classi contenitore di dati:** Quando lo scopo principale della classe è memorizzare dati, e hai bisogno di `__init__`, `__repr__`, `__eq__` automatici.
*   **Oggetti immutabili:** Quando hai bisogno di oggetti il cui stato non dovrebbe cambiare dopo la creazione (`frozen=True`).
*   **Configurazioni:** Per definire la struttura dei parametri di configurazione.
*   **Oggetti di trasferimento dati (DTO):** Per trasferire dati strutturati tra parti di un'applicazione.
*   **Logica di business semplice:** Quando i metodi della classe operano principalmente sui dati della classe stessa, non hanno uno stato interno complesso o effetti collaterali.

### Quando NON usare le Dataclass?

*   **Classi con comportamento ricco:** Quando una classe ha una logica di business complessa, molti metodi che interagiscono con sistemi esterni, o uno stato interno complesso, è meglio usare una classe normale.
*   **Modelli OR-mapping (ORM):** Anche se le dataclass possono essere parte di un ORM, non sostituiscono i modelli ORM completi, che spesso richiedono metodi specifici per lavorare con un database, caricamento pigro, ecc.
*   **Polimorfismo e gerarchia di ereditarietà profonda:** Se hai una gerarchia di classi complessa con polimorfismo profondo e override del comportamento, le classi normali possono essere più flessibili.

### Conclusione

Le `dataclass` sono un'aggiunta potente e conveniente a Python che semplifica notevolmente la creazione di classi orientate ai dati. Aiutano a scrivere codice più pulito, leggibile e manutenibile, e opzioni come `slots=True` e `kw_only=True` offrono opportunità aggiuntive per l'ottimizzazione delle prestazioni e il miglioramento dell'ergonomia dell'API del tuo codice. Non dimenticare `field()` per la configurazione dettagliata di ogni campo e `fields()` per l'introspezione!
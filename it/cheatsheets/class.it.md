# Classi in `python`

Le classi sono uno dei meccanismi fondamentali della programmazione orientata agli oggetti (OOP) in Python. Una classe può essere pensata come un "modello" o un "progetto" per la creazione di oggetti che hanno attributi (dati) e metodi (funzioni). Gli oggetti creati da una classe sono chiamati istanze della classe. Le classi consentono di strutturare il codice, migliorarne il riutilizzo e facilitarne la manutenzione.

### Struttura di una classe

```python
class ClassName:
    # Attributi della classe
    def __init__(self, param1, param2):
        # Costruttore (inizializzatore) della classe
        self.param1 = param1
        self.param2 = param2

    # Metodi della classe
    def method(self):
        return f'{self.param1} e {self.param2}'
```

1.  **Costruttore** (`__init__`):
    Il costruttore `__init__` è un metodo speciale che viene automaticamente chiamato quando viene creato un nuovo oggetto. Viene utilizzato per inizializzare gli attributi dell'oggetto.

    -   `self`: un parametro che è un riferimento all'istanza corrente della classe. In Python, è obbligatorio passarlo come primo parametro in tutti i metodi della classe (non viene passato quando il metodo viene chiamato).
    -   Attributi come `param1` e `param2` vengono assegnati all'oggetto tramite `self`. Questi attributi possono quindi essere utilizzati da altri metodi della classe.

2.  **Attributi della classe**:
    Gli attributi sono variabili che appartengono agli oggetti di questa classe. Sono definiti all'interno del costruttore (`__init__`) e possono essere accessibili tramite un riferimento all'oggetto.

3.  **Metodi della classe**:
    I metodi sono funzioni che possono manipolare gli attributi dell'oggetto. I metodi possono utilizzare i dati dell'oggetto, modificarli o eseguire altre operazioni.

### Creazione di un oggetto classe

Una volta definita una classe, è possibile creare oggetti di quella classe. Gli oggetti sono istanze della classe.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f'{self.year} {self.make} {self.model}'

# Creazione di un oggetto
my_car = Car('Toyota', 'Corolla', 2020)
print(my_car.description())  # Output: 2020 Toyota Corolla
```

-   In questo esempio, abbiamo creato un oggetto `my_car` della classe `Car`. Quando l'oggetto viene creato, vengono passati i valori per gli attributi `make`, `model` e `year`, che vengono memorizzati nell'oggetto.
-   Il metodo `description()` consente di ottenere una rappresentazione stringa dell'auto.

### Tipi di metodi

1.  **Metodi di istanza**: Sono metodi ordinari che operano sulle istanze della classe. Accettano un riferimento all'oggetto come primo parametro (solitamente `self`).

    Esempio:
    ```python
    def method(self):
        pass
    ```

2.  **Metodi di classe**: Metodi che accettano la classe stessa come primo parametro. Per definire tali metodi, viene utilizzato il decoratore `@classmethod`. Possono modificare lo stato della classe stessa, non solo delle sue singole istanze.

    Esempio:
    ```python
    class MyClass:
        @classmethod
        def class_method(cls):
            pass
    ```

3.  **Metodi statici**: Sono metodi che non utilizzano `self` o `cls` (cioè non hanno accesso né all'istanza né alla classe). I metodi statici sono dichiarati utilizzando il decoratore `@staticmethod`. Possono essere utili quando un metodo non dipende dallo stato dell'oggetto o della classe, ma è correlato alla logica che appartiene alla classe.

    Esempio:
    ```python
    class MyClass:
        @staticmethod
        def static_method():
            pass
    ```

### Ereditarietà

Uno dei principi chiave dell'OOP è l'**ereditarietà**. Una classe può ereditare il comportamento di un'altra classe, estendendone o modificandone la funzionalità. Ciò consente il riutilizzo del codice, evitando la duplicazione.

```python
class Animal:
    def speak(self):
        return 'Voce di animale'

class Dog(Animal):  # La classe Dog eredita dalla classe Animal
    def speak(self):
        return 'Bau'

# Creazione di oggetti
dog = Dog()
print(dog.speak())  # Output: Bau
```

-   La classe `Dog` eredita il metodo `speak` dalla classe `Animal`, ma lo sovrascrive per restituire la stringa `'Bau'`.

### Polimorfismo

Il **polimorfismo** significa la capacità di oggetti di classi diverse di utilizzare gli stessi metodi con implementazioni diverse. In Python, questo è possibile grazie all'ereditarietà e alla sovrascrittura dei metodi.

```python
class Cat(Animal):
    def speak(self):
        return 'Miao'

# Creazione di oggetti
cat = Cat()
print(cat.speak())  # Output: Miao
```

Qui `Cat` sovrascrive anche il metodo `speak`, ma restituisce un valore diverso. Ciò consente di chiamare il metodo `speak` indipendentemente dal tipo di oggetto.

### Incapsulamento

L'**incapsulamento** consente di nascondere i dettagli interni dell'implementazione e di fornire accesso ai dati tramite metodi pubblici. Ciò aiuta a prevenire l'uso improprio dei dati.

```python
class Car:
    def __init__(self, make, model):
        self._make = make  # Attributo protetto
        self._model = model

    def get_make(self):
        return self._make

    def set_make(self, make):
        self._make = make

# Creazione di un oggetto
my_car = Car('Toyota', 'Corolla')
print(my_car.get_make())  # Output: Toyota
my_car.set_make('Honda')
print(my_car.get_make())  # Output: Honda
```

Qui gli attributi `_make` e `_model` sono protetti (in Python, un underscore di solito significa che questi attributi non dovrebbero essere usati direttamente al di fuori della classe), ma possono essere acceduti e modificati tramite i metodi `get_make` e `set_make`.

### Altre caratteristiche delle classi

1.  **Distruttore** (`__del__`):
    Un metodo speciale che viene chiamato quando un oggetto viene distrutto (ad esempio, quando esce dall'ambito). Può essere utilizzato per pulire le risorse.

    Esempio:
    ```python
    class MyClass:
        def __del__(self):
            print("Oggetto distrutto")

    obj = MyClass()
    del obj  # L'oggetto verrà distrutto e verrà chiamato il metodo __del__
    ```

2.  **Metodi magici**:
    Sono metodi speciali con due underscore (ad esempio, `__init__`, `__str__`, `__repr__`, `__eq__`). Consentono di sovrascrivere il comportamento standard di operazioni come la creazione di oggetti, il confronto, la rappresentazione stringa degli oggetti, ecc.

    Esempio:
    ```python
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f'Point({self.x}, {self.y})'

    p = Point(3, 4)
    print(p)  # Output: Point(3, 4)
    ```

---

[Al sommario](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)

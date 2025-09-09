# Klassen in `python`

Klassen sind einer der grundlegenden Mechanismen der objektorientierten Programmierung (OOP) in Python. Eine Klasse kann als "Vorlage" oder "Blaupause" für die Erstellung von Objekten betrachtet werden, die Attribute (Daten) und Methoden (Funktionen) besitzen. Objekte, die auf der Grundlage einer Klasse erstellt werden, werden als Instanzen der Klasse bezeichnet. Klassen ermöglichen es, Code zu strukturieren, seine Wiederverwendbarkeit zu verbessern und seine Wartung zu erleichtern.

### Struktur einer Klasse

```python
class ClassName:
    # Klassenattribute
    def __init__(self, param1, param2):
        # Konstruktor (Initialisierer) der Klasse
        self.param1 = param1
        self.param2 = param2

    # Klassenmethoden
    def method(self):
        return f'{self.param1} und {self.param2}'
```

1.  **Konstruktor** (`__init__`):
    Der Konstruktor `__init__` ist eine spezielle Methode, die automatisch aufgerufen wird, wenn ein neues Objekt erstellt wird. Er wird zur Initialisierung der Objektattribute verwendet.

    -   `self`: Ein Parameter, der eine Referenz auf die aktuelle Instanz der Klasse ist. In Python muss er obligatorisch als erster Parameter in allen Klassenmethoden übergeben werden (er wird beim Methodenaufruf nicht übergeben).
    -   Attribute wie `param1` und `param2` werden dem Objekt über `self` zugewiesen. Diese Attribute können dann von anderen Methoden der Klasse verwendet werden.

2.  **Klassenattribute**:
    Attribute sind Variablen, die zu Objekten dieser Klasse gehören. Sie werden innerhalb des Konstruktors (`__init__`) definiert und können über eine Objektreferenz aufgerufen werden.

3.  **Klassenmethoden**:
    Methoden sind Funktionen, die die Attribute eines Objekts manipulieren können. Methoden können Objektdaten verwenden, ändern oder andere Operationen ausführen.

### Erstellen eines Klassenobjekts

Sobald eine Klasse definiert ist, können Objekte dieser Klasse erstellt werden. Objekte sind Instanzen der Klasse.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f'{self.year} {self.make} {self.model}'

# Erstellen eines Objekts
my_car = Car('Toyota', 'Corolla', 2020)
print(my_car.description())  # Ausgabe: 2020 Toyota Corolla
```

-   In diesem Beispiel haben wir ein Objekt `my_car` der Klasse `Car` erstellt. Beim Erstellen des Objekts werden Werte für die Attribute `make`, `model` und `year` übergeben, die im Objekt gespeichert werden.
-   Die Methode `description()` liefert eine String-Darstellung des Autos.

### Methodentypen

1.  **Instanzmethoden**: Dies sind reguläre Methoden, die auf Instanzen der Klasse wirken. Sie akzeptieren eine Objektreferenz als ersten Parameter (normalerweise `self`).

    Beispiel:
    ```python
    def method(self):
        pass
    ```

2.  **Klassenmethoden**: Methoden, die die Klasse selbst als ersten Parameter akzeptieren. Für die Definition solcher Methoden wird der Dekorator `@classmethod` verwendet. Sie können den Zustand der Klasse selbst ändern, nicht nur einzelne Instanzen.

    Beispiel:
    ```python
    class MyClass:
        @classmethod
        def class_method(cls):
            pass
    ```

3.  **Statische Methoden**: Dies sind Methoden, die weder `self` noch `cls` verwenden (d.h. sie haben keinen Zugriff auf die Instanz oder die Klasse). Statische Methoden werden mit dem Dekorator `@staticmethod` deklariert. Sie können nützlich sein, wenn eine Methode nicht vom Zustand des Objekts oder der Klasse abhängt, aber mit der Logik der Klasse verbunden ist.

    Beispiel:
    ```python
    class MyClass:
        @staticmethod
        def static_method():
            pass
    ```

### Vererbung

Eines der Schlüsselprinzipien der OOP ist die **Vererbung**. Eine Klasse kann das Verhalten einer anderen Klasse erben, indem sie deren Funktionalität erweitert oder ändert. Dies ermöglicht die Wiederverwendung von Code und vermeidet Duplizierung.

```python
class Animal:
    def speak(self):
        return 'Tierstimme'

class Dog(Animal):  # Klasse Dog erbt von Klasse Animal
    def speak(self):
        return 'Wuff'

# Erstellen von Objekten
dog = Dog()
print(dog.speak())  # Ausgabe: Wuff
```

-   Die Klasse `Dog` erbt die Methode `speak` von der Klasse `Animal`, überschreibt sie jedoch, um den String `'Wuff'` zurückzugeben.

### Polymorphie

**Polymorphie** bedeutet die Fähigkeit von Objekten verschiedener Klassen, dieselben Methoden mit unterschiedlicher Implementierung zu verwenden. In Python ist dies durch Vererbung und Methodenüberschreibung möglich.

```python
class Cat(Animal):
    def speak(self):
        return 'Miau'

# Erstellen von Objekten
cat = Cat()
print(cat.speak())  # Ausgabe: Miau
```

Hier überschreibt `Cat` ebenfalls die Methode `speak`, gibt aber einen anderen Wert zurück. Dies ermöglicht es, die Methode `speak` unabhängig vom Objekttyp aufzurufen.

### Kapselung

**Kapselung** ermöglicht es, interne Implementierungsdetails zu verbergen und den Zugriff auf Daten über öffentliche Methoden bereitzustellen. Dies hilft, die falsche Verwendung von Daten zu verhindern.

```python
class Car:
    def __init__(self, make, model):
        self._make = make  # Geschütztes Attribut
        self._model = model

    def get_make(self):
        return self._make

    def set_make(self, make):
        self._make = make

# Erstellen eines Objekts
my_car = Car('Toyota', 'Corolla')
print(my_car.get_make())  # Ausgabe: Toyota
my_car.set_make('Honda')
print(my_car.get_make())  # Ausgabe: Honda
```

Hier sind die Attribute `_make` und `_model` geschützt (normalerweise bedeutet ein Unterstrich in Python, dass diese Attribute nicht direkt außerhalb der Klasse verwendet werden sollten), aber der Zugriff und die Änderung sind über die Methoden `get_make` und `set_make` möglich.

### Weitere Merkmale von Klassen

1.  **Destruktor** (`__del__`):
    Eine spezielle Methode, die aufgerufen wird, wenn ein Objekt zerstört wird (z.B. wenn es den Gültigkeitsbereich verlässt). Sie kann zur Freigabe von Ressourcen verwendet werden.

    Beispiel:
    ```python
    class MyClass:
        def __del__(self):
            print("Objekt zerstört")

    obj = MyClass()
    del obj  # Das Objekt wird zerstört und die Methode __del__ wird aufgerufen
    ```

2.  **Magische Methoden**:
    Dies sind spezielle Methoden mit zwei Unterstrichen (z.B. `__init__`, `__str__`, `__repr__`, `__eq__`). Sie ermöglichen es, das Standardverhalten von Operationen wie Objekterstellung, Vergleich, String-Darstellung von Objekten usw. zu überschreiben.

    Beispiel:
    ```python
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f'Point({self.x}, {self.y})'

    p = Point(3, 4)
    print(p)  # Ausgabe: Point(3, 4)
    ```

---

[Zum Inhaltsverzeichnis](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)

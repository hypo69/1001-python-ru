# Klasy w `python`

Klasy to jeden z podstawowych mechanizmów programowania obiektowego (OOP) w Pythonie. Klasę można sobie wyobrazić jako "szablon" lub "projekt" do tworzenia obiektów, które posiadają atrybuty (dane) i metody (funkcje). Obiekty stworzone na podstawie klasy nazywane są instancjami klasy. Klasy pozwalają na strukturyzowanie kodu, poprawę jego ponownego użycia i ułatwienie jego utrzymania.

### Struktura klasy

```python
class ClassName:
    # Atrybuty klasy
    def __init__(self, param1, param2):
        # Konstruktor (inicjalizator) klasy
        self.param1 = param1
        self.param2 = param2

    # Metody klasy
    def method(self):
        return f'{self.param1} i {self.param2}'
```

1.  **Konstruktor** (`__init__`):
    Konstruktor `__init__` to specjalna metoda, która jest automatycznie wywoływana podczas tworzenia nowego obiektu. Służy do inicjalizacji atrybutów obiektu.

    -   `self`: parametr, który jest odwołaniem do bieżącej instancji klasy. W Pythonie musi być przekazywany jako pierwszy parametr we wszystkich metodach klasy (nie jest przekazywany podczas wywoływania metody).
    -   Atrybuty, takie jak `param1` i `param2`, są przypisywane do obiektu za pomocą `self`. Atrybuty te mogą być następnie używane przez inne metody klasy.

2.  **Atrybuty klasy**:
    Atrybuty to zmienne, które należą do obiektów tej klasy. Są one definiowane wewnątrz konstruktora (`__init__`) i mogą być dostępne za pomocą odwołania do obiektu.

3.  **Metody klasy**:
    Metody to funkcje, które mogą manipulować atrybutami obiektu. Metody mogą używać danych obiektu, zmieniać je lub wykonywać inne operacje.

### Tworzenie obiektu klasy

Gdy klasa jest zdefiniowana, można tworzyć obiekty tej klasy. Obiekty są instancjami klasy.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f'{self.year} {self.make} {self.model}'

# Tworzenie obiektu
my_car = Car('Toyota', 'Corolla', 2020)
print(my_car.description())  # Wyjście: 2020 Toyota Corolla
```

-   W tym przykładzie stworzyliśmy obiekt `my_car` klasy `Car`. Podczas tworzenia obiektu przekazywane są wartości dla atrybutów `make`, `model` i `year`, które są przechowywane w obiekcie.
-   Metoda `description()` pozwala uzyskać tekstową reprezentację samochodu.

### Typy metod

1.  **Metody instancji**: Są to zwykłe metody, które działają na instancjach klasy. Przyjmują odwołanie do obiektu jako pierwszy parametr (zazwyczaj `self`).

    Przykład:
    ```python
    def method(self):
        pass
    ```

2.  **Metody klasy**: Metody, które przyjmują samą klasę jako pierwszy parametr. Do definiowania takich metod używa się dekoratora `@classmethod`. Mogą one zmieniać stan samej klasy, a nie jej poszczególnych instancji.

    Przykład:
    ```python
    class MyClass:
        @classmethod
        def class_method(cls):
            pass
    ```

3.  **Metody statyczne**: Są to metody, które nie używają `self` ani `cls` (czyli nie mają dostępu ani do instancji, ani do klasy). Metody statyczne są deklarowane za pomocą dekoratora `@staticmethod`. Mogą być przydatne, gdy metoda nie zależy od stanu obiektu ani klasy, ale jest związana z logiką należącą do klasy.

    Przykład:
    ```python
    class MyClass:
        @staticmethod
        def static_method():
            pass
    ```

### Dziedziczenie

Jedną z kluczowych zasad OOP jest **dziedziczenie**. Klasa może dziedziczyć zachowanie innej klasy, rozszerzając lub zmieniając jej funkcjonalność. Pozwala to na ponowne użycie kodu, unikając duplikacji.

```python
class Animal:
    def speak(self):
        return 'Głos zwierzęcia'

class Dog(Animal):  # Klasa Dog dziedziczy po klasie Animal
    def speak(self):
        return 'Hau'

# Tworzenie obiektów
dog = Dog()
print(dog.speak())  # Wyjście: Hau
```

-   Klasa `Dog` dziedziczy metodę `speak` z klasy `Animal`, ale nadpisuje ją, aby zwrócić ciąg `'Hau'`.

### Polimorfizm

**Polimorfizm** oznacza zdolność obiektów różnych klas do używania tych samych metod z różną implementacją. W Pythonie jest to możliwe dzięki dziedziczeniu i nadpisywaniu metod.

```python
class Cat(Animal):
    def speak(self):
        return 'Miau'

# Tworzenie obiektów
cat = Cat()
print(cat.speak())  # Wyjście: Miau
```

Tutaj `Cat` również nadpisuje metodę `speak`, ale zwraca inną wartość. Pozwala to na wywołanie metody `speak` niezależnie od typu obiektu.

### Hermetyzacja

**Hermetyzacja** pozwala ukryć wewnętrzne szczegóły implementacji i zapewnić dostęp do danych za pośrednictwem publicznych metod. Pomaga to zapobiegać nieprawidłowemu użyciu danych.

```python
class Car:
    def __init__(self, make, model):
        self._make = make  # Chroniony atrybut
        self._model = model

    def get_make(self):
        return self._make

    def set_make(self, make):
        self._make = make

# Tworzenie obiektu
my_car = Car('Toyota', 'Corolla')
print(my_car.get_make())  # Wyjście: Toyota
my_car.set_make('Honda')
print(my_car.get_make())  # Wyjście: Honda
```

Tutaj atrybuty `_make` i `_model` są chronione (zazwyczaj w Pythonie podkreślenie oznacza, że te atrybuty nie powinny być używane bezpośrednio poza klasą), ale dostęp do nich można uzyskać i zmienić za pomocą metod `get_make` i `set_make`.

### Inne cechy klas

1.  **Destruktor** (`__del__`):
    Specjalna metoda, która jest wywoływana, gdy obiekt jest niszczony (na przykład po wyjściu z zakresu widoczności). Może być używana do zwalniania zasobów.

    Przykład:
    ```python
    class MyClass:
        def __del__(self):
            print("Obiekt zniszczony")

    obj = MyClass()
    del obj  # Obiekt zostanie zniszczony i wywołana zostanie metoda __del__
    ```

2.  **Metody magiczne**:
    Są to specjalne metody z dwoma podkreśleniami (na przykład `__init__`, `__str__`, `__repr__`, `__eq__`). Pozwalają one nadpisywać standardowe zachowanie operacji, takich jak tworzenie obiektów, porównywanie, wyświetlanie obiektów w postaci tekstowej itp.

    Przykład:
    ```python
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f'Point({self.x}, {self.y})'

    p = Point(3, 4)
    print(p)  # Wyjście: Point(3, 4)
    ```

---

[Do spisu treści](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)

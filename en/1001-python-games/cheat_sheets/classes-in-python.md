# Classes in `python`

Classes are one of the main mechanisms of object-oriented programming (OOP) in Python. A class can be thought of as a "template" or "blueprint" for creating objects that have attributes (data) and methods (functions). Objects created based on a class are called instances of the class. Classes allow you to structure code, improve its reusability, and facilitate its maintenance.

### Class Structure

```python
class ClassName:
    # Class attributes
    def __init__(self, param1, param2):
        # Constructor (initializer) of the class
        self.param1 = param1
        self.param2 = param2

    # Class methods
    def method(self):
        return f'{self.param1} and {self.param2}'
```

1. **Constructor** (`__init__`):
   The `__init__` constructor is a special method that is automatically called when a new object is created. It is used to initialize the object's attributes.

   - `self`: a parameter that is a reference to the current instance of the class. In Python, it must be passed as the first parameter in all class methods (it is not passed when calling the method).
   - Attributes, such as `param1` and `param2`, are assigned to the object via `self`. These attributes can then be used by other class methods.

2. **Class attributes**:
   Attributes are variables that belong to objects of this class. They are defined within the constructor (`__init__`) and can be accessed using an object reference.

3. **Class methods**:
   Methods are functions that can manipulate an object's attributes. Methods can use object data, modify it, or perform other operations.

### Creating a class object

Once a class is defined, objects of that class can be created. Objects are instances of the class.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f'{self.year} {self.make} {self.model}'

# Creating an object
my_car = Car('Toyota', 'Corolla', 2020)
print(my_car.description())  # Output: 2020 Toyota Corolla
```

- In this example, we created a `my_car` object of the `Car` class. When creating the object, values for the `make`, `model`, and `year` attributes are passed, which are stored in the object.
- The `description()` method allows you to get a string representation of the car.

### Types of methods

1. **Instance methods**: These are regular methods that operate on instances of the class. They take a reference to the object as the first parameter (usually `self`).

   Example:
   ```python
   def method(self):
       pass
   ```

2. **Class methods**: Methods that take the class itself as the first parameter. The `@classmethod` decorator is used to define such methods. They can change the state of the class itself, not its individual instances.

   Example:
   ```python
   class MyClass:
       @classmethod
       def class_method(cls):
           pass
   ```

3. **Static methods**: These are methods that do not use `self` or `cls` (i.e., they do not have access to either the instance or the class). Static methods are declared using the `@staticmethod` decorator. They can be useful when a method does not depend on the state of the object or class, but is related to logic belonging to the class.

   Example:
   ```python
   class MyClass:
       @staticmethod
       def static_method():
           pass
   ```

### Inheritance

One of the key principles of OOP is **inheritance**. A class can inherit the behavior of another class, extending or modifying its functionality. This allows code reuse, avoiding duplication.

```python
class Animal:
    def speak(self):
        return 'Animal voice'

class Dog(Animal):  # The Dog class inherits from the Animal class
    def speak(self):
        return 'Woof'

# Creating objects
dog = Dog()
print(dog.speak())  # Output: Woof
```

- The `Dog` class inherits the `speak` method from the `Animal` class, but overrides it to return the string 'Woof'.

### Polymorphism

**Polymorphism** means the ability of objects of different classes to use the same methods with different implementations. In Python, this is possible due to inheritance and method overriding.

```python
class Cat(Animal):
    def speak(self):
        return 'Meow'

# Creating objects
cat = Cat()
print(cat.speak())  # Output: Meow
```

Here, `Cat` also overrides the `speak` method, but returns a different value. This allows you to call the `speak` method regardless of the object type.

### Encapsulation

**Encapsulation** allows you to hide internal implementation details and provide access to data through public methods. This helps prevent improper data usage.

```python
class Car:
    def __init__(self, make, model):
        self._make = make  # Protected attribute
        self._model = model

    def get_make(self):
        return self._make

    def set_make(self, make):
        self._make = make

# Creating an object
my_car = Car('Toyota', 'Corolla')
print(my_car.get_make())  # Output: Toyota
my_car.set_make('Honda')
print(my_car.get_make())  # Output: Honda
```

Here, the `_make` and `_model` attributes are protected (usually in Python, an underscore means that these attributes should not be used directly outside the class), but they can be accessed and modified through the `get_make` and `set_make` methods.

### Other class features

1. **Destructor** (`__del__`):
   A special method that is called when an object is destroyed (e.g., when it goes out of scope). It can be used to clean up resources.

   Example:
   ```python
   class MyClass:
       def __del__(self):
           print("Object destroyed")

   obj = MyClass()
   del obj  # The object will be destroyed and the __del__ method will be called
   ```

2. **Magic methods**:
   These are special methods with two underscores (e.g., `__init__`, `__str__`, `__repr__`, `__eq__`). They allow you to override the standard behavior of operations such as object creation, comparison, string representation of objects, etc.

   Example:
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

  [To table of contents](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)

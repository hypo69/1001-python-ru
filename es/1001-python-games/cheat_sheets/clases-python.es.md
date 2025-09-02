# Clases en `python`

Las clases son uno de los mecanismos principales de la programación orientada a objetos (POO) en Python. Una clase puede considerarse como una "plantilla" o "plano" para crear objetos que tienen atributos (datos) y métodos (funciones). Los objetos creados a partir de una clase se denominan instancias de la clase. Las clases permiten estructurar el código, mejorar su reutilización y facilitar su mantenimiento.

### Estructura de una clase

```python
class ClassName:
    # Atributos de clase
    def __init__(self, param1, param2):
        # Constructor (inicializador) de la clase
        self.param1 = param1
        self.param2 = param2

    # Métodos de clase
    def method(self):
        return f'{self.param1} y {self.param2}'
```

1. **Constructor** (`__init__`):
   El constructor `__init__` es un método especial que se llama automáticamente al crear un nuevo objeto. Se utiliza para inicializar los atributos del objeto.

   - `self`: parámetro que es una referencia a la instancia actual de la clase. En Python, es obligatorio pasarlo como primer parámetro en todos los métodos de clase (no se pasa al llamar al método).
   - Los atributos, como `param1` y `param2`, se asignan al objeto a través de `self`. Estos atributos pueden ser utilizados posteriormente por otros métodos de la clase.

2. **Atributos de clase**:
   Los atributos son variables que pertenecen a los objetos de esta clase. Se definen dentro del constructor (`__init__`) y se puede acceder a ellos usando una referencia al objeto.

3. **Métodos de clase**:
   Los métodos son funciones que pueden manipular los atributos del objeto. Los métodos pueden usar los datos del objeto, modificarlos o realizar otras operaciones.

### Creación de un objeto de clase

Una vez que se define una clase, se pueden crear objetos de esa clase. Los objetos son instancias de la clase.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f'{self.year} {self.make} {self.model}'

# Creación de un objeto
my_car = Car('Toyota', 'Corolla', 2020)
print(my_car.description())  # Salida: 2020 Toyota Corolla
```

- En este ejemplo, creamos un objeto `my_car` de la clase `Car`. Al crear el objeto, se pasan los valores para los atributos `make`, `model` y `year`, que se almacenan en el objeto.
- El método `description()` permite obtener una representación de cadena del coche.

### Tipos de métodos

1. **Métodos de instancia**: Son métodos normales que operan sobre instancias de la clase. Toman una referencia al objeto como primer parámetro (normalmente `self`).

   Ejemplo:
   ```python
   def method(self):
       pass
   ```

2. **Métodos de clase**: Métodos que toman la clase misma como primer parámetro. Para definir tales métodos se utiliza el decorador `@classmethod`. Pueden cambiar el estado de la clase misma, no solo de sus instancias individuales.

   Ejemplo:
   ```python
   class MyClass:
       @classmethod
       def class_method(cls):
           pass
   ```

3. **Métodos estáticos**: Son métodos que no usan `self` ni `cls` (es decir, no tienen acceso ni a la instancia ni a la clase). Los métodos estáticos se declaran usando el decorador `@staticmethod`. Pueden ser útiles cuando un método no depende del estado del objeto o de la clase, pero está relacionado con la lógica que pertenece a la clase.

   Ejemplo:
   ```python
   class MyClass:
       @staticmethod
       def static_method():
           pass
   ```

### Herencia

Uno de los principios clave de la POO es la **herencia**. Una clase puede heredar el comportamiento de otra clase, extendiendo o modificando su funcionalidad. Esto permite la reutilización del código, evitando la duplicación.

```python
class Animal:
    def speak(self):
        return 'Sonido de animal'

class Dog(Animal):  # La clase Dog hereda de la clase Animal
    def speak(self):
        return 'Guau'

# Creación de objetos
dog = Dog()
print(dog.speak())  # Salida: Guau
```

- La clase `Dog` hereda el método `speak` de la clase `Animal`, pero lo sobrescribe para devolver la cadena `'Guau'`.

### Polimorfismo

El **polimorfismo** significa la capacidad de objetos de diferentes clases para usar los mismos métodos con diferentes implementaciones. En Python, esto es posible gracias a la herencia y la sobrescritura de métodos.

```python
class Cat(Animal):
    def speak(self):
        return 'Miau'

# Creación de objetos
cat = Cat()
print(cat.speak())  # Salida: Miau
```

Aquí, `Cat` también sobrescribe el método `speak`, pero devuelve un valor diferente. Esto permite llamar al método `speak` independientemente del tipo de objeto.

### Encapsulación

La **encapsulación** permite ocultar los detalles internos de implementación y proporcionar acceso a los datos a través de métodos públicos. Esto ayuda a prevenir el uso indebido de los datos.

```python
class Car:
    def __init__(self, make, model):
        self._make = make  # Atributo protegido
        self._model = model

    def get_make(self):
        return self._make

    def set_make(self, make):
        self._make = make

# Creación de un objeto
my_car = Car('Toyota', 'Corolla')
print(my_car.get_make())  # Salida: Toyota
my_car.set_make('Honda')
print(my_car.get_make())  # Salida: Honda
```

Aquí, los atributos `_make` y `_model` están protegidos (normalmente en Python, un guion bajo significa que estos atributos no deben usarse directamente fuera de la clase), pero se puede acceder a ellos y modificarlos a través de los métodos `get_make` y `set_make`.

### Otras características de las clases

1. **Destructor** (`__del__`):
   Un método especial que se llama cuando un objeto es destruido (por ejemplo, cuando sale del ámbito). Se puede usar para liberar recursos.

   Ejemplo:
   ```python
   class MyClass:
       def __del__(self):
           print("Objeto destruido")

   obj = MyClass()
   del obj  # El objeto será destruido y se llamará al método __del__
   ```

2. **Métodos mágicos**:
   Son métodos especiales con dos guiones bajos (por ejemplo, `__init__`, `__str__`, `__repr__`, `__eq__`). Permiten sobrescribir el comportamiento estándar de operaciones como la creación de objetos, la comparación, la representación de objetos como cadenas, etc.

   Ejemplo:
   ```python
   class Point:
       def __init__(self, x, y):
           self.x = x
           self.y = y

       def __repr__(self):
           return f'Point({self.x}, {self.y})'

   p = Point(3, 4)
   print(p)  # Salida: Point(3, 4)
   ```

 ---

  [Al índice](https://github.com/hypo69/101_python_computer_games_ru/blob/master/cheat_sheets#readme)

### `question_803.md`

**Вопрос 803.** Что такое "абстракция" в объектно-ориентированном программировании (ООП)?

A. Это возможность создания новых классов на основе существующих.
B. Это способность объектов разных классов вести себя единообразно через общий интерфейс.
C. Это принцип, позволяющий скрыть детали реализации объекта и предоставлять доступ к нему через публичный интерфейс.
D. Это механизм для обработки ошибок и исключений.

**Правильный ответ: C**

**Объяснение:**

В объектно-ориентированном программировании (ООП) абстракция — это принцип сокрытия сложной внутренней реализации объекта и предоставления простого, понятного интерфейса для работы с ним. Абстракция позволяет работать с объектом, не зная деталей его внутреннего устройства.

*  **Вариант A** не верен: Это определение наследования.
*   **Вариант B** не верен: Это определение полиморфизма.
*   **Вариант C** верен:  Абстракция - это сокрытие внутренней реализации и предоставление доступа к ней через публичный интерфейс.
*   **Вариант D** не верен: Это определение для try-except блоков.

**Как работает абстракция:**

1.  Абстракция позволяет скрыть сложные детали реализации объекта, оставляя только необходимый интерфейс для взаимодействия.
2.  Она позволяет разработчикам работать с объектом на более высоком уровне, не углубляясь в подробности.
3.  Она способствует модульности и упрощает поддержку и модификацию кода.
4. В Python, абстракция может быть реализована через абстрактные классы или интерфейсы.

**Пример:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
       """абстрактный метод"""
       pass
class Circle(Shape):
    def __init__(self, radius: int):
        self.radius = radius

    def area(self) -> float: # Реализуем метод класса Shape
        """Расчет площади круга."""
        return 3.14 * self.radius**2

class Square(Shape):
  def __init__(self, side: int):
    self.side = side

  def area(self) -> float: # Реализуем метод класса Shape
    """Расчет площади квадрата"""
    return self.side**2

circle: Circle = Circle(5)
square: Square = Square(10)

def display_area(shape: Shape):
   print(f"Площадь: {shape.area()}") # Полиморфный вызов метода area()

display_area(circle) # Вывод: Площадь: 78.5
display_area(square) # Вывод: Площадь: 100
```
**В результате:**

*  Мы можем работать с `circle` и `square`, используя общий интерфейс `shape` (метод `area`), при этом не зная деталей их реализации.

Таким образом, **вариант C** является правильным ответом.

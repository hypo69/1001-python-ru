### `question_010.md` (DIP - Practical Application)

**Вопрос 010.** Какой из следующих фрагментов кода на Python *наиболее точно* иллюстрирует применение принципа инверсии зависимостей (Dependency Inversion Principle - DIP)?

A.

```python
class LightBulb:
    def turn_on(self):
        print("LightBulb: Bulb turned on")

class Switch:
    def __init__(self, bulb: LightBulb):
        self.bulb = bulb

    def operate(self):
        self.bulb.turn_on()
```

B.

```python
class LightBulb:
    def turn_on(self):
        print("LightBulb: Bulb turned on")

class Switch:
    def __init__(self):
        self.bulb = LightBulb()

    def operate(self):
        self.bulb.turn_on()
```

C.

```python
from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self): pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: Bulb turned on")

class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self):
        self.device.turn_on()
```

D.

```python
class LightBulb:
    def turn_on(self):
        print("LightBulb: Bulb turned on")

class Switch:
    def __init__(self):
        pass

    def operate(self, bulb: LightBulb):
        bulb.turn_on()
```

**Правильный ответ: C**

**Объяснение:**

Принцип инверсии зависимостей (DIP) предполагает, что высокоуровневые модули не должны зависеть от низкоуровневых модулей. Оба должны зависеть от абстракций. Вариант C *наиболее точно* демонстрирует это.

*   **Вариант A:**  `Switch` напрямую зависит от `LightBulb` (низкоуровневого модуля). Это *нарушение* DIP.
*   **Вариант B:**  То же самое, что и A. `Switch` создает экземпляр `LightBulb`, что увеличивает зависимость.
*   **Вариант C:**  `Switch` зависит от абстракции `Switchable` (интерфейса). `LightBulb` реализует этот интерфейс. Это соответствует DIP.  `Switch` не знает, что включает, только то, что объект умеет `turn_on`.
*   **Вариант D:**  Зависимость передается через аргумент метода `operate`, что снижает связность, но всё же не использует абстракцию.

**Пример:**

В этом примере легко заменить `LightBulb` на другой `Switchable` девайс, например `Fan`, не меняя код `Switch`:

```python
from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self): pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: Bulb turned on")

class Fan(Switchable):
    def turn_on(self):
        print("Fan: Fan started")

class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self):
        self.device.turn_on()

bulb = LightBulb()
switch = Switch(bulb)
switch.operate() # Output: LightBulb: Bulb turned on

fan = Fan()
switch = Switch(fan)
switch.operate() # Output: Fan: Fan started
```

**В результате:**

Вариант C наиболее точно демонстрирует DIP, так как `Switch` зависит от абстракции `Switchable`, а не от конкретной реализации `LightBulb`.

Таким образом, вариант C является правильным.

### `question_008.md` (ISP - Code Example)

**Вопрос 008.** Какой из следующих вариантов кода на Python *наиболее полно* демонстрирует применение принципа разделения интерфейсов (Interface Segregation Principle - ISP)?

A.

```python
class Worker: # code omitted
    def work(self): pass
    def eat(self): pass

class робот(Worker):
    def work(self): pass
    def eat(self): pass
```

B.

```python
class WorkerInterface: # code omitted
    def work(self): pass
    def eat(self): pass

class Worker(WorkerInterface):
    def work(self): pass
    def eat(self): pass
```

C.

```python
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self): pass

class Eatable(ABC):
    @abstractmethod
    def eat(self): pass

class Worker(Workable, Eatable):
    def work(self): pass
    def eat(self): pass

class Robot(Workable):
    def work(self): pass
```

D.

```python
class Worker(ABC):
    @abstractmethod
    def work(self): pass
    @abstractmethod
    def eat(self): pass

class Human(Worker):
    def work(self): pass
    def eat(self): pass

class Robot(Worker):
    def work(self): pass
    # Robot doesn't need to eat, but has to implement it
    def eat(self): pass
```

**Правильный ответ: C**

**Объяснение:**

Принцип разделения интерфейсов (ISP) рекомендует создавать много небольших, специализированных интерфейсов вместо одного большого. Это позволяет классам реализовывать только те методы, которые им действительно нужны.

*   **Вариант A:** Не демонстрирует ISP, так как все классы реализуют один и тот же интерфейс.
*   **Вариант B:** То же самое, что и А, но через интерфейс, что не сильно меняет ситуацию.
*   **Вариант C:** `Workable` и `Eatable` определены как отдельные интерфейсы (абстрактные классы). `Worker` реализует оба интерфейса, а `Robot` реализует только `Workable`, что соответствует ISP. `Robot` не нужно реализовывать `Eatable`, так как он не ест.
*   **Вариант D:** `Robot` вынужден реализовать метод `eat()`, который ему не нужен, что является нарушением ISP.

**Пример:**

Этот код показывает разделение интерфейсов, где `Robot` реализует только необходимые ему методы:

```python
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Worker(Workable, Eatable):
    def work(self):
        print("Worker is working")

    def eat(self):
        print("Worker is eating")

class Robot(Workable):
    def work(self):
        print("Robot is working")

worker = Worker()
worker.work()
worker.eat()

robot = Robot()
robot.work()
```

**В результате:**

Только вариант C демонстрирует правильное применение ISP, где интерфейсы разделены на более мелкие и классы реализуют только необходимые им интерфейсы.

Таким образом, вариант C является правильным.

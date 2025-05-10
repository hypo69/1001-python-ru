### `question_005.md` (OCP - Нарушение)

**Вопрос 005.** В каком из следующих примеров кода на Python *наиболее явно* нарушается принцип открытости/закрытости (OCP)?

A.
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass
```

B.

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
```

C.

```python
class PaymentProcessor:
    def process_payment(self, payment_type, amount):
        if payment_type == "credit_card":
            # Code to process credit card payment
            pass
        elif payment_type == "paypal":
            # Code to process PayPal payment
            pass
        elif payment_type == "stripe":
            # Code to process Stripe payment
            pass
        else:
            raise ValueError("Invalid payment type")
```

D.

```python
class ReportGenerator:
    def generate_report(self, data, format):
        if format == "pdf":
            # Code to generate PDF report
            pass
        elif format == "csv":
            # Code to generate CSV report
            pass
```

**Правильный ответ: C**

**Объяснение:**

Принцип открытости/закрытости (OCP) гласит, что классы должны быть открыты для расширения, но закрыты для модификации. В варианте C класс `PaymentProcessor` *нарушает OCP*, потому что для добавления нового способа оплаты потребуется *изменять* существующий код класса `PaymentProcessor`.

*   **Вариант A:**  Класс не имеет реализаций.
*   **Вариант B:**  Есть расширение класса, без изменения родительского класса.
*   **Вариант C:** Класс `PaymentProcessor` *нарушает OCP*.
*   **Вариант D:** Класс `ReportGenerator` *нарушает OCP*.

**Пример рефакторинга (для PaymentProcessor):**

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        # Code to process credit card payment
        pass

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        # Code to process PayPal payment
        pass

class PaymentProcessor:
    def process_payment(self, payment_method: PaymentMethod, amount):
        payment_method.process_payment(amount)
```

**В результате:**

Классы и сущности должны быть спроектированы так, чтобы новое поведение можно было добавлять без изменения существующего кода.

Таким образом, вариант C является правильным.

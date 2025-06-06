### `question_507.md`

**Вопрос 507** Какой способ позволяет поменять местами значения двух переменных в Python без использования третьей временной переменной?

-   A. Используя оператор присваивания (=) с временной переменной.
-   B. Используя метод `swap()`.
-   C. Используя множественное присваивание.
-   D. Используя арифметические операции.

**Правильный ответ: C**

**Объяснение:**

В Python есть удобный и элегантный способ поменять значения двух переменных местами без необходимости использовать дополнительную временную переменную. Это делается с помощью множественного присваивания (tuple packing and unpacking).

*   **Множественное присваивание:**
    *   Создается кортеж справа от знака присваивания, содержащий значения, которые нужно переставить.
    *   Слева от знака присваивания указываются имена переменных, которым нужно присвоить значения.
    *   Python присваивает значения из кортежа переменным в порядке их следования.

**Разбор вариантов:**
*   **A. Используя оператор присваивания (=) с временной переменной:** Неправильно. Это традиционный способ обмена, но он требует временной переменной.
*   **B. Используя метод `swap()`:** Неправильно. В Python нет встроенного метода `swap()`.
*  **C. Используя множественное присваивание:** Правильно. Это самый короткий и Pythonic способ обмена.
*   **D. Используя арифметические операции:** Неправильно. Хотя обмен можно сделать через арифметику, это не является простым и стандартным способом в Python, а также может работать не со всеми типами данных.

**Пример обмена значениями с множественным присваиванием:**

```python
a = 10
b = 20

print(f"До обмена: a = {a}, b = {b}")

a, b = b, a  # множественное присваивание, переменные меняются местами

print(f"После обмена: a = {a}, b = {b}")

# Вывод
# До обмена: a = 10, b = 20
# После обмена: a = 20, b = 10
```

**В результате:**
*   Множественное присваивание позволяет менять значения переменных местами, лаконично и эффективно.
*   Это один из примеров элегантности и гибкости Python.
*   Этот способ работает не только с числами, но и с любыми типами данных.

Таким образом, правильным ответом является **C. Используя множественное присваивание.**

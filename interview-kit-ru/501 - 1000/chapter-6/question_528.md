### `question_528.md`

**Вопрос 528.** Какой из представленных вариантов кода является корректным однострочным решением для подсчета количества заглавных букв в текстовом файле?

-   A. `sum(1 for line in open(filename) for char in line if char.isupper())`
-   B. `sum(char.isupper() for line in open(filename) for char in line)`
-   C. `len([char for line in open(filename) for char in line if char.isupper()])`
-   D. `count = 0; with open(filename) as f: for line in f: for char in line: if char.isupper(): count +=1`

**Правильный ответ: A**

**Объяснение:**

Данный вопрос касается использования генераторов и функций высшего порядка для лаконичного решения задач в Python.

*   **Понимание задачи:** Необходимо прочитать текстовый файл, пройти посимвольно по его содержимому и подсчитать количество заглавных букв.
*   **Однострочное решение:**
    *   `open(filename)` открывает файл для чтения.
    *   `for line in open(filename)`:  генерирует строки из файла поочередно.
    *    `for char in line`: генерирует символы из каждой строки поочередно
    *   `if char.isupper()`: условие проверки, является ли текущий символ заглавной буквой.
    *   `1 for ... if char.isupper()`: генераторное выражение, которое возвращает `1` для каждой заглавной буквы.
    *   `sum(...)`: функция sum принимает генератор и суммирует все единицы, подсчитывая количество заглавных букв.

**Разбор вариантов:**

*   **A. `sum(1 for line in open(filename) for char in line if char.isupper())`:** Правильно. Это компактное однострочное решение, использующее генератор и функцию `sum()`.
*   **B. `sum(char.isupper() for line in open(filename) for char in line)`:** Неправильно. Здесь суммируются результаты `True` и `False` (логические значения), а не количество заглавных букв.
*  **C. `len([char for line in open(filename) for char in line if char.isupper()])`**: Правильно. Но этот вариант использует list comprehension, что менее эффективно, чем генераторное выражение в варианте А.
*  **D. `count = 0; with open(filename) as f: for line in f: for char in line: if char.isupper(): count +=1`:** Неправильно. Это многострочный код, а требуется однострочное решение.

**Пример использования:**
Предположим, у нас есть файл `test.txt` со следующим содержанием:

```
Hello World!
Python Is AWESOME.
```
```python
filename = "test.txt"
count = sum(1 for line in open(filename) for char in line if char.isupper())
print(count) # Выведет 5
```
**В результате:**
*   Генераторы и list comprehension позволяют писать компактный и лаконичный код.
*   Однострочные решения могут быть удобными для простых задач, но стоит учитывать читаемость кода.
*   Использование генераторов более эффективно чем list comprehension в данном случае.

Таким образом, правильным ответом является **A. `sum(1 for line in open(filename) for char in line if char.isupper())`**.

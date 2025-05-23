### question_514


**Вопрос 514:**
```python
def apply_operation(x, y, operation):
    return operation(x,y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result1 = apply_operation(5, 2, add)
result2 = apply_operation(5, 2, multiply)
print(result1, result2)
```
Какой будет результат выполнения этого кода?

A. 7 10
B. 10 7
C. 7 25
D. Произойдет ошибка.

**Правильный ответ: A**

**Объяснение:**
Этот код демонстрирует концепцию функций высшего порядка и передачу функций в качестве аргументов в Python.

1.  **Функция `apply_operation`:**
    *   Принимает три аргумента: `x`, `y` (числа) и `operation` (функция).
    *   Возвращает результат вызова функции `operation` с аргументами `x` и `y`.

2.  **Функция `add`:**
    *   Принимает два аргумента: `a` и `b`.
    *   Возвращает сумму `a` и `b`.

3.  **Функция `multiply`:**
    *   Принимает два аргумента: `a` и `b`.
    *   Возвращает произведение `a` и `b`.

4.  **Вызовы `apply_operation`:**
    *   `result1 = apply_operation(5, 2, add)`: Функция `add` передается как аргумент `operation`. `apply_operation` вызовет `add(5, 2)`, что вернет `5 + 2 = 7`.
    *   `result2 = apply_operation(5, 2, multiply)`: Функция `multiply` передается как аргумент `operation`. `apply_operation` вызовет `multiply(5, 2)`, что вернет `5 * 2 = 10`.

5. **Вывод** `print(result1, result2)` выведет значения переменных `result1` и `result2`, разделенные пробелом.

**Разбор вариантов:**

*   **A. 7 10:** Правильно. `result1` равен 7, а `result2` равен 10.
*   **B. 10 7:** Неправильно. Порядок операций обратный.
*   **C. 7 25:** Неправильно. Неправильный результат для `result2`.
*  **D. Произойдет ошибка:** Неправильно, код выполнится без ошибок.

**Код для файла `question_514.md`:**
```markdown
### `question_514.md`

**Вопрос 514.** Какой будет результат выполнения следующего кода?

```python
def apply_operation(x, y, operation):
    return operation(x,y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result1 = apply_operation(5, 2, add)
result2 = apply_operation(5, 2, multiply)
print(result1, result2)
```

- A. 7 10
- B. 10 7
- C. 7 25
- D. Произойдет ошибка.

**Правильный ответ: A**

**Объяснение:**

Этот код демонстрирует концепцию функций высшего порядка и передачу функций в качестве аргументов в Python.

*   **Функция `apply_operation`:** Принимает три аргумента: два числа (`x`, `y`) и функцию (`operation`). Она возвращает результат вызова переданной функции `operation` с аргументами `x` и `y`.
*   **Функции `add` и `multiply`:** Это простые функции, которые выполняют сложение и умножение соответственно.
*   **Вызовы `apply_operation`:**
    *   `result1` присваивается результат вызова `apply_operation` с числами 5 и 2 и функцией `add`. Функция `add(5, 2)` вернёт 7.
    *   `result2` присваивается результат вызова `apply_operation` с числами 5 и 2 и функцией `multiply`. Функция `multiply(5, 2)` вернёт 10.

В результате, `print(result1, result2)` выведет `7 10`.

**Дополнительные замечания:**

- В Python функции являются объектами первого класса, что означает, что их можно передавать как аргументы в другие функции, возвращать из функций и присваивать переменным.
- Функции, которые принимают другие функции в качестве аргументов или возвращают их, называются функциями высшего порядка.
- Эта возможность делает Python очень гибким и мощным языком.


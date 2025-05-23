### `question_017.md`

**Вопрос 17.** Каково будет поведение следующей Python функции?

```python
def check_number(n):
    if n % 2 == 0:
        return "Even"
    elif n % 3 == 0:
        return "Divisible by 3"
    else:
        return "Other"
```

- A. Функция возвращает `"Even"` только если `n` делится на 2 и 3.
- B. Функция возвращает `"Divisible by 3"` для всех чисел, делящихся на 3, независимо от того, являются ли они четными.
- C. Функция возвращает `"Even"` для всех четных чисел, и `"Divisible by 3"` для чисел не четных, но делящихся на 3.
- D. Функция не может вернуть `"Other"`.

**Правильный ответ: C**

**Объяснение:**

Функция `check_number(n)` проверяет число `n` на соответствие определенным условиям и возвращает строку в зависимости от результата проверки.

*   **`if n % 2 == 0:`**: Проверяет, является ли число `n` четным (то есть, делится ли оно на 2 без остатка). Если условие истинно, функция немедленно возвращает строку `"Even"` и прекращает выполнение.

*   **`elif n % 3 == 0:`**: Если предыдущее условие ложно (т.е. число `n` не является четным), проверяется, делится ли `n` на 3 без остатка. Если это условие истинно, функция возвращает строку `"Divisible by 3"` и прекращает выполнение.

*   **`else:`**: Если ни одно из предыдущих условий не выполнилось (т.е. число `n` не является ни четным, ни кратным 3), функция возвращает строку `"Other"`.
    
Давайте проанализируем варианты ответов:
    
*   **Вариант A** не верен: Функция возвращает `"Even"` если число делится только на 2, а не на 2 и 3.
*   **Вариант B** не верен: Если число четное (делится на 2), то ветка `if n % 2 == 0:` выполняется первой и функция возвращает `"Even"`, не проверяя делимость на 3.
*   **Вариант C** верен: Именно так работает функция, проверяя сначала на четность и потом на делимость на 3.
*   **Вариант D** не верен: Функция может вернуть `"Other"`, если число не соответствует ни одному из первых двух условий.

**Примеры:**

```python
def check_number(n: int) -> str:
    if n % 2 == 0:
        return "Even"
    elif n % 3 == 0:
        return "Divisible by 3"
    else:
        return "Other"

print(check_number(4))   # Вывод: Even
print(check_number(9))  # Вывод: Divisible by 3
print(check_number(7))  # Вывод: Other
print(check_number(6)) # Вывод: Even (число делится на 2, первая ветка выполняется)
```

**В результате:**

*   `check_number(4)` возвращает `"Even"`, так как 4 делится на 2.
*   `check_number(9)` возвращает `"Divisible by 3"`, так как 9 нечетное, но делится на 3.
*   `check_number(7)` возвращает `"Other"`, так как 7 не делится ни на 2, ни на 3.
*   `check_number(6)` возвращает `"Even"`, так как 6 делится на 2, и последующие условия не проверяются.

Таким образом, **вариант C** является единственным верным.

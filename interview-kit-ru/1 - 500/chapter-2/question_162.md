### `question_162.md`

**Вопрос 62.** Каков будет вывод следующего кода?

```python
x: int = 10
y: int = 20
if x > 5:
    if y < 15:
        print("Оба условия верны")
    else:
        print("x больше 5, но y не меньше 15")
else:
    print("x не больше 5")
```

A. `x не больше 5`
B. `Оба условия верны`
C. `x больше 5, но y не меньше 15`
D. Ошибка

**Правильный ответ: C**

**Объяснение:**

Этот код демонстрирует вложенные условные операторы `if-else`.

1.  **Инициализация:** `x` устанавливается равным 10, а `y` равным 20.
2.  **Внешний `if`:** `if x > 5:` проверяет, что `x` больше 5, это условие истинно, так как `x` равно 10.
3.  **Внутренний `if`:** Выполняется блок кода внутреннего оператора `if`. `if y < 15:` проверяет, что `y` меньше 15. Это условие ложно, так как `y` равно 20.
4.  **Внутренний `else`:** Так как условие внутреннего `if` ложно, то выполняется код, вложенный в `else`.

Теперь посмотрим на варианты ответа:

*   **Вариант A** не верен:  Внешнее условие `x > 5` истинно, поэтому блок `else` не выполнится.
*   **Вариант B** не верен: Условие внутреннего `if` ложно, поэтому блок `"Оба условия верны"` не выполнится.
*   **Вариант C** верен:  Внутреннее `else` выводит строку  `"x больше 5, но y не меньше 15"`, потому что условие `y<15` ложно.
*   **Вариант D** не верен:  Код синтаксически корректный и ошибки не будет.

**Пример:**

```python
x: int = 10
y: int = 20
if x > 5:
    if y < 15:
        print("Оба условия верны")
    else:
        print("x больше 5, но y не меньше 15") # Вывод: x больше 5, но y не меньше 15
else:
    print("x не больше 5")
```

**В результате:**
*   Выводится строка `"x больше 5, но y не меньше 15"`.

Таким образом, **вариант C** является правильным.

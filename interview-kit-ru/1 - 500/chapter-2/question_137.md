### `question_137.md`

**Вопрос 37.** Как используются вложенные условные операторы `if`?

A. Для выполнения нескольких различных блоков кода одновременно.
B. Для указания условия, которое должно быть истинным, прежде чем будет проверено другое условие.
C. Для оптимизации производительности кода за счет уменьшения количества проверок условий.
D. Для перехвата исключений, которые могут возникнуть в коде.

**Правильный ответ: B**

**Объяснение:**

Вложенные условные операторы `if` используются для создания более сложной логики, где выполнение определенных действий зависит от нескольких условий.
Внешний оператор `if` проверяет первое условие, и, если оно выполняется, происходит переход к внутреннему оператору `if`, который проверяет второе условие, и так далее.

*   **Вариант A** не верен:  `if` выполняет только один блок за раз.
*   **Вариант B** верен:  Вложенные `if` нужны, чтобы проверить условие только при выполнении предыдущего условия.
*   **Вариант C** не верен:  Вложенные `if` могут снизить производительность, поскольку добавляют новые проверки.
*   **Вариант D** не верен: `try-except` используются для отлавливания исключений.

**Пример:**

```python
x: int = 10
y: int = 5

if x > 0:
    print("x является положительным числом")
    if y > 0:
        print("y является положительным числом")
        if x > y:
            print("x больше y")
        else:
            print("x не больше y")
    else:
        print("y не является положительным числом")
else:
  print("x не является положительным числом")
```

**В результате:**
В коде выше, внутренние `if` операторы выполняются только если выполняется первый `if x > 0`.

Таким образом, **вариант B** является правильным.

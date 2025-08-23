### `question_015.md`

**Вопрос 15.** При итерировании по списку в Python для вычисления суммы его элементов, какая из следующих конструкций цикла правильно сформулирована, чтобы избежать ошибки `IndexError` и успешно вычислить общую сумму?

```python
- A. list_values = [1, 2, 3, 4, 5]; total = 0; for i in range(len(list_values) + 1): total += list_values[i]; print(total)
- B. list_values = [1, 2, 3, 4, 5]; total = 0; for value in list_values: total += value; print(total)
- C. list_values = [1, 2, 3, 4, 5]; total = 0; for i in range(1, len(list_values)): total += list_values[i]; print(total)
- D. list_values = [1, 2, 3, 4, 5]; total = 0; for i in range(len(list_values) - 1): total += list_values[i]; print(total)
```

**Правильный ответ: B**

**Объяснение:**

Для итерации по элементам списка в Python существует несколько способов. Важно правильно выбрать способ, чтобы избежать ошибок, таких как `IndexError`, которая возникает при попытке обратиться к несуществующему индексу.

*   **Вариант A**: `list_values = [1, 2, 3, 4, 5]; total = 0; for i in range(len(list_values) + 1): total += list_values[i]; print(total)` - Неправильный вариант. Цикл `for` в этом варианте пытается перебрать индексы от 0 до `len(list_values)`, включительно, что приведет к `IndexError` на последней итерации, потому что индексы списка начинаются с 0 и заканчиваются на `len(list_values) - 1`.

*   **Вариант B**: `list_values = [1, 2, 3, 4, 5]; total = 0; for value in list_values: total += value; print(total)` - Это правильный вариант. Цикл `for` в этом варианте итерирует напрямую по элементам списка, а не по их индексам. Это простой, эффективный и идиоматичный способ итерации по спискам в Python, при котором автоматически перебираются все элементы списка без необходимости использовать индексы.
    
*   **Вариант C**: `list_values = [1, 2, 3, 4, 5]; total = 0; for i in range(1, len(list_values)): total += list_values[i]; print(total)` - Неправильный вариант. Этот цикл пропустит первый элемент списка (с индексом 0), поскольку он итерирует по диапазону от 1 до `len(list_values) - 1`.

*   **Вариант D**: `list_values = [1, 2, 3, 4, 5]; total = 0; for i in range(len(list_values) - 1): total += list_values[i]; print(total)` - Неправильный вариант. Этот цикл пропустит последний элемент списка (с индексом `len(list_values) - 1`), поскольку он итерирует до `len(list_values) - 2`.

**Пример:**

```python
# Пример с правильным вариантом (B)
list_values: list[int] = [1, 2, 3, 4, 5]
total: int = 0
for value in list_values:
    total += value
print(f"Сумма элементов: {total}")  # Вывод: Сумма элементов: 15

# Пример с неправильным вариантом (A) - вызовет IndexError
list_values: list[int] = [1, 2, 3, 4, 5]
total: int = 0
try:
    for i in range(len(list_values) + 1):
        total += list_values[i]
    print(total)
except IndexError as e:
     print(e) # Вывод: list index out of range
```

**В результате:**

*   **Вариант B** успешно итерирует по всем элементам списка, суммирует их и выводит результат `15`.
*   **Вариант A** вызовет ошибку `IndexError` при попытке обратиться к индексу 5, которого нет в списке.

Таким образом, только **вариант B** корректно и эффективно вычисляет сумму элементов списка.

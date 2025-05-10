### `question_412.md`

**Вопрос 412.** Каков результат выполнения следующего кода Python и как работает метод `isdisjoint()`?

```python
set_x = {0, 1, 2, 3, 4}
list_y = [5, 6, 7, 8, 9]
print(set_x.isdisjoint(list_y))

list_y[0] = 4
print(set_x.isdisjoint(list_y))

fset = frozenset(['march', 'dec', 'feb', 'may'])
tuple_y = ('july', 'aug', 'june', 'jan', 'may')
print(fset.isdisjoint(tuple_y))


fset = frozenset(['march', 'dec', 'feb'])
print(fset.isdisjoint(tuple_y))
```

-   A. `True False True False`
-   B. `False True False True`
-   C. `True False False True`
-   D. `False True True False`

**Правильный ответ: C**

**Объяснение:**

Этот код демонстрирует использование метода `isdisjoint()` для проверки, не имеют ли множество и итерируемый объект общих элементов. Метод `isdisjoint()`  возвращает `True`, если множество и итерируемый объект не имеют общих элементов, и `False`, если имеют.

1.  **Первый блок:**
    *   `set_x = {0, 1, 2, 3, 4}`: Создается множество `set_x` с элементами от 0 до 4.
    *   `list_y = [5, 6, 7, 8, 9]`: Создается список `list_y` с элементами от 5 до 9.
    *  `set_x.isdisjoint(list_y)`: Проверяет, есть ли общие элементы между `set_x` и `list_y`. Поскольку общих элементов нет, возвращается `True`.
2. **Второй блок:**
     *   `list_y[0] = 4`: Изменяется первый элемент списка `list_y`, так что теперь `list_y` это `[4, 6, 7, 8, 9]`.
     * `set_x.isdisjoint(list_y)`: Проверяет, есть ли общие элементы между `set_x` и измененным `list_y`. Поскольку число 4 является общим элементом, возвращается `False`.
3.  **Третий блок:**
    *   `fset = frozenset(['march', 'dec', 'feb', 'may'])`: Создается `frozenset` (неизменяемое множество) с элементами.
    *   `tuple_y = ('july', 'aug', 'june', 'jan', 'may')`: Создается кортеж `tuple_y`.
     *  `fset.isdisjoint(tuple_y)`:  проверяет, есть ли общие элементы между `fset` и `tuple_y`. Так как у них есть общий элемент `may`, метод возвращает `False`.
4.  **Четвертый блок:**
    * `fset = frozenset(['march', 'dec', 'feb'])`:  Создается `frozenset`  с новыми элементами, которые не содержатся в  `tuple_y`.
    * `fset.isdisjoint(tuple_y)`:  проверяет, есть ли общие элементы между `fset` и `tuple_y`. Поскольку общих элементов нет, возвращается `True`.

**Разбор вариантов:**
*   **A. `True False True False`:** Неправильно.
*   **B. `False True False True`:** Неправильно.
*  **C. `True False False True`:** Правильно.
*   **D. `False True True False`:** Неправильно.

**В результате:**
*  Метод `isdisjoint()`  возвращает `True`  если нету общих элементов,  и `False`  если общие элементы есть.
*  Примеры показывают, как изменяемые данные могут повлиять на результат вызова `isdisjoint`.

Таким образом, правильным ответом является **C. `True False False True`**.

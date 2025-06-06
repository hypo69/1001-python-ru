### `question_597.md`

**Вопрос 597.** Как работает функция `map()` в Python? Опишите ее назначение и приведите пример ее использования.

-   A. Функция `map()` используется для фильтрации элементов в последовательности на основе заданного условия.
-   B. Функция `map()` используется для объединения всех элементов последовательности в одно значение.
-   C. Функция `map()` применяется для сортировки элементов последовательности в порядке возрастания.
-   D. Функция `map()` применяет заданную функцию к каждому элементу итерируемого объекта и возвращает итератор с результатами.

**Правильный ответ: D**

**Объяснение:**

Функция `map()` в Python — это встроенная функция, которая применяется для выполнения заданной функции к каждому элементу итерируемого объекта (например, списка, кортежа, множества, словаря, и т.д.). `map()`  возвращает итератор, который содержит результаты применения функции.

*   **Основные характеристики `map()`:**
    *   **Итерируемый объект:** Функция `map()` работает с любым итерируемым объектом.
    *   **Функция-преобразователь:** Принимает функцию как первый аргумент, которая будет применяться к элементам итерируемого объекта.
    *   **Ленивое вычисление:**  `map()` не вычисляет результаты сразу, а создает итератор, который генерирует их по мере запроса.
    *   **Итератор результатов:**  Функция возвращает итератор, который содержит преобразованные элементы.
    *   **Преобразование:** Используется для преобразования элементов коллекции.

*   **Синтаксис `map()`:**
    *   `map(function, iterable, ...)`
         *  `function` - функция, применяемая к каждому элементу `iterable`.
         *   `iterable` - итерируемый объект (список, кортеж, строка и др.). Можно передавать несколько итерируемых объектов.
         * Возвращает итератор.

**Примеры:**
```python
# Пример 1: использование map() с обычной функцией
def add_5(x):
    return x + 5

numbers = [1, 2, 3, 4, 5]
result = map(add_5, numbers)
print(list(result))  # Вывод: [6, 7, 8, 9, 10]

# Пример 2: использование map() с лямбда функцией
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, numbers)
print(list(result))  # Вывод: [2, 4, 6, 8, 10]

# Пример 3: использование map() с несколькими итерируемыми объектами
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = map(lambda x, y: x + y, list1, list2)
print(list(result))  # Вывод: [5, 7, 9]

# Пример с преобразованием типов
strings = ["1", "2", "3"]
int_numbers = list(map(int, strings))
print(int_numbers) # Выведет [1, 2, 3]
```

**Разбор вариантов:**
*   **A. Функция `map()` используется для фильтрации элементов в последовательности на основе заданного условия.:** Неправильно.
*   **B. Функция `map()` используется для объединения всех элементов последовательности в одно значение.:** Неправильно. Это делает функция `reduce`.
*  **C. Функция `map()` применяется для сортировки элементов последовательности в порядке возрастания.:** Неправильно.
*   **D. Функция `map()` применяет заданную функцию к каждому элементу итерируемого объекта и возвращает итератор с результатами.:** Правильно.

**В результате:**
*  `map` является удобной функцией для применения преобразования ко всем элементам итерируемого объекта.
*  Возвращает итератор.
* `map`  может применяться к одному или нескольким итерируемым объектам.

Таким образом, правильным ответом является **D. Функция `map()` применяет заданную функцию к каждому элементу итерируемого объекта и возвращает итератор с результатами.**

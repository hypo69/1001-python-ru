

### `question_59.md`

**Вопрос 59.** Какую встроенную функцию Python вы бы использовали, чтобы найти наибольшее число в списке целых чисел?

- A. `max()`
- B. `sum()`
- C. `len()`
- D. `high()`

**Правильный ответ: A**

**Объяснение:**

В Python для поиска наибольшего значения в последовательности (например, списке, кортеже, строке, множестве или другом итерируемом объекте) используется встроенная функция `max()`.

*   **Вариант A** верен: `max()` возвращает наибольший элемент в итерируемом объекте.
*   **Вариант B** не верен: `sum()` возвращает сумму всех элементов.
*   **Вариант C** не верен:  `len()` возвращает длину (количество элементов) последовательности.
*   **Вариант D** не верен: `high()` не является встроенной функцией Python.

**Как работает `max()`:**

1.  `max()` принимает итерируемый объект в качестве аргумента (или несколько аргументов).
2.  Он возвращает наибольший элемент в итерируемом объекте (или наибольшее значение среди переданных аргументов).
3.  Для итерируемых объектов он сравнивает элементы, используя оператор `>` по умолчанию, но можно передать свою функцию для сравнения.

**Пример:**

```python
my_numbers: list[int] = [10, 5, 20, 8, 15]

# Находим максимальное число в списке
max_value: int = max(my_numbers)
print(f"Наибольшее число: {max_value}") # Вывод: Наибольшее число: 20

# Находим максимальное число из нескольких чисел
max_value: int = max(5, 10, 2, 15)
print(f"Наибольшее число: {max_value}") # Вывод: Наибольшее число: 15
```

**В результате:**

*   `max(my_numbers)` возвращает наибольшее число из списка `my_numbers`.
*   `max(5, 10, 2, 15)` возвращает наибольшее из переданных чисел.
  
Таким образом, **вариант A** является правильным ответом.

### `question_047.md`

**Вопрос 47.** Как лямбда-функция Python облегчает быстрое определение функций, и каковы ее типичные варианты использования в программировании?

- A. Лямбда-функции в Python используются для создания новых объектов функций для постоянного использования в приложениях, с теми же возможностями, что и функции, определенные с помощью `def`.
- B. Они позволяют определять небольшие анонимные функции в одной строке, обычно используемые там, где объекты функций требуются на короткие периоды, например, с функциями, такими как `map()` или `filter()`.
- C. Этот тип функции автоматически управляет распределением памяти и сборкой мусора, значительно повышая производительность приложения.
- D. Лямбда-функции в первую очередь используются для объявления и управления глобальными переменными в локальных областях видимости для улучшения модульности и повторного использования кода.

**Правильный ответ: B**

**Объяснение:**

Лямбда-функции в Python - это анонимные функции, то есть функции без имени. Они определяются с помощью ключевого слова `lambda` и используются для создания простых функций "на лету" в одну строку.

*   **Вариант A** не верен: Лямбда-функции не предназначены для постоянного использования и имеют ограниченные возможности по сравнению с обычными функциями, созданными с помощью `def`.

*   **Вариант B** верен: Лямбда-функции - это анонимные функции, определяемые в одну строку, и они обычно используются, когда нужна простая функция для кратковременного использования (например, при передаче в `map()`, `filter()`, `sort()`).
    
*   **Вариант C** не верен: Лямбда-функции не управляют памятью автоматически. Они работают так же, как обычные функции с точки зрения управления памятью.

*   **Вариант D** не верен: Лямбда-функции не связаны с управлением глобальными переменными.

**Ключевые характеристики лямбда-функций:**

1.  **Анонимность:**  Лямбда-функции не имеют имени, в отличие от обычных функций, определенных с помощью `def`.
2.  **Компактность:**  Они записываются в одну строку и могут содержать только одно выражение.
3.  **Область применения:** Лямбда-функции часто используются в качестве аргументов для функций высшего порядка, таких как `map()`, `filter()`, `sorted()` и т.д., где нужно передать простую функцию для обработки данных.
4.  **Ограничения:** Лямбда-функции не могут содержать множественные выражения или сложные конструкции, например циклы и условные операторы.

**Пример:**

```python
# Пример использования lambda с map()
numbers: list[int] = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Квадраты чисел: {squared_numbers}") # Вывод: Квадраты чисел: [1, 4, 9, 16, 25]

# Пример использования lambda с filter()
numbers: list[int] = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Чётные числа: {even_numbers}") # Вывод: Чётные числа: [2, 4, 6]

# Пример использования лямбда с сортировкой списка
points: list[tuple[int, int]] = [(3, 1), (1, 2), (2, 3)]
sorted_points = sorted(points, key=lambda p: p[1])
print(f"Сортировка по 2ому элементу кортежа: {sorted_points}") # Вывод: Сортировка по 2ому элементу кортежа: [(3, 1), (1, 2), (2, 3)]
```

**В результате:**
*   Лямбда-функция используется для возведения в квадрат каждого элемента списка numbers с помощью `map()`.
*   Лямбда-функция используется для фильтрации четных чисел из списка `numbers` c помощью `filter()`.
*  Лямбда-функция используется для сортировки списка кортежей `points` по второму элементу.

Таким образом, **вариант B** является правильным ответом.

### `question_644.md`

**Вопрос 644.** Какие методы в Python используются для преобразования строки в верхний и нижний регистр?

-   A.  Используйте методы `uppercase()` и `lowercase()`.
-   B.  Используйте методы `toUpperCase()` и `toLowerCase()`.
-   C.  Используйте методы `upper()` и `lower()`.
-   D.  Используйте функции `toUpper()` и `toLower()`.

**Правильный ответ: C**

**Объяснение:**

В Python для преобразования строк в верхний и нижний регистр используются встроенные методы строк `upper()` и `lower()`.

*   **Метод `upper()`:**
    *   **Преобразование в верхний регистр:**  Преобразует все символы строки в верхний регистр.
    *   **Строка:** Применяется к строковым объектам.
    *   **Возвращает новую строку:**  Не изменяет исходную строку, а возвращает новую.
*  **Метод `lower()`:**
     *   **Преобразование в нижний регистр:** Преобразует все символы строки в нижний регистр.
     *   **Строка:** Применяется к строковым объектам.
     *   **Возвращает новую строку:** Не изменяет исходную строку, а возвращает новую.

**Примеры:**

```python
# Пример 1: Преобразование в верхний регистр
small_word = 'potatocake'
upper_word = small_word.upper()
print(f"Исходная строка: {small_word}") # Выведет potatocake
print(f"Строка в верхнем регистре: {upper_word}")  # Выведет: POTATOCAKE

# Пример 2: Преобразование в нижний регистр
big_word = 'FISHCAKE'
lower_word = big_word.lower()
print(f"Исходная строка: {big_word}")
print(f"Строка в нижнем регистре: {lower_word}")  # Выведет: fishcake

# Пример 3: использование с пробелами
my_string = "  test String  "
print(f"'{my_string.upper()}'") # Выведет: '  TEST STRING  '
print(f"'{my_string.lower()}'") # Выведет: '  test string  '
# Пример 4:  различные символы
my_string2 = "АБВ гДЖ  123  "
print(f"'{my_string2.upper()}'")  # Выведет 'АБВ ГДЖ  123  '
print(f"'{my_string2.lower()}'")  # Выведет 'абв гдж  123  '
```

**Разбор вариантов:**
*  **A. Используйте методы `uppercase()` и `lowercase()`.:** Неправильно.
*   **B. Используйте методы `toUpperCase()` и `toLowerCase()`.:** Неправильно.
*  **C. Используйте методы `upper()` и `lower()`.:** Правильно.
*   **D. Используйте функции `toUpper()` и `toLower()`.:** Неправильно.

**В результате:**
* Методы  `upper()` и `lower()` используются для преобразования строк в верхний и нижний регистр соответственно.
*   Методы возвращают новый обьект строки,  исходная строка не меняется.

Таким образом, правильным ответом является **C. Используйте методы `upper()` и `lower()`.**

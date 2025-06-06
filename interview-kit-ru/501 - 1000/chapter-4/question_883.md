### `question_882.md`

**Вопрос 882.** Если `my_list = [-1, 2, 31, -44, 5, -6]`, что вернет выражение `my_list[-1]`?

A.  `-1`
B.  `5`
C.  `6`
D.  `-6`

**Правильный ответ: D**

**Объяснение:**

В Python списки индексируются с нуля. Кроме того, поддерживается использование отрицательных индексов для доступа к элементам с конца списка.

*   **Положительная индексация:** `my_list[0]` — первый элемент, `my_list[1]` — второй и так далее.
*   **Отрицательная индексация:** `my_list[-1]` — последний элемент, `my_list[-2]` — предпоследний и так далее.

1.  `my_list = [-1, 2, 31, -44, 5, -6]` - Создается список.
2.  `my_list[-1]` - Обращение к элементу с индексом -1, что соответствует последнему элементу списка.

*   **Вариант A не верен:** `my_list[0]` = `-1`
*   **Вариант B не верен:** `my_list[-2]` = `5`
*   **Вариант C не верен:** `6` не является корректным, потому что значение, хранящееся в ячейке списка отрицательное
*   **Вариант D верен:** Это правильный ответ.

**В результате:**

Выражение `my_list[-1]` возвращает последний элемент списка, который в данном случае равен `-6`.

Таким образом, вариант D является правильным.
### `question_695.md`

**Вопрос 695.** Дан массив `capacity`, представляющий вместимость `n` сумок, и массив `rocks`, где `rocks[i]` — это количество камней, уже находящихся в `i`-ой сумке. Также дано целое число `additionalRocks`, представляющее количество камней, которые можно добавить в любые сумки. Разработайте алгоритм, который вычисляет максимальное количество сумок, которое можно заполнить, распределив `additionalRocks`.

**Примеры:**

```
Ввод: capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2
Вывод: 3

Ввод: capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100
Вывод: 3
```

- A. Для решения этой задачи нужно сначала отсортировать массив capacity, затем последовательно заполнять сумки, пока не закончатся камни.
- B. Для решения задачи нужно сначала отсортировать разницу между capacity и rocks, а затем последовательно заполнять сумки пока не закончатся камни.
- C.  Для решения задачи, нужно перебрать все комбинации, чтобы получить наиболее оптимальный результат, что сделает задачу неэффективной.
- D. Для решения задачи нужно использовать жадный алгоритм, который сначала заполняет сумки с наименьшей разницей между вместимостью и количеством камней в них.

**Правильный ответ: B**

**Объяснение:**

Для решения этой задачи можно использовать жадный алгоритм, который заключается в следующем:  создается новый список с разницей между capacity и rocks, который сортируется в порядке возрастания, а затем,  камни  последовательно распределяются в сумки в зависимости от их величины, пока  дополнительные камни `additionalRocks` не закончатся.

*  **Алгоритм (жадный подход):**
    1.   **Вычисление разницы:** Создаем список, где каждый элемент это разница между `capacity[i]` и `rocks[i]`, т.е. сколько камней нужно добавить в каждую сумку.
    2. **Сортировка:** Сортируем этот список по возрастанию.
    3.  **Итерация и распределение:** Итерируемся по отсортированному списку и в каждой итерации добавляем необходимое кол-во камней в сумку, если `additionalRocks` хватает.
         * Если `additionalRocks`  не хватает для заполнения всех сумок, то прерываем цикл.
   4.   **Подсчет:** Считаем сколько сумок мы смогли заполнить.
*   **Почему это работает:**
    *   Жадный подход заключается в том, что мы сначала заполняем те сумки, которые требуют меньшее количество камней.
   *    На каждом этапе выбора локально лучшего решения (заполнять сумки по минимуму), мы  получим глобально оптимальное решение.

* **Преимущества алгоритма:**
    * **Оптимальность:** Жадный подход обеспечивает оптимальное решение для поставленной задачи.
    *  **Линейная сложность:**  Временная сложность равна O(n log n) из за необходимости сортировки списка.
    *   **Простота:** Легко реализуется.

**Примеры (псевдокод):**
```
function maximum_filled_bags(capacity, rocks, additionalRocks):
  differences = []
  for i in range(length(capacity)):
    differences.append(capacity[i] - rocks[i])
  sort differences
  count = 0
  for i in differences:
    if additionalRocks >= differences[i]:
        additionalRocks -= differences[i]
        count += 1
  return count
```
**Примеры реализации в Python:**

```python
def maximum_filled_bags(capacity, rocks, additionalRocks):
    differences = []
    for i in range(len(capacity)):
        differences.append(capacity[i] - rocks[i])
    differences.sort()
    count = 0
    for diff in differences:
        if additionalRocks >= diff:
            additionalRocks -= diff
            count += 1
        else:
            break
    return count

capacity1 = [2,3,4,5]
rocks1 = [1,2,4,4]
additionalRocks1 = 2
print(f"Ввод: capacity = {capacity1}, rocks = {rocks1}, additionalRocks = {additionalRocks1}")
print(f"Вывод: {maximum_filled_bags(capacity1, rocks1, additionalRocks1)}") # Вывод: 3

capacity2 = [10,2,2]
rocks2 = [2,2,0]
additionalRocks2 = 100
print(f"Ввод: capacity = {capacity2}, rocks = {rocks2}, additionalRocks = {additionalRocks2}")
print(f"Вывод: {maximum_filled_bags(capacity2, rocks2, additionalRocks2)}") # Вывод: 3
```

**Разбор вариантов:**
*  **A. Для решения этой задачи нужно сначала отсортировать массив capacity, затем последовательно заполнять сумки, пока не закончатся камни.:** Неправильно.
*  **B. Для решения этой задачи нужно сначала отсортировать разницу между capacity и rocks, а затем последовательно заполнять сумки пока не закончатся камни.:** Правильно.
*  **C. Для решения задачи, нужно перебрать все комбинации, чтобы получить наиболее оптимальный результат, что сделает задачу неэффективной.:** Неправильно. Этот подход займет O(2^n) времени.
*   **D. Для решения этой задачи нужно использовать жадный алгоритм, который сначала заполняет сумки с наименьшей разницей между вместимостью и количеством камней в них.:** Правильно, но не достаточно, так как не описана реализация.

**В результате:**
*  Жадный алгоритм является эффективным для решения данной задачи.
*   Алгоритм сортирует разницы между вместимостью и количеством камней для каждой сумки.
*  Позволяет получить максимальное количество сумок, которые можно заполнить, используя  `additionalRocks`.

Таким образом, правильным ответом является **B. Для решения этой задачи нужно сначала отсортировать разницу между capacity и rocks, а затем последовательно заполнять сумки пока не закончатся камни.**

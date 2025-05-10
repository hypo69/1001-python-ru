### `question_761.md`

**Вопрос 761.** Дан указатель на голову односвязного списка `head`. Разработайте алгоритм на Python для сортировки узлов списка по значению в порядке возрастания, с временной сложностью `O(n log n)` и пространственной сложностью `O(1)`.

**Примеры:**

```
Ввод: head = [4,2,1,3]
Вывод: [1,2,3,4]

Ввод: head = [-1,5,3,4,0]
Вывод: [-1,0,3,4,5]
```

- A. Для решения задачи нужно использовать алгоритм сортировки пузырьком (bubble sort) так как он является простым в реализации.
- B. Для решения задачи нужно использовать быструю сортировку (quick sort).
- C. Для решения задачи нужно использовать сортировку слиянием (merge sort),  используя рекурсивный подход и разбиение списка на части.
- D. Для решения задачи подойдет только алгоритм сортировки выбором (selection sort).

**Правильный ответ: C**

**Объяснение:**

Для решения задачи сортировки односвязного списка с ограничением по временной сложности `O(n log n)` и пространственной сложности `O(1)`, наиболее подходящим является использование алгоритма сортировки слиянием (Merge Sort).  Сортировка слиянием хорошо подходит для связных списков, так как не требует постоянного доступа к элементам, и может быть  реализована с использованием рекурсии  за `O(log n)` , что в данном случае не создаст  дополнительную память на стеке, из за особенностей алгоритма  (с разбиением на части, а не проход от начала до конца).

*   **Алгоритм (сортировка слиянием):**
    1.  **Рекурсивное деление:**
       *  Находим середину списка, и делим список на две части (для этого используем два указателя: slow, fast).
       *  Рекурсивно вызываем  функцию  для сортировки левой и правой части списка.
       *   **Базовый случай:** Если список состоит из нуля или одного элемента, возвращаем его без изменений.
    2.   **Слияние:** Используем  вспомогательную функцию `merge` для слияния двух отсортированных списков:
        *   Создаем новый список `merged_list`  и сравниваем  элементы с  левого и правого подсписка и добавляем их по возрастанию в `merged_list`.
       *   Добавляем оставшиеся элементы  последовательно, если они остались после завершения цикла.
       *   Возвращаем  результат из  `merged_list` .

*   **Преимущества алгоритма:**
    *   **Сложность O(n log n):** Имеет временную сложность  `O(n log n)`.
    *   **Использование рекурсии:** Разбиение на подзадачи  с помощью рекурсии, позволяет легко реализовать слияние.
    *   **Эффективность:**  Сортировка  списка происходит на месте без использования дополнительной  памяти (только  указатели).
*   **Почему другие варианты не подходят:**
     * **Bubble sort, Insertion Sort, Selection Sort:** имеют квадратичную сложность `O(n^2)`,  и не подходят для этой задачи.
      * **Quick sort:**  Quick sort на связанном списке  не всегда эффективен, а так же реализация  его не является простой задачей.

**Примеры (псевдокод):**
```
function sort_linked_list(head):
   if head is null or head.next is null
     return head
     middle = find middle of list with pointers
    left = head;
   right  =  middle.next
   middle.next = null # split
   left =  sort_linked_list(left);
  right = sort_linked_list(right);
    return merge (left, right)

function merge(left, right):
   new_head = create empty list
  while left and right are not null:
      if left.val <= right.val
           append left to  new_head
           left=left.next
      else:
         append right to new_head
           right=right.next
    append to new_head all elements of  left or right if still not done.
  return new_head
```
**Примеры реализации в Python:**
```python
class ListNode:
   def __init__(self, val=0, next=None):
     self.val = val
     self.next = next


def sort_linked_list(head):
    if not head or not head.next:
        return head

    # find middle node
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow
    right_part = mid.next
    mid.next = None # разрываем на два списка


    left_part = sort_linked_list(head)
    right_part = sort_linked_list(right_part)
    return merge(left_part, right_part)

def merge(left, right):
   dummy = ListNode(0) # фиктивный узел.
   curr = dummy
   while left and right:
        if left.val <= right.val:
           curr.next=left
           left = left.next
        else:
           curr.next=right
           right = right.next
        curr = curr.next

   if left:
       curr.next = left
   elif right:
        curr.next = right

   return dummy.next

# helper function to print list
def print_linked_list(head):
    res = []
    while head:
      res.append(head.val)
      head = head.next
    print(res)


head1 = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
print(f"Ввод: head = [4,2,1,3]")
head1_sorted = sort_linked_list(head1)
print("Вывод: ", end = "")
print_linked_list(head1_sorted) # Выведет: [1, 2, 3, 4]

head2 = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
print(f"Ввод: head = [-1,5,3,4,0]")
head2_sorted = sort_linked_list(head2)
print("Вывод: ", end = "")
print_linked_list(head2_sorted) #  Выведет: [-1, 0, 3, 4, 5]

```
**Разбор вариантов:**

*  **A. Для решения задачи нужно использовать алгоритм сортировки пузырьком (bubble sort) так как он является простым в реализации.:** Неправильно. Сортировка пузырьком имеет сложность O(n^2).
*   **B. Для решения задачи нужно использовать быструю сортировку (quick sort).:** Неправильно.  Быстрая сортировка  в связных списках не так эффективна.
*  **C. Для решения задачи нужно использовать сортировку слиянием (merge sort),  используя рекурсивный подход и разбиение списка на части.:** Правильно.
*   **D. Для решения задачи подойдет только алгоритм сортировки выбором (selection sort).:** Неправильно. Сортировка выбором имеет сложность O(n^2).

**В результате:**
*  Алгоритм сортировки слиянием позволяет отсортировать связанный список с временной сложностью `O(n log n)`.
*  Рекурсия используется для разбиения  списка на подсписки, а  функция `merge()` - для их слияния.
*   Алгоритм не использует  дополнительную память.

Таким образом, правильным ответом является **C. Для решения задачи нужно использовать сортировку слиянием (merge sort),  используя рекурсивный подход и разбиение списка на части.**

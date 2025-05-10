### `question_727.md`

**Вопрос 727.** Даны два списка: `preorder` (предзаказный обход) и `inorder` (инфиксный обход), которые представляют обходы одного и того же бинарного дерева. Разработайте алгоритм, который строит бинарное дерево из этих списков, и представьте результат в виде ASCII кода.

*   **Предзаказный обход (preorder):** Корень -> Левый поддерево -> Правый поддерево.
*   **Инфиксный обход (inorder):** Левый поддерево -> Корень -> Правый поддерево.

**Изображение дерева в ASCII:**

```
    3
   / \
  9  20
    /  \
   15  7
```
**Примеры:**
```
Ввод:  preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Вывод: [3,9,20,null,null,15,7]

Ввод: preorder = [-1], inorder = [-1]
Вывод: [-1]
```
-   A.  Для решения задачи нужно использовать метод вставки элементов в дерево на основе их значения, где левый ребенок меньше корня, а правый больше.
-  B. Для решения задачи необходимо использовать рекурсивный алгоритм, который построит дерево по заданным обходам.
-  C. Для решения задачи необходимо использовать алгоритм, который обойдет дерево в ширину (BFS).
-   D.  Для решения задачи подойдет только алгоритм линейного поиска.

**Правильный ответ: B**

**Объяснение:**

Для построения бинарного дерева из его предзаказного (preorder) и инфиксного (inorder) обходов, оптимальным будет использование рекурсивного алгоритма. Рекурсия позволяет обрабатывать поддеревья и строить дерево пошагово.

*   **Алгоритм (рекурсивный):**
    1.  **Базовые случаи:**
         *  Если `preorder` или `inorder` пусты, возвращаем `null`.
    2.   **Корень:** Первый элемент `preorder` является корнем текущего дерева.
       *   Создаем узел с этим значением `root = TreeNode(preorder[0])`.
    3. **Ищем корень в inorder:**  Находим индекс корня в `inorder` списке.  Этот индекс разделяет `inorder` на левую и правую части.
         *  Индекс `root_index`  указывает на позицию корня в  `inorder`.
    4.  **Построение левого поддерева:**
         *   Выделяем части `preorder` и  `inorder` которые относятся к левому поддереву, и рекурсивно вызываем  функцию для левого поддерева.
             * `preorder_left = preorder[1 : root_index +1]`
           *   `inorder_left = inorder[ : root_index]`
           *    `root.left  =  build_tree(preorder_left, inorder_left)`
    5.   **Построение правого поддерева:**
          *   Выделяем части `preorder` и `inorder` которые относятся к правому поддереву, и рекурсивно вызываем  функцию для правого поддерева.
          *  `preorder_right = preorder[root_index + 1:]`
          *  `inorder_right = inorder[root_index + 1 : ]`
          *  `root.right  = build_tree(preorder_right, inorder_right)`

    6. **Возвращение корня:**  Возвращаем корень, который представляет собой дерево.

*   **Преимущества алгоритма:**
    *   **Рекурсивный обход:** Позволяет легко обходить дерево и строить его на каждом шаге.
    *   **Чёткая структура:** Разбивает задачу на подзадачи, что позволяет реализовать алгоритм с минимальным количеством кода.

**Примеры (псевдокод):**
```
function build_tree(preorder, inorder):
    if preorder is empty:
        return null
    root_val = preorder[0]
    root = new TreeNode(root_val)
    root_index = find_index(root_val, inorder)
    preorder_left = preorder[1:root_index + 1]
    inorder_left = inorder[0:root_index]
    root.left = build_tree(preorder_left, inorder_left)
    preorder_right = preorder[root_index + 1:]
    inorder_right = inorder[root_index + 1: ]
    root.right = build_tree(preorder_right, inorder_right)
     return root
```
**Примеры реализации в Python:**

```python
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def build_tree(preorder, inorder):
    if not preorder:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    root_index = inorder.index(root_val)
    preorder_left = preorder[1:root_index + 1]
    inorder_left = inorder[ : root_index]
    root.left = build_tree(preorder_left, inorder_left)
    preorder_right = preorder[root_index + 1:]
    inorder_right = inorder[root_index + 1: ]
    root.right = build_tree(preorder_right, inorder_right)
    return root

# функция для вывода дерева в виде списка

def print_tree(root):
    if not root:
      return [None]
    else:
       return [root.val] + print_tree(root.left) + print_tree(root.right)



preorder1 = [3, 9, 20, 15, 7]
inorder1 = [9, 3, 15, 20, 7]
root1 = build_tree(preorder1, inorder1)
print(f"Ввод:  preorder = {preorder1}, inorder = {inorder1}")
print(f"Вывод: {print_tree(root1)}") # Выведет: [3, 9, None, None, 20, 15, None, None, 7, None, None]

preorder2 = [-1]
inorder2 = [-1]
root2 = build_tree(preorder2, inorder2)
print(f"Ввод:  preorder = {preorder2}, inorder = {inorder2}")
print(f"Вывод: {print_tree(root2)}") # Выведет: [-1]
```

**Разбор вариантов:**

*  **A. Для решения задачи нужно использовать метод вставки элементов в дерево на основе их значения, где левый ребенок меньше корня, а правый больше.:** Неправильно. Этот метод работает только с BST, а входные данные не гарантируют этого.
* **B. Для решения задачи необходимо использовать рекурсивный алгоритм, который построит дерево по заданным обходам.:** Правильно.
*   **C. Для решения задачи необходимо использовать алгоритм, который обойдет дерево в ширину (BFS).:** Неправильно, BFS не позволяет строить дерево, используя preorder и inorder обходы.
*   **D. Для решения задачи подойдет только алгоритм линейного поиска.:** Неправильно.

**В результате:**
*  Рекурсивный алгоритм эффективно строит бинарное дерево, используя  preorder и inorder обходы.
*  Алгоритм разделяет  списки в зависимости от расположения корня, используя при этом  свойства обхода деревьев.

Таким образом, правильным ответом является **B. Для решения задачи необходимо использовать рекурсивный алгоритм, который построит дерево по заданным обходам.**

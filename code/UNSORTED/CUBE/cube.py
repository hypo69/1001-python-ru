"""
CUBE
=================

Сложность: 5
-----------------

Игра "Куб" - это игра-головоломка, где игрок должен собрать куб, перемещая его грани. Куб представлен в виде матрицы 3x3, где каждая ячейка представляет собой грань куба. Игрок может перемещать грани куба вверх, вниз, влево и вправо. Цель игры - собрать куб, расположив грани в правильном порядке.
Правила игры:
1. Куб представлен в виде матрицы 3x3.
2. Игрок может перемещать грани куба, вводя команды: U (вверх), D (вниз), L (влево), R (вправо).
3. Цель игры - собрать куб, расположив грани в правильном порядке.
4. Начальная позиция куба генерируется случайным образом.
5. Игра заканчивается, когда куб собран, то есть когда все грани расположены в правильном порядке.
-----------------
Алгоритм:
1. Инициализировать куб случайными значениями от 1 до 9 в виде матрицы 3x3.
2. Вывести куб на экран.
3. Начать игровой цикл:
    3.1. Запросить у игрока ввод команды для перемещения грани куба (U, D, L, R).
    3.2. Выполнить перемещение грани в соответствии с командой:
       - Если команда "U", то сдвинуть все ряды вверх.
       - Если команда "D", то сдвинуть все ряды вниз.
       - Если команда "L", то сдвинуть все столбцы влево.
       - Если команда "R", то сдвинуть все столбцы вправо.
    3.3. Вывести куб на экран.
    3.4. Проверить, собран ли куб.
    3.5. Если куб собран, вывести сообщение о победе и закончить игру.
    3.6. Если куб не собран, вернуться к шагу 3.1.
-----------------

"""
import random

def generate_cube():
    """Генерирует случайный куб 3x3."""
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    cube = [numbers[i:i+3] for i in range(0, 9, 3)]
    return cube

def display_cube(cube):
    """Выводит куб на экран."""
    for row in cube:
        print('  '.join(map(str, row)))

def move_cube(cube, move):
    """Перемещает грани куба."""
    if move == 'U':
        # сдвигаем все ряды вверх
        temp = cube[0]
        for i in range(2):
            cube[i] = cube[i+1]
        cube[2] = temp
    elif move == 'D':
        # сдвигаем все ряды вниз
        temp = cube[2]
        for i in range(2, 0, -1):
            cube[i] = cube[i-1]
        cube[0] = temp
    elif move == 'L':
        # сдвигаем все столбцы влево
        temp = [row[0] for row in cube]
        for i in range(3):
            for j in range(2):
                cube[i][j] = cube[i][j+1]
            cube[i][2] = temp[i]
    elif move == 'R':
         # сдвигаем все столбцы вправо
        temp = [row[2] for row in cube]
        for i in range(3):
            for j in range(2, 0, -1):
                cube[i][j] = cube[i][j-1]
            cube[i][0] = temp[i]
    return cube

def is_solved(cube):
  """Проверяет, собран ли куб."""
  # Проверка, что все числа идут по порядку от 1 до 9
  expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  actual = []
  for row in cube:
    actual.extend(row)
  return actual == expected

# Инициализация куба
cube = generate_cube()
# Вывод куба на экран
display_cube(cube)

# Основной игровой цикл
while True:
    # Запрашиваем ввод хода у пользователя
    move = input("Введите ход (U, D, L, R): ").upper()
    # Проверяем корректность введенного хода
    if move not in ['U', 'D', 'L', 'R']:
        print("Неверный ход. Попробуйте еще раз.")
        continue
    # Перемещаем грани куба
    cube = move_cube(cube, move)
    # Вывод куба на экран
    display_cube(cube)
    # Проверяем, собран ли куб
    if is_solved(cube):
        print("Поздравляю! Вы собрали куб!")
        break # Завершаем цикл, если куб собран

"""
Объяснение кода:
1.  **Импорт модуля `random`**:
   -  `import random`: Импортирует модуль `random`, который используется для перемешивания элементов куба.
2.  **Функция `generate_cube()`**:
    -   `numbers = list(range(1, 10))`: Создает список чисел от 1 до 9, который будет использоваться для заполнения куба.
    -   `random.shuffle(numbers)`: Перемешивает список чисел в случайном порядке.
    -   `cube = [numbers[i:i+3] for i in range(0, 9, 3)]`: Создает матрицу 3x3 (куб) из перемешанных чисел.
    -   Возвращает созданный куб.
3.  **Функция `display_cube(cube)`**:
    -   Выводит текущее состояние куба на экран, форматируя его в виде матрицы.
4.  **Функция `move_cube(cube, move)`**:
    -   Получает куб и ход (`move`) в качестве аргументов.
    -   Выполняет перемещение граней куба в зависимости от введенной команды.
        -   **`if move == 'U':`**:  Сдвигает все ряды куба вверх.
        -   **`elif move == 'D':`**: Сдвигает все ряды куба вниз.
        -   **`elif move == 'L':`**: Сдвигает все столбцы куба влево.
        -   **`elif move == 'R':`**: Сдвигает все столбцы куба вправо.
    -   Возвращает куб после перемещения.
5.  **Функция `is_solved(cube)`**:
    -   Проверяет, собран ли куб, сравнивая текущую последовательность чисел с ожидаемой последовательностью (1-9).
    -   `expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]`: Создает список с ожидаемой последовательностью чисел.
    -   `actual = []`: Инициализирует пустой список для сохранения текущей последовательности чисел из куба.
    -   `for row in cube: actual.extend(row)`: Добавляет в список `actual` все числа из куба.
    -   `return actual == expected`: Возвращает `True`, если куб собран, и `False` в противном случае.
6.  **Основная часть программы**:
    -   `cube = generate_cube()`: Создает начальный куб.
    -   `display_cube(cube)`: Выводит начальный куб на экран.
    -   **Игровой цикл `while True:`**:
        -   `move = input("Введите ход (U, D, L, R): ").upper()`: Запрашивает у пользователя ввод хода и преобразует его в верхний регистр.
        -   **Проверка корректности хода**:
            - `if move not in ['U', 'D', 'L', 'R']:`: Проверяет, является ли ход допустимым (U, D, L или R).
            - `print("Неверный ход. Попробуйте еще раз.")`: Если ход недопустимый, выводит сообщение об ошибке и переходит к следующей итерации цикла.
            - `continue` - переходит к следующей итерации цикла
        -   `cube = move_cube(cube, move)`: Перемещает грани куба в соответствии с введенным ходом.
        -   `display_cube(cube)`: Выводит обновленный куб на экран.
        -   **Проверка, собран ли куб**:
            -   `if is_solved(cube):`: Проверяет, собран ли куб.
            -   `print("Поздравляю! Вы собрали куб!")`: Выводит сообщение о победе.
            -   `break`: Завершает игровой цикл.
"""

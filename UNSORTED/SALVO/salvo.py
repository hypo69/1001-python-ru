"""
SALVO:
=================
Сложность: 7
-----------------
Игра "SALVO" представляет собой морской бой, в котором игрок пытается потопить корабли противника, которые расположены на сетке. Игрок вводит координаты для стрельбы, и игра сообщает о попадании или промахе.
Цель игры - потопить все корабли противника за минимальное количество ходов.
Игра заканчивается, когда все корабли противника будут потоплены.

Правила игры:
1.  Игра происходит на сетке 10x10.
2.  Противник размещает корабли (количество и размеры не указаны в коде).
3.  Игрок вводит координаты (X, Y) для стрельбы.
4.  После каждого выстрела игра сообщает о результате: "MISS", "HIT", или "SINK".
5.  Игра заканчивается, когда все корабли противника потоплены.
6.  Счетчик выстрелов ведется.

-----------------
Алгоритм:
1. Инициализировать игровое поле (10x10).
2. Разместить корабли противника на поле (алгоритм размещения не указан в коде).
3. Инициализировать счетчик выстрелов нулем.
4. Начать цикл "пока не все корабли потоплены":
    4.1 Запросить у игрока координаты выстрела (X, Y).
    4.2 Увеличить счетчик выстрелов на 1.
    4.3 Если выстрел попал в корабль, то:
        4.3.1 Пометить клетку как "hit".
        4.3.2 Если корабль потоплен, то вывести сообщение "SINK".
        4.3.3 Если корабль не потоплен, вывести сообщение "HIT".
    4.4 Если выстрел не попал в корабль, то:
        4.4.1 Вывести сообщение "MISS".
5. Вывести сообщение о победе и количество выстрелов.
6. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeBoard["<p align='left'>Инициализация игрового поля:
    <code><b>board[10][10] = 0</b></code><br><code><b>ships = [x, y]...</b></code></p>"]
    InitializeBoard --> InitializeShots["<code><b>numberOfShots = 0</b></code>"]
    InitializeShots --> GameLoopStart{"Начало цикла: пока не все корабли потоплены"}
    GameLoopStart -- Да --> InputCoordinates["Ввод координат X,Y: <code><b>userX, userY</b></code>"]
    InputCoordinates --> IncreaseShots["<code><b>numberOfShots = numberOfShots + 1</b></code>"]
    IncreaseShots --> CheckHit{"Проверка: <code><b>board[userX][userY] == ship?</b></code>"}
    CheckHit -- Да --> MarkHit["Отметить клетку: <code><b>board[userX][userY] = 'hit'</b></code>"]
    MarkHit --> CheckSink{"Проверка: корабль потоплен?"}
    CheckSink -- Да --> OutputSink["Вывод сообщения: <b>SINK</b>"]
    CheckSink -- Нет --> OutputHit["Вывод сообщения: <b>HIT</b>"]
    OutputHit --> GameLoopStart
    OutputSink --> GameLoopStart
    CheckHit -- Нет --> OutputMiss["Вывод сообщения: <b>MISS</b>"]
    OutputMiss --> GameLoopStart
    GameLoopStart -- Нет --> OutputWin["Вывод сообщения: <b>YOU SUNK ALL MY SHIPS IN {numberOfShots} SHOTS</b>"]
    OutputWin --> End["Конец"]

```
Legenda:
    Start - Начало программы.
    InitializeBoard - Инициализация игрового поля размером 10x10 и размещение кораблей противника.
    InitializeShots - Инициализация счетчика выстрелов, устанавливая его в 0.
    GameLoopStart - Начало игрового цикла, который продолжается, пока не потоплены все корабли противника.
    InputCoordinates - Запрос у пользователя ввода координат X и Y для выстрела.
    IncreaseShots - Увеличение счетчика выстрелов на 1.
    CheckHit - Проверка, попал ли выстрел в корабль на игровом поле.
    MarkHit - Помечаем клетку на игровом поле как "hit", если был сделан выстрел по кораблю
    CheckSink - Проверка, потоплен ли корабль, по которому был произведен выстрел
    OutputSink - Вывод сообщения "SINK", если корабль потоплен.
    OutputHit - Вывод сообщения "HIT", если выстрел попал в корабль, но он не был потоплен.
    OutputMiss - Вывод сообщения "MISS", если выстрел не попал в корабль.
    OutputWin - Вывод сообщения о победе, когда все корабли противника потоплены, и количества выстрелов.
    End - Конец программы.
"""
import random

# Функция для создания игрового поля
def create_board(size):
    """Создает игровое поле заданного размера, заполненное нулями."""
    return [[0 for _ in range(size)] for _ in range(size)]

# Функция для случайного размещения кораблей (упрощенная версия)
def place_ships(board, ships_lengths):
    """Размещает корабли на игровом поле."""
    ships = []
    for length in ships_lengths:
        placed = False
        while not placed:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                row = random.randint(0, len(board) - 1)
                col = random.randint(0, len(board) - length)
                if all(board[row][col + i] == 0 for i in range(length)):
                     for i in range(length):
                         board[row][col + i] = 1
                     ships.append((row, col, orientation, length))
                     placed = True

            elif orientation == 'vertical':
                row = random.randint(0, len(board) - length)
                col = random.randint(0, len(board) - 1)
                if all(board[row + i][col] == 0 for i in range(length)):
                    for i in range(length):
                        board[row + i][col] = 1
                    ships.append((row, col, orientation, length))
                    placed = True

    return ships

def is_sunk(board, ship):
    row, col, orientation, length = ship
    if orientation == 'horizontal':
      return all(board[row][col + i] == 'hit' for i in range(length))
    else:
       return all(board[row + i][col] == 'hit' for i in range(length))
    
def print_board(board):
    """Выводит игровое поле в консоль, скрывая расположение кораблей."""
    size = len(board)
    print("  " + " ".join(str(i) for i in range(size)))
    for i, row in enumerate(board):
        print(str(i) + " " + " ".join('~' if cell == 0 or cell == 1 else cell for cell in row))

def play_salvo():
    """Основная функция игры Salvo."""
    board_size = 10
    ships_lengths = [2, 3, 4, 5]
    board = create_board(board_size)
    ships = place_ships(board, ships_lengths)
    numberOfShots = 0
    sunk_ships_count = 0
    print_board(board)
    while sunk_ships_count < len(ships):
        try:
            x = int(input("Введите координату X (0-9): "))
            y = int(input("Введите координату Y (0-9): "))
            if not (0 <= x < board_size and 0 <= y < board_size):
                print("Неверные координаты. Попробуйте снова.")
                continue

        except ValueError:
            print("Неверный ввод. Пожалуйста, введите числа от 0 до 9.")
            continue

        numberOfShots += 1
        if board[x][y] == 1:
            board[x][y] = 'hit'
            ship_sunk = False
            for ship in ships:
              if is_sunk(board, ship):
                  print("SINK")
                  ship_sunk = True
                  sunk_ships_count += 1
                  ships.remove(ship)
                  break
            if not ship_sunk:
              print("HIT")
        elif board[x][y] == 0:
            board[x][y] = 'miss'
            print("MISS")
        else:
           print("Вы уже стреляли по этим координатам")
        
        print_board(board)


    print(f"YOU SUNK ALL MY SHIPS IN {numberOfShots} SHOTS")

if __name__ == "__main__":
    play_salvo()
"""
Объяснение кода:
1.  **Импорт модуля `random`**:
    - `import random`: Импортирует модуль `random` для генерации случайных чисел и выбора случайного направления для размещения кораблей.

2.  **Функция `create_board(size)`**:
    -   `def create_board(size):`: Определяет функцию, которая создает игровое поле в виде двумерного списка.
    -   `return [[0 for _ in range(size)] for _ in range(size)]`: Возвращает список, представляющий игровое поле. Все ячейки инициализируются значением `0`, что означает пустое поле.

3.  **Функция `place_ships(board, ships_lengths)`**:
    - `def place_ships(board, ships_lengths)`: Определяет функцию для размещения кораблей на игровом поле. Принимает игровое поле `board` и список длин кораблей `ships_lengths`.
    - `ships = []`: Инициализирует список для хранения данных о размещенных кораблях.
    - `for length in ships_lengths:`: Начинает цикл по длинам кораблей
    -  `placed = False`: Инициализирует флаг для контроля размещения корабля.
    -  `while not placed:`: Начинает цикл, пока корабль не будет успешно размещен.
    - `orientation = random.choice(['horizontal', 'vertical'])`: Выбирает случайное направление (горизонтальное или вертикальное) для размещения корабля.
    -  Блоки `if orientation == 'horizontal'` и `elif orientation == 'vertical'` отвечают за попытку размещения корабля в выбранном направлении.
         -  `row = random.randint(0, len(board) - 1)` и `col = random.randint(0, len(board) - length)`: Генерируются случайные начальные координаты для размещения корабля.
        - `all(board[row][col + i] == 0 for i in range(length))`: Проверяется, что все клетки, необходимые для размещения корабля, свободны.
    -   Если все условия выполнены, то корабль размещается (`board[row][col + i] = 1`)  на поле, данные о корабле сохраняются в список `ships`, и цикл `while not placed` завершается.
    -  `return ships`: Функция возвращает список с данными о размещенных кораблях.

4.  **Функция `is_sunk(board, ship)`**:
    - `def is_sunk(board, ship):`: Функция, которая проверяет, потоплен ли корабль
    -  `row, col, orientation, length = ship`: распаковывает данные о корабле
    -   Блоки `if orientation == 'horizontal'` и `else` возвращают  `True`, если все части корабля помечены как 'hit', иначе возвращают `False`

5.  **Функция `print_board(board)`**:
    -   `def print_board(board):`: Определяет функцию для вывода игрового поля в консоль.
    -  `print("  " + " ".join(str(i) for i in range(size)))`: Выводит номера столбцов для удобства пользователя.
    - `print(str(i) + " " + " ".join('~' if cell == 0 or cell == 1 else cell for cell in row))`: Для каждой строки выводит номер строки и ячейки игрового поля:
        -   `'~'` выводится, если в ячейке `0` или `1` (пустая клетка или неповрежденная часть корабля).
        -   Значение ячейки выводится, если оно не `0` и не `1` (например, 'hit' или 'miss').

6.  **Функция `play_salvo()`**:
    -   `def play_salvo():`: Определяет главную функцию игры.
    -   `board_size = 10`: Задает размер игрового поля.
    -  `ships_lengths = [2, 3, 4, 5]`: Список длин кораблей для размещения.
    -   `board = create_board(board_size)`: Создает игровое поле.
    -  `ships = place_ships(board, ships_lengths)`: Размещает корабли на поле.
    -   `numberOfShots = 0`: Инициализирует счетчик выстрелов.
    -   `sunk_ships_count = 0`: Инициализирует счетчик потопленных кораблей.
    -   `print_board(board)`: Выводит начальное состояние игрового поля.
    -  `while sunk_ships_count < len(ships)`: Запускает игровой цикл, пока не все корабли потоплены.
     -   `try...except ValueError`: обрабатывает ошибку, если пользователь ввел не числа
    -  `x = int(input("Введите координату X (0-9): "))` и  `y = int(input("Введите координату Y (0-9): "))`  запрашивают координаты выстрела.
    -   `if not (0 <= x < board_size and 0 <= y < board_size):`: Проверяет, что координаты корректны.
    -  `numberOfShots += 1`: Увеличивает счетчик выстрелов.
        -   Блок `if board[x][y] == 1:` выполняется, если выстрел попал в корабль.
         - `board[x][y] = 'hit'` - отметка попадания в корабль
         -  перебирает все корабли и проверяет, потоплен ли какой-либо из них, с помощью функции `is_sunk`.
          - если корабль потоплен, то выводит сообщение, увеличивает счетчик потопленных кораблей и удаляет данные о потопленном корабле из списка `ships`
         -  если корабль не потоплен, то выводит сообщение `HIT`
      - `elif board[x][y] == 0:` выполняется, если выстрел не попал в корабль.
         -  `board[x][y] = 'miss'` помечает клетку, как клетку в которую был произведен выстрел, но не было попадания
         - выводит сообщение `MISS`
      -  `else:` выполняется, если по этим координатам уже был произведен выстрел.
    -   `print_board(board)`: Выводит текущее состояние игрового поля.
    -   `print(f"YOU SUNK ALL MY SHIPS IN {numberOfShots} SHOTS")`: Выводит сообщение о победе и количестве выстрелов.
7.  **Условный запуск**:
    -   `if __name__ == "__main__":`: Проверяет, что файл запущен как основной скрипт.
    -   `play_salvo()`: Вызывает функцию для запуска игры.

"""

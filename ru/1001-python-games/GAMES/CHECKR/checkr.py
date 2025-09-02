"""
CHECKR:
=================
Сложность: 5
-----------------
Игра "Шашки" - это текстовая реализация упрощенной версии игры в шашки. Игра происходит на доске 8x8, где игрок играет против компьютера. Цель игры - достичь противоположного конца доски одной из своих шашек, избегая при этом захвата шашек противника.

Правила игры:
1.  Игрок и компьютер ходят по очереди.
2.  Игрок управляет шашками, обозначаемыми '1'.
3.  Компьютер управляет шашками, обозначаемыми '2'.
4.  Доска представляет собой сетку 8x8, где '.' обозначает пустое место.
5.  Игрок вводит координаты текущей позиции и желаемой позиции.
6.  Ход шашки - перемещение на одну клетку по диагонали вперед.
7.  Шашка может перепрыгивать через шашку противника, если за ней есть свободное место.
8.  Если шашка достигает противоположного конца доски, она превращается в дамку (это в коде не реализовано).
9.  Компьютер делает случайный допустимый ход.
10. Игра заканчивается, если одна из сторон достигает конца доски или не имеет допустимых ходов.
-----------------
Алгоритм:
1.  Инициализировать доску 8x8 с начальным расположением шашек.
2.  Отрисовать доску.
3.  Начать игровой цикл:
    3.1. Запросить ввод хода игрока (текущая и желаемая позиции).
    3.2. Проверить валидность ввода.
    3.3. Если ввод невалидный, запросить повторный ввод.
    3.4. Выполнить ход игрока, если ход допустим.
    3.5. Проверить, достиг ли игрок противоположного конца доски. Если да, закончить игру.
    3.6. Ход компьютера:
        3.6.1. Найти все возможные ходы компьютера.
        3.6.2. Выбрать случайный ход из возможных.
        3.6.3. Выполнить ход компьютера.
    3.7. Проверить, достиг ли компьютер противоположного конца доски. Если да, закончить игру.
    3.8. Отрисовать доску.
4.  Если ни одна из сторон не выиграла, перейти к шагу 3.
5.  По окончании игры вывести сообщение о победе или поражении.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeBoard["Инициализация доски: <code><b>board[8][8]</b></code> с начальным расположением шашек"]
    InitializeBoard --> DrawBoard["Отрисовка доски"]
    DrawBoard --> GameLoopStart{"Начало игрового цикла"}
    GameLoopStart --> PlayerInput["Ввод хода игрока: <code><b>currentPosition, nextPosition</b></code>"]
    PlayerInput --> ValidateInput{"Проверка валидности ввода: <code><b>isInputValid(currentPosition, nextPosition)</b></code>"}
    ValidateInput -- Невалидный ввод --> PlayerInput
    ValidateInput -- Валидный ввод --> PlayerMove{"Выполнение хода игрока: <code><b>updateBoard(currentPosition, nextPosition)</b></code>"}
    PlayerMove --> PlayerWinCheck{"Проверка победы игрока: <code><b>checkWin(player)</b></code>"}
    PlayerWinCheck -- Да --> OutputPlayerWin["Вывод сообщения: <b>Игрок выиграл</b>"]
    OutputPlayerWin --> End["Конец"]
    PlayerWinCheck -- Нет --> ComputerTurn{"Ход компьютера"}
    ComputerTurn --> FindPossibleMoves["Поиск возможных ходов компьютера"]
    FindPossibleMoves --> ChooseRandomMove["Выбор случайного хода компьютера"]
    ChooseRandomMove --> ComputerMove{"Выполнение хода компьютера: <code><b>updateBoard(currentPosition, nextPosition)</b></code>"}
    ComputerMove --> ComputerWinCheck{"Проверка победы компьютера: <code><b>checkWin(computer)</b></code>"}
    ComputerWinCheck -- Да --> OutputComputerWin["Вывод сообщения: <b>Компьютер выиграл</b>"]
    OutputComputerWin --> End
    ComputerWinCheck -- Нет --> DrawBoard
     GameLoopStart  -- Конец Игры --> End
```
Legenda:
    Start - Начало программы.
    InitializeBoard - Инициализация игровой доски (8x8) с начальным расположением шашек.
    DrawBoard - Отрисовка текущего состояния игровой доски в консоль.
    GameLoopStart - Начало основного игрового цикла.
    PlayerInput - Запрос у игрока ввода координат текущей позиции и желаемой позиции для хода.
    ValidateInput - Проверка введенных координат на корректность и соответствие правилам игры.
    PlayerMove - Выполнение хода игрока на игровой доске.
    PlayerWinCheck - Проверка, достиг ли игрок условия победы (достижение противоположного конца доски).
    OutputPlayerWin - Вывод сообщения о победе игрока.
    ComputerTurn - Переход хода к компьютеру.
    FindPossibleMoves - Поиск всех возможных ходов для компьютера.
    ChooseRandomMove - Выбор случайного допустимого хода для компьютера.
    ComputerMove - Выполнение хода компьютера на игровой доске.
    ComputerWinCheck - Проверка, достиг ли компьютер условия победы (достижение противоположного конца доски).
    OutputComputerWin - Вывод сообщения о победе компьютера.
     End - Конец игры.
"""
import random

# Глобальные переменные для представления доски
BOARD_SIZE = 8
EMPTY = '.'
PLAYER = '1'
COMPUTER = '2'


def initialize_board():
    """Инициализирует доску 8x8 с начальным расположением шашек."""
    board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    # Размещаем шашки игрока и компьютера в начальных позициях
    for i in range(3):
        for j in range(BOARD_SIZE):
            if (i + j) % 2 != 0:
                board[i][j] = PLAYER
    for i in range(BOARD_SIZE - 3, BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if (i + j) % 2 != 0:
                board[i][j] = COMPUTER
    return board


def draw_board(board):
    """Отрисовывает текущее состояние доски в консоль."""
    print("  ", end="")
    for i in range(BOARD_SIZE):
        print(i, end=" ")
    print()
    for i, row in enumerate(board):
        print(i, " ".join(row))


def is_valid_move(board, row, col, new_row, new_col, player):
    """Проверяет, является ли ход игрока допустимым."""

    if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and 0 <= new_row < BOARD_SIZE and 0 <= new_col < BOARD_SIZE):
        return False

    if board[row][col] != player:
        return False

    if board[new_row][new_col] != EMPTY:
        return False

    row_diff = new_row - row
    col_diff = new_col - col
    
    if abs(row_diff) != 1 or abs(col_diff) != 1:
        return False
    
    if player == PLAYER and row_diff > 0:
        return False
    
    if player == COMPUTER and row_diff < 0:
        return False

    return True
def update_board(board, row, col, new_row, new_col):
    """Обновляет доску после хода."""
    board[new_row][new_col] = board[row][col]
    board[row][col] = EMPTY


def check_win(board, player):
    """Проверяет, достиг ли игрок или компьютер победы."""
    if player == PLAYER:
        for j in range(BOARD_SIZE):
          if board[BOARD_SIZE-1][j] == PLAYER:
            return True
    if player == COMPUTER:
        for j in range(BOARD_SIZE):
          if board[0][j] == COMPUTER:
            return True
    return False


def get_computer_moves(board):
    """Находит все возможные ходы компьютера."""
    moves = []
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == COMPUTER:
                for dr in [-1, 1]:
                    for dc in [-1, 1]:
                       new_row, new_col = row + dr , col + dc
                       if is_valid_move(board, row, col, new_row, new_col,COMPUTER):
                            moves.append((row, col, new_row, new_col))
    return moves


def computer_turn(board):
    """Выполняет ход компьютера."""
    possible_moves = get_computer_moves(board)
    if possible_moves:
        row, col, new_row, new_col = random.choice(possible_moves)
        update_board(board, row, col, new_row, new_col)


def player_turn(board):
    """Запрашивает и выполняет ход игрока."""
    while True:
        try:
            current_row = int(input("Введите строку текущей позиции (0-7): "))
            current_col = int(input("Введите столбец текущей позиции (0-7): "))
            new_row = int(input("Введите строку новой позиции (0-7): "))
            new_col = int(input("Введите столбец новой позиции (0-7): "))
            if is_valid_move(board, current_row, current_col, new_row, new_col, PLAYER):
                update_board(board, current_row, current_col, new_row, new_col)
                break
            else:
              print("Недопустимый ход, попробуйте еще раз.")
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите целые числа.")


def play_checkers():
    """Основная функция игры в шашки."""
    board = initialize_board()
    draw_board(board)
    while True:
        player_turn(board)
        if check_win(board, PLAYER):
            print("Поздравляю! Вы выиграли!")
            break
        
        computer_turn(board)
        if check_win(board, COMPUTER):
            print("Компьютер выиграл!")
            break
        draw_board(board)


if __name__ == "__main__":
    play_checkers()
"""
Объяснение кода:

1. **Импорт модуля random**:
   - `import random`: Импортирует модуль `random`, который используется для выбора случайного хода компьютера.

2. **Глобальные переменные**:
   - `BOARD_SIZE`: Размер доски (8x8).
   - `EMPTY`: Символ для пустой клетки.
   - `PLAYER`: Символ для шашки игрока ('1').
   - `COMPUTER`: Символ для шашки компьютера ('2').

3. **Функция `initialize_board()`**:
   - Создает и инициализирует игровую доску как список списков (двумерный массив).
   - Расставляет начальные позиции шашек игрока ('1') и компьютера ('2').

4. **Функция `draw_board(board)`**:
   - Принимает текущее состояние доски.
   - Выводит доску в консоль с нумерацией строк и столбцов для удобства пользователя.

5. **Функция `is_valid_move(board, row, col, new_row, new_col, player)`**:
   - Проверяет, является ли ход игрока или компьютера допустимым:
     - Проверка нахождения в пределах доски.
     - Проверка, принадлежит ли шашка игроку.
     - Проверка, является ли целевая клетка пустой.
     - Проверка на движение только по диагонали на одну клетку.
    - Проверка на движение шашки игрока только вперед.
    - Проверка на движение шашки компьютера только вперед.

6. **Функция `update_board(board, row, col, new_row, new_col)`**:
   - Обновляет доску после хода:
     - Перемещает шашку из текущей позиции в новую.
     - Помечает текущую позицию как пустую.

7.  **Функция `check_win(board, player)`**:
    - Проверяет, достиг ли игрок или компьютер конца доски, что означает победу.
    - Для игрока проверяется достижение шашкой последней строки.
    - Для компьютера проверяется достижение шашкой первой строки.

8.  **Функция `get_computer_moves(board)`**:
    - Находит все возможные ходы компьютера:
        - Проходит по всем клеткам доски и ищет шашки компьютера.
        - Проверяет все возможные диагональные ходы для каждой шашки.
        - Возвращает список кортежей (row, col, new_row, new_col) доступных ходов.

9.  **Функция `computer_turn(board)`**:
    - Выполняет ход компьютера:
        - Получает список возможных ходов.
        - Выбирает случайный ход из списка.
        - Обновляет доску в соответствии с выбранным ходом.
    
10.  **Функция `player_turn(board)`**:
     - Запрашивает у игрока ввод координат текущей позиции и желаемой позиции.
     - Проверяет валидность ввода.
     - Выполняет ход, если ввод валидный.
     - Если ввод невалидный, запрашивает повторный ввод.

11. **Функция `play_checkers()`**:
    - Основная функция игры:
        - Инициализирует доску.
        - Выводит доску на экран.
        - Запускает игровой цикл, пока не будет достигнута победа одной из сторон:
            - Ход игрока.
            - Проверка победы игрока.
            - Ход компьютера.
            - Проверка победы компьютера.
            - Вывод доски после каждого хода.

12. **Запуск игры**:
    - `if __name__ == "__main__":`: Этот блок гарантирует, что функция `play_checkers()` будет запущена, только если файл исполняется напрямую, а не импортируется как модуль.
    - `play_checkers()`: Вызывает функцию для начала игры.
"""

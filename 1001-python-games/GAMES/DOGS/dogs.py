"""
DOGS:
=================
Сложность: 5
-----------------
Игра "Собаки" представляет собой текстовую игру, в которой игрок управляет двумя собаками, и пытается поймать воров. Игрок вводит команды для перемещения собак, а воры перемещаются случайно. Цель игры - поймать воров за минимальное количество ходов.
Правила игры:
1. Игроку предоставляется поле размером 10x10. 
2. Две собаки и два вора располагаются на поле случайным образом.
3. Игрок управляет собаками, вводя команды:
    - 'L' - переместить обеих собак влево
    - 'R' - переместить обеих собак вправо
    - 'U' - переместить обеих собак вверх
    - 'D' - переместить обеих собак вниз
    - 'F' - переместить первую собаку
    - 'S' - переместить вторую собаку
4. При каждом ходе воры перемещаются случайно.
5. Цель игры - поймать воров, переместив собак в те же позиции, что и воры.
6. Игра заканчивается, когда обе собаки поймают воров.

-----------------
Алгоритм:
1. Инициализировать поле размером 10x10.
2. Разместить двух собак (D1 и D2) и двух воров (T1 и T2) в случайных позициях на поле.
3. Инициализировать счетчик ходов в 0.
4. Пока обе собаки не поймают воров:
    4.1 Увеличить счетчик ходов на 1.
    4.2 Вывести текущее состояние поля с позициями собак и воров.
    4.3 Запросить у игрока ввод команды перемещения собак (L, R, U, D, F, S).
    4.4 Обработать ввод игрока:
        - Если команда 'L': переместить обеих собак влево (если это возможно).
        - Если команда 'R': переместить обеих собак вправо (если это возможно).
        - Если команда 'U': переместить обеих собак вверх (если это возможно).
        - Если команда 'D': переместить обеих собак вниз (если это возможно).
        - Если команда 'F': переместить первую собаку в соответствии с пользовательским вводом (вверх, вниз, вправо, влево).
        - Если команда 'S': переместить вторую собаку в соответствии с пользовательским вводом (вверх, вниз, вправо, влево).
    4.5 Переместить воров (T1 и T2) в случайном направлении.
    4.6 Проверить, поймали ли собаки воров:
        - Если D1 == T1 и D2 == T2, то вывести сообщение о победе и завершить игру.
        - Если D1 == T2 и D2 == T1, то вывести сообщение о победе и завершить игру.
5. Вывести общее количество ходов, затраченное на поимку воров.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeGame["Инициализация игры:<br><code><b>
    field = 10x10<br>
    dog1 = random_position<br>
    dog2 = random_position<br>
    thief1 = random_position<br>
    thief2 = random_position<br>
    moves = 0
    </b></code>"]
    InitializeGame --> LoopStart{"Начало цикла: пока воры не пойманы"}
    LoopStart -- Да --> IncreaseMoves["<code><b>moves = moves + 1</b></code>"]
    IncreaseMoves --> DisplayField["Вывод поля<br>с позициями собак<br>и воров"]
    DisplayField --> InputCommand["Ввод команды<br>игроком: <code><b>command</b></code>"]
    InputCommand --> MoveDogs{"Перемещение<br>собак в соответствии<br>с командой"}
    MoveDogs --> MoveThieves["Перемещение<br>воров случайным<br>образом"]
    MoveThieves --> CheckCatch{"Проверка:<br><code><b>dog1 == thief1 and dog2 == thief2</b></code><br>или<br><code><b>dog1 == thief2 and dog2 == thief1</b></code>"}
     CheckCatch -- Да --> OutputWin["Вывод сообщения о победе и количестве ходов"]
    OutputWin --> End["Конец"]
    CheckCatch -- Нет --> LoopStart
    LoopStart -- Нет --> End
```
**Legenda**:
   - Start - Начало программы.
   - InitializeGame - Инициализация игровых переменных: создается игровое поле, задаются случайные начальные позиции для двух собак и двух воров, а также инициализируется счетчик ходов.
   - LoopStart - Начало цикла игры, который продолжается, пока воры не будут пойманы.
   - IncreaseMoves - Увеличение счетчика ходов.
   - DisplayField - Вывод текущего состояния игрового поля с позициями собак и воров.
   - InputCommand - Получение команды от игрока для перемещения собак.
   - MoveDogs - Перемещение собак на игровом поле в соответствии с полученной командой.
   - MoveThieves - Перемещение воров случайным образом на игровом поле.
   - CheckCatch - Проверка, пойманы ли воры. Условие выполнено, если координаты первой собаки совпадают с координатами первого вора, а координаты второй собаки совпадают с координатами второго вора, или наоборот.
   - OutputWin - Вывод сообщения о победе и количестве сделанных ходов.
   - End - Конец программы.
"""

import random

# Константы для размеров поля
FIELD_SIZE = 10

# Функция для создания игрового поля
def create_field():
    """
    Создает игровое поле размером FIELD_SIZE x FIELD_SIZE, представляя его как список списков.
    """
    return [['.' for _ in range(FIELD_SIZE)] for _ in range(FIELD_SIZE)]

# Функция для случайного размещения объекта на поле
def place_object(field, symbol):
  """
  Размещает объект (собаку или вора) на случайной свободной позиции на поле.

  :param field: Двумерный список, представляющий игровое поле.
  :param symbol: Символ объекта, который нужно разместить на поле.
  :return: Кортеж с координатами (row, col) размещенного объекта.
  """
  while True:
    row = random.randint(0, FIELD_SIZE - 1)
    col = random.randint(0, FIELD_SIZE - 1)
    if field[row][col] == '.': # Проверяем, что место свободно
      field[row][col] = symbol
      return row, col

# Функция для вывода поля на экран
def print_field(field):
  """
    Выводит текущее состояние игрового поля на экран.

    :param field: Двумерный список, представляющий игровое поле.
    """
  for row in field:
    print(' '.join(row))


# Функция для обработки ввода команд пользователя
def get_user_command():
  """
  Запрашивает у пользователя команду для перемещения собак.
  Команды:
    - 'L' - переместить обеих собак влево
    - 'R' - переместить обеих собак вправо
    - 'U' - переместить обеих собак вверх
    - 'D' - переместить обеих собак вниз
    - 'F' - переместить первую собаку
    - 'S' - переместить вторую собаку
  :return: Строка - команда пользователя.
  """
  while True:
        command = input("Введите команду (L/R/U/D/F/S): ").upper()
        if command in ('L', 'R', 'U', 'D', 'F', 'S'):
            return command
        else:
            print("Неверная команда. Попробуйте снова.")

# Функция для перемещения собак
def move_dogs(field, dog1, dog2, command):
    """
    Перемещает собак в соответствии с командой пользователя.
    :param field: игровое поле
    :param dog1: координаты первой собаки
    :param dog2: координаты второй собаки
    :param command: команда пользователя
    """
    dog1_row, dog1_col = dog1
    dog2_row, dog2_col = dog2
    # Перемещение обеих собак
    if command == 'L':
        if dog1_col > 0:
           field[dog1_row][dog1_col] = '.' # Очищаем старую позицию
           dog1_col -= 1
        if dog2_col > 0:
           field[dog2_row][dog2_col] = '.'
           dog2_col -= 1
    elif command == 'R':
        if dog1_col < FIELD_SIZE - 1:
          field[dog1_row][dog1_col] = '.'
          dog1_col += 1
        if dog2_col < FIELD_SIZE - 1:
          field[dog2_row][dog2_col] = '.'
          dog2_col += 1
    elif command == 'U':
        if dog1_row > 0:
           field[dog1_row][dog1_col] = '.'
           dog1_row -= 1
        if dog2_row > 0:
           field[dog2_row][dog2_col] = '.'
           dog2_row -= 1
    elif command == 'D':
        if dog1_row < FIELD_SIZE - 1:
          field[dog1_row][dog1_col] = '.'
          dog1_row += 1
        if dog2_row < FIELD_SIZE - 1:
           field[dog2_row][dog2_col] = '.'
           dog2_row += 1
    # Перемещение одной из собак
    elif command == 'F':
      while True:
          direction = input("Введите направление для первой собаки (L/R/U/D): ").upper()
          if direction in ('L', 'R', 'U', 'D'):
              break
          else:
            print("Неверное направление. Попробуйте снова.")
      field[dog1_row][dog1_col] = '.' # Очищаем старую позицию
      if direction == 'L' and dog1_col > 0:
          dog1_col -= 1
      elif direction == 'R' and dog1_col < FIELD_SIZE - 1:
          dog1_col += 1
      elif direction == 'U' and dog1_row > 0:
          dog1_row -= 1
      elif direction == 'D' and dog1_row < FIELD_SIZE - 1:
          dog1_row += 1
    elif command == 'S':
      while True:
        direction = input("Введите направление для второй собаки (L/R/U/D): ").upper()
        if direction in ('L', 'R', 'U', 'D'):
            break
        else:
            print("Неверное направление. Попробуйте снова.")
      field[dog2_row][dog2_col] = '.'  # Очищаем старую позицию
      if direction == 'L' and dog2_col > 0:
        dog2_col -= 1
      elif direction == 'R' and dog2_col < FIELD_SIZE - 1:
        dog2_col += 1
      elif direction == 'U' and dog2_row > 0:
        dog2_row -= 1
      elif direction == 'D' and dog2_row < FIELD_SIZE - 1:
        dog2_row += 1

    field[dog1_row][dog1_col] = 'D'
    field[dog2_row][dog2_col] = 'D'
    return (dog1_row, dog1_col), (dog2_row, dog2_col)


# Функция для перемещения воров
def move_thieves(field, thief1, thief2):
  """
    Перемещает воров случайным образом на игровом поле.

    :param field: Двумерный список, представляющий игровое поле.
    :param thief1: Координаты первого вора (row, col).
    :param thief2: Координаты второго вора (row, col).
    :return: Кортежи с новыми координатами воров ((row1, col1), (row2, col2)).
    """
  thief1_row, thief1_col = thief1
  thief2_row, thief2_col = thief2
  
  field[thief1_row][thief1_col] = '.'
  field[thief2_row][thief2_col] = '.'

  # Случайное перемещение первого вора
  while True:
        direction = random.choice(['L', 'R', 'U', 'D'])
        new_thief1_row, new_thief1_col = thief1_row, thief1_col
        if direction == 'L' and thief1_col > 0:
            new_thief1_col -= 1
        elif direction == 'R' and thief1_col < FIELD_SIZE - 1:
            new_thief1_col += 1
        elif direction == 'U' and thief1_row > 0:
            new_thief1_row -= 1
        elif direction == 'D' and thief1_row < FIELD_SIZE - 1:
            new_thief1_row += 1
        
        if field[new_thief1_row][new_thief1_col] == '.' or (new_thief1_row, new_thief1_col) == (thief2_row, thief2_col):
            thief1_row, thief1_col = new_thief1_row, new_thief1_col
            break

  # Случайное перемещение второго вора
  while True:
        direction = random.choice(['L', 'R', 'U', 'D'])
        new_thief2_row, new_thief2_col = thief2_row, thief2_col
        if direction == 'L' and thief2_col > 0:
            new_thief2_col -= 1
        elif direction == 'R' and thief2_col < FIELD_SIZE - 1:
            new_thief2_col += 1
        elif direction == 'U' and thief2_row > 0:
            new_thief2_row -= 1
        elif direction == 'D' and thief2_row < FIELD_SIZE - 1:
            new_thief2_row += 1
            
        if field[new_thief2_row][new_thief2_col] == '.' or (new_thief2_row, new_thief2_col) == (thief1_row, thief1_col):
            thief2_row, thief2_col = new_thief2_row, new_thief2_col
            break

  field[thief1_row][thief1_col] = 'T'
  field[thief2_row][thief2_col] = 'T'
  return (thief1_row, thief1_col), (thief2_row, thief2_col)


# Функция для проверки, пойманы ли воры
def check_catch(dog1, dog2, thief1, thief2):
  """
    Проверяет, поймали ли собаки воров. Возвращает True, если пойманы, False - в противном случае.
    :param dog1: Кортеж с координатами первой собаки (row, col).
    :param dog2: Кортеж с координатами второй собаки (row, col).
    :param thief1: Кортеж с координатами первого вора (row, col).
    :param thief2: Кортеж с координатами второго вора (row, col).
    :return: True, если воры пойманы, False в противном случае.
    """
  if (dog1 == thief1 and dog2 == thief2) or (dog1 == thief2 and dog2 == thief1):
    return True
  return False


# Основная функция игры
def play_dogs_game():
    """
    Основная функция, запускающая игру "Собаки".
    """
    # Инициализация игры
    field = create_field() # Создаем пустое поле
    dog1 = place_object(field, 'D') # Размещаем первую собаку
    dog2 = place_object(field, 'D') # Размещаем вторую собаку
    thief1 = place_object(field, 'T') # Размещаем первого вора
    thief2 = place_object(field, 'T') # Размещаем второго вора
    moves = 0 # Счетчик ходов

    # Основной игровой цикл
    while True:
        moves += 1
        print(f"Ход: {moves}")
        print_field(field) # Выводим текущее состояние поля
        
        command = get_user_command()
        dog1, dog2 = move_dogs(field, dog1, dog2, command)
        thief1, thief2 = move_thieves(field, thief1, thief2)

        # Проверяем, пойманы ли воры
        if check_catch(dog1, dog2, thief1, thief2):
            print_field(field)
            print(f"ПОЗДРАВЛЯЮ! Вы поймали воров за {moves} ходов!")
            break # Завершаем игру, если воры пойманы


# Запускаем игру, если скрипт запущен как основной
if __name__ == "__main__":
    play_dogs_game()

"""
Объяснение кода:
1. **Импорт модуля random:**
    -   `import random`: Импортирует модуль `random` для генерации случайных чисел и выбора случайных перемещений.
2. **Константа `FIELD_SIZE`**:
    -   `FIELD_SIZE = 10`: Определяет размер игрового поля.
3. **Функция `create_field()`**:
    -   Создает игровое поле размером `FIELD_SIZE x FIELD_SIZE` и возвращает его в виде списка списков, заполненных точками, представляющими пустые клетки.
4. **Функция `place_object(field, symbol)`**:
    -   Размещает объект (`symbol`) на случайной свободной позиции в `field`.
    -   Возвращает координаты размещенного объекта.
5. **Функция `print_field(field)`**:
    -   Выводит текущее состояние игрового поля `field` на экран.
6. **Функция `get_user_command()`**:
    -   Запрашивает у пользователя команду для управления собаками (L, R, U, D, F, S).
    -   Проверяет корректность ввода и возвращает команду в верхнем регистре.
7. **Функция `move_dogs(field, dog1, dog2, command)`**:
    -   Перемещает собак в соответствии с введенной командой:
        -   `L`, `R`, `U`, `D` - перемещают обеих собак.
        -   `F` - перемещает первую собаку в соответствии с дополнительным вводом направления (L, R, U, D).
        -   `S` - перемещает вторую собаку в соответствии с дополнительным вводом направления (L, R, U, D).
    -   Обновляет позиции собак на поле и возвращает новые координаты.
8. **Функция `move_thieves(field, thief1, thief2)`**:
    -   Перемещает воров на случайную свободную позицию.
    -   Обновляет позиции воров на поле и возвращает их новые координаты.
9. **Функция `check_catch(dog1, dog2, thief1, thief2)`**:
    -   Проверяет, пойманы ли воры. Возвращает `True`, если первая собака находится в той же позиции, что и первый вор, а вторая собака находится в той же позиции, что и второй вор, или наоборот, иначе возвращает `False`.
10. **Функция `play_dogs_game()`**:
    -   Основная функция игры:
        -   Создает поле, размещает собак и воров.
        -   Запускает игровой цикл, который продолжается, пока воры не будут пойманы.
        -   Выводит текущее состояние поля и запрашивает команду пользователя.
        -   Перемещает собак и воров.
        -   Проверяет, пойманы ли воры, и выводит сообщение о победе, если это так.
11. **Условие `if __name__ == "__main__":`**:
    -   Гарантирует, что игра будет запущена только при запуске файла напрямую, а не при импорте его как модуля.
    -   Вызывает функцию `play_dogs_game()` для начала игры.
"""

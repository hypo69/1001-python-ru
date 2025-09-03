"""
HURKLE:
=================
Сложность: 5
-----------------
Игра "HURKLE" - это игра в угадывание местоположения "HURKLE", который скрыт на карте 10x10. Игрок делает ходы, вводя координаты, и получает подсказки о том, где находится HURKLE относительно его предположений. Цель игры - найти HURKLE за минимальное количество ходов.
Правила игры:
1. HURKLE прячется на карте 10x10. Координаты HURKLE выбираются случайно.
2. Игрок делает ходы, вводя координаты x и y.
3. После каждого хода игрок получает подсказку, указывающую направление (север, юг, восток, запад, северо-восток, юго-восток, северо-запад, юго-запад) от введенной игроком координаты до местоположения HURKLE.
4. Игра продолжается до тех пор, пока игрок не угадает местоположение HURKLE.
-----------------
Алгоритм:
1.  Сгенерировать случайные координаты HURKLE (X и Y) в диапазоне от 1 до 10.
2.  Установить количество ходов равным 0.
3.  Начать игровой цикл:
    3.1. Увеличить счетчик ходов на 1.
    3.2. Запросить у игрока ввод координат X и Y.
    3.3. Если введенные координаты равны координатам HURKLE, вывести сообщение о победе и количестве ходов. Завершить игру.
    3.4. Иначе, определить направление от введенных координат до координат HURKLE и вывести подсказку (направление).
4. Повторять игровой цикл, пока HURKLE не будет найден.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:
    <code><b>
    hurkleX = random(1, 10)
    hurkleY = random(1, 10)
    numberOfGuesses = 0
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: пока HURKLE не найден"}
    LoopStart -- Да --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputCoordinates["Ввод координат пользователем: <code><b>userX, userY</b></code>"]
    InputCoordinates --> CheckWin{"Проверка: <code><b>userX == hurkleX and userY == hurkleY</b></code>?"}
    CheckWin -- Да --> OutputWin["Вывод сообщения: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["Конец"]
    CheckWin -- Нет --> CalculateDirection["Вычисление направления: <code><b>direction = getDirection(userX, userY, hurkleX, hurkleY)</b></code>"]
    CalculateDirection --> OutputDirection["Вывод сообщения: <b>{direction}</b>"]
    OutputDirection --> LoopStart
    LoopStart -- Нет --> End
```
Legenda:
    Start - Начало программы.
    InitializeVariables - Инициализация переменных: hurkleX и hurkleY (координаты HURKLE) генерируются случайным образом от 1 до 10, numberOfGuesses (количество попыток) устанавливается в 0.
    LoopStart - Начало цикла, который продолжается, пока HURKLE не найден.
    IncreaseGuesses - Увеличение счетчика количества попыток на 1.
    InputCoordinates - Запрос у пользователя ввода координат X и Y и сохранение их в переменных userX и userY.
    CheckWin - Проверка, равны ли введенные координаты userX и userY координатам HURKLE hurkleX и hurkleY.
    OutputWin - Вывод сообщения о победе, если координаты совпадают, с указанием количества попыток.
    End - Конец программы.
    CalculateDirection - Вычисление направления от координат пользователя до координат HURKLE.
    OutputDirection - Вывод сообщения с направлением.
"""
```python
import random

# Функция для определения направления HURKLE
def get_direction(user_x, user_y, hurkle_x, hurkle_y):
    """
    Определяет направление от координат пользователя к координатам HURKLE.
    Args:
        user_x (int): Координата X, введенная пользователем.
        user_y (int): Координата Y, введенная пользователем.
        hurkle_x (int): Координата X HURKLE.
        hurkle_y (int): Координата Y HURKLE.
    Returns:
        str: Строка, представляющая направление.
    """
    if user_x < hurkle_x and user_y < hurkle_y:
        return "СЕВЕРО-ВОСТОК"
    elif user_x < hurkle_x and user_y > hurkle_y:
        return "ЮГО-ВОСТОК"
    elif user_x > hurkle_x and user_y < hurkle_y:
        return "СЕВЕРО-ЗАПАД"
    elif user_x > hurkle_x and user_y > hurkle_y:
        return "ЮГО-ЗАПАД"
    elif user_x < hurkle_x:
        return "ВОСТОК"
    elif user_x > hurkle_x:
        return "ЗАПАД"
    elif user_y < hurkle_y:
        return "СЕВЕР"
    else:
        return "ЮГ"

# Генерируем случайные координаты HURKLE
hurkle_x = random.randint(1, 10)
hurkle_y = random.randint(1, 10)

# Инициализируем счетчик ходов
numberOfGuesses = 0

# Основной игровой цикл
while True:
    # Увеличиваем счетчик ходов
    numberOfGuesses += 1

    # Запрашиваем ввод координат у пользователя
    try:
        user_x = int(input("Введите X координату (1-10): "))
        user_y = int(input("Введите Y координату (1-10): "))
    except ValueError:
        print("Пожалуйста, введите целые числа.")
        continue

    # Проверяем, угадал ли пользователь местоположение HURKLE
    if user_x == hurkle_x and user_y == hurkle_y:
        print(f"ПОЗДРАВЛЯЮ! Вы нашли HURKLE за {numberOfGuesses} ходов!")
        break

    # Вычисляем и выводим направление
    direction = get_direction(user_x, user_y, hurkle_x, hurkle_y)
    print(direction)
```
"""
Объяснение кода:
1.  **Импорт модуля `random`**:
   -  `import random`: Импортирует модуль `random`, который используется для генерации случайных чисел.
2.  **Функция `get_direction(user_x, user_y, hurkle_x, hurkle_y)`**:
    -   Определяет функцию, принимающую координаты пользователя и HURKLE.
    -   Определяет направление от координат пользователя к координатам HURKLE и возвращает строку с направлением.
3.  **Инициализация координат HURKLE**:
    -   `hurkle_x = random.randint(1, 10)`: Генерирует случайную x-координату HURKLE от 1 до 10.
    -   `hurkle_y = random.randint(1, 10)`: Генерирует случайную y-координату HURKLE от 1 до 10.
4.  **Инициализация количества попыток**:
    -   `numberOfGuesses = 0`: Инициализирует переменную `numberOfGuesses` для подсчета ходов игрока.
5.  **Основной игровой цикл `while True:`**:
    -   Бесконечный цикл, который продолжается до тех пор, пока игрок не угадает местоположение HURKLE (будет выполнена команда `break`).
    -   `numberOfGuesses += 1`: Увеличивает счетчик попыток на 1 при каждом новом витке цикла.
    -   **Ввод данных**:
        -   `try...except ValueError`: Блок try-except обрабатывает возможные ошибки ввода. Если пользователь введет не целые числа, то будет выведено сообщение об ошибке.
        -   `user_x = int(input("Введите X координату (1-10): "))`: Запрашивает у пользователя x-координату и преобразует ее в целое число.
        -   `user_y = int(input("Введите Y координату (1-10): "))`: Запрашивает у пользователя y-координату и преобразует ее в целое число.
    -   **Условие победы**:
        -   `if user_x == hurkle_x and user_y == hurkle_y:`: Проверяет, совпадают ли введенные координаты с координатами HURKLE.
        -   `print(f"ПОЗДРАВЛЯЮ! Вы нашли HURKLE за {numberOfGuesses} ходов!")`: Выводит сообщение о победе и количестве ходов.
        -   `break`: Завершает цикл (игру), если HURKLE найден.
     -   **Вычисление и вывод направления**:
        -    `direction = get_direction(user_x, user_y, hurkle_x, hurkle_y)`: Вызывает функцию `get_direction` для получения направления.
        -    `print(direction)`: Выводит направление для игрока.
"""

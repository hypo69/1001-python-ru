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

"""
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


"""
CHIEF:
=================
Сложность: 4
-----------------
Игра "CHIEF" - это игра, в которой игрок выступает в роли начальника, планирующего производство на фабрике. Игрок устанавливает количество произведенных изделий каждого типа, и компьютер определяет, соответствуют ли эти значения необходимым требованиям. Если нет, игроку сообщается, какие именно значения были неверны. Цель игры - достичь оптимального производства, правильно угадывая количество изделий.

Правила игры:
1. Компьютер загадывает три значения в диапазоне от 1 до 10: `targetA`, `targetB` и `targetC`.
2. Игрок вводит свои предположения о значениях `userA`, `userB` и `userC`.
3. Компьютер проверяет, совпадают ли введенные значения с загаданными.
4. Если все три значения угаданы, игра заканчивается победой.
5. Если хотя бы одно значение не совпадает, компьютер выводит, какие именно значения были неверными.
6. Игра продолжается до тех пор, пока игрок не угадает все три значения.
-----------------
Алгоритм:
1.  Сгенерировать случайные целые числа `targetA`, `targetB` и `targetC` в диапазоне от 1 до 10.
2.  Начать цикл "пока не угаданы все числа":
    2.1 Запросить у игрока ввод трех целых чисел: `userA`, `userB` и `userC`.
    2.2 Инициализировать строку `message` как пустую.
    2.3 Если `userA` не равно `targetA`, добавить "A" к `message`.
    2.4 Если `userB` не равно `targetB`, добавить "B" к `message`.
    2.5 Если `userC` не равно `targetC`, добавить "C" к `message`.
    2.6 Если `message` не пустая, вывести сообщение "WRONG ON " и `message`.
    2.7 Иначе, вывести сообщение "YOU GOT IT!".
3. Конец игры.
-----------------

"""
import random

# Генерируем случайные числа от 1 до 10 для targetA, targetB и targetC
targetA = random.randint(1, 10)
targetB = random.randint(1, 10)
targetC = random.randint(1, 10)


# Бесконечный цикл, пока игрок не угадает все числа
while True:
    # Запрашиваем ввод трех чисел от пользователя
    try:
        userA = int(input("Введите число для A (от 1 до 10): "))
        userB = int(input("Введите число для B (от 1 до 10): "))
        userC = int(input("Введите число для C (от 1 до 10): "))
    except ValueError:
        print("Пожалуйста, введите целые числа.")
        continue

    # Инициализируем строку для сообщения об ошибках
    message = ""

    # Проверяем, верно ли число A
    if userA != targetA:
        message += "A"  # Если неверно, добавляем "A" в сообщение

    # Проверяем, верно ли число B
    if userB != targetB:
        message += "B" # Если неверно, добавляем "B" в сообщение

    # Проверяем, верно ли число C
    if userC != targetC:
        message += "C" # Если неверно, добавляем "C" в сообщение

    # Если есть ошибки, выводим сообщение о том, какие числа неверны
    if message != "":
        print(f"WRONG ON {message}")
    # Если все числа верны, поздравляем игрока и завершаем игру
    else:
        print("YOU GOT IT!")
        break
"""
Объяснение кода:
1.  **Импорт модуля `random`**:
    -   `import random`: Импортирует модуль `random`, необходимый для генерации случайных чисел.

2.  **Генерация случайных чисел**:
    -   `targetA = random.randint(1, 10)`: Генерирует случайное целое число от 1 до 10 и присваивает его переменной `targetA`.
    -   `targetB = random.randint(1, 10)`: Генерирует случайное целое число от 1 до 10 и присваивает его переменной `targetB`.
    -   `targetC = random.randint(1, 10)`: Генерирует случайное целое число от 1 до 10 и присваивает его переменной `targetC`.
   Эти переменные представляют собой загаданные числа, которые игрок должен угадать.
3.  **Основной игровой цикл**:
    -   `while True:`: Запускает бесконечный цикл, который будет продолжаться до тех пор, пока игрок не угадает все три числа.
    -   **Ввод чисел от пользователя**:
    	-	`try...except ValueError`: Блок try-except обрабатывает возможные ошибки ввода. Если пользователь введет не целое число, то будет выведено сообщение об ошибке.
    	-  `userA = int(input("Введите число для A (от 1 до 10): "))`: Запрашивает у пользователя ввод числа для `A`, преобразует его в целое число и сохраняет в переменной `userA`.
    	-  Аналогично, запрашивает ввод чисел для `B` и `C` и сохраняет их в `userB` и `userC` соответственно.
    -   `message = ""`: Инициализирует пустую строку `message`, которая будет использоваться для хранения информации о том, какие числа были введены неправильно.
4.  **Проверка введенных чисел**:
    -  `if userA != targetA:`: Проверяет, не равно ли введенное пользователем число `userA` загаданному числу `targetA`.
    -  `message += "A"`: Если `userA` не равно `targetA`, добавляет символ "A" к строке `message`, указывая, что число `A` было введено неверно.
    - Аналогичные проверки выполняются для чисел `B` и `C`.
5.  **Вывод результатов**:
    -   `if message != "":`: Проверяет, не пуста ли строка `message`.
    -   `print(f"WRONG ON {message}")`: Если строка `message` не пуста, выводит сообщение о том, какие числа были введены неправильно (например, "WRONG ON AB" - это означает, что числа `A` и `B` были введены неверно).
    -   `else:`: Выполняется, если строка `message` пуста (то есть все числа угаданы правильно).
    -   `print("YOU GOT IT!")`: Выводит сообщение о победе.
    -   `break`: Завершает цикл и игру, если все числа угаданы.
"""

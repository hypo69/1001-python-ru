"""
MUGWMP:
=================
Сложность: 4
-----------------
Игра "MUGWMP" - это текстовая игра, в которой игрок угадывает четырехзначное число, сгенерированное компьютером. После каждой попытки игрок получает подсказки в виде количества правильно угаданных цифр на своих местах (MUG) и количества правильно угаданных цифр не на своих местах (WMP). Цель - угадать число за минимальное количество попыток.

Правила игры:
1. Компьютер генерирует случайное четырехзначное число, где все цифры уникальны.
2. Игрок вводит свои четырехзначные предположения.
3. После каждой попытки компьютер сообщает количество "MUG" (правильные цифры на правильных местах) и "WMP" (правильные цифры не на своих местах).
4. Игра продолжается, пока игрок не угадает число.

-----------------
Алгоритм:
1. Сгенерировать случайное четырехзначное число, где все цифры уникальны.
2. Установить число попыток в 0.
3. Начать цикл "пока число не угадано":
    3.1. Увеличить число попыток на 1.
    3.2. Запросить у игрока четырехзначное число.
    3.3. Проверить, является ли введенное число корректным (четырехзначным и с уникальными цифрами). Если нет, вывести сообщение об ошибке и запросить ввод повторно.
    3.4. Если введенное число совпадает с загаданным, перейти к шагу 4.
    3.5. Подсчитать количество MUG (цифры на своих местах) и WMP (цифры не на своих местах).
    3.6. Вывести подсказку в формате "MUG = X, WMP = Y".
4. Вывести сообщение "YOU GOT IT IN {число попыток} GUESSES!"
5. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> GenerateSecretNumber["<p align='left'>Генерация секретного 4-значного числа 
    <code><b>secretNumber</b></code></p>"]
    GenerateSecretNumber --> InitializeAttempts["<code><b>numberOfGuesses = 0</b></code>"]
    InitializeAttempts --> LoopStart{"Начало цикла: пока не угадано"}
    LoopStart -- Да --> IncreaseGuesses["<code><b>numberOfGuesses = numberOfGuesses + 1</b></code>"]
    IncreaseGuesses --> InputGuess["Ввод 4-значного числа: <code><b>userGuess</b></code>"]
    InputGuess --> ValidateGuess["<p align='left'>Проверка корректности ввода: 
    <code><b>len(userGuess) == 4 &amp;&amp; unique(userGuess)</b></code></p>"]
    ValidateGuess -- Нет --> InputError["Вывод сообщения об ошибке ввода"]
    InputError --> InputGuess
    ValidateGuess -- Да --> CheckWin["Проверка: <code><b>userGuess == secretNumber</b></code>?"]
    CheckWin -- Да --> OutputWin["Вывод сообщения: <b>YOU GOT IT IN <code>{numberOfGuesses}</code> GUESSES!</b>"]
    OutputWin --> End["Конец"]
    CheckWin -- Нет --> CalculateMugWmp["<p align='left'>Расчет MUG (совпадения на местах) и WMP (совпадения не на местах):
    <code><b>mug = countMug(userGuess, secretNumber)
    wmp = countWmp(userGuess, secretNumber)</b></code></p>"]
    CalculateMugWmp --> OutputMugWmp["Вывод: <b>MUG = <code>{mug}</code>, WMP = <code>{wmp}</code></b>"]
    OutputMugWmp --> LoopStart
    LoopStart -- Нет --> End
```
Legenda:
    Start - Начало программы.
    GenerateSecretNumber - Генерация секретного четырехзначного числа с уникальными цифрами.
    InitializeAttempts - Инициализация счетчика количества попыток (numberOfGuesses) в 0.
    LoopStart - Начало цикла, который продолжается, пока число не угадано.
    IncreaseGuesses - Увеличение счетчика количества попыток на 1.
    InputGuess - Запрос ввода четырехзначного числа у пользователя.
    ValidateGuess - Проверка корректности введенного числа (4 символа, все цифры уникальны).
    InputError - Вывод сообщения об ошибке ввода, если введенные данные некорректны.
    CheckWin - Проверка, совпадает ли введенное число с секретным числом.
    OutputWin - Вывод сообщения о победе, если числа совпадают, с указанием количества попыток.
    End - Конец программы.
    CalculateMugWmp - Расчет количества MUG (совпадения на своих местах) и WMP (совпадения не на своих местах).
    OutputMugWmp - Вывод подсказок MUG и WMP.
"""
import random

def generate_secret_number():
    """Генерирует случайное четырехзначное число с уникальными цифрами."""
    digits = list(range(10))
    random.shuffle(digits)
    return "".join(map(str, digits[:4]))

def count_mug_wmp(secret, guess):
    """
    Считает количество MUG (совпадений на своих местах) и WMP (совпадений не на своих местах).
    
    Args:
    secret (str): Секретное число.
    guess (str): Предположение игрока.
    
    Returns:
    tuple: Кортеж, содержащий количество MUG и WMP.
    """
    mug = 0
    wmp = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            mug += 1
        elif guess[i] in secret:
            wmp += 1
    return mug, wmp

# 1. Генерируем случайное четырехзначное число с уникальными цифрами
secret_number = generate_secret_number()

# 2. Инициализируем счетчик попыток
number_of_guesses = 0

# 3. Основной игровой цикл
while True:
    # 3.1. Увеличиваем счетчик попыток
    number_of_guesses += 1

    # 3.2. Запрашиваем ввод числа у пользователя
    while True:
        user_guess = input("Введите четырехзначное число с уникальными цифрами: ")

        # 3.3. Проверяем корректность ввода
        if len(user_guess) != 4 or not user_guess.isdigit() or len(set(user_guess)) != 4:
            print("Ошибка ввода. Пожалуйста, введите корректное четырехзначное число с уникальными цифрами.")
        else:
            break

    # 3.4. Проверяем, угадано ли число
    if user_guess == secret_number:
        print(f"ПОЗДРАВЛЯЮ! Вы угадали число за {number_of_guesses} попыток!")
        break  # Завершаем цикл, если число угадано

    # 3.5. Подсчитываем MUG и WMP
    mug, wmp = count_mug_wmp(secret_number, user_guess)

    # 3.6. Выводим подсказку
    print(f"MUG = {mug}, WMP = {wmp}")

"""
Объяснение кода:
1.  **Импорт модуля `random`**:
    - `import random`: Импортирует модуль `random`, который используется для генерации случайного числа.

2.  **Функция `generate_secret_number()`**:
    -  `def generate_secret_number():`: Определяет функцию для генерации секретного четырехзначного числа с уникальными цифрами.
    -  `digits = list(range(10))`: Создает список цифр от 0 до 9.
    -  `random.shuffle(digits)`: Перемешивает цифры случайным образом.
    -  `return "".join(map(str, digits[:4]))`: Возвращает строку из первых четырех перемешанных цифр, формируя четырехзначное число.

3.  **Функция `count_mug_wmp(secret, guess)`**:
    - `def count_mug_wmp(secret, guess):`: Определяет функцию для подсчета MUG и WMP.
    - `mug = 0`, `wmp = 0`: Инициализирует счетчики MUG и WMP.
    - `for i in range(len(secret)):`: Итерируется по цифрам секретного числа.
        - `if secret[i] == guess[i]:`: Если цифра на текущей позиции совпадает, увеличивает счетчик MUG.
        - `elif guess[i] in secret:`: Если цифра из предположения есть в секретном числе, но не на своей позиции, увеличивает счетчик WMP.
    - `return mug, wmp`: Возвращает кортеж с MUG и WMP.
    
4.  **Основная часть программы**:
   - `secret_number = generate_secret_number()`: Генерирует секретное число с помощью функции `generate_secret_number()`.
    - `number_of_guesses = 0`: Инициализирует счетчик попыток.
    - `while True:`: Начинает бесконечный цикл, пока игрок не угадает число.
        - `number_of_guesses += 1`: Увеличивает счетчик попыток.
        - `while True:`: Внутренний цикл для проверки ввода пользователя.
            - `user_guess = input("Введите четырехзначное число с уникальными цифрами: ")`: Запрашивает ввод у пользователя.
            - `if len(user_guess) != 4 or not user_guess.isdigit() or len(set(user_guess)) != 4:`: Проверяет ввод на корректность (четыре цифры, все цифры уникальные).
            - `else: break`: Если ввод корректен, выходит из внутреннего цикла.
        - `if user_guess == secret_number:`: Проверяет, угадано ли число.
            - `print(f"ПОЗДРАВЛЯЮ! Вы угадали число за {number_of_guesses} попыток!")`: Выводит сообщение о победе.
            - `break`: Выходит из основного цикла.
        - `mug, wmp = count_mug_wmp(secret_number, user_guess)`: Вызывает функцию `count_mug_wmp` для подсчета MUG и WMP.
        - `print(f"MUG = {mug}, WMP = {wmp}")`: Выводит подсказку с MUG и WMP.

"""

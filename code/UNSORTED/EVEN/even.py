"""
EVEN:
=================
Сложность: 2
-----------------
Игра "Четное число" - это простая игра, в которой компьютер генерирует случайное число от 1 до 100, а игрок должен угадать, является ли это число четным или нечетным. Игрок вводит 'E' для четного или 'O' для нечетного. 
После ввода компьютер сообщает, был ли игрок прав.
Игра продолжается до тех пор, пока игрок не решит выйти.

Правила игры:
1. Компьютер генерирует случайное целое число от 1 до 100.
2. Игрок должен ввести 'E', если считает, что число четное, или 'O', если считает, что число нечетное.
3. Компьютер проверяет, является ли сгенерированное число четным или нечетным.
4. Компьютер сообщает игроку, был ли его ответ правильным.
5. Игра продолжается до тех пор, пока игрок не введет 'Q' для выхода.
-----------------
Алгоритм:
1. Начать цикл "пока игрок не введет 'Q'":
    1.1 Сгенерировать случайное целое число от 1 до 100.
    1.2 Запросить у игрока ввод 'E' для четного или 'O' для нечетного.
    1.3 Если ввод игрока равен 'Q', завершить программу.
    1.4 Если сгенерированное число четное и игрок ввел 'E', или если сгенерированное число нечетное и игрок ввел 'O', то вывести "CORRECT".
    1.5 Иначе, вывести "WRONG".
    1.6 Перейти к началу цикла.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> LoopStart{"Начало цикла: пока не введено 'Q'"}
    LoopStart -- Да --> GenerateNumber["Сгенерировать случайное число <code><b>targetNumber = random(1, 100)</b></code>"]
    GenerateNumber --> InputGuess["Ввод ответа игрока: <code><b>userGuess</b></code> (E/O/Q)"]
    InputGuess --> CheckQuit{"Проверка: <code><b>userGuess == 'Q'?</b></code>"}
    CheckQuit -- Да --> End["Конец"]
    CheckQuit -- Нет --> CheckEven["Проверка: <code><b>targetNumber % 2 == 0</b></code>?"]
    CheckEven -- Да --> CheckUserEven{"Проверка: <code><b>userGuess == 'E'?</b></code>"}
    CheckEven -- Нет --> CheckUserOdd{"Проверка: <code><b>userGuess == 'O'?</b></code>"}
    CheckUserEven -- Да --> OutputCorrect["Вывод: <b>CORRECT</b>"]
    CheckUserOdd -- Да --> OutputCorrect
    CheckUserEven -- Нет --> OutputWrong["Вывод: <b>WRONG</b>"]
    CheckUserOdd -- Нет --> OutputWrong
    OutputCorrect --> LoopStart
    OutputWrong --> LoopStart
    
```
**Legenda**:
    Start - Начало программы.
    LoopStart - Начало цикла, который продолжается, пока пользователь не введет 'Q'.
    GenerateNumber - Генерация случайного целого числа в диапазоне от 1 до 100.
    InputGuess - Запрос у пользователя ввода 'E' (четное), 'O' (нечетное) или 'Q' (выход).
    CheckQuit - Проверка, ввел ли пользователь 'Q' для выхода из игры.
    End - Конец программы.
    CheckEven - Проверка, является ли сгенерированное число четным.
    CheckUserEven - Проверка, ввел ли пользователь 'E' (четное) при четном числе.
    CheckUserOdd - Проверка, ввел ли пользователь 'O' (нечетное) при нечетном числе.
    OutputCorrect - Вывод сообщения "CORRECT", если пользователь угадал четность числа.
    OutputWrong - Вывод сообщения "WRONG", если пользователь не угадал четность числа.
"""
import random

# Бесконечный цикл для игры
while True:
    # Генерируем случайное число от 1 до 100
    targetNumber = random.randint(1, 100)
    
    # Запрашиваем у пользователя ввод: E - четное, O - нечетное, Q - выход
    userGuess = input("Введите 'E' для четного, 'O' для нечетного, 'Q' для выхода: ").upper()
    
    # Проверяем, хочет ли пользователь выйти из игры
    if userGuess == 'Q':
        print("Выход из игры.")
        break  # Завершаем цикл, если пользователь ввел 'Q'

    # Проверяем, угадал ли пользователь четность числа
    if (targetNumber % 2 == 0 and userGuess == 'E') or (targetNumber % 2 != 0 and userGuess == 'O'):
        print("CORRECT") # Выводим сообщение, если пользователь угадал
    else:
        print("WRONG") # Выводим сообщение, если пользователь не угадал

"""
Объяснение кода:
1.  **Импорт модуля `random`**:
   -  `import random`: Импортирует модуль `random`, который используется для генерации случайного числа.

2.  **Основной цикл `while True:`**:
    -   `while True:`: Бесконечный цикл, который продолжается до тех пор, пока игрок не решит выйти.
    -   **Генерация случайного числа**:
        -   `targetNumber = random.randint(1, 100)`: Генерирует случайное целое число от 1 до 100 и сохраняет его в переменной `targetNumber`.
    -   **Ввод данных**:
        -   `userGuess = input("Введите 'E' для четного, 'O' для нечетного, 'Q' для выхода: ").upper()`: Запрашивает у пользователя ввод символа (E, O или Q). Применяется метод `.upper()`, чтобы привести ввод к верхнему регистру для корректного сравнения.
    -   **Условие выхода**:
        -   `if userGuess == 'Q':`: Проверяет, ввел ли пользователь 'Q' для выхода из игры.
        -   `print("Выход из игры.")`: Выводит сообщение о выходе.
        -   `break`: Завершает цикл, если пользователь хочет выйти.
    -   **Проверка четности**:
        -   `(targetNumber % 2 == 0 and userGuess == 'E') or (targetNumber % 2 != 0 and userGuess == 'O')`: Проверяет, угадал ли пользователь четность числа. Если число четное и пользователь ввел 'E', или число нечетное и пользователь ввел 'O', условие будет истинным.
        -   `print("CORRECT")`: Выводит сообщение, что пользователь угадал, если условие истинно.
        -   `else:`: В противном случае, пользователь не угадал четность числа.
        -   `print("WRONG")`: Выводит сообщение, что пользователь не угадал.
"""

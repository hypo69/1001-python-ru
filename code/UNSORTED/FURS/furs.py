"""
FURS:
=================
Сложность: 4
-----------------
Игра "Меха" - это текстовая игра, в которой компьютер генерирует случайный текст, состоящий из случайных слов и цифр. Игрок пытается угадать, какие случайные слова и цифры были сгенерированы. Игра продолжается до тех пор, пока игрок не угадает все сгенерированные слова и цифры.

Правила игры:
1. Компьютер выбирает случайные 4-е слова из списка (в данном случае это заранее заданный список)
2. Компьютер выбирает случайные 4-е цифры из диапазона от 0 до 9.
3. Игрок должен ввести слова и цифры, которые, по его мнению, были выбраны компьютером.
4. Если игрок угадывает одно или несколько слов или цифр, компьютер выводит в какой позиции он угадал.
5. Игра продолжается до тех пор, пока игрок не угадает все слова и цифры.
-----------------
Алгоритм:
1. Инициализировать список слов и пустой список для хранения выбранных слов и цифр.
2. Выбрать случайным образом 4 слова из списка.
3. Выбрать случайным образом 4 цифры от 0 до 9.
4. Начать цикл "пока все не угадано"
  4.1 Запросить ввод у игрока, в виде 4-х слов и 4-х цифр через пробел.
  4.2 Преобразовать введенную строку в список слов и список цифр.
  4.3 Итерировать по списку слов и цифр, сравнивая с выбранными словами и цифрами, выводя сообщение, если угадано.
5. Вывести сообщение "YOU GOT IT!"
6. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeGame["<p align='left'>Инициализация:
    <code><b>
    words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    chosenWords = []
    chosenDigits = []
    </b></code></p>"]
    InitializeGame --> ChooseWordsDigits["<p align='left'>Выбор случайных 4-х слов и 4-х цифр:
    <code><b>
    chosenWords = random.sample(words, 4)
    chosenDigits = [random.randint(0, 9) for _ in range(4)]
    </b></code></p>"]
    ChooseWordsDigits --> GameLoopStart{"Начало цикла: пока не угадано"}
    GameLoopStart -- Да --> InputUserGuess["Ввод от пользователя: 4 слова и 4 цифры"]
    InputUserGuess --> ParseInput["Разбор ввода пользователя: слова и цифры"]
    ParseInput --> CheckGuess{"<p align='left'>Проверка соответствия:
    <code><b>
    for each word in userWords, digit in userDigits:
        if word == chosenWord:
            print('Угадано слово...')
        if digit == chosenDigit:
            print('Угадана цифра...')
    </b></code></p>"}
    CheckGuess --> CheckWin{"<p align='left'>Проверка победы:
     <code><b>
    all words and digits correct?
    </b></code></p>"}
    CheckWin -- Да --> OutputWin["Вывод: <b>YOU GOT IT!</b>"]
    OutputWin --> End["Конец"]
    CheckWin -- Нет --> GameLoopStart
    GameLoopStart -- Нет --> End
```

Legenda:
    Start - Начало программы.
    InitializeGame - Инициализация переменных: список words (список возможных слов), chosenWords (список выбранных слов) и chosenDigits (список выбранных цифр).
    ChooseWordsDigits - Выбор случайных 4-х слов из списка words и 4-х случайных цифр.
    GameLoopStart - Начало цикла, который продолжается, пока все слова и цифры не будут угаданы.
    InputUserGuess - Запрос у пользователя ввода 4-х слов и 4-х цифр.
    ParseInput - Разбор введенной пользователем строки на список слов и список цифр.
    CheckGuess - Проверка соответствия введенных пользователем слов и цифр с загаданными. Вывод подсказок при совпадении.
    CheckWin - Проверка, угаданы ли все слова и цифры.
    OutputWin - Вывод сообщения о победе.
    End - Конец программы.
"""
import random

# Список возможных слов
words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# Пустой список для хранения выбранных слов
chosenWords = []
# Пустой список для хранения выбранных цифр
chosenDigits = []

# Выбираем случайным образом 4 слова из списка
chosenWords = random.sample(words, 4)
# Выбираем случайным образом 4 цифры от 0 до 9
chosenDigits = [random.randint(0, 9) for _ in range(4)]

# Основной игровой цикл
while True:
    # Запрашиваем ввод от пользователя
    user_input = input("Введите 4 слова (A-J) и 4 цифры (0-9) через пробел: ").upper()
    # Разбиваем ввод на список слов и список цифр
    userWords = user_input.split()[:4]  # Берем первые 4 элемента как слова
    userDigits = user_input.split()[4:]  # Берем следующие 4 элемента как цифры

    # Флаг для отслеживания, угадал ли пользователь все
    all_correct = True
    
    # Проверяем слова на соответствие
    for i in range(4):
      if userWords[i] == chosenWords[i]:
        print(f"Слово {userWords[i]} в позиции {i+1} угадано")
      else:
        all_correct = False
    # Проверяем цифры на соответствие
    for i in range(4):
      try:
        if int(userDigits[i]) == chosenDigits[i]:
            print(f"Цифра {userDigits[i]} в позиции {i+1} угадана")
        else:
          all_correct = False
      except ValueError:
         print(f"Ошибка: '{userDigits[i]}' не является цифрой. Попробуйте еще раз.")
         all_correct = False
         break
      
    # Если все слова и цифры угаданы, завершаем игру
    if all_correct:
        print("YOU GOT IT!")
        break
    
    
"""
Объяснение кода:
1.  **Импорт модуля `random`**:
    - `import random`: Импортирует модуль для работы со случайными числами и выборками.

2.  **Инициализация переменных**:
    - `words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']`: Список возможных слов для выбора.
    - `chosenWords = []`: Пустой список для хранения выбранных слов.
    - `chosenDigits = []`: Пустой список для хранения выбранных цифр.
3.  **Выбор случайных слов и цифр**:
    - `chosenWords = random.sample(words, 4)`: Выбирает случайные 4 слова из списка `words` без повторений.
    - `chosenDigits = [random.randint(0, 9) for _ in range(4)]`: Генерирует список из 4 случайных цифр в диапазоне от 0 до 9.
4.  **Основной игровой цикл `while True:`**:
    - Бесконечный цикл, который продолжается, пока игрок не угадает все слова и цифры (условие `all_correct` станет `True`).
    - `user_input = input("Введите 4 слова (A-J) и 4 цифры (0-9) через пробел: ").upper()`: Запрашивает у пользователя ввод, преобразует его в верхний регистр.
    - `userWords = user_input.split()[:4]`: Разделяет ввод на слова (берутся первые 4 элемента)
    - `userDigits = user_input.split()[4:]`: Разделяет ввод на цифры (берутся следующие 4 элемента)
5.  **Проверка соответствия**:
    -  `all_correct = True`: Устанавливаем флаг `all_correct` в `True` перед проверкой.
    -  **Цикл проверки слов**:
        -  `for i in range(4):` Цикл по 4 позициям слов
        -  `if userWords[i] == chosenWords[i]:` Проверка на соответствие слова в позиции
        - `print(f"Слово {userWords[i]} в позиции {i+1} угадано")`: Выводит сообщение, если слово угадано.
        - `else: all_correct = False`: Если хоть одно слово не угадано, флаг `all_correct` устанавливается в `False`.
    -  **Цикл проверки цифр**:
        - `for i in range(4):` Цикл по 4 позициям цифр
        - `try...except ValueError`: Обработка ошибок ввода, если пользователь ввел не цифру.
        - `if int(userDigits[i]) == chosenDigits[i]:` Проверка на соответствие цифры в позиции
        -  `print(f"Цифра {userDigits[i]} в позиции {i+1} угадана")`: Вывод сообщения, если цифра угадана.
        - `else: all_correct = False`: Если хоть одна цифра не угадана, флаг `all_correct` устанавливается в `False`.
        - `if not all_correct: break`: Если ошибка при вводе, прерывает цикл проверки цифр.
6.  **Проверка победы и завершение игры**:
    - `if all_correct:`: Если флаг `all_correct` остается `True`, значит все угадано.
    -  `print("YOU GOT IT!")`: Выводит сообщение о победе.
    - `break`: Завершает основной цикл и игру.
"""

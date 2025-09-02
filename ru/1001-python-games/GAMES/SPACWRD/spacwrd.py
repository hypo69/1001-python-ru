
SPACWRD:
=================
Сложность: 4
-----------------
Игра "Космическое слово" - это текстовая игра, в которой игрок пытается угадать загаданное компьютером слово, вводя буквы. Компьютер отображает слово с пробелами вместо неугаданных букв. После каждой попытки игрок получает информацию о том, сколько букв он угадал, и может продолжать угадывать оставшиеся. Игра заканчивается, когда игрок угадывает все буквы слова.

Правила игры:
1. Компьютер выбирает случайное слово из заданного списка.
2. Игрок видит слово, где все буквы заменены на пробелы.
3. Игрок вводит букву.
4. Компьютер проверяет, есть ли эта буква в загаданном слове.
5. Если буква есть, компьютер открывает все ее позиции в слове.
6. Если буквы нет, сообщение об этом не выводится.
7. Игра продолжается до тех пор, пока все буквы слова не будут угаданы.
8. После каждой попытки выводится текущее состояние слова с открытыми буквами и количество угаданных букв.
-----------------
Алгоритм:
1. Задать список слов для игры.
2. Выбрать случайное слово из списка.
3. Инициализировать переменные:
   - слово с пробелами (закрытое слово)
   - количество правильно угаданных букв
   - массив из угаданных букв.
4. Начать цикл "пока слово не угадано":
   4.1 Вывести текущее состояние слова (с открытыми буквами)
   4.2 Запросить у игрока ввод буквы.
   4.3 Проверить наличие буквы в загаданном слове.
   4.4 Если буква есть:
       4.4.1 Обновить закрытое слово: открыть все позиции этой буквы
       4.4.2 Обновить массив угаданных букв.
       4.4.3 Обновить счетчик угаданных букв
   4.5 Если все буквы слова открыты, перейти к шагу 5.
5. Вывести сообщение "YOU GOT IT!".
6. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:
    <code><b>
    wordList = ['APPLE', 'BANANA', 'CHERRY', ...]
    targetWord = random_word(wordList)
    guessedWord = '_' * len(targetWord)
    guessedLetters = []
    correctGuesses = 0
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: пока не угадано"}
    LoopStart -- Да --> OutputWord["Вывод: <code><b>guessedWord</b></code>"]
    OutputWord --> InputLetter["Ввод буквы пользователем: <code><b>userLetter</b></code>"]
    InputLetter --> CheckLetter{"Проверка: <code><b>userLetter in targetWord?</b></code>"}
    CheckLetter -- Да --> UpdateWord["<p align='left'>Обновление:
    <code><b>
    guessedWord = reveal_letters(targetWord, guessedWord, userLetter)
    guessedLetters.append(userLetter)
    correctGuesses = correct_guesses(guessedLetters,targetWord)

    </b></code></p>"]
     UpdateWord --> CheckWin{ "Проверка:<code><b>correctGuesses == len(targetWord)?</b></code>"}
    CheckLetter -- Нет --> CheckWin
    CheckWin -- Да --> OutputWin["Вывод сообщения: <b>YOU GOT IT!</b>"]
    OutputWin --> End["Конец"]
    CheckWin -- Нет --> LoopStart
    LoopStart -- Нет --> End
    

```
**Legenda:**
   * **Start** - Начало игры.
   * **InitializeVariables** - Инициализация переменных:
        - `wordList` - список слов для игры.
        - `targetWord` - случайно выбранное слово из списка.
        - `guessedWord` - слово, которое игрок видит с пробелами вместо букв.
        - `guessedLetters` - список угаданных букв.
        - `correctGuesses` - количество правильно угаданных букв.
   * **LoopStart** - Начало игрового цикла, который продолжается, пока слово не угадано.
   * **OutputWord** - Вывод текущего состояния слова, с открытыми буквами (если они были угаданы).
   * **InputLetter** - Запрос у пользователя ввода буквы.
   * **CheckLetter** - Проверка, есть ли введенная буква в загаданном слове.
   * **UpdateWord** - Обновление слова: открытие всех позиций введенной буквы и добавление этой буквы в список угаданных букв и подсчёт угаданных букв.
   * **CheckWin** - Проверка, угаданы ли все буквы слова.
   * **OutputWin** - Вывод сообщения о победе.
   * **End** - Конец игры.
"""


import random

def choose_word(word_list):
    """Выбирает случайное слово из списка."""
    return random.choice(word_list)

def display_word(word, guessed_letters):
  """Отображает слово, скрывая неугаданные буквы."""
  display = ""
  for letter in word:
    if letter in guessed_letters:
      display += letter + " "
    else:
      display += "_ "
  return display.strip()

def update_word(word, guessed_word, user_letter):
    """Обновляет отображаемое слово, открывая угаданные буквы."""
    updated_word = ""
    for i in range(len(word)):
        if word[i] == user_letter:
          updated_word += user_letter + " "
        else:
            updated_word += guessed_word[i*2] + " "
    return updated_word.strip()


def correct_guesses(guessed_letters, target_word):
    """
    Считает количество правильно угаданных букв в слове.
    """
    count = 0
    unique_letters = set(target_word)
    for letter in guessed_letters:
        if letter in unique_letters:
            count += 1
            unique_letters.remove(letter)
    return len(set(target_word)) - len(unique_letters)


def play_spaceword_game():
    """Основная логика игры "Космическое слово"."""
    word_list = ["APPLE", "BANANA", "CHERRY", "DATE", "ELDERBERRY", "FIG", "GRAPE", "KIWI", "LEMON", "MANGO",
    "ORANGE", "PEACH", "QUINCE", "RASPBERRY", "STRAWBERRY", "TANGERINE", "WATERMELON"
    ]
    target_word = choose_word(word_list) # Выбираем слово
    guessed_word = "_ " * len(target_word) # Создаем закрытое слово
    guessed_letters = []  # Список угаданных букв
    correct_guesses_count = 0
    
    print("Добро пожаловать в игру 'Космическое слово'!")
    print("Я загадал слово. Попробуй его угадать, вводя по одной букве.")
    

    while correct_guesses_count < len(target_word):
        print("\nСлово:", guessed_word)
        user_letter = input("Введите букву: ").upper() # Запрашиваем букву
        
        if user_letter in target_word:
            guessed_letters.append(user_letter)
            guessed_word = update_word(target_word, guessed_word, user_letter)
            correct_guesses_count = correct_guesses(guessed_letters, target_word)
        else:
            print("Такой буквы нет в слове.")

        
        if correct_guesses_count == len(target_word):
           print("\nYOU GOT IT!")
           break

if __name__ == "__main__":
    play_spaceword_game()
"""
Объяснение кода:
1. **Импорт модуля `random`**:
   - `import random`: Импортирует модуль `random` для выбора случайного слова.

2. **Функция `choose_word(word_list)`**:
   - Принимает список слов `word_list` в качестве аргумента.
   - `return random.choice(word_list)`: Возвращает случайное слово из списка.

3. **Функция `display_word(word, guessed_letters)`**:
   - Принимает слово `word` и список угаданных букв `guessed_letters`.
   - Создает строку `display`, в которой отображает буквы из `word` если они есть в `guessed_letters` или знак `_`.
   - Возвращает отображаемое слово.

4. **Функция `update_word(word, guessed_word, user_letter)`**:
    -   Принимает загаданное слово `word`, текущее отображение слова `guessed_word`, и введенную пользователем букву `user_letter`.
    -   Создает строку `updated_word`, которая сначала пустая.
    -   Циклом `for` проверяет каждую букву в слове `word`.
    -   Если текущая буква равна `user_letter`, то добавляет ее в `updated_word` c пробелом.
    -   В противном случае добавляет символ из `guessed_word`.
    -   Возвращает обновленную строку с открытыми буквами.

5. **Функция `correct_guesses(guessed_letters, target_word)`**:
    -  Принимает список угаданных букв `guessed_letters` и загаданное слово `target_word`.
    -  Создаёт множество `unique_letters` из букв слова `target_word` для отслеживания уникальных букв.
    -  Циклом `for` считает сколько букв из `guessed_letters` есть в слове.
    -  Исключает уже подсчитанные буквы из `unique_letters`.
    -  Возвращает количество угаданных букв, которое равно разнице длинны множества уникальных букв и длинны остатка множества.

6. **Функция `play_spaceword_game()`**:
   - Основная функция игры.
   - `word_list`: Список слов для игры.
   - `target_word = choose_word(word_list)`: Выбирает случайное слово.
    -   `guessed_word = "_ " * len(target_word)`: Создает строку, представляющую слово, в котором все буквы заменены пробелами.
   -   `guessed_letters = []`: Создает пустой список для хранения угаданных букв.
   -   Выводит приветствие и описание игры.
   -   **Основной игровой цикл `while True`**:
      -   `print("\nСлово:", guessed_word)`: Выводит текущее состояние слова.
      -   `user_letter = input("Введите букву: ").upper()`: Запрашивает ввод буквы и переводит ее в верхний регистр.
      -    **Проверка введенной буквы:**
        -   `if user_letter in target_word:`: Если буква есть в загаданном слове, то добавляем ее в список угаданных, обновляем слово и счётчик.
        -   `else:`: Если буквы нет в слове, то выводим сообщение об ошибке.
        -   Если угаданных букв столько же, сколько букв в слове, то выводится сообщение о победе и цикл завершается.

7. **Запуск игры**:
   - `if __name__ == "__main__":`: Запускает функцию `play_spaceword_game()`, если скрипт запущен напрямую.
   - `play_spaceword_game()`: Вызов функции для начала игры.
"""
```
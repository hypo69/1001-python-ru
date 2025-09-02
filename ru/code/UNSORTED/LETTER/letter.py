import random

def letter_guessing_game():
    # Генерация случайной буквы русского алфавита
    target_letter = random.choice('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
    attempts = 0

    print("Добро пожаловать в игру 'УГАДАЙ БУКВУ'!")
    print("Попробуйте угадать букву, которую я загадал (А-Я).")

    while True:
        # Запрос ввода от игрока
        guess = input("Введите вашу букву: ").strip().upper()

        # Проверка корректности ввода
        if len(guess) != 1 or guess not in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
            print("Пожалуйста, введите одну корректную букву русского алфавита (А-Я).")
            continue

        attempts += 1

        # Проверка угаданной буквы
        if guess == target_letter:
            print(f"ВЫ УГАДАЛИ ЗА {attempts} ПОПЫТОК!")
            break
        elif guess < target_letter:
            print("РАНЬШЕ В АЛФАВИТЕ.")
        else:
            print("ПОЗЖЕ В АЛФАВИТЕ.")

import random

# Функция для вычисления числа Фибоначчи
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Инициализация счетчика попыток
numberOfGuesses = 0
# Генерируем случайное число от 1 до 100
targetNumber = random.randint(1, 100)

# Основной игровой цикл
while True:
    # Увеличиваем количество попыток
    numberOfGuesses += 1
    # Вычисляем число Фибоначчи для текущей попытки
    fibonacciNumber = fibonacci(numberOfGuesses)
    # Возводим загаданное число в степень числа Фибоначчи
    poweredNumber = targetNumber ** fibonacciNumber

    # Запрашиваем ввод числа у пользователя
    try:
        userGuess = int(input(f"Попытка {numberOfGuesses}: Введите число: "))
    except ValueError:
         print("Пожалуйста, введите целое число.")
         continue

    # Проверяем, угадано ли число
    if userGuess == poweredNumber:
        print(f"ПОЗДРАВЛЯЮ! Вы угадали число за {numberOfGuesses} попыток!")
        break  # Завершаем цикл, если число угадано
    else:
         print("Попробуйте ещё раз!") # Сообщаем, что нужно попробовать еще раз
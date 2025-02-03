
```python
import datetime
import random

def calculate_age(birth_date_str):
    """Рассчитывает возраст на основе строки с датой рождения."""
    birth_date = datetime.datetime.strptime(birth_date_str, '%d.%m.%Y').date()
    current_date = datetime.date.today()
    age_years = current_date.year - birth_date.year
    if current_date.month < birth_date.month or (
            current_date.month == birth_date.month and current_date.day < birth_date.day):
        age_years -= 1
    return age_years


def play_age_guessing_game():
    """Игра по угадыванию возраста."""
    print("Добро пожаловать в игру 'Угадай возраст'! ")

    while True:
        try:
            birth_year = random.randint(1900, datetime.date.today().year)
            birth_month = random.randint(1, 12)
            birth_day = random.randint(1, 28) # упрощаем, чтобы не проверять дни в каждом месяце
            
            birth_date_str = f"{birth_day:02}.{birth_month:02}.{birth_year}"  # формируем строку даты
            
            real_age = calculate_age(birth_date_str)
            
            print(f"\nЯ загадал дату рождения, попробуй отгадать сколько человеку лет на текущий момент.")
            
            guess_age = int(input("Твой вариант: "))
            
            if guess_age == real_age:
                print("Ура, ты угадал!")
            else:
                print(f"Не угадал, правильный ответ: {real_age}")

            play_again = input("Сыграем еще раз? (д/н): ")
            if play_again.lower() != "д":
                print("Спасибо за игру!")
                break

        except ValueError:
           print("Некорректный ввод. Пожалуйста, введите целое число.")


if __name__ == "__main__":
    play_age_guessing_game()
```

**Как это работает:**

1.  **`calculate_age(birth_date_str)`:** Эта функция извлекает возраст из строки, как в примере из изображения.
2.  **`play_age_guessing_game()`:**
    *   Приветствует игрока.
    *   Запускает бесконечный цикл (пока игрок не решит закончить).
    *   Случайным образом генерирует дату рождения.
    *   Рассчитывает "правильный" возраст, используя `calculate_age`.
    *   Предлагает пользователю ввести свой вариант возраста.
    *   Сравнивает ввод пользователя с реальным возрастом и сообщает результат.
    *   Спрашивает игрока, хочет ли он сыграть еще раз.
    *   Прерывает цикл, если игрок не хочет играть.
3.  **`if __name__ == "__main__":`:** Это стандартный Python-приём, чтобы запустить `play_age_guessing_game()` только при непосредственном запуске скрипта.

**Как запустить:**

1.  Сохраните код в файл с расширением `.py` (например, `age_game.py`).
2.  Запустите файл в терминале, выполнив команду:
    ```bash
    python age_game.py
    ```

**Как играть:**

1.  Игра предложит вам угадать возраст, который был вычислен по случайной дате рождения.
2.  Введите свой вариант ответа.
3.  Вы увидите, угадали вы или нет, и при желании сможете сыграть ещё раз.

**Улучшения:**

*   Можно добавить сложность (например, ограничение по времени).
*   Сделать ввод более защищённым (особенно в части ввода даты рождения, когда её вводит пользователь).
*   Можно добавить уровни сложности (в зависимости от диапазона лет).

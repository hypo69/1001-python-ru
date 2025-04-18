**LETTER GUESSING GAME (Русский алфавит)**  
**Описание:**  
Игра "LETTER" похожа на игру "Угадай число", но вместо числа компьютер загадывает случайную букву русского алфавита. Ваша задача — угадать эту букву, используя подсказки, которые вы получаете после каждой попытки. Обычно для угадывания буквы требуется не более пяти попыток.  

**Правила игры:**  
1. Компьютер выбирает случайную букву русского алфавита (от А до Я).  
2. Игрок вводит свои предположения о загаданной букве.  
3. После каждой попытки компьютер сообщает, находится ли введенная буква в алфавите до или после загаданной буквы.  
4. Игра продолжается до тех пор, пока игрок не угадает загаданную букву.  

**Алгоритм:**  
1. Установить число попыток в 0.  
2. Сгенерировать случайную букву русского алфавита (от А до Я).  
3. Начать цикл "пока буква не угадана":  
    3.1. Увеличить число попыток на 1.  
    3.2. Запросить у игрока ввод буквы.  
    3.3. Если введенная буква равна загаданной, перейти к шагу 4.  
    3.4. Если введенная буква находится в алфавите до загаданной, вывести сообщение "РАНЬШЕ В АЛФАВИТЕ".  
    3.5. Если введенная буква находится в алфавите после загаданной, вывести сообщение "ПОЗЖЕ В АЛФАВИТЕ".  
4. Вывести сообщение "ВЫ УГАДАЛИ ЗА {число попыток} ПОПЫТОК!"  
5. Конец игры.  

**Пример игры:**  
- Компьютер загадал букву **М**.  
- Игрок вводит букву **Д**.  
  Компьютер: "РАНЬШЕ В АЛФАВИТЕ".  
- Игрок вводит букву **С**.  
  Компьютер: "ПОЗЖЕ В АЛФАВИТЕ".  
- Игрок вводит букву **М**.  
  Компьютер: "ВЫ УГАДАЛИ ЗА 3 ПОПЫТКИ!"  

---

### Код на Python для игры с русским алфавитом:

```python
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

# Запуск игры
letter_guessing_game()
```

### Как работает код:
1. **Генерация случайной буквы:**  
   Используется `random.choice` для выбора случайной буквы из строки `'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'`.

2. **Основной игровой цикл:**  
   - Игрок вводит букву, которая приводится к верхнему регистру и проверяется на корректность.  
   - Если буква введена корректно, увеличивается счетчик попыток.  
   - Если буква угадана, игра завершается с сообщением о победе.  
   - Если буква не угадана, выводится подсказка: "РАНЬШЕ В АЛФАВИТЕ" (если буква находится раньше в алфавите) или "ПОЗЖЕ В АЛФАВИТЕ" (если буква находится позже).

3. **Завершение игры:**  
   Игра заканчивается, когда игрок угадывает букву, и выводится количество попыток.

### Пример работы программы:
```
Добро пожаловать в игру 'УГАДАЙ БУКВУ'!
Попробуйте угадать букву, которую я загадал (А-Я).
Введите вашу букву: Д
РАНЬШЕ В АЛФАВИТЕ.
Введите вашу букву: С
ПОЗЖЕ В АЛФАВИТЕ.
Введите вашу букву: М
ВЫ УГАДАЛИ ЗА 3 ПОПЫТКИ!
```


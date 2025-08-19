"""
<YAHTZE>:
=================
Сложность: 6
-----------------
Игра "Yahtzee" - это игра в кости, где игрок бросает пять кубиков и пытается набрать очки, составляя комбинации, такие как пары, тройки, фулл-хаусы, стрейты и т.д. 
Игрок имеет три попытки бросить кости для каждой комбинации, с возможностью оставить некоторые кости и перебросить остальные.
Игра состоит из 13 раундов, каждый раунд оценивается по одной из комбинаций. В конце игры очки суммируются.
Правила игры:
1. В каждом раунде игрок бросает 5 кубиков.
2. После первого броска игрок может оставить любые кубики и перебросить оставшиеся.
3. После второго броска игрок может снова оставить любые кубики и перебросить оставшиеся.
4. После третьего броска игрок должен выбрать одну из доступных категорий для записи результата.
5. Категории включают:
   - Сумму всех единиц, двоек, троек, четверок, пятерок и шестерок.
   - Комбинации: 3 одинаковых, 4 одинаковых, фулл хаус, малый стрейт, большой стрейт, yahtzee (все 5 одинаковых), шанс.
6. Каждая категория может быть использована только один раз за игру.
7. Игра состоит из 13 раундов, по одному для каждой категории.
8. После 13 раундов очки суммируются.
-----------------
Алгоритм:
1. Инициализировать массив категорий, представляющих комбинации для записи очков, и массив для хранения очков.
2. Начать цикл из 13 раундов:
   2.1. Инициализировать массив бросков, представляющий 5 игральных костей.
   2.2. Начать цикл из 3 попыток броска:
        2.2.1. Сгенерировать 5 случайных чисел (от 1 до 6) для массива бросков.
        2.2.2. Вывести результаты броска на экран.
        2.2.3. Если это не третья попытка, запросить у игрока, какие кубики он хочет перебросить.
        2.2.4. Перебросить выбранные кубики (сохраняя не переброшенные).
   2.3. Вывести список доступных категорий, которые еще не использовались.
   2.4. Запросить у игрока выбор категории.
   2.5. Вычислить количество очков для выбранной категории, согласно броску кубиков.
   2.6. Записать количество очков в массив очков для соответствующей категории.
3. Вычислить общую сумму очков.
4. Вывести таблицу очков по категориям и общую сумму.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeGame["Инициализация игры: <br><code><b>categories = [...]<br>scores = [...]<br>used_categories = []</b></code>"]
    InitializeGame --> RoundLoopStart{"Начало цикла: 13 раундов"}
    RoundLoopStart -- Да --> InitializeDice["Инициализация бросков: <code><b>dice = []</b></code>"]
    InitializeDice --> RollLoopStart{"Начало цикла: 3 попытки броска"}
    RollLoopStart -- Да --> RollDice["Бросок костей: <code><b>dice = random(1-6, 5)</b></code>"]
    RollDice --> OutputDice["Вывод результата броска: <code><b>dice</b></code>"]
    OutputDice --> CheckRollAttempt{"Проверка: <code><b>rollAttempt < 3?</b></code>"}
    CheckRollAttempt -- Да --> InputKeepDice["Запрос какие кубики оставить: <code><b>keep_indices</b></code>"]
    InputKeepDice --> ReRollDice["Перебросить выбранные кубики"]
    ReRollDice --> RollLoopStart
    CheckRollAttempt -- Нет --> OutputAvailableCategories["Вывод доступных категорий"]
     OutputAvailableCategories--> InputCategoryChoice["Выбор категории: <code><b>category</b></code>"]
     InputCategoryChoice --> CalculateScore["Подсчет очков для категории: <code><b>score = calculateScore(dice, category)</b></code>"]
    CalculateScore --> UpdateScorecard["Записать очки в таблицу: <code><b>scores[category] = score<br>used_categories.add(category)</b></code>"]
     UpdateScorecard --> RoundLoopStart
      RoundLoopStart -- Нет --> CalculateTotalScore["Суммировать очки: <code><b>totalScore = sum(scores)</b></code>"]
      CalculateTotalScore --> OutputScorecard["Вывод таблицы очков: <code><b>scores, totalScore</b></code>"]
       OutputScorecard--> End["Конец"]
```
Legenda:
    Start - Начало программы.
    InitializeGame - Инициализация переменных:  массивы категорий, очков, использованных категорий.
    RoundLoopStart - Начало цикла, который выполняется 13 раз (количество раундов в игре).
    InitializeDice - Инициализация массива для бросков костей
    RollLoopStart - Начало цикла, который выполняется 3 раза (максимальное количество бросков в раунде).
    RollDice - Генерируется случайный бросок 5 кубиков со значениями от 1 до 6.
    OutputDice - Выводит текущие результаты броска.
    CheckRollAttempt - Проверка, не достигло ли число бросков 3, максимального количества бросков в раунде.
    InputKeepDice - Запрос у пользователя, какие кости оставить.
    ReRollDice - Переброс невыбранных костей.
    OutputAvailableCategories - Вывод списка доступных категорий.
    InputCategoryChoice - Запрос у пользователя выбора категории.
    CalculateScore - Подсчет очков для выбранной категории в соответствии с броском.
    UpdateScorecard - Запись очков в таблицу и добавление выбранной категории в список использованных.
    CalculateTotalScore - Суммирование очков из всех категорий.
    OutputScorecard - Вывод таблицы очков по категориям и общей суммы.
    End - Конец программы.
"""
import random

def roll_dice():
    """Бросает 5 кубиков и возвращает результаты."""
    return [random.randint(1, 6) for _ in range(5)]

def calculate_score(dice, category):
    """Вычисляет очки для выбранной категории."""
    counts = {}
    for die in dice:
        counts[die] = counts.get(die, 0) + 1

    if category in ['1', '2', '3', '4', '5', '6']:
        value = int(category)
        return sum(die for die in dice if die == value)
    elif category == '3 of a kind':
        for count in counts.values():
            if count >= 3:
                return sum(dice)
        return 0
    elif category == '4 of a kind':
        for count in counts.values():
            if count >= 4:
                return sum(dice)
        return 0
    elif category == 'full house':
        if 2 in counts.values() and 3 in counts.values():
            return 25
        return 0
    elif category == 'small straight':
        dice.sort()
        unique_dice = sorted(list(set(dice)))
        for i in range(len(unique_dice) - 3):
            if unique_dice[i+1] == unique_dice[i] + 1 and \
               unique_dice[i+2] == unique_dice[i] + 2 and \
               unique_dice[i+3] == unique_dice[i] + 3:
                return 30
        return 0
    elif category == 'large straight':
          dice.sort()
          unique_dice = sorted(list(set(dice)))
          if len(unique_dice) == 5:
              for i in range(len(unique_dice)-1):
                if unique_dice[i+1] != unique_dice[i]+1:
                  return 0
              return 40
          return 0
    elif category == 'yahtzee':
        if len(set(dice)) == 1:
            return 50
        return 0
    elif category == 'chance':
        return sum(dice)
    return 0

def play_yahtzee():
    """Основная функция для игры в Yahtzee."""
    categories = [
      '1', '2', '3', '4', '5', '6',
      '3 of a kind', '4 of a kind',
      'full house', 'small straight', 'large straight',
      'yahtzee', 'chance'
    ]
    scores = {category: None for category in categories}  # Словарь для хранения очков
    used_categories = set()  # Множество использованных категорий

    for round_num in range(1, 14):
        print(f"\n----- Раунд {round_num} -----")
        dice = roll_dice()  # Бросаем кубики
        print(f"Первый бросок: {dice}")

        for roll_attempt in range(1, 3): # Даем 3 попытки
            keep_dice_str = input(f"Попытка {roll_attempt}, какие кубики оставить (введите номера через пробел, от 1 до 5, 0 = перебросить все, n = ничего не перебрасывать)? ")
            
            if keep_dice_str.lower() == 'n':
              break
            if keep_dice_str == '0':
              dice = roll_dice()
              print(f"Новый бросок: {dice}")
              continue
            try:
                keep_indices = [int(i) - 1 for i in keep_dice_str.split()] # Получаем список индексов кубиков, которые нужно оставить
                if not all(0 <= index < 5 for index in keep_indices):
                  print("Неверные индексы, попробуйте еще раз.")
                  continue
                new_dice = [] # Новый список кубиков
                for i in range(5): # Проходим по всем кубикам
                  if i not in keep_indices: # Если кубик не нужно оставлять, то бросаем его заново
                    new_dice.append(random.randint(1, 6))
                  else: # Иначе, добавляем кубик в новый список из старого
                    new_dice.append(dice[i])
                dice = new_dice
                print(f"Новый бросок: {dice}")
            except ValueError:
                print("Неверный ввод, попробуйте еще раз.")
        
        available_categories = [cat for cat in categories if cat not in used_categories] # Список доступных категорий
        print("Доступные категории:")
        for i, cat in enumerate(available_categories, start=1):
            print(f"{i}. {cat}")
        
        while True:
            try:
                choice_index = int(input("Выберите номер категории для записи очков: "))-1 # Запрашиваем выбор
                if  0 <= choice_index < len(available_categories) :
                    category_choice = available_categories[choice_index]
                    break
                else:
                    print('Неверный номер категории, попробуйте еще раз.')
            except ValueError:
                print('Неверный ввод, попробуйте еще раз.')
        
        score = calculate_score(dice, category_choice) # Вычисляем очки
        scores[category_choice] = score # Записываем очки
        used_categories.add(category_choice) # Добавляем категорию в список использованных
        print(f"Очки за категорию {category_choice}: {score}")

    # Выводим таблицу очков
    print("\n----- Итоговая таблица очков -----")
    for category, score in scores.items():
      print(f"{category}: {score if score is not None else 0}")

    total_score = sum(score if score is not None else 0 for score in scores.values())
    print(f"Общий счет: {total_score}")

if __name__ == "__main__":
    play_yahtzee()
"""
Объяснение кода:
1. **Импорт модуля `random`**:
   -  `import random`: Импортирует модуль `random`, который используется для генерации случайных чисел.

2. **Функция `roll_dice()`**:
    -   `def roll_dice():`: Определяет функцию, которая имитирует бросок пяти игральных костей.
    -  `return [random.randint(1, 6) for _ in range(5)]`:  Генерирует список из 5 случайных чисел в диапазоне от 1 до 6, представляющих результаты броска кубиков.

3. **Функция `calculate_score(dice, category)`**:
    - `def calculate_score(dice, category):`: Определяет функцию для расчета очков для выбранной категории.
    -  `counts = {}`: Инициализирует пустой словарь для подсчета количества каждого значения на кубиках.
    -  `for die in dice: counts[die] = counts.get(die, 0) + 1`: Подсчитывает количество каждого значения на кубиках
    -  Условные блоки `if category in [...]`: Проверяет, какая категория выбрана игроком и вычисляет очки.
        -  Для категорий от 1 до 6 суммирует только те кубики, которые соответствуют выбранной категории.
        -  Для "3 of a kind" и "4 of a kind" проверяет наличие 3 или 4 одинаковых значений и возвращает сумму всех кубиков или 0.
        -  Для "full house" проверяет наличие пары и тройки и возвращает 25 очков, иначе 0.
        -  Для "small straight" проверяет наличие 4 последовательных чисел и возвращает 30 очков, иначе 0.
        -   Для "large straight" проверяет наличие 5 последовательных чисел и возвращает 40 очков, иначе 0.
        -   Для "yahtzee" проверяет наличие 5 одинаковых значений и возвращает 50 очков, иначе 0.
        -   Для "chance" возвращает сумму всех кубиков.

4. **Функция `play_yahtzee()`**:
    -  `def play_yahtzee():`: Определяет основную функцию игры Yahtzee.
    - `categories = [...]`: Определяет список всех возможных категорий.
    - `scores = {category: None for category in categories}`: Создает словарь для хранения набранных очков для каждой категории, начальное значение None.
    - `used_categories = set()`: Создает множество для хранения использованных категорий.
    - `for round_num in range(1, 14):`: Основной игровой цикл. Всего 13 раундов.
        -  `dice = roll_dice()`: Бросает 5 кубиков, результат сохраняется в переменной `dice`.
        -  `print(f"Первый бросок: {dice}")`: Выводит результат первого броска на экран.
        -  `for roll_attempt in range(1, 3):`: Цикл для дополнительных бросков (до двух раз).
            -  `keep_dice_str = input(...)`: Запрашивает у игрока, какие кубики нужно оставить, вводятся индексы (1-5) через пробел, 0 - перебросить все, n - не перебрасывать.
            - `if keep_dice_str.lower() == 'n': break`: Если игрок вводит `n`, то цикл бросков завершается
            - `if keep_dice_str == '0':`: Если игрок вводит `0`, то все кубики перебрасываются заново.
            - `try... except ValueError`: Блок try-except для обработки ошибок ввода.
            - `keep_indices = [int(i) - 1 for i in keep_dice_str.split()]`: Преобразует введенные индексы в список индексов для оставления кубиков.
            -  `new_dice = []` Создается пустой массив для новых кубиков.
            -   `for i in range(5):`: Цикл по всем кубикам.
            -   `if i not in keep_indices:`: Если кубик не нужно оставлять, то он перебрасывается заново.
            -  `else:`: Если кубик нужно оставить, то он добавляется в новый список из старого.
            - `dice = new_dice`: Обновляет массив кубиков.
            - `print(f"Новый бросок: {dice}")`: Выводит результаты нового броска на экран.
        - `available_categories = [cat for cat in categories if cat not in used_categories]`: формируется список доступных категорий.
        - `print("Доступные категории:")` и `for ...`: Выводится список доступных категорий на экран.
        - `while True:`: Цикл для выбора категории игроком.
             - `try... except ValueError:`: Блок try-except для обработки ошибок ввода.
             - `choice_index = int(input(...))-1`: Запрашивает ввод номера выбранной категории.
             -  `if  0 <= choice_index < len(available_categories) :`: Проверка, что выбранный индекс существует в массиве доступных категорий.
             - `category_choice = available_categories[choice_index]`: Сохраняем выбранную категорию.
             - `break`: Завершаем цикл, если ввод корректен.
        - `score = calculate_score(dice, category_choice)`: Вычисляет очки для выбранной категории.
        - `scores[category_choice] = score`: Сохраняет очки в словаре `scores`.
        - `used_categories.add(category_choice)`: Добавляет выбранную категорию в множество `used_categories`.
        - `print(f"Очки за категорию {category_choice}: {score}")`: Выводит набранные очки для выбранной категории.
    -  `print("\n----- Итоговая таблица очков -----")` и `for ...`: Вывод итоговой таблицы очков.
    -  `total_score = sum(score if score is not None else 0 for score in scores.values())`: Подсчет общего количества очков.
    - `print(f"Общий счет: {total_score}")`: Вывод общего количества очков.

5. **Запуск игры**:
    - `if __name__ == "__main__":`: Этот блок гарантирует, что функция `play_yahtzee()` будет запущена, только если файл исполняется напрямую, а не импортируется как модуль.
    - `play_yahtzee()`: Вызывает функцию для начала игры.
"""

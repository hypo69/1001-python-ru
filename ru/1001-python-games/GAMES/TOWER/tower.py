"""
TOWER:
=================
Сложность: 4
-----------------
Игра "Башня" - это игра, в которой игрок пытается построить башню, вводя высоту каждого этажа. Цель - построить башню как можно выше, но есть ограничение: если текущий этаж будет меньше предыдущего, то башня рухнет.

Правила игры:
1. Игрок начинает с высоты первого этажа.
2. На каждом последующем этапе игрок вводит высоту следующего этажа.
3. Если высота текущего этажа больше высоты предыдущего этажа, то этаж добавляется к башне, и игра продолжается.
4. Если высота текущего этажа равна или меньше высоты предыдущего этажа, то башня рушится, и игра заканчивается.
5. Цель игры - построить башню как можно выше, то есть как можно больше этажей.
-----------------
Алгоритм:
1. Установить начальную высоту башни 0.
2. Установить начальную высоту предыдущего этажа 0.
3. Установить номер этажа 0.
4. Начать цикл:
   4.1 Увеличить номер этажа на 1.
   4.2 Запросить у игрока ввод высоты текущего этажа.
   4.3 Если высота текущего этажа больше высоты предыдущего этажа:
       4.3.1 Установить высоту предыдущего этажа равной высоте текущего этажа.
   4.4 Иначе:
      4.4.1 Вывести сообщение о том, что башня рухнула.
      4.4.2 Вывести сообщение о высоте башни, то есть номер этажа минус 1.
      4.4.3 Завершить игру.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:<br><code><b>towerHeight = 0</b></code><br><code><b>previousFloorHeight = 0</b></code><br><code><b>floorNumber = 0</b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла"}
    LoopStart --> IncreaseFloorNumber["<code><b>floorNumber = floorNumber + 1</b></code>"]
    IncreaseFloorNumber --> InputFloorHeight["Ввод высоты текущего этажа: <code><b>currentFloorHeight</b></code>"]
    InputFloorHeight --> CheckFloorHeight{"Проверка: <code><b>currentFloorHeight > previousFloorHeight</b></code>?"}
    CheckFloorHeight -- Да --> UpdatePreviousFloorHeight["<code><b>previousFloorHeight = currentFloorHeight</b></code>"]
    UpdatePreviousFloorHeight --> LoopStart
    CheckFloorHeight -- Нет --> OutputGameOver["Вывод сообщения: <b>TOWER COLLAPSED!</b>"]
    OutputGameOver --> OutputTowerHeight["Вывод сообщения: <b>TOWER HEIGHT IS <code>{floorNumber - 1}</code></b>"]
    OutputTowerHeight --> End["Конец"]
```
Legenda:
    Start - Начало программы.
    InitializeVariables - Инициализация переменных: towerHeight (высота башни) устанавливается в 0, previousFloorHeight (высота предыдущего этажа) устанавливается в 0, floorNumber (номер этажа) устанавливается в 0.
    LoopStart - Начало цикла, продолжающегося до тех пор, пока башня не рухнет.
    IncreaseFloorNumber - Увеличение номера этажа на 1.
    InputFloorHeight - Запрос у пользователя ввода высоты текущего этажа и сохранение его в переменной currentFloorHeight.
    CheckFloorHeight - Проверка, больше ли высота текущего этажа currentFloorHeight высоты предыдущего этажа previousFloorHeight.
    UpdatePreviousFloorHeight - Обновление высоты предыдущего этажа previousFloorHeight значением высоты текущего этажа currentFloorHeight.
    OutputGameOver - Вывод сообщения о том, что башня рухнула.
    OutputTowerHeight - Вывод сообщения о высоте башни (floorNumber - 1).
    End - Конец программы.

"""


# Инициализация переменных
towerHeight = 0 # текущая высота башни
previousFloorHeight = 0 # высота предыдущего этажа
floorNumber = 0 # номер текущего этажа

# Начало основного цикла игры
while True:
    # Увеличиваем номер этажа
    floorNumber += 1

    try:
        # Запрашиваем высоту текущего этажа
        currentFloorHeight = int(input(f"Введите высоту этажа {floorNumber}: "))
    except ValueError:
        print("Пожалуйста, введите целое число.")
        continue

    # Проверяем, больше ли текущая высота этажа предыдущей
    if currentFloorHeight > previousFloorHeight:
        # Если больше, то обновляем высоту предыдущего этажа
        previousFloorHeight = currentFloorHeight
    else:
        # Если текущая высота меньше или равна предыдущей, то башня рушится
        print("БАШНЯ РУХНУЛА!")
        print(f"Высота башни: {floorNumber - 1}")
        break  # Завершаем игру

"""
Объяснение кода:
1.  **Инициализация переменных:**
    - `towerHeight = 0`: Переменная `towerHeight` (высота башни) инициализируется нулем.
    - `previousFloorHeight = 0`: Переменная `previousFloorHeight` (высота предыдущего этажа) инициализируется нулем.
    - `floorNumber = 0`: Переменная `floorNumber` (номер текущего этажа) инициализируется нулем.
2.  **Основной цикл игры `while True:`**:
    - Цикл продолжается до тех пор, пока башня не рухнет (т.е., пока не выполнится команда `break`).
    -  `floorNumber += 1`: Увеличивает номер этажа на 1 перед каждой новой итерацией цикла.
    - **Ввод данных**:
        -   `try...except ValueError`: Блок try-except обрабатывает возможные ошибки ввода. Если пользователь введет не целое число, то будет выведено сообщение об ошибке.
        -  `currentFloorHeight = int(input(f"Введите высоту этажа {floorNumber}: "))`: Запрашивает у пользователя высоту текущего этажа и сохраняет его в `currentFloorHeight`.
    -  **Проверка условия падения башни**:
       -   `if currentFloorHeight > previousFloorHeight:`: Проверяет, больше ли текущая высота этажа, чем высота предыдущего этажа.
       -   Если условие верно, то: `previousFloorHeight = currentFloorHeight` - высота предыдущего этажа обновляется до высоты текущего этажа.
       -   `else`: Если условие не выполняется (текущая высота этажа меньше или равна предыдущей), то:
           - `print("БАШНЯ РУХНУЛА!")`: Выводится сообщение о падении башни.
           - `print(f"Высота башни: {floorNumber - 1}")`: Выводится сообщение об итоговой высоте башни.
           - `break`:  цикл завершается.
"""

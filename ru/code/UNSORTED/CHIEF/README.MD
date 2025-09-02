CHIEF:
=================
Сложность: 4
-----------------
Игра "CHIEF" - это игра, в которой игрок выступает в роли начальника, планирующего производство на фабрике. Игрок устанавливает количество произведенных изделий каждого типа, и компьютер определяет, соответствуют ли эти значения необходимым требованиям. Если нет, игроку сообщается, какие именно значения были неверны. Цель игры - достичь оптимального производства, правильно угадывая количество изделий.

Правила игры:
1. Компьютер загадывает три значения в диапазоне от 1 до 10: `targetA`, `targetB` и `targetC`.
2. Игрок вводит свои предположения о значениях `userA`, `userB` и `userC`.
3. Компьютер проверяет, совпадают ли введенные значения с загаданными.
4. Если все три значения угаданы, игра заканчивается победой.
5. Если хотя бы одно значение не совпадает, компьютер выводит, какие именно значения были неверными.
6. Игра продолжается до тех пор, пока игрок не угадает все три значения.
-----------------
Алгоритм:
1.  Сгенерировать случайные целые числа `targetA`, `targetB` и `targetC` в диапазоне от 1 до 10.
2.  Начать цикл "пока не угаданы все числа":
    2.1 Запросить у игрока ввод трех целых чисел: `userA`, `userB` и `userC`.
    2.2 Инициализировать строку `message` как пустую.
    2.3 Если `userA` не равно `targetA`, добавить "A" к `message`.
    2.4 Если `userB` не равно `targetB`, добавить "B" к `message`.
    2.5 Если `userC` не равно `targetC`, добавить "C" к `message`.
    2.6 Если `message` не пустая, вывести сообщение "WRONG ON " и `message`.
    2.7 Иначе, вывести сообщение "YOU GOT IT!".
3. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:
    <code><b>
    targetA = random(1, 10)
    targetB = random(1, 10)
    targetC = random(1, 10)
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: пока не угадано"}
    LoopStart --> InputValues["<p align='left'>Ввод чисел пользователем:
    <code><b>
    userA
    userB
    userC
    </b></code></p>"]
    InputValues --> InitializeMessage["<code><b>message = ""</b></code>"]
    InitializeMessage --> CheckA{"Проверка: <code><b>userA == targetA?</b></code>"}
    CheckA -- Нет --> AppendA["<code><b>message = message + 'A'</b></code>"]
    AppendA --> CheckB{"Проверка: <code><b>userB == targetB?</b></code>"}
    CheckA -- Да --> CheckB
    CheckB -- Нет --> AppendB["<code><b>message = message + 'B'</b></code>"]
    AppendB --> CheckC{"Проверка: <code><b>userC == targetC?</b></code>"}
    CheckB -- Да --> CheckC
    CheckC -- Нет --> AppendC["<code><b>message = message + 'C'</b></code>"]
    AppendC --> CheckMessage{"Проверка: <code><b>message != "" ?</b></code>"}
    CheckC -- Да --> CheckMessage
    CheckMessage -- Да --> OutputWrong["Вывод сообщения: <b>WRONG ON {message}</b>"]
    OutputWrong --> LoopStart
    CheckMessage -- Нет --> OutputWin["Вывод сообщения: <b>YOU GOT IT!</b>"]
    OutputWin --> End["Конец"]
    LoopStart -- Нет --> End
```
Legenda:
    Start - Начало программы.
    InitializeVariables - Инициализация переменных: `targetA`, `targetB`, `targetC` генерируются случайным образом от 1 до 10.
    LoopStart - Начало цикла, который продолжается, пока игрок не угадает все числа.
    InputValues - Запрос у пользователя ввода трех чисел `userA`, `userB`, `userC`.
    InitializeMessage - Инициализация пустой строки `message`.
    CheckA - Проверка, равно ли введенное число `userA` загаданному числу `targetA`.
    AppendA - Добавление 'A' к `message`, если `userA` не равно `targetA`.
    CheckB - Проверка, равно ли введенное число `userB` загаданному числу `targetB`.
    AppendB - Добавление 'B' к `message`, если `userB` не равно `targetB`.
    CheckC - Проверка, равно ли введенное число `userC` загаданному числу `targetC`.
    AppendC - Добавление 'C' к `message`, если `userC` не равно `targetC`.
    CheckMessage - Проверка, является ли строка `message` пустой.
    OutputWrong - Вывод сообщения "WRONG ON" и содержимого `message`, если строка не пуста.
    OutputWin - Вывод сообщения "YOU GOT IT!", если строка `message` пуста.
    End - Конец программы.
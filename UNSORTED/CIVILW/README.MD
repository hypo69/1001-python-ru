CIVILW:
=================
Сложность: 7
-----------------
Игра "Гражданская война" представляет собой симуляцию сражения между двумя армиями: Конфедерацией и Союзом. Игрок управляет Конфедерацией и принимает решения о численности своих войск и типе атак (прямая атака или обходной маневр). Цель игры - победить армию Союза, минимизируя свои потери. Игра учитывает случайные факторы, влияющие на исход сражения, что делает каждое сражение уникальным.

Правила игры:
1.  Игрок управляет армией Конфедерации и должен победить армию Союза.
2.  Игрок вводит количество солдат для атаки.
3.  Игрок выбирает тип атаки: прямая (1) или обходная (2).
4.  В зависимости от выбора игрока и случайных факторов, производится расчет потерь для обеих сторон.
5.  После каждого сражения, игра выводит текущую численность войск обеих сторон.
6.  Игра завершается победой одной из сторон, когда численность войск противника становится равна или меньше 0.
-----------------
Алгоритм:
1. Установить начальную численность армии Союза (UnionForce) равной 1000 и армии Конфедерации (ConfederateForce) равной 800.
2. Начать цикл "пока обе армии имеют численность больше 0":
    2.1. Запросить у игрока количество солдат, которых он хочет отправить в атаку (AttackForce).
        2.1.1. Если AttackForce больше, чем имеющиеся силы Конфедерации (ConfederateForce), то вывести сообщение "Недостаточно сил" и вернуться к началу шага 2.1
    2.2. Запросить у игрока тип атаки: прямая (1) или обходная (2) (AttackType).
    2.3. Вычислить потери Конфедерации (ConfederateLosses) случайным образом, умножив AttackForce на случайное число от 0 до 0.4 (для прямой атаки) или на случайное число от 0 до 0.2 (для обходного маневра).
        2.3.1. Если ConfederateLosses больше, чем AttackForce, ConfederateLosses установить равным AttackForce.
    2.4. Вычислить потери Союза (UnionLosses) случайным образом, умножив AttackForce на случайное число от 0 до 0.3.
        2.4.1. Если AttackType равно 2, то увеличить UnionLosses на случайное число от 0 до 100.
    2.5. Обновить численность армий:
        ConfederateForce = ConfederateForce - ConfederateLosses
        UnionForce = UnionForce - UnionLosses
    2.6. Вывести текущую численность армий обеих сторон.
    2.7. Проверить условие победы:
        2.7.1. Если UnionForce меньше или равен 0, то вывести сообщение "Конфедерация победила!" и закончить игру.
        2.7.2. Если ConfederateForce меньше или равен 0, то вывести сообщение "Союз победил!" и закончить игру.
3. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeForces["<p align='left'>Инициализация переменных:<br><code><b>unionForce = 1000</b></code><br><code><b>confederateForce = 800</b></code></p>"]
    InitializeForces --> LoopStart{"Начало цикла: пока обе армии > 0"}
    LoopStart -- Да --> InputAttackForce["<p align='left'>Ввод количества атакующих:<br><code><b>attackForce</b></code></p>"]
    InputAttackForce --> CheckForce{"Проверка:<br><code><b>attackForce > confederateForce?</b></code>"}
    CheckForce -- Да --> OutputInsufficient["Вывод сообщения: <b>Недостаточно сил</b>"]
    OutputInsufficient --> InputAttackForce
    CheckForce -- Нет --> InputAttackType["<p align='left'>Ввод типа атаки:<br><b>1 - прямая</b>, <b>2 - обходная</b><br><code><b>attackType</b></code></p>"]
    InputAttackType --> CalculateConfederateLosses["<p align='left'>Расчет потерь Конфедерации:<br><code><b>confederateLosses = attackForce * random(0, 0.4)</b></code><br>(или <code><b>random(0, 0.2)</b></code> для обходной атаки)<br>Если <code><b>confederateLosses > attackForce</b></code>, то <code><b>confederateLosses = attackForce</b></code></p>"]
    CalculateConfederateLosses --> CalculateUnionLosses["<p align='left'>Расчет потерь Союза:<br><code><b>unionLosses = attackForce * random(0, 0.3)</b></code><br>Если <code><b>attackType = 2</b></code>, то <code><b>unionLosses += random(0, 100)</b></code></p>"]
    CalculateUnionLosses --> UpdateForces["<p align='left'>Обновление численности армий:<br><code><b>confederateForce -= confederateLosses</b></code><br><code><b>unionForce -= unionLosses</b></code></p>"]
    UpdateForces --> OutputForces["<p align='left'>Вывод численности армий:<br><code><b>confederateForce</b></code>, <code><b>unionForce</b></code></p>"]
    OutputForces --> CheckUnionWin{"Проверка:<br><code><b>unionForce <= 0?</b></code>"}
    CheckUnionWin -- Да --> OutputConfederateWin["Вывод сообщения: <b>Конфедерация победила!</b>"]
    OutputConfederateWin --> End["Конец"]
    CheckUnionWin -- Нет --> CheckConfederateWin{"Проверка:<br><code><b>confederateForce <= 0?</b></code>"}
     CheckConfederateWin -- Да --> OutputUnionWin["Вывод сообщения: <b>Союз победил!</b>"]
    OutputUnionWin --> End
    CheckConfederateWin -- Нет --> LoopStart
    LoopStart -- Нет --> End
```
    
Legenda:
    Start - Начало программы.
    InitializeForces - Инициализация начальной численности войск Союза (unionForce = 1000) и Конфедерации (confederateForce = 800).
    LoopStart - Начало цикла, который продолжается, пока обе армии имеют численность больше 0.
    InputAttackForce - Запрос у игрока количества солдат для атаки (attackForce).
    CheckForce - Проверка, достаточно ли у Конфедерации сил для атаки (attackForce > confederateForce).
    OutputInsufficient - Вывод сообщения "Недостаточно сил", если атакующих больше, чем имеющихся сил.
    InputAttackType - Запрос у игрока выбора типа атаки: прямая (1) или обходная (2).
    CalculateConfederateLosses - Расчет потерь Конфедерации (confederateLosses) на основе attackForce и типа атаки, с учетом случайного фактора. Если потери превышают attackForce, потери устанавливаются равными attackForce.
    CalculateUnionLosses - Расчет потерь Союза (unionLosses) на основе attackForce и типа атаки, с учетом случайного фактора. При обходной атаке потери Союза дополнительно увеличиваются случайным числом.
    UpdateForces - Обновление численности войск обеих армий после сражения.
    OutputForces - Вывод текущей численности армий Конфедерации и Союза.
    CheckUnionWin - Проверка, победила ли Конфедерация (численность армии Союза <= 0).
    OutputConfederateWin - Вывод сообщения о победе Конфедерации.
    CheckConfederateWin - Проверка, победил ли Союз (численность армии Конфедерации <= 0).
    OutputUnionWin - Вывод сообщения о победе Союза.
    End - Конец программы.
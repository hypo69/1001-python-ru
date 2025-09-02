```
ORBIT:
=================
Сложность: 5
-----------------
Игра "ORBIT" - это текстовая игра, в которой игрок управляет космическим кораблем, вращающимся вокруг планеты. Цель игры - задать начальную скорость и угол, чтобы корабль вышел на стабильную орбиту.  Игрок должен угадать значения начальной скорости и угла, чтобы вывести корабль на орбиту. Игра использует симуляцию гравитационного притяжения для расчета траектории полета корабля.
Правила игры:
1. Игрок вводит начальную скорость и угол для космического корабля.
2. Игра моделирует траекторию полета корабля под воздействием гравитации.
3. Если корабль не выводится на орбиту, игроку предлагается ввести новые значения скорости и угла.
4. Игра продолжается, пока корабль не выйдет на орбиту, или не закончится количество попыток.
5. Если корабль выходит на орбиту, то игра сообщает игроку об этом.
-----------------
Алгоритм:
1. Инициализация переменных:
   - Установить начальное количество попыток в 0
   - Установить максимальное количество попыток (например 10).
2. Начать цикл "пока число попыток меньше максимального количества":
    2.1. Увеличить число попыток на 1.
    2.2. Запросить у игрока ввод начальной скорости (V).
    2.3. Запросить у игрока ввод начального угла (A).
    2.4. Преобразовать угол из градусов в радианы.
    2.5. Рассчитать компоненты начальной скорости Vx и Vy (Vx = V * Cos(A), Vy = V * Sin(A)).
    2.6. Установить начальные координаты x и y.
    2.7. Начать симуляцию движения (цикл):
        2.7.1. Рассчитать расстояние до планеты R (R = Корень(x*x + y*y)).
        2.7.2. Рассчитать ускорение Ax и Ay (Ax = -x / R^3, Ay = -y / R^3).
        2.7.3. Обновить компоненты скорости (Vx = Vx + Ax, Vy = Vy + Ay).
        2.7.4. Обновить координаты (x = x + Vx, y = y + Vy).
        2.7.5. Проверить, вышло ли тело на стабильную орбиту (если x^2 + y^2 примерно равно R^2 в течении некоторого времени).
        2.7.6. Если тело вышло на орбиту или вышло за рамки, выйти из цикла симуляции.
    2.8. Если тело вышло на стабильную орбиту, вывести сообщение "ORBIT ESTABLISHED" и перейти к шагу 3.
    2.9. Если тело не вышло на орбиту, вывести сообщение "FAILED", и повторить цикл с шага 2.
3. Конец игры.
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeVariables["<p align='left'>Инициализация переменных:
    <code><b>
    numberOfTries = 0<br>
    maxTries = 10
    </b></code></p>"]
    InitializeVariables --> LoopStart{"Начало цикла: <code><b>numberOfTries &lt; maxTries</b></code>"}
    LoopStart -- Да --> IncreaseTries["<code><b>numberOfTries = numberOfTries + 1</b></code>"]
    IncreaseTries --> InputVelocity["Ввод начальной скорости: <code><b>initialVelocity</b></code>"]
    InputVelocity --> InputAngle["Ввод начального угла: <code><b>initialAngle</b></code>"]
    InputAngle --> CalculateVelocityComponents["<p align='left'>Вычисление:
    <code><b>
    angleInRadians = initialAngle * PI / 180<br>
    velocityX = initialVelocity * cos(angleInRadians)<br>
    velocityY = initialVelocity * sin(angleInRadians)
    </b></code></p>"]
    CalculateVelocityComponents --> InitializePosition["<p align='left'>Инициализация:
    <code><b>
    x = initialX<br>
    y = initialY
    </b></code></p>"]
    InitializePosition --> SimulationLoopStart{"Начало симуляции: пока не на орбите или не вышли за рамки"}
    SimulationLoopStart --> CalculateDistance["<p align='left'>Расчет расстояния:
        <code><b>distance = sqrt(x^2 + y^2)</b></code></p>"]
    CalculateDistance --> CalculateAcceleration["<p align='left'>Расчет ускорения:
        <code><b>
        accelerationX = -x / distance^3<br>
        accelerationY = -y / distance^3
        </b></code></p>"]
    CalculateAcceleration --> UpdateVelocity["<p align='left'>Обновление скорости:
        <code><b>
        velocityX = velocityX + accelerationX<br>
        velocityY = velocityY + accelerationY
        </b></code></p>"]
    UpdateVelocity --> UpdatePosition["<p align='left'>Обновление позиции:
        <code><b>
        x = x + velocityX<br>
        y = y + velocityY
        </b></code></p>"]
    UpdatePosition --> CheckOrbit{"Проверка: <code><b>На орбите?</b></code>"}
    CheckOrbit -- Да --> OutputOrbitEstablished["Вывод: <b>ORBIT ESTABLISHED</b>"]
    OutputOrbitEstablished --> End["Конец"]
    CheckOrbit -- Нет --> CheckOutOfBound{"Проверка: <code><b>Вышли за рамки?</b></code>"}
    CheckOutOfBound -- Да --> SimulationLoopEnd["Конец цикла симуляции"]
    CheckOutOfBound -- Нет --> SimulationLoopStart
     SimulationLoopEnd --> CheckTries{"Проверка: <code><b>numberOfTries < maxTries?</b></code>"}
    CheckTries -- Да --> LoopStart
    CheckTries -- Нет --> OutputFailed["Вывод: <b>FAILED</b>"]
    OutputFailed --> End
    LoopStart -- Нет --> End
```
    
**Legenda:**
    Start - Начало программы.
    InitializeVariables - Инициализация переменных: numberOfTries (количество попыток) устанавливается в 0, maxTries (максимальное количество попыток) устанавливается в 10.
    LoopStart - Начало цикла, который продолжается, пока количество попыток меньше максимального.
    IncreaseTries - Увеличение счетчика количества попыток на 1.
    InputVelocity - Запрос у пользователя ввода начальной скорости и сохранение его в переменной initialVelocity.
    InputAngle - Запрос у пользователя ввода начального угла и сохранение его в переменной initialAngle.
    CalculateVelocityComponents - Вычисление компонентов начальной скорости: угол преобразуется в радианы, вычисляются компоненты velocityX и velocityY.
    InitializePosition - Инициализация начальных координат x и y.
    SimulationLoopStart - Начало цикла симуляции, который продолжается пока не достигнута орбита или не вышли за рамки.
    CalculateDistance - Расчет расстояния от объекта до центра планеты.
    CalculateAcceleration - Расчет ускорения по осям x и y, основываясь на расстоянии до планеты.
    UpdateVelocity - Обновление скорости объекта на основе ускорения.
    UpdatePosition - Обновление позиции объекта на основе скорости.
    CheckOrbit - Проверка, выведен ли объект на стабильную орбиту.
    OutputOrbitEstablished - Вывод сообщения о том, что орбита установлена.
    End - Конец программы.
    CheckOutOfBound - Проверка, не вышел ли объект за рамки моделирования.
    SimulationLoopEnd - Завершение цикла симуляции.
    CheckTries - Проверка, не превысило ли количество попыток максимальное значение.
    OutputFailed - Вывод сообщения о том, что не удалось выйти на орбиту.
```python
import math

# Константы для симуляции
INITIAL_X = 100  # Начальная координата X
INITIAL_Y = 0   # Начальная координата Y
TIME_STEP = 0.1   # Шаг времени для симуляции
ORBIT_TOLERANCE = 10  # Допустимое отклонение для определения стабильной орбиты
MAX_STEPS = 1000  # Максимальное количество шагов симуляции
MAX_TRIES = 10 # Максимальное количество попыток

def simulate_orbit(initial_velocity, initial_angle):
    """
    Моделирует орбиту космического корабля вокруг планеты.

    Args:
        initial_velocity (float): Начальная скорость корабля.
        initial_angle (float): Начальный угол направления корабля в градусах.

    Returns:
         bool: True, если орбита установлена; False в противном случае.
    """
    # Преобразуем угол из градусов в радианы
    angle_in_radians = math.radians(initial_angle)

    # Вычисляем компоненты начальной скорости
    velocity_x = initial_velocity * math.cos(angle_in_radians)
    velocity_y = initial_velocity * math.sin(angle_in_radians)

    # Начальные координаты
    x = INITIAL_X
    y = INITIAL_Y
    
    # Переменные для проверки стабильной орбиты
    last_distance = 0
    orbit_count = 0
    
    # Моделирование движения
    for step in range(MAX_STEPS):
        # Рассчитываем расстояние до планеты
        distance = math.sqrt(x * x + y * y)

        # Рассчитываем ускорение (гравитация)
        acceleration_x = -x / (distance ** 3)
        acceleration_y = -y / (distance ** 3)

        # Обновляем скорость
        velocity_x += acceleration_x * TIME_STEP
        velocity_y += acceleration_y * TIME_STEP

        # Обновляем позицию
        x += velocity_x * TIME_STEP
        y += velocity_y * TIME_STEP

        # Проверяем стабильность орбиты.
        if abs(distance - last_distance) < ORBIT_TOLERANCE:
           orbit_count += 1
        else:
           orbit_count = 0
        
        if orbit_count > 50: # Проверяем, что у нас 50 раз подряд расстояние не меняется.
            return True # Орбита стабильна

        last_distance = distance
        
        # Проверка выхода за рамки
        if abs(x) > 500 or abs(y) > 500 :
            return False
    
    return False # Не удалось установить орбиту
   
# Основной цикл игры
def play_orbit_game():
    """
    Запускает игру по моделированию орбиты.
    """
    
    number_of_tries = 0

    while number_of_tries < MAX_TRIES:
        number_of_tries += 1
        
        try:
            # Запрашиваем у пользователя начальную скорость и угол
            initial_velocity = float(input("Введите начальную скорость (например, 5): "))
            initial_angle = float(input("Введите начальный угол в градусах (например, 45): "))
        except ValueError:
            print("Пожалуйста, введите корректные числовые значения.")
            continue

        # Запускаем моделирование
        orbit_established = simulate_orbit(initial_velocity, initial_angle)

        if orbit_established:
            print("ORBIT ESTABLISHED")
            return  # Завершаем игру
        else:
             print("FAILED")
    print("GAME OVER")


# Запускаем игру, только если скрипт исполняется напрямую.
if __name__ == "__main__":
    play_orbit_game()

```
  
"""
Объяснение кода:

1. **Импорт модуля `math`**:
   - `import math`: Импортирует модуль `math`, который используется для математических операций, таких как `cos`, `sin`, `sqrt` и `radians`.

2. **Константы**:
    - `INITIAL_X`, `INITIAL_Y`: Начальные координаты космического корабля.
    - `TIME_STEP`: Шаг времени для симуляции движения.
    - `ORBIT_TOLERANCE`: Допустимое отклонение в расстоянии для определения стабильной орбиты.
    - `MAX_STEPS`: Максимальное количество шагов симуляции, для предотвращения бесконечного цикла.
    - `MAX_TRIES`: Максимальное количество попыток для пользователя вывести корабль на орбиту.
    
3. **Функция `simulate_orbit(initial_velocity, initial_angle)`**:
    -   `angle_in_radians = math.radians(initial_angle)`: Преобразует угол из градусов в радианы, так как тригонометрические функции в Python работают с радианами.
    -   `velocity_x = initial_velocity * math.cos(angle_in_radians)`: Вычисляет начальную компоненту скорости по оси X.
    -   `velocity_y = initial_velocity * math.sin(angle_in_radians)`: Вычисляет начальную компоненту скорости по оси Y.
    -   `x = INITIAL_X`, `y = INITIAL_Y`: Устанавливает начальные координаты корабля.
    -   **Цикл симуляции**:
        -   `for step in range(MAX_STEPS)`:  Цикл, который моделирует движение космического корабля в течение `MAX_STEPS` шагов.
        -   `distance = math.sqrt(x * x + y * y)`: Вычисляет расстояние от корабля до центра планеты.
        -   `acceleration_x = -x / (distance ** 3)`: Вычисляет ускорение по оси X (гравитационное притяжение).
        -   `acceleration_y = -y / (distance ** 3)`: Вычисляет ускорение по оси Y (гравитационное притяжение).
        -   `velocity_x += acceleration_x * TIME_STEP`: Обновляет скорость по оси X.
        -   `velocity_y += acceleration_y * TIME_STEP`: Обновляет скорость по оси Y.
        -   `x += velocity_x * TIME_STEP`: Обновляет координату X.
        -   `y += velocity_y * TIME_STEP`: Обновляет координату Y.
        -   **Проверка стабильной орбиты**:
            -   `if abs(distance - last_distance) < ORBIT_TOLERANCE:`: Проверяем, изменилось ли расстояние до центра планеты на допустимое значение.
            -   `orbit_count += 1` увеличиваем счетчик если расстояние в пределах допуска
            -   `else: orbit_count = 0`: сбрасываем счетчик, если расстояние меняется.
            -   `if orbit_count > 50`: Проверяем, что у нас 50 раз подряд расстояние не меняется.
            -   `return True`: Возвращаем `True`, если корабль вышел на стабильную орбиту
        -   `last_distance = distance`: запоминаем последнее значение расстояния.
        -    **Проверка выхода за рамки**:
            -  `if abs(x) > 500 or abs(y) > 500`: Проверяет, не вышел ли корабль за рамки моделирования.
            -  `return False`: Возвращаем `False`, если корабль вышел за рамки.
    -  `return False`:  Возвращает `False`, если орбита не была установлена за `MAX_STEPS` шагов.

4. **Функция `play_orbit_game()`**:
    -   `number_of_tries = 0`: Инициализирует счетчик попыток пользователя.
    -   **Цикл `while number_of_tries < MAX_TRIES`**: Цикл, который продолжается, пока число попыток не достигнет `MAX_TRIES`.
    -   `number_of_tries += 1`: Увеличивает счетчик попыток.
    -   `try...except ValueError`: Обработка исключений, если пользователь ввел некорректное значение.
    -   `initial_velocity = float(input("Введите начальную скорость (например, 5): "))`: Запрашивает у пользователя ввод начальной скорости.
    -   `initial_angle = float(input("Введите начальный угол в градусах (например, 45): "))`: Запрашивает у пользователя ввод начального угла в градусах.
    -   `orbit_established = simulate_orbit(initial_velocity, initial_angle)`: Вызывает функцию `simulate_orbit` для моделирования орбиты.
    -   `if orbit_established: print("ORBIT ESTABLISHED"); return`: Если орбита установлена, выводится сообщение и игра заканчивается.
    -   `else: print("FAILED")`: Если орбита не установлена, выводится сообщение о неудаче.
    -   `print("GAME OVER")`: Выводится в конце игры, если не удалось вывести на орбиту за `MAX_TRIES` попыток.

5. **Запуск игры**:
    -   `if __name__ == "__main__":`: Проверяет, запущен ли скрипт напрямую.
    -   `play_orbit_game()`: Вызывает функцию `play_orbit_game` для начала игры.

"""

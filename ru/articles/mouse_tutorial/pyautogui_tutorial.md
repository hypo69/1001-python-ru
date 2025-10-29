
## 3. Файл статьи для `pyautogui`: `pyautogui_tutorial.md`

```markdown
# Управление мышью в Python: Библиотека 'pyautogui'

Библиотека `pyautogui` — это мощный инструмент для автоматизации графического интерфейса пользователя (GUI). Помимо управления мышью, он включает управление клавиатурой, скриншоты и поиск изображений.

## Шаг 1: Установка

```bash
pip install pyautogui
```

## Шаг 2: Безопасность и настройки **(Важная особенность)**

`pyautogui` включает механизм экстренного завершения: быстрое перемещение курсора в верхний левый угол (0, 0) прервет выполнение.

```python
import pyautogui
# Установите паузу между всеми командами pyautogui
pyautogui.PAUSE = 0.1 
# Включает/отключает механизм экстренного завершения в углу (по умолчанию True)
pyautogui.FAILSAFE = True 
```

## Шаг 3: Получение информации об экране

`pyautogui` предоставляет удобные функции для работы с размером экрана.

```python
screen_width, screen_height = pyautogui.size()
print(f"Разрешение экрана: {screen_width}x{screen_height}")
```

## Шаг 4: Перемещение и Щелчки

Для перемещения используется `pyautogui.moveTo()`. Для щелчков — `pyautogui.click()`, который включает как перемещение, так и щелчок.

```python
# Перемещение курсора в (100, 100)
pyautogui.moveTo(100, 100, duration=0.5)

# Двойной щелчок по текущей позиции
pyautogui.doubleClick()

# Правый щелчок по (200, 200)
pyautogui.rightClick(200, 200)
```

## Шаг 5: Перетаскивание (Drag)

`pyautogui` использует `pyautogui.dragTo()` для абсолютного перетаскивания и `pyautogui.dragRel()` для относительного.

```python
# Перетаскивание относительно текущей позиции (на 100 вправо, на 100 вниз)
pyautogui.dragRel(100, 100, duration=0.5) 
```

## Шаг 6: Прокрутка **(Специальные возможности)**

Функция `pyautogui.scroll()` позволяет прокручивать окно.

```python
# Прокрутка вверх на 100 единиц
pyautogui.scroll(100)
```

## Шаг 7: Текущее положение

Получение текущих координат:

```python
current_x, current_y = pyautogui.position()
```

## Шаг 8: Пример рисования

Полный пример, включающий функции `draw_pyautogui_square` и `draw_pyautogui_circle` (см. `pyautogui_manipulation.py`).

---

## 4. Код для `pyautogui`: `pyautogui_manipulation.py`

(Этот файл является той же версией, которую я предоставлял ранее, адаптированной для `pyautogui`).

```python
# pyautogui_manipulation.py

import pyautogui
import time
import math

# ======================================================================
# Настройки безопасности и паузы
# ======================================================================
pyautogui.PAUSE = 0.1 # Пауза после каждого вызова функции
pyautogui.FAILSAFE = True # Экстренное завершение в верхнем левом углу

# ======================================================================
# Вспомогательные функции для рисования
# ======================================================================

def draw_pyautogui_square(size):
    """Рисует квадрат, используя pyautogui.dragRel."""
    print(f"Рисуем квадрат размером {size}...")
    # dragRel() = относительное перетаскивание
    pyautogui.dragRel(size, 0, duration=0.25)
    pyautogui.dragRel(0, size, duration=0.25)
    pyautogui.dragRel(-size, 0, duration=0.25)
    pyautogui.dragRel(0, -size, duration=0.25)
    print("Квадрат нарисован.")

def draw_pyautogui_circle(radius):
    """
    Рисует круг, используя абсолютное позиционирование pyautogui.moveTo 
    с нажатой кнопкой.
    """
    print(f"Рисуем круг радиусом {radius}...")
    
    current_x, current_y = pyautogui.position() 
    
    # Центр круга относительно текущей позиции. 
    # Смещаем центр для начала рисования
    center_x = current_x
    center_y = current_y 
    
    pyautogui.mouseDown() # Нажимаем левую кнопку
    
    # Рисуем круг, используя абсолютные координаты
    for i in range(0, 360, 5):
        angle = math.radians(i)
        
        # Рассчитываем абсолютные координаты точки на окружности
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        
        # moveTo() перемещает курсор. Так как кнопка нажата, происходит перетаскивание.
        pyautogui.moveTo(x, y, duration=0.01)
        
    pyautogui.mouseUp() # Отпускаем кнопку
    print("Круг нарисован.")


# ======================================================================
# Основная часть программы (Выполнение учебных шагов)
# ======================================================================

if __name__ == "__main__":
    
    print("--- Запуск учебного кода 'pyautogui_manipulation.py' (Библиотека: pyautogui) ---")
    
    # --- Шаг 3: Информация об экране ---
    print("\n--- Шаг 3: Информация об экране ---")
    screen_width, screen_height = pyautogui.size()
    print(f"Разрешение экрана: {screen_width}x{screen_height}")
    time.sleep(1)

    # --- Шаг 4: Перемещение и Щелчки ---
    print("\n--- Шаг 4: Перемещение и Щелчки ---")
    print("ВНИМАНИЕ: Курсор мыши сейчас будет перемещаться и кликать!")
    
    # Перемещение курсора в (100, 100)
    pyautogui.moveTo(100, 100, duration=0.5)
    print("Курсор перемещен в (100, 100).")
    time.sleep(1)
    
    # Щелчки
    pyautogui.click(200, 200) 
    print("Выполнен левый щелчок по (200, 200).")
    time.sleep(1)
    
    pyautogui.doubleClick() 
    print("Выполнен двойной щелчок.")
    time.sleep(1)
    
    pyautogui.rightClick() 
    print("Выполнен правый щелчок.")
    time.sleep(1)


    # --- Шаг 5: Перетаскивание (Drag) ---
    print("\n--- Шаг 5: Перетаскивание (Drag) ---")
    pyautogui.moveTo(400, 400, duration=0.5)
    print("Курсор перемещен в (400, 400).")
    
    # Перетаскивание на 100 пикселей вниз и вправо
    pyautogui.dragRel(100, 100, duration=0.5) 
    print("Выполнено относительное перетаскивание.")
    time.sleep(1)


    # --- Шаг 6: Прокрутка ---
    print("\n--- Шаг 6: Прокрутка ---")
    # Прокрутка вниз на 50 единиц
    pyautogui.scroll(-50) 
    print("Выполнена прокрутка вниз.")
    time.sleep(1)


    # --- Шаг 7: Текущее положение ---
    print("\n--- Шаг 7: Текущее положение ---")
    current_x, current_y = pyautogui.position()
    print(f"Текущее положение: ({current_x}, {current_y})")
    time.sleep(1)


    # --- Шаг 8: Рисование (Квадрат и Круг) ---
    print("\n--- Шаг 8: Рисование (Квадрат и Круг) ---")
    print("ВНИМАНИЕ: Переместите курсор в пустую область (например, в Paint) для рисования!")
    pyautogui.moveTo(500, 500, duration=0.5) # Перемещаем курсор в стартовую точку
    time.sleep(2) 
    
    # 1. Рисуем квадрат
    draw_pyautogui_square(100)
    time.sleep(1) 
    
    # 2. Рисуем круг (начнется с последней позиции курсора)
    draw_pyautogui_circle(50)
    
    print("\n--- Код PyAutoGUI завершен ---")
```
## Управление мышью в Python: пошаговое руководство


**Шаг 1: Установка библиотеки `mouse`**

```bash
pip install mouse
```

**Шаг 2: Симулирование щелчков мышью**

&nbsp;&nbsp;&nbsp;&nbsp; Библиотека `mouse` позволяет имитировать щелчки левой, правой и средней кнопок мыши:

```python
import mouse

# Левый щелчок
mouse.click('left')

# Правый щелчок
mouse.click('right')

# Средний щелчок
mouse.click('middle')

# Проверка нажатия кнопки
is_pressed = mouse.is_pressed("right")
print(f"Правая кнопка нажата: {is_pressed}")
```

*Примечание: рекомендуется тестировать код по отдельности в интерактивной среде, такой как IPython или Jupyter Notebook.*


**Шаг 3: Получение позиции курсора мыши**

Функция `mouse.get_position()` возвращает текущие координаты курсора (x, y):

```python
position = mouse.get_position()
print(f"Позиция курсора: {position}")
```

Координаты (0, 0) обычно соответствуют левому верхнему углу экрана.  Наличие нескольких мониторов может повлиять на значения координат.


**Шаг 4: Перетаскивание мыши**

&nbsp;&nbsp;&nbsp;&nbsp; Для перетаскивания курсора используется функция `mouse.drag()`:

```python
# Перетаскивание из (0, 0) в (100, 100) относительно текущей позиции (относительное перемещение)
mouse.drag(0, 0, 100, 100, absolute=False, duration=0.1)

# Перетаскивание из абсолютной позиции (100, 100) в абсолютную позицию (200, 200)
mouse.drag(100, 100, 200, 200, absolute=True, duration=0.2)
```

`absolute=False` указывает на относительное перемещение, а `absolute=True` – на абсолютное.  `duration` задает продолжительность перетаскивания в секундах.


**Шаг 5: Перемещение мыши**

&nbsp;&nbsp;&nbsp;&nbsp; Функция `mouse.move()` перемещает курсор в указанную позицию:

```python
# Перемещение на 100 пикселей вправо и 50 пикселей вниз относительно текущей позиции
mouse.move(100, 50, absolute=False, duration=0.2)

# Перемещение в абсолютную позицию (200, 300)
mouse.move(200, 300, absolute=True, duration=0.1)
```


**Шаг 6: Обработка событий мыши**

&nbsp;&nbsp;&nbsp;&nbsp; Можно использовать функции `mouse.on_click()` и `mouse.on_right_click()` для создания обработчиков событий щелчков:


```python
def left_click_handler():
    print("Нажата левая кнопка мыши")

def right_click_handler():
    print("Нажата правая кнопка мыши")


mouse.on_click(left_click_handler)
mouse.on_right_click(right_click_handler)

# ... (ваш код) ...

# Для удаления обработчиков:
mouse.unhook_all()
```


**Шаг 7: Прокрутка колеса мыши**

&nbsp;&nbsp;&nbsp;&nbsp; Функция `mouse.wheel()` имитирует прокрутку:

```python
# Прокрутка вниз на один шаг
mouse.wheel(-1)

# Прокрутка вверх на три шага
mouse.wheel(3)
```


**Шаг 8: Запись и воспроизведение событий мыши**

&nbsp;&nbsp;&nbsp;&nbsp; Можно записывать последовательность событий мыши и затем воспроизводить их:

```python
# Запись событий до нажатия правой кнопки
events = mouse.record()

# Воспроизведение записанных событий (исключая последний - нажатие правой кнопки)
mouse.play(events[:-1])
```


**Шаг 9: Пример: Рисование фигуры (дополнительно)**

&nbsp;&nbsp;&nbsp;&nbsp; Этот пример рисует квадрат и круг в графическом редакторе (например, Paint):

```python
import mouse
import math
import time

def draw_square(size):
    mouse.press()  # Нажимаем левую кнопку
    mouse.move(size, 0, absolute=False, duration=0.2)
    mouse.move(0, size, absolute=False, duration=0.2)
    mouse.move(-size, 0, absolute=False, duration=0.2)
    mouse.move(0, -size, absolute=False, duration=0.2)
    mouse.release() # Отпускаем кнопку

def draw_circle(radius):
    mouse.press()
    for i in range(0, 360, 5):
        angle = math.radians(i)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        mouse.move(x, y, absolute=False, duration=0.01)
    mouse.release()

if __name__ == "__main__":
    draw_square(200)
    time.sleep(1)  # Пауза перед рисованием круга
    draw_circle(100)
```

Перед запуском этого кода убедитесь, что курсор мыши находится в нужном месте в графическом редакторе.

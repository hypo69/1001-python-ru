# mouse_manipulation_pynput.py
# Учебный код для демонстрации работы с библиотекой 'pynput.mouse' в Python.
# ----------------------------------------------------------------------
# Шаг 1: Установка библиотеки 'pynput' (выполнить в терминале):
# pip install pynput
# ----------------------------------------------------------------------

from pynput import mouse
from pynput.mouse import Controller, Button
import math
import time

# ======================================================================
# Шаг 9: Вспомогательные функции для рисования
# ======================================================================

def draw_square(size):
    """Рисует квадрат, используя относительное перемещение."""
    print(f"Рисуем квадрат размером {size}...")
    mouse_ctrl = Controller()
    
    # Нажимаем левую кнопку
    mouse_ctrl.press(Button.left)
    
    # Рисуем 4 стороны (относительное перемещение)
    mouse_ctrl.move(size, 0)
    time.sleep(0.2)
    mouse_ctrl.move(0, size)
    time.sleep(0.2)
    mouse_ctrl.move(-size, 0)
    time.sleep(0.2)
    mouse_ctrl.move(0, -size)
    time.sleep(0.2)
    
    # Отпускаем кнопку
    mouse_ctrl.release(Button.left)
    print("Квадрат нарисован.")


def draw_circle(radius):
    """
    Рисует круг. Использует абсолютное позиционирование.
    """
    print(f"Рисуем круг радиусом {radius}...")
    mouse_ctrl = Controller()
    
    # Текущая позиция — центр круга
    center_x, center_y = mouse_ctrl.position
    
    mouse_ctrl.press(Button.left)
    
    # Рисуем точки по окружности
    for i in range(0, 360, 5):
        angle = math.radians(i)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        mouse_ctrl.position = (x, y)
        time.sleep(0.01)  # небольшая задержка для плавности
    
    mouse_ctrl.release(Button.left)
    print("Круг нарисован.")


# ======================================================================
# Основная часть программы
# ======================================================================

if __name__ == "__main__":
    mouse_ctrl = Controller()
    print("--- Запуск учебного кода 'mouse_manipulation_pynput.py' ---")

    # --- Шаг 2: Симулирование щелчков и проверка нажатия ---
    print("\n--- Шаг 2: Щелчки и проверка нажатия ---")
    
    # ВНИМАНИЕ: Раскомментируйте, чтобы выполнить реальный клик
    # mouse_ctrl.click(Button.left)
    # mouse_ctrl.click(Button.right)
    
    print("Пожалуйста, нажмите и удерживайте правую кнопку мыши (3 сек)...")
    time.sleep(3)
    # pynput не предоставляет прямой функции is_pressed,
    # поэтому проверка состояния кнопки невозможна без слушателя.
    # Это ограничение — состояние кнопок отслеживается только через Listener.
    print("Примечание: pynput не позволяет напрямую проверить, нажата ли кнопка вне Listener.")
    time.sleep(1)


    # --- Шаг 3: Получение позиции курсора ---
    print("\n--- Шаг 3: Получение позиции курсора ---")
    position = mouse_ctrl.position
    print(f"Текущая позиция курсора: {position}")
    time.sleep(1)


    # --- Шаг 5: Перемещение курсора ---
    print("\n--- Шаг 5: Перемещение курсора ---")
    print("ВНИМАНИЕ: Курсор мыши сейчас будет перемещаться!")
    mouse_ctrl.position = (200, 300)
    print("Курсор перемещён в (200, 300).")
    time.sleep(1)


    # --- Шаг 4: Перетаскивание (drag) ---
    print("\n--- Шаг 4: Перетаскивание ---")
    # В pynput drag делается вручную: press → move → release
    mouse_ctrl.position = (200, 300)
    mouse_ctrl.press(Button.left)
    mouse_ctrl.position = (300, 400)
    time.sleep(0.5)
    mouse_ctrl.release(Button.left)
    print("Выполнено перетаскивание из (200, 300) в (300, 400).")
    time.sleep(2)


    # --- Шаг 6: Обработка событий мыши ---
    print("\n--- Шаг 6: Обработка событий мыши ---")
    
    def on_click(x, y, button, pressed):
        if button == Button.left and pressed:
            print(f">> [ОБРАБОТЧИК] Левый клик в ({x}, {y})")
    
    listener = mouse.Listener(on_click=on_click)
    listener.start()
    print("Обработчик левого щелчка активен на 5 секунд. Попробуйте кликнуть.")
    time.sleep(5)
    listener.stop()
    listener.join()  # дожидаемся завершения потока
    print("Обработчики удалены.")
    time.sleep(1)


    # --- Шаг 7: Прокрутка колеса мыши ---
    print("\n--- Шаг 7: Прокрутка колеса мыши ---")
    mouse_ctrl.scroll(0, -2)  # dx=0, dy=-2 → вниз
    print("Выполнена прокрутка колеса вниз.")
    time.sleep(1)


    # --- Шаг 8: Запись и воспроизведение событий ---
    print("\n--- Шаг 8: Запись и воспроизведение ---")
    print("Библиотека pynput НЕ поддерживает встроенную запись/воспроизведение.")
    print("Для реализации нужно вручную логировать события и воспроизводить их.")
    print("Пример такого подхода выходит за рамки учебного скрипта.")
    time.sleep(1)


    # --- Шаг 9: Рисование фигур ---
    print("\n--- Шаг 9: Рисование (Квадрат и Круг) ---")
    print("ВНИМАНИЕ: Переместите курсор в пустую область (например, в Paint)!")
    time.sleep(3)

    draw_square(100)
    time.sleep(1)
    draw_circle(50)

    print("\n--- Код завершён ---")
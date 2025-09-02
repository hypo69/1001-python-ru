"""
Игра "Исследователь химическеских элементов" (Расширенная версия)

Этот код позволяет пользователю вводить химический символ и получать подробную
информацию об этом элементе из периодической таблицы, используя библиотеку
'periodictable'. Добавлены возможности поиска ближайшего элемента по атомной
массе и изучения (базовой) информации о валентности.
"""

import periodictable  # Импортируем библиотеку для работы с периодической таблицей

def get_element_info(symbol):
    """
    Получает и отображает основную информацию о химическом элементе по его символу.

    Аргументы:
        symbol (str): Химический символ элемента (например, 'Na', 'He', 'O').
    """
    element = getattr(periodictable, symbol, None)  # Пытаемся получить элемент по символу
    if element:
        print(f"\n--- Информация об элементе '{element.name}' ({element.symbol}) ---")
        print(f"Название: {element.name}")
        print(f"Символ: {element.symbol}")
        print(f"Атомный номер: {element.number}")
        print(f"Атомная масса: {element.mass} u")
        if hasattr(element, 'valence'):
            print(f"Валентность (примерно): {element.valence}")
        else:
            print("Информация о валентности недоступна.")
        return element
    else:
        print(f"Элемент '{symbol}' не найден в периодической таблице.")
        return None

def find_closest_by_mass(target_mass, exclude_element=None):
    """
    Находит элемент с атомной массой, наиболее близкой к заданной.

    Аргументы:
        target_mass (float): Целевая атомная масса для поиска.
        exclude_element (periodictable.Element, optional): Элемент, который следует исключить из поиска (например, сам введенный элемент). По умолчанию None.

    Возвращает:
        periodictable.Element или None: Элемент с ближайшей атомной массой, или None, если не найден.
    """
    closest_element = None
    min_difference = float('inf')

    for symbol in periodictable.elements:
        element = getattr(periodictable, symbol)
        if exclude_element and element.symbol == exclude_element.symbol:
            continue  # Пропускаем исключенный элемент

        difference = abs(element.mass - target_mass)
        if difference < min_difference:
            min_difference = difference
            closest_element = element
        elif difference == min_difference and closest_element and element.number < closest_element.number:
            # Если разница одинаковая, выбираем элемент с меньшим атомным номером (произвольное решение)
            closest_element = element

    return closest_element

def explore_valence(element):
    """
    Предоставляет (базовую) информацию о валентности элемента, если она доступна.

    Аргументы:
        element (periodictable.Element): Объект элемента для изучения валентности.
    """
    if element and hasattr(element, 'valence'):
        print(f"\n--- Информация о валентности '{element.name}' ---")
        print(f"Возможные валентности (примерно): {element.valence}")
        print("Обратите внимание: это упрощенное представление валентности.")
        print("Реальные валентные состояния могут быть более сложными.")
    elif element:
        print(f"\nИнформация о валентности для '{element.name}' недоступна.")

def main():
    while True:
        symbol = input("\nВведите химический элемент (или 'выход' для завершения): ").capitalize()
        if symbol == 'Выход':
            break

        element = get_element_info(symbol)

        if element:
            while True:
                action = input("\nВыберите действие:\n"
                               "1. Найти ближайший элемент по атомной массе\n"
                               "2. Изучить валентность\n"
                               "3. Ввести другой элемент\n"
                               "Введите номер действия: ")
                if action == '1':
                    try:
                        target_mass = float(input("Введите целевую атомную массу (или оставьте пустым для массы текущего элемента): ") or element.mass)
                        closest = find_closest_by_mass(target_mass, element)
                        if closest:
                            print(f"\nБлижайший элемент по атомной массе ({target_mass:.4f} u):")
                            print(f"{closest.name} ({closest.symbol}), атомная масса: {closest.mass:.4f} u")
                        else:
                            print("Не удалось найти ближайший элемент.")
                    except ValueError:
                        print("Некорректный ввод атомной массы.")
                elif action == '2':
                    explore_valence(element)
                elif action == '3':
                    break
                else:
                    print("Некорректный ввод. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main()


"""
Дополнительные возможности:
- Функция find_closest_by_mass: находит элемент с атомной массой, наиболее близкой к заданной.
- Функция explore_valence: отображает (если доступно) информацию о валентности элемента.
- Интерактивное меню: позволяет пользователю выбирать действия после ввода элемента.
"""

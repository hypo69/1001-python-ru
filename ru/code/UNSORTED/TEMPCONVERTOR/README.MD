
# Калькулятор температуры на Python

Этот проект содержит два варианта реализации калькулятора температуры, который может конвертировать значения между градусами Цельсия, Фаренгейта и Кельвина.

## Файлы проекта

1.  **`convertor_kcf.py`**: Реализация калькулятора температуры с использованием отдельных функций.
2.  **`convertor_kcf_dataclass.py`**: Реализация калькулятора температуры с использованием `dataclass`.
3.  **`readme.md`**: Этот файл с описанием проекта.

## Описание `convertor_kcf.py`

Этот файл содержит реализацию калькулятора температуры с использованием отдельных функций. Код разделен на несколько блоков:

### 1. Функции конвертации

В этом блоке определены основные функции для конвертации температуры между различными единицами измерения:

```python
def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Конвертирует температуру из градусов Цельсия в градусы Фаренгейта.

    Args:
        celsius: Температура в градусах Цельсия.

    Returns:
        Температура в градусах Фаренгейта.
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Конвертирует температуру из градусов Фаренгейта в градусы Цельсия.

    Args:
        fahrenheit: Температура в градусах Фаренгейта.

    Returns:
        Температура в градусах Цельсия.
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def celsius_to_kelvin(celsius: float) -> float:
    """
    Конвертирует температуру из градусов Цельсия в Кельвины.

    Args:
        celsius: Температура в градусах Цельсия.

    Returns:
        Температура в Кельвинах.
    """
    kelvin = celsius + 273.15
    return kelvin


def kelvin_to_celsius(kelvin: float) -> float:
    """
    Конвертирует температуру из Кельвинов в градусы Цельсия.

    Args:
        kelvin: Температура в Кельвинах.

    Returns:
        Температура в градусах Цельсия.
    """
    celsius = kelvin - 273.15
    return celsius


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """
    Конвертирует температуру из градусов Фаренгейта в Кельвины.

    Args:
        fahrenheit: Температура в градусах Фаренгейта.

    Returns:
        Температура в Кельвинах.
    """
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)
    return kelvin


def kelvin_to_fahrenheit(kelvin: float) -> float:
    """
    Конвертирует температуру из Кельвинов в градусы Фаренгейта.

    Args:
        kelvin: Температура в Кельвинах.

    Returns:
        Температура в градусах Фаренгейта.
    """
    celsius = kelvin_to_celsius(kelvin)
    fahrenheit = celsius_to_fahrenheit(celsius)
    return fahrenheit
```

Каждая функция имеет:

-   **Аннотацию типов:** `(celsius: float) -> float` указывает на тип аргумента и возвращаемого значения.
-   **Docstring:** Строка документации описывает назначение функции, аргументы и возвращаемое значение.
-   **Логика:** Функция выполняет конвертацию согласно известным формулам.

### 2. Универсальная функция конвертации

```python
def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """
    Конвертирует температуру из одной единицы измерения в другую.

    Args:
        value: Температура для конвертации.
        from_unit: Исходная единица измерения ('C', 'F', 'K').
        to_unit: Целевая единица измерения ('C', 'F', 'K').

    Returns:
        Конвертированная температура.

    Raises:
        ValueError: Если указаны некорректные единицы измерения.
    """
    if from_unit == to_unit:
        return value  # нет необходимости в конвертации

    if from_unit == 'C':
        if to_unit == 'F':
            return celsius_to_fahrenheit(value)
        elif to_unit == 'K':
            return celsius_to_kelvin(value)
    elif from_unit == 'F':
        if to_unit == 'C':
            return fahrenheit_to_celsius(value)
        elif to_unit == 'K':
            return fahrenheit_to_kelvin(value)
    elif from_unit == 'K':
        if to_unit == 'C':
            return kelvin_to_celsius(value)
        elif to_unit == 'F':
            return kelvin_to_fahrenheit(value)

    raise ValueError("Некорректные единицы измерения.")
```

Эта функция принимает значение температуры, исходную единицу измерения и целевую единицу измерения. На основе этих параметров она вызывает соответствующую функцию конвертации. Если единицы измерения одинаковы, она возвращает исходное значение. Если переданы некорректные единицы измерения, она вызывает `ValueError`.

### 3. Функция `main`

```python
def main():
    """
    Главная функция для взаимодействия с пользователем.
    """
    while True:
        print("\nВыберите действие:")
        print("1. Конвертировать температуру")
        print("2. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            try:
                value = float(input("Введите температуру: "))
                from_unit = input("Введите исходную единицу измерения (C, F, K): ").upper()
                to_unit = input("Введите целевую единицу измерения (C, F, K): ").upper()

                result = convert_temperature(value, from_unit, to_unit)
                print(f"Результат: {result:.2f} {to_unit}")

            except ValueError as e:
                print(f"Ошибка: {e}")
            except Exception as e:
                 print(f"Непредвиденная ошибка: {e}")

        elif choice == '2':
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
```

Функция `main` содержит бесконечный цикл, в котором пользователю предлагается выбрать действие. Если пользователь выбирает конвертацию, программа запрашивает значение температуры, исходную и целевую единицы измерения, вызывает функцию `convert_temperature` и выводит результат. Также, мы обрабатываем возможные ошибки ввода с помощью `try-except` блока.

## Описание `convertor_kcf_dataclass.py`

Этот файл содержит реализацию калькулятора температуры с использованием `dataclass`.

### 1. `dataclass` `TemperatureConverter`

```python
from dataclasses import dataclass

@dataclass
class TemperatureConverter:
    """
    Класс для конвертации температур между градусами Цельсия, Фаренгейта и Кельвина.
    """

    def celsius_to_fahrenheit(self, celsius: float) -> float:
        ... # Определение методов конвертации
```

-   **Импорт `dataclass`:** Мы импортируем декоратор `dataclass` из модуля `dataclasses`.
-   **Класс `TemperatureConverter`:** Мы создаем класс `TemperatureConverter` и декорируем его с помощью `@dataclass`. Это автоматически создаст конструктор и другие необходимые методы для класса.
-   **Методы класса:** Все наши функции конвертации теперь являются методами класса `TemperatureConverter`. Первый параметр `self` указывает на экземпляр класса.

Методы конвертации аналогичны методам в `convertor_kcf.py`, за исключением того, что они являются методами класса и принимают `self` в качестве первого аргумента.

### 2. Функция `convert_temperature`

```python
    def convert_temperature(self, value: float, from_unit: str, to_unit: str) -> float:
        ... # Вызов методов класса
```

Эта функция, также как и в `convertor_kcf.py`, принимает значение температуры, исходную единицу измерения и целевую единицу измерения. Но теперь она вызывает методы класса `TemperatureConverter`.

### 3. Функция `main`

```python
def main():
    """
    Главная функция для взаимодействия с пользователем.
    """
    converter = TemperatureConverter()

    while True:
       ... # Взаимодействие с пользователем
            result = converter.convert_temperature(value, from_unit, to_unit)
        ...
```

В функции `main` мы создаем экземпляр класса `TemperatureConverter` с именем `converter`. Теперь мы вызываем методы конвертации через этот экземпляр, например: `converter.convert_temperature()`.

## Сравнение двух подходов

-   **`convertor_kcf.py`:** Функции конвертации существуют независимо друг от друга, что может быть менее организованным для более сложных программ.
-   **`convertor_kcf_dataclass.py`:** Все функции конвертации сгруппированы в классе, что делает код более модульным и читаемым. `dataclass` также обеспечивает автоматическое создание конструктора и других методов.

## Запуск кода

Чтобы запустить любой из файлов, убедись, что у тебя установлен Python. Затем выполни в терминале:

```bash
python convertor_kcf.py
```

или

```bash
python convertor_kcf_dataclass.py
```

Оба подхода решают одну и ту же задачу, но с использованием разных способов организации кода. 
`dataclass` позволяет более структурировано подойти к решению задачи и упрощает сопровождение и расширение кода.
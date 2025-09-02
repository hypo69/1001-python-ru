from dataclasses import dataclass


@dataclass
class TemperatureConverter:
    """
    Класс для конвертации температур между градусами Цельсия, Фаренгейта и Кельвина.
    """

    def celsius_to_fahrenheit(self, celsius: float) -> float:
        """
        Конвертирует температуру из градусов Цельсия в градусы Фаренгейта.

        Args:
            celsius: Температура в градусах Цельсия.

        Returns:
            Температура в градусах Фаренгейта.
        """
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

    def fahrenheit_to_celsius(self, fahrenheit: float) -> float:
        """
        Конвертирует температуру из градусов Фаренгейта в градусы Цельсия.

        Args:
            fahrenheit: Температура в градусах Фаренгейта.

        Returns:
            Температура в градусах Цельсия.
        """
        celsius = (fahrenheit - 32) * 5/9
        return celsius

    def celsius_to_kelvin(self, celsius: float) -> float:
        """
        Конвертирует температуру из градусов Цельсия в Кельвины.

        Args:
            celsius: Температура в градусах Цельсия.

        Returns:
            Температура в Кельвинах.
        """
        kelvin = celsius + 273.15
        return kelvin

    def kelvin_to_celsius(self, kelvin: float) -> float:
        """
        Конвертирует температуру из Кельвинов в градусы Цельсия.

        Args:
            kelvin: Температура в Кельвинах.

        Returns:
            Температура в градусах Цельсия.
        """
        celsius = kelvin - 273.15
        return celsius

    def fahrenheit_to_kelvin(self, fahrenheit: float) -> float:
        """
        Конвертирует температуру из градусов Фаренгейта в Кельвины.

        Args:
            fahrenheit: Температура в градусах Фаренгейта.

        Returns:
            Температура в Кельвинах.
        """
        celsius = self.fahrenheit_to_celsius(fahrenheit)
        kelvin = self.celsius_to_kelvin(celsius)
        return kelvin

    def kelvin_to_fahrenheit(self, kelvin: float) -> float:
        """
        Конвертирует температуру из Кельвинов в градусы Фаренгейта.

        Args:
            kelvin: Температура в Кельвинах.

        Returns:
            Температура в градусах Фаренгейта.
        """
        celsius = self.kelvin_to_celsius(kelvin)
        fahrenheit = self.celsius_to_fahrenheit(celsius)
        return fahrenheit

    def convert_temperature(self, value: float, from_unit: str, to_unit: str) -> float:
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
                return self.celsius_to_fahrenheit(value)
            elif to_unit == 'K':
                return self.celsius_to_kelvin(value)
        elif from_unit == 'F':
            if to_unit == 'C':
                return self.fahrenheit_to_celsius(value)
            elif to_unit == 'K':
                return self.fahrenheit_to_kelvin(value)
        elif from_unit == 'K':
            if to_unit == 'C':
                return self.kelvin_to_celsius(value)
            elif to_unit == 'F':
                return self.kelvin_to_fahrenheit(value)

        raise ValueError("Некорректные единицы измерения.")


def main():
    """
    Главная функция для взаимодействия с пользователем.
    """
    converter = TemperatureConverter()

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

                result = converter.convert_temperature(value, from_unit, to_unit)
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
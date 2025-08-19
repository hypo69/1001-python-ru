import random
import string
from typing import List, Optional

class FakeDataGenerator:
    """
    генерации фейковых данных.

    Реализует основные функции, такие как генерация имен, адресов, номеров телефонов и других данных.
    """

    first_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'Diana']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia']
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    streets = ['Main St', 'Elm St', '2nd Ave', 'Park Blvd', 'Oak Dr']
    domains = ['example.com', 'mail.com', 'test.org', 'website.net']

    def random_name(self) -> str:
        """
        Генерация случайного полного имени.

        Returns:
            str: Полное имя, состоящее из случайного имени и фамилии.
        """
        first_name = random.choice(self.first_names)
        last_name = random.choice(self.last_names)
        return f'{first_name} {last_name}'

    def random_email(self) -> str:
        """
        Генерация случайного email-адреса.

        Returns:
            str: Email-адрес в формате `имя.фамилия@домен`.
        """
        first_name = random.choice(self.first_names).lower()
        last_name = random.choice(self.last_names).lower()
        domain = random.choice(self.domains)
        return f'{first_name}.{last_name}@{domain}'

    def random_phone(self) -> str:
        """
        Генерация случайного номера телефона в формате `+1-XXX-XXX-XXXX`.

        Returns:
            str: Номер телефона.
        """
        return f'+1-{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}'

    def random_address(self) -> str:
        """
        Генерация случайного адреса.

        Returns:
            str: Адрес в формате `улица, город`.
        """
        street = random.choice(self.streets)
        city = random.choice(self.cities)
        house_number = random.randint(1, 9999)
        return f'{house_number} {street}, {city}'

    def random_string(self, length: int = 10) -> str:
        """
        Генерация случайной строки заданной длины.

        Args:
            length (int, optional): Длина строки. По умолчанию 10.

        Returns:
            str: Случайная строка, содержащая буквы и цифры.
        """
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def random_int(self, min_value: int = 0, max_value: int = 100) -> int:
        """
        Генерация случайного целого числа в заданном диапазоне.

        Args:
            min_value (int, optional): Минимальное значение. По умолчанию 0.
            max_value (int, optional): Максимальное значение. По умолчанию 100.

        Returns:
            int: Случайное целое число.
        """
        return random.randint(min_value, max_value)

    def random_choice(self, options: List[str]) -> str:
        """
        Выбор случайного элемента из списка.

        Args:
            options (List[str]): Список значений для выбора.

        Returns:
            str: Случайный элемент из списка.
        """
        return random.choice(options)

# Пример использования
if __name__ == '__main__':
    faker = FakeDataGenerator()

    print(f'Name: {faker.random_name()}')
    print(f'Email: {faker.random_email()}')
    print(f'Phone: {faker.random_phone()}')
    print(f'Address: {faker.random_address()}')
    print(f'Random String: {faker.random_string(12)}')
    print(f'Random Int: {faker.random_int(50, 150)}')
    print(f'Random Choice: {faker.random_choice(["Option1", "Option2", "Option3"])}')

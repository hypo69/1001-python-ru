Code represents a `FakeDataGenerator` class, designed to generate fake (random) data, such as names, addresses, phone numbers, email addresses, and others. This class can be useful for testing, populating databases, creating demo data, and other tasks where random value generation is required.

---

### **Code operation description**

#### **1. Import libraries**
```python
import random
import string
from typing import List, Optional
```
- **random** – used for generating random numbers, selecting random elements from lists, and other random operations.
- **string** – provides a set of characters (e.g., letters, digits) that can be used to generate strings.
- **typing** – used for type annotations to improve code readability and maintainability.

---

#### **2. `FakeDataGenerator` class**
The class contains a set of methods for generating various types of data.

##### **Class attributes**
```python
first_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'Diana']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
streets = ['Main St', 'Elm St', '2nd Ave', 'Park Blvd', 'Oak Dr']
domains = ['example.com', 'mail.com', 'test.org', 'website.net']
```
- These attributes are lists with predefined values that are used to generate random data.

---

##### **Class methods**

###### **1. `random_name()`**
```python
def random_name(self) -> str:
    """
    Generates a random full name.

    Returns:
        str: Full name, consisting of a random first name and last name.
    """
    first_name = random.choice(self.first_names)
    last_name = random.choice(self.last_names)
    return f'{first_name} {last_name}'
```
- **Description:** Generates a random full name, consisting of a random first name and last name.
- **How it works:**
  - Uses `random.choice()` to select a random first name from the `first_names` list.
  - Uses `random.choice()` to select a random last name from the `last_names` list.
  - Returns a string in the format "First Name Last Name".

---

###### **2. `random_email()`**
```python
def random_email(self) -> str:
    """
    Generates a random email address.

    Returns:
        str: Email address in the format `firstname.lastname@domain`.
    """
    first_name = random.choice(self.first_names).lower()
    last_name = random.choice(self.last_names).lower()
    domain = random.choice(self.domains)
    return f'{first_name}.{last_name}@{domain}'
```
- **Description:** Generates a random email address.
- **How it works:**
  - Uses `random.choice()` to select a random first name and last name.
  - Converts the selected first name and last name to lowercase using `.lower()`.
  - Uses `random.choice()` to select a random domain from the `domains` list.
  - Returns a string in the format "firstname.lastname@domain".

---

###### **3. `random_phone()`**
```python
def random_phone(self) -> str:
    """
    Generates a random phone number in the format `+1-XXX-XXX-XXXX`.

    Returns:
        str: Phone number.
    """
    return f'+1-{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}'
```
- **Description:** Generates a random phone number in the format "+1-XXX-XXX-XXXX".
- **How it works:**
  - Uses `random.randint()` to generate random numbers in the specified ranges.
  - Formats the string according to the specified pattern.

---

###### **4. `random_address()`**
```python
def random_address(self) -> str:
    """
    Generates a random address.

    Returns:
        str: Address in the format `street, city`.
    """
    street = random.choice(self.streets)
    city = random.choice(self.cities)
    house_number = random.randint(1, 9999)
    return f'{house_number} {street}, {city}'
```
- **Description:** Generates a random address.
- **How it works:**
  - Uses `random.choice()` to select a random street and city.
  - Uses `random.randint()` to generate a random house number.
  - Returns a string in the format "house_number street, city".

---

###### **5. `random_string()`**
```python
def random_string(self, length: int = 10) -> str:
    """
    Generates a random string of a given length.

    Args:
        length (int, optional): Length of the string. Defaults to 10.

    Returns:
        str: Random string containing letters and digits.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
```
- **Description:** Generates a random string of a given length, consisting of letters and digits.
- **How it works:**
  - Uses `random.choices()` to select random characters from the `string.ascii_letters + string.digits` string.
  - Joins the selected characters into a string using `''.join()`.

---

###### **6. `random_int()`**
```python
def random_int(self, min_value: int = 0, max_value: int = 100) -> int:
    """
    Generates a random integer within a given range.

    Args:
        min_value (int, optional): Minimum value. Defaults to 0.
        max_value (int, optional): Maximum value. Defaults to 100.

    Returns:
        int: Random integer.
    """
    return random.randint(min_value, max_value)
```
- **Description:** Generates a random integer within a given range.
- **How it works:**
  - Uses `random.randint()` to generate a random number within the specified range.

---

###### **7. `random_choice()`**
```python
def random_choice(self, options: List[str]) -> str:
    """
    Selects a random element from a list.

    Args:
        options (List[str]): List of values to choose from.

    Returns:
        str: Random element from the list.
    """
    return random.choice(options)
```
- **Description:** Selects a random element from the passed list.
- **How it works:**
  - Uses `random.choice()` to select a random element from the `options` list.

---

#### **3. Example usage**
```python
if __name__ == '__main__':
    faker = FakeDataGenerator()

    print(f'Name: {faker.random_name()}')
    print(f'Email: {faker.random_email()}')
    print(f'Phone: {faker.random_phone()}')
    print(f'Address: {faker.random_address()}')
    print(f'Random String: {faker.random_string(12)}')
    print(f'Random Int: {faker.random_int(50, 150)}')
    print(f'Random Choice: {faker.random_choice(["Option1", "Option2", "Option3"])}')
```
- An instance of the `FakeDataGenerator` class is created.
- Class methods are called to generate various types of data.
- Results are printed to the screen.

---

### **Summary**
The `FakeDataGenerator` class provides a convenient interface for generating random data, such as names, email addresses, phone numbers, addresses, and others. This class can be extended to generate additional data types or configured for use in specific projects.
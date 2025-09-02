### Как получить информацию о любой стране с помощью Python и REST API


В основе скрипта лежит всего две вещи:
1.  **Библиотека `requests`**: Стандарт де-факто в Python для отправки HTTP-запросов.
2.  **REST Countries API**: Бесплатный и открытый API, который не требует ключей авторизации и предоставляет массу данных о странах.

#### Шаг 1: Подготовка окружения

Для начала убедитесь, что у вас установлен Python. Затем нам понадобится библиотека `requests`. Если у вас ее еще нет, установите ее с помощью pip:

```bash
pip install requests
```

#### Шаг 2: Базовый скрипт для получения информации

Давайте воссоздадим и разберем код с изображения. Он позволяет найти страну по её полному названию на английском языке.

```python
import requests

# URL API для поиска страны по имени
API_URL = "https://restcountries.com/v3.1/name/"

def get_country_info(country_name):
    """
    Получает и выводит информацию о стране из REST Countries API.
    """
    print(f"\n--- Поиск информации о стране: {country_name} ---")
    try:
        # Формируем полный URL и отправляем GET-запрос
        response = requests.get(f"{API_URL}{country_name}")
        
        # Проверяем, успешен ли был запрос (код 200-299)
        if response.ok:
            # API возвращает список стран, берем первый результат
            data = response.json()[0]
            
            # Извлекаем данные с помощью .get() для безопасного доступа
            # Если ключ отсутствует, будет использовано значение по умолчанию
            name = data.get("name", {}).get("common", "Неизвестно")
            capital = data.get("capital", ["Нет столицы"])[0]
            population = data.get("population", "Нет данных")
            area = data.get("area", "Нет данных")
            region = data.get("region", "Нет данных")
            
            # Валюты хранятся в словаре, нам нужны их коды (ключи)
            currencies_data = data.get("currencies", {})
            currencies = ", ".join(currencies_data.keys()) if currencies_data else "Нет данных"

            # Выводим информацию
            print(f"Общая информация о стране '{name}':")
            print(f"  -> Столица: {capital}")
            print(f"  -> Население: {population} человек")
            print(f"  -> Площадь: {area} км²")
            print(f"  -> Регион: {region}")
            print(f"  -> Валюты: {currencies}")
            
        else:
            # Если страна не найдена (например, ошибка 404)
            print(f"Ошибка: Страна '{country_name}' не найдена. Проверьте правильность ввода (нужно английское название).")
            
    except requests.exceptions.RequestException as e:
        # Обработка ошибок сети (нет интернета и т.д.)
        print(f"Ошибка соединения: {e}")
    except Exception as e:
        # Обработка других возможных ошибок (например, некорректный JSON)
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    print("Программа: Информация о странах")
    while True:
        choice = input("\nМеню:\n1. Получить информацию о стране\n2. Выйти\nВыберите действие (1-2): ").strip()
        
        if choice == "1":
            country_name_input = input("Введите название страны (на английском): ").strip()
            if country_name_input:
                get_country_info(country_name_input)
            else:
                print("Название страны не может быть пустым.")
        elif choice == "2":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
```

**Пример работы:**

```
Меню:
1. Получить информацию о стране
2. Выйти
Выберите действие (1-2): 1
Введите название страны (на английском): Germany

--- Поиск информации о стране: Germany ---
Общая информация о стране 'Germany':
  -> Столица: Berlin
  -> Население: 83240525 человек
  -> Площадь: 357022.0 км²
  -> Регион: Europe
  -> Валюты: EUR
```

---

### Расширяем функционал: Больше возможностей

API `REST Countries` позволяет искать страны не только по названию. Давайте добавим новые функции в наш скрипт!

#### Возможность 1: Поиск стран по валюте

А что, если мы хотим найти все страны, где используется, например, евро (EUR)? Для этого есть специальный эндпоинт `/currency/{code}`.

Добавим новую функцию:

```python
def get_countries_by_currency(currency_code):
    """
    Находит и выводит список стран, использующих указанную валюту.
    """
    print(f"\n--- Поиск стран с валютой: {currency_code.upper()} ---")
    try:
        response = requests.get(f"https://restcountries.com/v3.1/currency/{currency_code}")
        if response.ok:
            countries = response.json()
            print(f"Найдено {len(countries)} стран:")
            # Выводим названия всех найденных стран
            country_names = [country.get("name", {}).get("common", "Неизвестно") for country in countries]
            for name in sorted(country_names):
                print(f"  - {name}")
        else:
            print(f"Ошибка: Страны с валютой '{currency_code}' не найдены или код некорректен.")
            
    except requests.exceptions.RequestException as e:
        print(f"Ошибка соединения: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
```

**Пример работы:**

```
Введите код валюты (например, USD, EUR, JPY): eur

--- Поиск стран с валютой: EUR ---
Найдено 36 стран:
  - Åland Islands
  - Andorra
  - Austria
  - Belgium
  ... и так далее
```

#### Возможность 2: Поиск стран по языку

Аналогично можно найти страны, где говорят на определенном языке. Эндпоинт: `/lang/{language}`.

Новая функция:

```python
def get_countries_by_language(language):
    """
    Находит и выводит список стран, где говорят на указанном языке.
    """
    print(f"\n--- Поиск стран с языком: {language.capitalize()} ---")
    try:
        response = requests.get(f"https://restcountries.com/v3.1/lang/{language}")
        if response.ok:
            countries = response.json()
            print(f"Найдено {len(countries)} стран, где говорят на языке '{language}':")
            country_names = [country.get("name", {}).get("common", "Неизвестно") for country in countries]
            for name in sorted(country_names):
                print(f"  - {name}")
        else:
            print(f"Ошибка: Страны с языком '{language}' не найдены.")
            
    except requests.exceptions.RequestException as e:
        print(f"Ошибка соединения: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
```

**Пример работы:**

```
Введите язык (на английском, например, Spanish, Arabic): portuguese

--- Поиск стран с языком: Portuguese ---
Найдено 9 стран, где говорят на языке 'portuguese':
  - Angola
  - Brazil
  - Cape Verde
  - Equatorial Guinea
  - Guinea-Bissau
  - Mozambique
  - Portugal
  - São Tomé and Príncipe
  - Timor-Leste
```

### Итоговый скрипт со всеми возможностями

Теперь объединим все наши функции в один скрипт с расширенным меню.

```python
import requests

# --- Функции для работы с API ---

def get_country_info(country_name):
    # ... (код функции из Шага 2) ...

def get_countries_by_currency(currency_code):
    # ... (код функции из Возможности 1) ...

def get_countries_by_language(language):
    # ... (код функции из Возможности 2) ...

# --- Основной блок с меню ---

if __name__ == "__main__":
    print("Программа: Информация о странах с использованием REST Countries API")
    while True:
        print("\n" + "="*40)
        print("Меню:")
        print("1. Найти страну по названию")
        print("2. Найти страны по коду валюты")
        print("3. Найти страны по языку")
        print("4. Выйти")
        print("="*40)
        
        choice = input("Выберите действие (1-4): ").strip()
        
        if choice == "1":
            country_name_input = input("Введите полное название страны (на английском): ").strip()
            if country_name_input:
                get_country_info(country_name_input)
            else:
                print("Название страны не может быть пустым.")
        
        elif choice == "2":
            currency_input = input("Введите код валюты (например, USD, EUR): ").strip()
            if currency_input:
                get_countries_by_currency(currency_input)
            else:
                print("Код валюты не может быть пустым.")

        elif choice == "3":
            language_input = input("Введите язык (на английском, например, Spanish): ").strip()
            if language_input:
                get_countries_by_language(language_input)
            else:
                print("Название языка не может быть пустым.")
                
        elif choice == "4":
            print("Выход из программы. Успешного кодирования!")
            break
            
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 4.")

```
*Примечание: для краткости я не стал дублировать код уже написанных функций в последнем блоке.*

### Заключение

Мы создали полезный консольный инструмент, который демонстрирует всю мощь и простоту работы с REST API в Python. Вы можете дальше развивать этот скрипт:
*   Добавить поиск по региону (`/region/{name}`) или столице (`/capital/{name}`).
*   Сохранять результаты в файл (CSV или JSON).
*   Интегрировать его с веб-фреймворком (Flask, Django) или создать телеграм-бота.

REST Countries API — отличная "песочница" для оттачивания навыков работы с внешними сервисами. Экспериментируйте и создавайте свои проекты
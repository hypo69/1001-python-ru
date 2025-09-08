import requests
import random
import re

def get_weather_from_wttr(city):
    """Получает прогноз погоды для города с wttr.in."""
    url = f"https://wttr.in/{city}?format=%t+%C"  # %t - температура, %C - описание
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Вызовет исключение для статусов 4xx/5xx
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении погоды для {city}: {e}")
        return "Недоступно"

def parse_weather_string(weather_str):
    """Парсит строку погоды и извлекает температуру и описание."""
    match = re.search(r'([+-]?\d+)[°C]?\s*(.*)', weather_str)
    if match:
        temp = int(match.group(1))
        description = match.group(2).strip()
        return temp, description
    return None, None

def play_weather_mystery_game():
    """Основная функция игры 'Тайна Погоды'."""
    print("Добро пожаловать в игру 'Тайна Погоды'!")
    print("Я покажу тебе код, который получает прогноз погоды:")
    print("```python")
    print("import requests")
    print("city = input('Введите название города: ')")
    print("url = f'https://wttr.in/{city}'")
    print("try:")
    print("    response = requests.get(url)")
    print("    print(response.text)")
    print("except Exception:")
    print("    print('Упс! Что-то пошло не так. Попробуйте позже.')")
    print("```")
    print("\nТвоя задача - угадать погоду в разных городах.")

    cities = ["Москва", "Лондон", "Нью-Йорк", "Токио", "Сидней", "Париж", "Рио-де-Жанейро", "Каир", "Пекин", "Берлин"]
    score = 0
    num_rounds = 3

    for round_num in range(num_rounds):
        print(f"\n--- Раунд {round_num + 1}/{num_rounds} ---")
        current_city = random.choice(cities)
        print(f"Предскажи погоду в городе: {current_city}")

        try:
            player_temp_guess = int(input("Как ты думаешь, какая температура (в °C)? "))
            player_desc_guess = input("Какое состояние погоды (например, 'ясно', 'облачно', 'дождь')? ").lower()
        except ValueError:
            print("Некорректный ввод температуры. Пожалуйста, введите целое число.")
            continue

        print(f"\nПолучаем реальный прогноз для {current_city}...")
        actual_weather_str = get_weather_from_wttr(current_city)
        actual_temp, actual_desc = parse_weather_string(actual_weather_str)
        
        if actual_temp is None:
            print(f"Не удалось получить точный прогноз для {current_city}. Пропускаем раунд.")
            continue

        print(f"Реальный прогноз: {actual_temp}°C, {actual_desc}")

        # Оценка предсказания
        temp_diff = abs(player_temp_guess - actual_temp)
        desc_match = player_desc_guess in actual_desc.lower()

        if temp_diff <= 3 and desc_match:
            print("Отлично! Ты угадал температуру с небольшой погрешностью и верно описал погоду!")
            score += 2
        elif temp_diff <= 5:
            print("Хорошо! Ты был близок к правильной температуре.")
            score += 1
        elif desc_match:
            print("Неплохо! Ты угадал состояние погоды, но температура не очень точна.")
            score += 1
        else:
            print("К сожалению, твоё предсказание не совсем точное.")

    print("\n--- Игра окончена! ---")
    print(f"Твой итоговый счёт: {score} из {num_rounds * 2} возможных баллов.")
    print("Спасибо за игру!")


if __name__ == "__main__":
    play_weather_mystery_game()
import numpy as np
import pandas as pd
from collections import Counter
from random import randint as rnd
import google.generativeai as genai
from typing import List, Dict, Tuple
import os
import random

# Проверяем наличие API ключа Gemini
if 'GOOGLE_API_KEY' not in os.environ:
    raise EnvironmentError("Не найден API ключ Gemini. Пожалуйста, установите переменную окружения GOOGLE_API_KEY.")
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')


def generate_random_dream_numbers(num_dreams: int, max_square: int = 48) -> List[int]:
    """Генерирует список случайных уникальных номеров "мечт"."""
    if num_dreams > max_square:
        raise ValueError("Количество мечт не может быть больше количества ячеек на поле.")
    return random.sample(range(1, max_square + 1), num_dreams)


class DreamGame:
    """
    Класс, моделирующий игру по сбору "мечт" на игровом поле.
    """

    def __init__(self, num_dreams: int, moves: int = 3, num_iterations: int = 100_000, max_square: int = 48):
        """
        Инициализирует игру.

        Args:
            num_dreams: Количество "мечт", которые нужно сгенерировать.
            moves: Количество бросков кубиков за одну игру.
            num_iterations: Количество симуляций игры.
            max_square: Максимальный номер ячейки
        """
        if num_dreams > max_square:
           raise ValueError(f"Количество мечт ({num_dreams}) не может быть больше количества ячеек на поле ({max_square}).")
        self.dream_numbers = generate_random_dream_numbers(num_dreams, max_square) # генерируем случайные номера мечт
        self.moves = moves
        self.num_iterations = num_iterations
        self.dreams: Dict[int, str] = {}
        self._generate_dream_names()  # Генерируем названия "мечт" при инициализации
    
    def _generate_dream_names(self) -> None:
        """
        Генерирует названия "мечт" с помощью модели Gemini.
        """
        prompt = f"Придумай {len(self.dream_numbers)} уникальных коротких (не более 5 слов) и интересных названий для \"мечт\", связанных с путешествиями, приключениями, развлечениями. Выдай ответ списком, где каждое название на новой строке."
        response = model.generate_content(prompt)
        
        if response.text:
            dream_names = response.text.strip().split('\n')
        else:
             raise ValueError("Модель Gemini не вернула никакого текста.")

        if len(dream_names) != len(self.dream_numbers):
            raise ValueError(f"Количество сгенерированных названий ({len(dream_names)}) не совпадает с количеством номеров мечт ({len(self.dream_numbers)}).")

        self.dreams = {number: f"{number}_{name}" for number, name in zip(self.dream_numbers, dream_names)}
        
    def _simulate_game(self) -> Counter[str]:
         """
         Симулирует одну игру и возвращает частоту посещения "мечт".

         Returns:
             Counter: Счетчик частот посещения "мечт".
         """
         dreams_frequency = Counter()
         square = 0
         visited_dreams = set()

         for _ in range(self.moves):
            square += rnd(1, 6) + rnd(1, 6)
            square = square % 48 if square > 48 else square

            if square in self.dream_numbers and square not in visited_dreams:
                dreams_frequency[self.dreams[square]] += 1
                visited_dreams.add(square) # Посещенная мечта добавляется в набор

         return dreams_frequency

    def run_experiment(self) -> pd.DataFrame:
        """
        Запускает симуляцию игры несколько раз и возвращает DataFrame с результатами.

        Returns:
            pandas.DataFrame: DataFrame с частотой и вероятностью посещения каждой "мечты".
        """
        dreams_frequency = sum( (self._simulate_game() for _ in range(self.num_iterations)), Counter()) # Складываем Counter() из генераторов
        df = pd.DataFrame(dreams_frequency.items(), columns=['Мечта', 'Частота']).sort_values('Частота', ascending=False)
        df['Вероятность'] = df['Частота'] / self.num_iterations
        return df

def run_simulation_with_intervals(moves: int, num_iterations: int) -> None:
    """
    Запускает симуляцию игры с разными интервалами количества мечт.

    Args:
        moves: Количество бросков кубиков за одну игру.
        num_iterations: Количество симуляций игры.
    """

    # 1. Случайное количество "мечт" в диапазоне (10 - 20)
    num_dreams_normal = random.randint(10, 20)
    game_normal = DreamGame(num_dreams=num_dreams_normal, moves=moves, num_iterations=num_iterations)
    df_normal = game_normal.run_experiment()
    print(f"Результаты с {num_dreams_normal} мечтами (диапазон 10-20):\n{df_normal}\n")

    # 2. Случайное количество "мечт" с плотностью чуть меньше (5 - 15)
    num_dreams_less = random.randint(5, 15)
    game_less = DreamGame(num_dreams=num_dreams_less, moves=moves, num_iterations=num_iterations)
    df_less = game_less.run_experiment()
    print(f"Результаты с {num_dreams_less} мечтами (диапазон 5-15):\n{df_less}\n")

    # 3. Случайное количество "мечт" с плотностью чуть больше (15 - 25)
    num_dreams_more = random.randint(15, 25)
    game_more = DreamGame(num_dreams=num_dreams_more, moves=moves, num_iterations=num_iterations)
    df_more = game_more.run_experiment()
    print(f"Результаты с {num_dreams_more} мечтами (диапазон 15-25):\n{df_more}\n")

if __name__ == '__main__':
    moves = 3  # Количество ходов за игру
    num_iterations = 10_000  # Количество симуляций
    run_simulation_with_intervals(moves, num_iterations)
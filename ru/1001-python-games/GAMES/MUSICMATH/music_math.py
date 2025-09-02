# @title Модуль MusicMath: примеры связи математики и музыки.

"""
Модуль MusicMath: примеры связи математики и музыки.
"""
import math
from fractions import Fraction
import re

def calculate_frequency(note_number, concert_a_freq=440.0):
    """
    Вычисляет частоту ноты, зная её номер в хроматической гамме.
    
    Args:
        note_number (int): Номер ноты относительно A4 (A4 = 0).
        concert_a_freq (float, optional): Частота ноты A4. Defaults to 440.0.
    
    Returns:
        float: Частота ноты в герцах.
    """
    return concert_a_freq * math.pow(2, note_number / 12)

def calculate_interval_ratio(note1_number, note2_number):
    """
    Вычисляет отношение частот между двумя нотами, зная их номера.
    
    Args:
        note1_number (int): Номер первой ноты.
        note2_number (int): Номер второй ноты.
    
    Returns:
         str: Отношение частот в виде простой дроби.
    """
    freq1 = calculate_frequency(note1_number)
    freq2 = calculate_frequency(note2_number)
    ratio = freq2/freq1 if freq2>freq1 else freq1/freq2
    fraction_ratio = Fraction(ratio).limit_denominator(100)  # Limit to reasonable denominators
    return str(fraction_ratio)

def calculate_tempo_duration(bpm, beat_length, beats):
     """
    Вычисляет общую продолжительность в секундах музыкального фрагмента.

    Args:
         bpm (int): Темп в ударах в минуту.
         beat_length(float): Продолжительность одного удара в секундах.
         beats (int): Количество ударов в музыкальном фрагменте.

    Returns:
        float: Общая продолжительность фрагмента в секундах.
    """
     return beat_length*beats

def calculate_note_duration(tempo, note_value):
    """
    Вычисляет длительность ноты в секундах.
    
    Args:
        tempo (int): Темп в ударах в минуту.
        note_value (float): Длительность ноты относительно целой ноты (1.0 = целая, 0.5 = половинная, 0.25 = четвертная и т.д.).

    Returns:
        float: Длительность ноты в секундах.
    """
    beat_duration = 60 / tempo
    return beat_duration * note_value

def calculate_rhythm_pattern(bar_length, note_values):
    """
    Рассчитывает общую продолжительность ритмического паттерна в секундах.
    
    Args:
         bar_length (float): Длительность такта в количестве целых нот.
         note_values (list): Список длительностей нот (относительно целой ноты)
    
    Returns:
         float: Общая длительность ритмического паттерна в секундах.
    """
    pattern_duration = 0
    for value in note_values:
       pattern_duration += bar_length * value
    return pattern_duration

def calculate_note_number(frequency, concert_a_freq=440.0):
    """
    Вычисляет номер ноты в хроматической гамме на основе частоты.
    
    Args:
        frequency (float): Частота ноты в герцах.
        concert_a_freq (float, optional): Частота ноты A4. Defaults to 440.0.
    
    Returns:
        int: Номер ноты относительно A4 (A4 = 0).
    """
    return round(12 * math.log2(frequency / concert_a_freq))

def generate_scale_frequencies(root_note_number, scale_pattern, concert_a_freq=440.0):
    """
    Генерирует частоты нот заданной гаммы.
    
    Args:
        root_note_number (int): Номер корневой ноты.
        scale_pattern (list): Шаблон гаммы (последовательность полутонов).
        concert_a_freq (float, optional): Частота ноты A4. Defaults to 440.0.
    
    Returns:
        list: Список частот нот в гамме.
    """
    frequencies = []
    current_note = root_note_number
    for interval in scale_pattern:
        frequencies.append(calculate_frequency(current_note, concert_a_freq))
        current_note += interval
    return frequencies

def calculate_tuning_deviation(target_frequency, actual_frequency):
    """
    Вычисляет отклонение частоты от целевой в процентах.
    
    Args:
        target_frequency (float): Целевая частота.
        actual_frequency (float): Фактическая частота.

    Returns:
        float: Процент отклонения.
    """
    return ((actual_frequency - target_frequency) / target_frequency) * 100

def get_note_name(note_number):
    """
    Возвращает название ноты по её номеру в хроматической гамме.

    Args:
        note_number (int): Номер ноты относительно A4 (A4 = 0).

    Returns:
        str: Название ноты (например, "A4", "C#5", "Bb3").
    """
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    octave = (note_number // 12) + 4  # A4 является 0, поэтому добавляем 4
    note_index = note_number % 12
    return f"{notes[note_index]}{octave}"

def get_note_info_from_freq(freq):
    """
    Выводит информацию о ноте по её частоте.

    Args:
        freq (float): Частота ноты в герцах.
    """
    note_num = calculate_note_number(freq)
    note_name = get_note_name(note_num)
    print(f"Частота {freq:.2f} Hz, соответствует ноте {note_name}, номер {note_num}")


def tune_instrument(target_freq, actual_freq):
    """
    Выводит информацию о том, насколько инструмент отклоняется от целевой частоты.

    Args:
        target_freq (float): Целевая частота.
        actual_freq (float): Фактическая частота.
    """
    dev = calculate_tuning_deviation(target_freq, actual_freq)
    if dev > 0:
        print(f"Завышение на {dev:.2f}%. Нужно понизить")
    elif dev < 0:
        print(f"Занижение на {abs(dev):.2f}%. Нужно повысить")
    else:
        print("Идеально настроено!")

def note_name_to_number(note_name):
    """
    Преобразует название ноты (например, "A4") в её номер относительно A4 (A4 = 0).

    Args:
        note_name (str): Название ноты (например, "A4", "C#5", "Bb3").

    Returns:
        int: Номер ноты относительно A4 (A4 = 0), или None, если ввод некорректен.
    """
    notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    match = re.match(r"([A-Ga-g]#?)(-?\d+)", note_name)
    if not match:
        return None
    note = match.group(1).upper()
    octave = int(match.group(2))
    
    try:
        note_index = notes.index(note)
    except ValueError:
        return None
    
    return (octave - 4) * 12 + note_index

def find_nearest_notes(frequency, concert_a_freq=440.0):
    """
    Находит две ближайшие ноты (сверху и снизу) к заданной частоте.

    Args:
        frequency (float): Частота ноты в герцах.
        concert_a_freq (float, optional): Частота ноты A4. Defaults to 440.0.

    Returns:
      tuple: кортеж (имя нижней ноты, имя верхней ноты).
    """
    note_number = 12 * math.log2(frequency / concert_a_freq)
    lower_note_num = math.floor(note_number)
    upper_note_num = math.ceil(note_number)

    lower_note_name = get_note_name(lower_note_num)
    upper_note_name = get_note_name(upper_note_num)
    return lower_note_name, upper_note_name
def print_musical_examples():
    """
    Выводит примеры использования функций.
    """
    print("---------------------------------------------------------")
    print("Примеры вычисления частот нот:")
    print(f"Частота ноты A4: {calculate_frequency(0):.2f} Hz")
    print(f"Частота ноты C5: {calculate_frequency(3):.2f} Hz")  # C5 на 3 полутона выше A4
    print(f"Частота ноты A3: {calculate_frequency(-12):.2f} Hz") # A3 на 12 полутона ниже A4
    print("---------------------------------------------------------")
    print("Примеры вычисления интервалов:")
    print(f"Отношение частот между A4 и C5: {calculate_interval_ratio(0, 3)}")
    print(f"Отношение частот между A4 и A5: {calculate_interval_ratio(0, 12)}")
    print(f"Отношение частот между C4 и G4: {calculate_interval_ratio(-9, -2)}")
    print("---------------------------------------------------------")
    print("Примеры расчета длительности нот:")
    print(f"Длительность четвертной ноты при темпе 120 BPM: {calculate_note_duration(120, 0.25):.3f} сек.")
    print(f"Длительность половинной ноты при темпе 60 BPM: {calculate_note_duration(60, 0.5):.3f} сек.")
    print(f"Длительность целой ноты при темпе 100 BPM: {calculate_note_duration(100, 1):.3f} сек.")
    print("---------------------------------------------------------")
    print("Пример расчета общей длительности музыкального фрагмента:")
    print(f"Длительность 4х тактов по 4/4 при 120BPM: {calculate_tempo_duration(120, 0.5, 16):.3f} сек")
    print("---------------------------------------------------------")
    print("Пример расчета продолжительности ритмического паттерна:")
    print(f"Длительность ритма 4/4 с нотами [0.25, 0.25, 0.5]: {calculate_rhythm_pattern(1, [0.25, 0.25, 0.5]):.2f} целых нот")
    print(f"Длительность ритма 2/4 с нотами [0.125, 0.125, 0.25]: {calculate_rhythm_pattern(0.5, [0.125, 0.125, 0.25]):.2f} целых нот")
    print("---------------------------------------------------------")

    print("---------------------------------------------------------")
    print("Пример определения номера ноты по частоте:")
    freq_example = 440.0
    note_number_example = calculate_note_number(freq_example)
    print(f"Номер ноты для частоты {freq_example:.2f} Hz: {note_number_example} (A4=0)")
    freq_example = 261.63
    note_number_example = calculate_note_number(freq_example)
    print(f"Номер ноты для частоты {freq_example:.2f} Hz: {note_number_example} (C4=-9)")
    print("---------------------------------------------------------")

    print("---------------------------------------------------------")
    print("Пример генерации частот гаммы:")
    major_scale = [2, 2, 1, 2, 2, 2, 1]  # Шаблон мажорной гаммы
    c_major_freqs = generate_scale_frequencies(-9, major_scale) # C4 = -9
    print("Частоты нот мажорной гаммы от C4 (C, D, E, F, G, A, B):")
    for freq in c_major_freqs:
        print(f"{freq:.2f} Hz", end=", ")
    print("\n---------------------------------------------------------")

    print("---------------------------------------------------------")
    print("Пример расчета отклонения от целевой частоты:")
    target_freq = 440.0
    actual_freq = 442.0
    deviation = calculate_tuning_deviation(target_freq, actual_freq)
    print(f"Отклонение {actual_freq:.2f} Hz от {target_freq:.2f} Hz: {deviation:.2f}%")
    target_freq = 261.63
    actual_freq = 260
    deviation = calculate_tuning_deviation(target_freq, actual_freq)
    print(f"Отклонение {actual_freq:.2f} Hz от {target_freq:.2f} Hz: {deviation:.2f}%")
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("Пример определения информации о ноте:")
    get_note_info_from_freq(440.0)
    get_note_info_from_freq(329.63)
    print("---------------------------------------------------------")
    print("Пример использования тюнера:")
    tune_instrument(440.0,438.0)
    tune_instrument(261.63, 262.0)
    tune_instrument(440.0, 440.0)
    print("---------------------------------------------------------")

if __name__ == "__main__":
    print_musical_examples()

    # Примеры с вводом пользователя (вне print_musical_examples):
    print("\n--- Примеры с вводом пользователя ---")

    
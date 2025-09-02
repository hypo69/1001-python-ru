Как подключить и использовать модель Melody RNN от Magenta, основываясь на Python и TensorFlow.

Версия питон 3.7

**1. Установка Magenta:**

Первым делом вам нужно установить библиотеку Magenta. Рекомендуемый способ установки - через pip.

*   **Создайте виртуальное окружение (рекомендуется):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```
*   **Установите Magenta:**
    ```bash
    pip install magenta
    ```
    *   **Примечание:** Magenta может потребовать TensorFlow. Если у вас его нет, pip установит его автоматически.
    *   **Для GPU ускорения:** Если у вас есть NVIDIA GPU и CUDA, вы можете установить версию TensorFlow с поддержкой GPU (смотрите документацию TensorFlow).

**2. Импорт необходимых модулей:**

После установки Magenta, импортируйте необходимые модули в ваш Python скрипт:
```python
import os
import magenta.music as mm
from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.common import sequence_example_lib
```

**3. Загрузка обученной модели:**

Модели Melody RNN обучены на больших наборах данных и доступны для загрузки. Вы можете выбрать одну из предобученных моделей (например, `attention_rnn` или `basic_rnn`).

*   **Инициализация модели:**
    ```python
    model_name = 'attention_rnn'  # Или 'basic_rnn'
    melody_rnn = melody_rnn_sequence_generator.MelodyRnnSequenceGenerator(
        model_name=model_name
    )
    ```
    *   При инициализации модель автоматически загрузит необходимые веса.

**4. Генерация мелодии:**

Теперь вы можете генерировать мелодию. Для этого используйте метод `generate()`:
```python
# Параметры генерации
temperature = 1.0  # Управляет случайностью, 1.0 - нормальное значение
num_steps = 128   # Количество шагов (длина) мелодии
primer_sequence = None #  Вы можете задать мелодию затравку, оставив None, модель начнёт с нуля.
# Создание мелодии
melody_sequence = melody_rnn.generate(
    temperature=temperature,
    steps=num_steps,
    primer_sequence=primer_sequence
)
```
*   `temperature`: Чем выше значение, тем более случайной и "креативной" будет генерация, но она также может стать менее связной.
*   `steps`: Задает количество шагов в сгенерированной мелодии.
*  `primer_sequence`: Задаёт мелодию, от которой модель отталкивается при генерации. Если `None`, модель начнет с нуля.

**5. Работа с MIDI:**

Сгенерированная мелодия представлена в виде `Sequence` объекта, который можно сохранить в MIDI-файл или использовать для дальнейшей обработки:
```python
# Сохранение в MIDI
output_dir = 'generated_music'
os.makedirs(output_dir, exist_ok=True)
midi_file = os.path.join(output_dir, 'generated_melody.mid')
mm.sequence_proto_to_midi_file(melody_sequence, midi_file)

print(f"Melody saved to: {midi_file}")
```

**6. Добавление аккордов и ударных (как в примере):**

Вы можете комбинировать сгенерированную мелодию с аккордовыми прогрессиями и партиями ударных, как это было показано в вашем примере кода:
```python
# Аккорды
chords = ["C", "G", "Am", "F"] * (num_steps // 4) # Создание аккордовой последовательности, повторением
chord_sequence = mm.ChordSequence(chords)
melody_with_chords_sequence = mm.sequences_lib.concatenate_sequences(melody_sequence, chord_sequence)

# Ударные
drum_pattern = mm.DrumTrack(
    [36, 0, 42, 0, 36, 0, 42, 0],
    start_step=0,
    steps_per_bar=num_steps//4,
    steps_per_quarter=4,
)

music_sequence = mm.sequences_lib.concatenate_sequences(melody_with_chords_sequence, drum_pattern)
music_sequence.tempos[0].qpm = 120  # Установка темпа

# Сохранение полного трека в MIDI
midi_file_with_chords_and_drums = os.path.join(output_dir, 'full_music.mid')
mm.sequence_proto_to_midi_file(music_sequence, midi_file_with_chords_and_drums)

print(f"Full music saved to: {midi_file_with_chords_and_drums}")
```

**Полный пример:**

```python
import os
import magenta.music as mm
from magenta.models.melody_rnn import melody_rnn_sequence_generator

# 1. Установка параметров
output_dir = 'generated_music'
os.makedirs(output_dir, exist_ok=True)

model_name = 'attention_rnn'
melody_rnn = melody_rnn_sequence_generator.MelodyRnnSequenceGenerator(
    model_name=model_name
)

temperature = 1.0
num_steps = 128
primer_sequence = None
# 2. Генерируем мелодию
melody_sequence = melody_rnn.generate(
    temperature=temperature,
    steps=num_steps,
    primer_sequence=primer_sequence
)

# 3. Добавляем аккорды
chords = ["C", "G", "Am", "F"] * (num_steps // 4)
chord_sequence = mm.ChordSequence(chords)
melody_with_chords_sequence = mm.sequences_lib.concatenate_sequences(melody_sequence, chord_sequence)


# 4. Добавляем ударные
drum_pattern = mm.DrumTrack(
    [36, 0, 42, 0, 36, 0, 42, 0],
    start_step=0,
    steps_per_bar=num_steps // 4,
    steps_per_quarter=4,
)
music_sequence = mm.sequences_lib.concatenate_sequences(melody_with_chords_sequence, drum_pattern)
music_sequence.tempos[0].qpm = 120


# 5. Сохраняем в MIDI
midi_file_with_chords_and_drums = os.path.join(output_dir, 'full_music.mid')
mm.sequence_proto_to_midi_file(music_sequence, midi_file_with_chords_and_drums)

print(f"Full music saved to: {midi_file_with_chords_and_drums}")

```

**Дополнительные советы:**

*   **Экспериментируйте с параметрами:** Попробуйте разные значения `temperature`, `num_steps`.
*   **Загрузите собственные MIDI:** Можно использовать собственные мелодии в качестве затравки (`primer_sequence`).
*   **Обучите модель на своих данных:** Если хотите специфический стиль, попробуйте обучить модель на собственном наборе данных.
*   **Изучите документацию Magenta:** Magenta предоставляет хорошую документацию и примеры.
*  **Обратите внимание:**  `primer_sequence` должен быть в виде `mm.NoteSequence()`.


# Игра "Речь в Текст - Текст в Речь"

## Описание

Эта игра объединяет в себе функциональность преобразования речи в текст (Speech-to-Text или STT) и текста в речь (Text-to-Speech или TTS). Вы можете либо говорить в микрофон, и услышать, как ваша речь преобразуется в текст, либо ввести текст, и прослушать, как он будет озвучен.

## Условия Игры

Игра предоставляет вам два основных режима:

1.  **Речь в текст (STT)**:
    *   Вы говорите в микрофон.
    *   Система записывает ваше аудио.
    *   Аудио преобразуется в текст и отображается на экране.
    *   Этот режим позволяет вам протестировать возможности распознавания речи системы.

2.  **Текст в речь (TTS)**:
    *   Вы вводите текст с клавиатуры.
    *   Система преобразует введенный текст в аудио.
    *   Вы слышите озвученный текст.
    *   Этот режим позволяет вам прослушать, как текст будет звучать при озвучке.

Игра позволяет вам переключаться между этими двумя режимами. Вы можете также выходить из игры.

## Как Запустить

1.  **Установите Python**: Если у вас не установлен Python, скачайте и установите его с [официального сайта](https://www.python.org/).
2.  **Установите необходимые библиотеки**: Используйте `pip` для установки библиотек:
    ```bash
    pip install SpeechRecognition gTTS mpg123
    ```

3.  **Скопируйте код в файл**: Скопируйте код Python, представленный ниже, в файл, например, `speech_game.py`.
4.  **Запустите игру**: В терминале или командной строке выполните:
    ```bash
    python speech_game.py
    ```

## Исходный код (Python)

```python
import speech_recognition as sr
from gtts import gTTS
import os
import tempfile

def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now:")
        try:
             audio = recognizer.listen(source, phrase_time_limit=5)
        except Exception as e:
            print ("Could not understand audio, try again")
            return None

    return audio


def transcribe_audio(audio):
    recognizer = sr.Recognizer()
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError as e:
        return f"API Error: {e}"


def text_to_speech(text, language = "en"):
   
    tts = gTTS(text=text, lang=language)
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete = True) as temp:
      tts.save(temp.name)
      os.system(f'mpg123 {temp.name}')

def main():
    while True:
        choice = input("Choose action: (1: STT, 2: TTS, 3: Exit) ")
        if choice == "1":
            audio = record_audio()
            if audio:
                text = transcribe_audio(audio)
                print("Transcribed Text:", text)
        elif choice == "2":
          text = input("Enter the text to synthesize: ")
          text_to_speech(text)
        elif choice == "3":
          break
        else:
            print("Invalid Choice")
        print()
    print ("Good Bye")

if __name__ == "__main__":
   main()
```

### Разбор кода

*   **`import` Statements**: Импортируются необходимые библиотеки:
    *   `speech_recognition` для распознавания речи.
    *   `gtts` для преобразования текста в речь.
    *   `os` и `tempfile` для управления временными файлами аудио.

*   **`record_audio()`**:
    *   Функция для записи аудио с микрофона.
    *   Использует `speech_recognition` для захвата аудио.

*   **`transcribe_audio(audio)`**:
    *   Принимает аудио, записанное ранее.
    *   Использует Google Speech Recognition API для преобразования аудио в текст.
    *   Возвращает распознанный текст или сообщение об ошибке.

*   **`text_to_speech(text, language="en")`**:
    *   Принимает текст и язык (по умолчанию английский) в качестве аргумента.
    *   Использует `gTTS` для преобразования текста в аудио.
     *   Сохраняет аудио во временный файл.
     *   Воспроизводит аудио с помощью `mpg123`.

*   **`main()`**:
    *   Главная функция, управляющая ходом игры.
    *   Предлагает пользователю выбор действия (STT, TTS или выход).
    *   Вызывает соответствующие функции для выполнения выбранного действия.
    *   Обрабатывает ввод пользователя и выводит результаты на консоль.

## Дополнительные Замечания

*   **Зависимости**: Этот код требует установленных библиотек `SpeechRecognition`, `gTTS`, и `mpg123`. Убедитесь, что они установлены перед запуском.
*   **Аудио**: Если `mpg123` не работает, вы можете использовать другой плеер для воспроизведения аудио, изменив функцию `text_to_speech`.


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
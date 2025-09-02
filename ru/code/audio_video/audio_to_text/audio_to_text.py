import speech_recognition as sr
from pydub import AudioSegment

# Initialize recognizer
recognizer = sr.Recognizer()

# Audio file path
audio_file = "audiobook.wav"

# Convert MP3 to WAV if the file is in MP3 format
# AudioSegment.from_mp3(audio_file).export(audio_file, format="wav")

# Work with the audio file
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)

# Text recognition
try:
    text = recognizer.recognize_google(audio_data)
    print("Extracted Text:", text)
except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError as e:
    print("API Error:", e)
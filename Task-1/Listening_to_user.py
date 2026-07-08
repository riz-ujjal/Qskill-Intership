import speech_recognition as sr
import pyaudio
def Listen():
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        audio = recognizer.listen(source)
        message = recognizer.recognize_google(audio)
    return message
Listen()
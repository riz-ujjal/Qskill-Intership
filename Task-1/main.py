import pyttsx3
import speech_recognition as sr
import pyaudio

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        audio = recognizer.listen(source)
        message = recognizer.recognize_google(audio)
    return message

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

while True :
    command = listen()
    print(command)
    if "stop" in command.lower() or "good bye" in command.lower():
        speak("GoodBye shutting down!")
        break
    elif "Hello" in command.lower():
        speak("Hello Ueser")


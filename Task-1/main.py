import pyttsx3
import speech_recognition as sr
import pyaudio
from Weather import get_weather
from News_Reader import News_Reading
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

    elif "weather" in command.lower() or "temperature" in command.lower():
        speak("Let me check the temperature for today...")
        speak("searching for your location...")
        speak(get_weather())
    
    elif "news" in command.lower():
        speak("Here are top two news for today!")
        speak(News_Reading())
    
        


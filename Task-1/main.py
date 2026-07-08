from Weather import get_weather
from News_Reader import News_Reading
from Listening_to_user import Listen
from Speaking_to_user import Speak

while True :
    command = Listen()
    print(command)
    if "stop" in command.lower() or "good bye" in command.lower() or "goodbye" in command.lower():
        Speak("GoodBye shutting down!")
        break
    
    elif "Hello" in command.lower():
        Speak("Hello Ueser")

    elif "weather" in command.lower() or "temperature" in command.lower():
        Speak("Let me check the temperature for today...")
        Speak("searching for your location...")
        Speak(get_weather())
    
    elif "news" in command.lower():
        Speak("Here are top two news for today!")
        Speak(News_Reading())
    
        


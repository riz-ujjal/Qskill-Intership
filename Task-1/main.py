from Weather import get_weather
from News_Reader import News_Reading
from Listening_to_user import Listen
from Speaking_to_user import Speak
from Task_setting import Task

while True :
    command = Listen()
    print(command)
    if "stop" in command or "good bye" in command  or "goodbye" in command or "no" in command :
        Speak("GoodBye shutting down!")
        break
    
    elif "Hello" in command :
        Speak("Hello Ueser")
        break

    elif "weather" in command  or "temperature" in command :
        Speak("Let me check the temperature for today...")
        Speak("searching for your location...")
        Speak(get_weather())
        break
    
    elif "news" in command :
        Speak("Here are top two news for today!")
        Speak(News_Reading())
        break   
    

    
        


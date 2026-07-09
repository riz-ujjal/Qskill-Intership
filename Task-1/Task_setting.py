from Listening_to_user import Listen
from Speaking_to_user import Speak

def Add_task():
    
    message = Listen()
    if "add" in message :
            text = message.replace("add", "").strip()
            if text != "":
                with open("Demo.txt", "a") as file :
                    file.write(text + "\n")
                    Speak( f"Added {text}")
            else :
                return "Did't catch say it again!"
        
Speak(Add_task())
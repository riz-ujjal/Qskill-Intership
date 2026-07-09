from Listening_to_user import Listen
from Speaking_to_user import Speak
message =Listen()
def Add_task():
    
    if "add" in message :
            text = message.replace("add", "").strip()

            if text != "":
                with open("Demo.txt", "a") as file :
                    file.write(text + "\n")
                    Speak( f"Added {text}")

            else :
                Speak("Did't catch say it again!")
Add_task()
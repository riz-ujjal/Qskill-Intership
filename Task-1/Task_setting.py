from Listening_to_user import Add_Task
from Speaking_to_user import Speak

def Task():
    message = Add_Task()
    while True:
    
        if "done" in message:
            Speak("ok We are Done")
            break

        elif "add" in message :
            text = message.replace("add", "").strip()
            if text != "":
                with open("Demo.txt", "a") as file :
                    file.write(text + "\n")
            else :
                return "Did't catch say it again!"
        return "Task  added successfully!"
Task()
Speak(Task())
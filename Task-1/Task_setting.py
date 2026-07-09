
def Add_task(message):
    text = message.replace("add", "").strip()       
    if text != "":
        with open("Demo.txt", "a") as file :
            file.write(text + "\n")
            return( f"Added {text}")

    else :
        return("Did't catch say it again!")

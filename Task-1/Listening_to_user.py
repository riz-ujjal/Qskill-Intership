import speech_recognition as sr
recognizer = sr.Recognizer()
def Listen():
    
    with sr.Microphone(device_index=2) as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        message = recognizer.recognize_google(audio)
        message = message.lower()
        print(message)
    return message
Listen()

def Add_Task():
    try :
        with sr.Microphone(device_index=2) as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            message = recognizer.recognize_google(audio)
            message = message.lower()
            print(message)
        return message
    except recognizer.UnknownValueError():
        message = f"Couldn't hear you clear"
        return message
        

Add_Task()
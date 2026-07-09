import speech_recognition as sr
recognizer = sr.Recognizer()

def Listen():
    
    try :
        with sr.Microphone(device_index=1) as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            message = recognizer.recognize_google(audio)
            message = message.lower()
            print("What i heard : " + message)
        return message
    
    except sr.UnknownValueError:
        message = "Couldn't hear you clear"
        return message

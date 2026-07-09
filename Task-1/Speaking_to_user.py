import pyttsx3
# from Task_setting import Add_task
# text = Add_task
def Speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
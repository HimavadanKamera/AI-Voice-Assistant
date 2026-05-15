import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 170)

def speak(text):

    print("Jarvis:", text)

    engine.say(text)

    engine.runAndWait()
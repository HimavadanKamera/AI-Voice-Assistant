import speech_recognition as sr

recognizer = sr.Recognizer()

def listen_command():

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(audio)

        print("You said:", command)

        return command.lower()

    except Exception as e:

        print(e)

        return ""
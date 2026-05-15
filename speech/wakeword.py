import speech_recognition as sr

recognizer = sr.Recognizer()

def detect_wake_word():

    with sr.Microphone() as source:

        print("Waiting for wake word...")

        while True:

            audio = recognizer.listen(source)

            try:

                text = recognizer.recognize_google(
                    audio
                ).lower()

                print(text)

                if "jarvis" in text:

                    print("Wake word detected")

                    return

            except:

                pass
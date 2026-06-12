import speech_recognition as sr
import webbrowser
from datetime import datetime

recognizer = sr.Recognizer()

print("Mini Voice Assistant Started...")

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        if "hello" in command:
            print("Hello Vibhu!")

        elif "time" in command:
            current_time = datetime.now().strftime("%H:%M:%S")
            print("Current Time:", current_time)

        elif "open google" in command:
            webbrowser.open("https://www.google.com")
            print("Opening Google...")

        elif "exit" in command:
            print("Goodbye!")
            break

        else:
            print("Command not recognized.")

    except Exception as e:
        print("Error:", e)
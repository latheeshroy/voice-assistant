import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def talk(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)

    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("You said:", command)
        return command
    except:
        talk("Sorry, I did not understand.")
        return ""

def run_assistant():
    command = take_command()

    if "play" in command:
        song = command.replace("play", "")
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("Current time is " + time)

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        talk(info)

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "open chrome" in command:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    elif "exit" in command:
        talk("Goodbye")
        sys.exit()

    else:
        talk("Command not recognized")

talk("Hello, I am your voice assistant")
while True:
    run_assistant()

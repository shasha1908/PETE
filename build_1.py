import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from googlesearch import search

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def intro():
    engine.say(
        "My name is PETE. Python Based Engine to increase Efficiency. I am Mr. Bhatt's virtual assistant and will control his laptop based on his commands.")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon")

    else:
        speak("Good evening")

    speak("What would you like to do?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ssbhatt@syr.edu', 'Shashwat_1908')
    server.sendmail('ssbhatt@syr.edu', to, content)
    server.close()


if __name__ == "__main__":

    intro()
    wishMe()
    while True:
        # if 1:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            speak('Processing...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'play music' in query:
            webbrowser.open("https://www.jiosaavn.com/random")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            print(strTime)
        elif 'open code' in query:
            speak("Opening code...")
            codePath = "C:/Program Files/JetBrains/PyCharm 2017.2.3/bin/pycharm64.exe"
            os.startfile(codePath)
        elif 'show my face' in query:
            codePather = "C:/Users/bhatt/Desktop/shashwat.jpg"
            os.startfile(codePather)
        elif 'your face' in query:
            webbrowser.open("https://thispersondoesnotexist.com/")
        elif 'send email to shashwat' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "bhattshashwat@ymail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Email Not sent")
        elif 'open sb' in query:
            path = "C:/Users/bhatt/Desktop/sb"
            os.startfile(path)
        elif 'play avengers' in query:
            path_a = "C:/Users/bhatt/Downloads/Avengers.Endgame.2019.1080p.HC.YG/Avengers.Endgame.2019.1080p.HC.HDTS.H264.AC3.YG.mkv"
            os.startfile(path_a)
        elif 'quit' in query:
            exit()


import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1])

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    
    else:
        speak("Good Evening")

    speak("I am jarvis. Please tell me how may i help you")

def TakeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said: {query}\n")


    except Exception as e:
        #print(e)
        print("say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com','your_password')
    server.sendmail('your_email@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    WishMe()
    #if 1:
    while True:
        query = TakeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open my gmail account' in query:
            webbrowser.open("gmail.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\microline\\Music'
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
        elif 'time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam , the time is {strTime}")
        elif 'open code' in query:
            path1 = "C:\\Users\\microline\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code"
            os.startfile(path1)
        elif 'open google' in query:
            path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
        elif 'email to urja' in query:
            try:
                speak("what should I say?")
                content = TakeCommand()
                to = "receivers_mail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry mam i am not able to send your email!")
        elif 'exit' in query:
            exit()


        

        
        

            



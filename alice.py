from gtts import gTTS
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

    


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)
    tts = gTTS(text=audio, lang='en')
    
    
def wishMe():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
         speak("good morning")
     elif hour>=12 and hour<18:
         speak("good afternoon")
     elif hour>=18 and hour<23:
         speak("good evening")
     else:
         speak("good night")
     speak("iam alice mam   please tell me how may i help you")       

#it takes microphone input from user and return string
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for background noise. One second")
        r.adjust_for_ambient_noise(source)
        print("listening.....")

        r.pause_threshold = 0.5
        r.phrase_threshold = 0.3
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said:",query)

    except Exception as e:
        print(e)
        speak("say that again please...")
        return "None"
    return query 
def sendEmail(to,content): 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yourmail7@gmail.com', 'your password')
    server.sendmail('yourmail7@gmail.com',to, content)    
    server.close()        

if __name__ == "__main__":
    speak("hello anu mam")
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()


    #logic for exection task
        if 'wikipedia' in query:
            speak('searching wikipedia..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open facebook' in query:
            webbrowser.open("fb.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'times of india' in query:
            webbrowser.open("times of india.com")
        elif 'open whatapp' in query:
            webbrowser.open("web.whatsapp.com")       
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Anu Nema\\Music\\Playlists' # \\ to escape charater
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))   
        elif 'tell me time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")     
            speak(f"the time is{strTime}")
        elif 'open code' in query:
            codePath = 'C:\\Users\\Anu Nema\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
        elif 'open excel' in query:
            codePath = 'C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE'
            os.startfile(codePath)
        elif 'open ppt' in query:
            codePath = '"C:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE"'
            os.startfile(codePath)
        elif 'open chrome' in query:
            codePath = 'C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe'
            os.startfile(codePath)
        elif 'open text' in query:
            codePath = 'C:\\Program Files\\Sublime Text 3\\sublime_text.exe'
            os.startfile(codePath)
        elif 'open gmail' in query:
            url = "gmail.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            
        elif 'email to anu' in query:
            try:
                speak("whats your message?")
                content = takeCommand()
                to = "yourmail.com"
                sendEmail(to, content)
                speak("email has sent")
            except Exception as e:
                print(e)
                speak("sorry email not sent")    
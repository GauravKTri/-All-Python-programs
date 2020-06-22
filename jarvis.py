import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import os






engine=pyttsx3.init('sapi5')
voices=engine.getPrpperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)





def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir.Please tell me how may i help you")

def takeCommand():
    #it takes microphone input  from the user and returns string as output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, Language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"
    return query

if __name__ == "__main__":
   wishme()
   while True:
       query=takeCommand().lower()
       if 'wikipedia' in query:
           speak('Searching Wikipedia...')
           query=query.replace("wikipedia", "")
           results=wikipedia.summary(query,sentences=4)
           speak("According to wikipedia")
           print(results)
           speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime(%H:%M:%S)
            speak(f"The time is: {strTime}")
        
               
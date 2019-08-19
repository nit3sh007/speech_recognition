import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import subprocess, sys

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty(voices[6],id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak('good moring')
    elif hour>=12 and hour<=18:
        speak('Good evening')
    else:
        speak('good night')

    speak('Hey ! How may i help you')
    __author__    = "Nitesh kumar"
    
def takecommnad():
    #take command convert and return into  string
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing')
        query = r.recognize_google(audio,language='en-in')
 # check use other recognizer service just press "CTRl"  and for more info  click on recognizer_google
        print(f"user said: {query}\n")
    except Exception as e:
        #print(e)
        print('say that again...')
        return 'None'
    return query
    
if __name__=="__main__":
    #speak('nitesh kuamr')
    wishme()
    #True
    while 1:
    #if 1:
      query = takecommnad().lower()
      if 'wikipedia' in query:

          speak('searching.. wikipedia')
          query = query.replace('wikipedia',"")
          results = wikipedia.summary(query,sentences = 2)
          speak('accorinding to wikipedia')
          print(results )
          speak(results)
      elif 'open youtube' in query:
          webbrowser.open('youtube.com')

      elif 'play music' in  query:
          music_dir = '/root/Desktop/music'
          songs = os.listdir(music_dir)
          print(songs)
          #return_code = songs(["ffplay", "-nodisp", "-autoexit", "../1.mp3"])
          #subprocess.call(["ffplay", "-nodisp", "-autoexit", "/root/Desktop/music"])

          #os.system(os.path.join(music_dir,songs[0]))

      elif 'time is ' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"Time is : {strTime}")

      elif 'tell me a joke' in query:
          speak('Haha I have no any jokes')

      elif 'who are you' in query:
            speak('I am your personal Assistent Sir')

      elif 'say 1 to 10' in query:
                for i in range(0,11):
                  speak(i)
      elif 'thanks' in query:
            speak(' Your welcome')
            
      elif 'stop' in query:
        SystemExit(0)

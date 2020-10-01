import pyttsx3
import pyttsx3.voice
# import pyttsx
import datetime
# from engine import Engine
Engine=pyttsx3.init('sapi5') 
voices=Engine.getProperty('voices')
print(voices[0].id)
Engine.setProperty('voices',voices[1].id)


def speak(audio):
    Engine.say(audio)
    Engine.runAndWait()


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning")

    elif hour >12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")


    speak("I am your assistant Sir,please let me know how can i help you?")
if __name__ == '__main__':
    wishme()

    

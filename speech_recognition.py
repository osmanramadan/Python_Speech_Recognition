import speech_recognition as sr
import pyttsx3
import time
import webbrowser


well=pyttsx3.init()
voices=well.getProperty("voices")
well.setProperty('voices',voices[0].id)

def speak(audio):
    well.say(audio)
    well.runAndWait()

def take_domand():
    dommand=sr.Recognizer()
    with sr.Microphone() as mic :
        print("say any thing")
        dommand.phrase_threshold=1
        audio=dommand.listen(mic)
        try:
            print("recording.......")
            query=dommand.recognize_google(audio,language='en')
            # if 'hello' in query:
            print(f"he said:{query}")
           
            if 'hello' in query:
                   speak("hello osman")
            elif 'I want to eat' in query:
                   speak("ok")
                   time.sleep(3)
                   webbrowser.open_new_tab("https://maps.google.com/")
            elif 'what is the time'  in  query:
                   speak("ok")
                   time.sleep(2)
                   c=time.clock()
                   print(c)
                   speak(c)
            else:
                   speak("your speech arent in menue")
            return query.lower if True else print("error") 
        except :
            speak('please say again')

speak("HELLO OSMAN CAN YOU NEEED ANY  HELP")
while True:
     s=take_domand()
     print(s)
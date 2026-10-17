import speech_recognition as sr
import webbrowser
import pyttsx3
recognizer=sr.Recognizer()   #this is Recognizer class for the text recognization
engine=pyttsx3.init()   #initialize the python text to speech . 
def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__=="__main__":
    speak("initializing jarvis.. ")
    
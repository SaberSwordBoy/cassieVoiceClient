import pyttsx3
import configparser

config = configparser.ConfigParser()
config.read("config/config.ini")

engine = pyttsx3.init()

# Rate
rate = engine.getProperty('rate')                     
engine.setProperty('rate', config.getint("TextToSpeech", "rate"))    

# Volume
volume = engine.getProperty('volume')
print (volume)
engine.setProperty('volume',config.getint("TextToSpeech", "volume"))

# Voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[config.getint("TextToSpeech", "voice")].id)

def speak_text(text):
    engine.say(text)
    engine.runAndWait()
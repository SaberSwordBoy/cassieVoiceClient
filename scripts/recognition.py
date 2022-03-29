import speech_recognition as sr
import configparser

recognizer = sr.Recognizer()
config = configparser.ConfigParser()
config.read("config/config.ini")

processing_method = config.get('SpeechRecognition', "processingMethod")
save_audio_files = config.getboolean("SpeechRecognition", "saveAudioFiles")

def listen():
    with sr.Microphone() as source:
        with sr.Microphone() as source:
            print("Start Talking")
            audio_text = recognizer.listen(source)
            print("Time over, thank you")
    
            try:
                # using google speech recognition
                print("Text: "+recognizer.recognize_google(audio_text))
            except:
                print("Sorry, could not understand. ")
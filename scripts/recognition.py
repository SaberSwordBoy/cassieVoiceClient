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
                if processing_method == 'google':
                    query = recognizer.recognize_google(audio_text)
                elif processing_method == 'idm':
                    query = recognizer.recognize_ibm(audio_text)
                elif processing_method == 'google_cloud':
                    query = recognizer.recognize_google_cloud(audio_text)
                elif processing_method == 'sphinx':
                    query = recognizer.recognize_google(audio_text)
                elif processing_method == 'houndify':
                    query = recognizer.recognize_houndify(audio_text)
            except:
                query = "Sorry, couldn't understand that. "
    return query
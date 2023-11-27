import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    voice_id = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0'
    engine.setProperty('voice', voice_id)
    print("")
    print(f"==> Revenant Ai : {text}")
    print("")
    engine.say(text)
    engine.runAndWait()


def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio,language="en")
            return query.lower()
        
        except:
            return ""

def MainExecution(query):
    Query = str(query).lower()

    if "hello" in Query:
        speak("Hello sir, Welcome Back!")

    elif "bye" in Query:
        speak("Nice to meet you sir, Have a nice day!")

while True:
    print("")
    Query = speechrecognition()
    MainExecution(Query)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pathlib
import warnings
import pyttsx3
import speech_recognition as sr

VoiceIsOnOrOff = False

warnings.simplefilter('ignore')

# nltk.download("punkt")

# def speak(text):
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     voice_id = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0'
#     engine.setProperty('voice', voice_id)
#     print("")
#     print(f"==> Revenant Ai : {text}")
#     print("")
#     engine.say(text)
#     engine.runAndWait()

def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en")
            return query.lower()

        except:
            return ""


ScriptDir = pathlib.Path().absolute()

url = "https://pi.ai/talk"
chrome_option = Options()
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
chrome_option.add_argument(f"user-agent={user_agent}")
chrome_option.add_argument('--profile-directory=Default')
# chrome_option.add_argument("--headless=new")
chrome_option.add_argument(f'user-data-dir={ScriptDir}\\chromedata')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_option)

driver.maximize_window()
driver.get(url=url)
sleep(5)

def VoiceOnButton():
    global VoiceIsOnOrOff
    Xpath = '/html/body/div/main/div/div/div[3]/div[3]/div/div[2]/button'
    driver.find_element(by=By.XPATH,value=Xpath).click()
    VoiceIsOnOrOff = True


def QuerySender(Query):
    XpathInput = '/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea'
    XpathSenderButton = '/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button'

    driver.find_element(by=By.XPATH,value=XpathInput).send_keys(Query)
    sleep(1)
    driver.find_element(by=By.XPATH,value=XpathSenderButton).click()
    sleep(1)


def Wait_for_result():
    sleep(1)
    XpathInput = '/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div[2]/textarea'
    driver.find_element(by=By.XPATH,value=XpathInput).send_keys("Testing....")
    sleep(1) 

    while True:
        Button = driver.find_element(by=By.XPATH,value="/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button").is_enabled() 
        try:
            if False==Button:
                pass

            else:
                driver.find_element(by=By.XPATH,value=XpathInput).clear()
                break
                
        except:
            break

def Result():
    Text = driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]").text
    return Text

def MainExecution():
    global VoiceIsOnOrOff
    Query = speechrecognition()
    QuerySender(Query=Query)
    if VoiceIsOnOrOff==False:
        VoiceOnButton()
    else:
        pass
    Wait_for_result()
    print(Result()) 

while True:
    MainExecution()

     
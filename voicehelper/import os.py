import speech_recognition as sr
from playsound import playsound
import os

def execute_command(command):
    commands = {
        "chrome": '"C:/Program Files/Google/Chrome/Application/chrome.exe"',
        "telegram": '"C:/Users/user/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Приложения Chrome/Telegram Web.lnk"',
        "instagram": '"C:/Users/user/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Приложения Chrome/Instagram.lnk"',
        "youtube": '"C:/Users/user/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Приложения Chrome/YouTube.lnk"'
    }
    path = commands.get(command)
    if path:
        os.startfile(path)
        print("Bajarildi: " + command)
        playsound(f'C:/code/allfiles/voicehelper/bajar.mp3')
        
    else:
        print("Noma'lum buyruq: " + command)

def listen_and_play():
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Iltimos, gapiring...")
            audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio, language='uz-UZ')
                print("Siz aytgan gap: " + text)
                if text.lower() in ["salom", "qalaysiz"]:
                    playsound(f'C:/code/allfiles/voicehelper/{text.lower()}.mp3')
                
                elif text.lower() in ["ochar"]:
                    playsound(f'C:/code/allfiles/voicehelper/ochir.mp3')
                    os.system("shutdown -s")
                    print('qurilmani ochmoqda!')
                    exit()
                    
                else:
                    execute_command(text.lower())
            except sr.UnknownValueError:
                print("Kechirasiz, ovozingizni tushuna olmadim.")
            except sr.RequestError as e:
                print(f"Google Speech Recognition xizmatidan foydalanib bo'lmadi; {e}")

if __name__ == "__main__":
    listen_and_play()

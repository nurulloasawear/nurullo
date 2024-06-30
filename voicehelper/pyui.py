import tkinter as tk
from threading import Thread
import speech_recognition as sr
import os
import webbrowser as wb
from playsound import playsound
# import HttpResponses as 

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
        playsound(f'C:/code/allfiles/voicehelper/internet.mp3')
        wb.open(f"https://www.google.com/search?q={command}")

def listen_and_play():
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)  # Ambient shovqinni aniqlash
            print("Iltimos, gapiring...")
            # Timeout and phrase limits are optionally added for better control
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            try:
                text = recognizer.recognize_google(audio, language='uz-UZ')
                print("Siz aytgan gap: " + text)
                
                if text.lower() in ["salom", "qalaysiz"]:
                    playsound(f'C:/code/allfiles/voicehelper/{text.lower()}.mp3')
                elif text.lower() == "o'chir":
                    playsound(f'C:/code/allfiles/voicehelper/ochir.mp3')
                    os.system("shutdown -s")
                    print('Qurilmani ochmoqda!')
                    exit()
                elif text.lower() =="instagram":
                    wb.open(f"darknet.com")
                    playsound(f'C:/code/allfiles/voicehelper/bajar.mp3')
                    print('Qurilmani ochmoqda!')  
                elif text.lower() in [ "darkweb", "hujum "]:
                    wb.open(f"instagram.com")
                    playsound(f"hujum1.mp3")
                    continue
    
                elif text.lower() == ["xayir","chiqish"]:
                    playsound(f'C:/code/allfiles/voicehelper/Xayr.mp3')
                    exit()  
                    os.system("exit")
                    print('Qurilmani ochmoqda!')
                    exit()   
                elif text.lower() in ["kod", "vs code", "code"]:
                    playsound(f'C:/code/allfiles/voicehelper/bajar.mp3')
                    os.system("code")
                wb.open(f"https://www.google.com/search?q={text}")
                playsound(f'C:/code/allfiles/voicehelper/internet.mp3')
           
            except sr.UnknownValueError:
                print("Kechirasiz, ovozingizni tushuna olmadim.")
            except sr.RequestError as e:
                print(f"Google Speech Recognition xizmatidan foydalanib bo'lmadi; {e}")

def start_listening_thread():
    listening_thread = Thread(target=listen_and_play)
    listening_thread.daemon = True
    listening_thread.start()

def main():
    root = tk.Tk()
    root.title("Ovozli Yordamchi")
    start_button = tk.Button(root, text="Ovozni eshitishni boshlash", command=start_listening_thread)
    start_button.pack()
    root.mainloop()

if __name__ == "__main__":
    main()

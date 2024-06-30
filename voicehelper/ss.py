import subprocess
import os

def grant_access(path):
    try:
        # Foydalanuvchi nomini olish (bu yerda "Everyone" umumiy foydalanuvchi guruhiga murojaat qilinmoqda)
        user_name = "Everyone"
        # CMD orqali ACL (Access Control List) sozlamalarini o'zgartirish
        subprocess.run(["icacls", path, "/grant", f"{user_name}:(F)"], check=True)
        print(f"{user_name} ga {path} yo'lidagi fayl yoki papkaga to'liq kirish huquqi berildi.")
    except subprocess.CalledProcessError as e:
        print("Ruxsat berishda xato yuz berdi:", e)

if __name__ == "__main__":
    # Fayl yoki papka yo'lini kiriting
    file_path = input("Fayl yoki papka yo'lini kiriting: ")
    grant_access(file_path)

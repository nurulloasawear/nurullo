import cv2
from pyzbar.pyzbar import decode

def qoshish():
    mahsulotlar = []  # Mahsulotlarni saqlash uchun ro'yxat
    t = open("Malumot.txt", "a")  # Ma'lumotlarni saqlash uchun fayl
    y = open("sotish.txt", "a")  # Sotuvlar tarixini saqlash uchun fayl
    v = open("Kunlik Savdo Hisoboti.txt", "a")  # Kunlik savdo hisobotini saqlash uchun fayl
    kamera = cv2.VideoCapture("http://10.20.2.200:8080/video") 

    while True:
        print("Mahsulot qo'shish uchun 1 ni tanlang")
        print("Mahsulotlarni ko'rish uchun 2 ni tanlang")
        print("Sotish uchun 3 ni tanlang")
        print("Kunlik savdo hisoboti uchun 4 ni tanlang")
        print("Chiqish uchun 5 ni bosing")

        tanlov = input("Tanlovni tanlang: ")

        if tanlov == "1":
            mahsulot_qoshish(mahsulotlar, t)
        elif tanlov == "2":
            mahsulotlarni_korish(mahsulotlar)
        elif tanlov == "3":
            sotish(mahsulotlar, y)
        elif tanlov == "4":
            kunlik_savdo_hisoboti(mahsulotlar, v)
        elif tanlov == "5":
            print("Dastur muvaffaqiyatli yakunlandi.")
            break
        else:
            print("Noto'g'ri tanlov!")

    t.close()
    y.close()
    v.close()

def mahsulot_qoshish(mahsulotlar, fayl):
    b = input("Mahsulot nomi: ")
    r = input("Mahsulot kelgan Sanasi (yyyy.mm.dd): ")
    c = input("Mahsulot yaroqliligi muddati (yyyy.mm.dd): ")
    d = input("Mahsulot donasi-blogi (blog db yoki dona db): ")
    f = input("Mahsulot qabul qilingan narxi: ")
    h = input("Kegan Mahsulotni umumiy % qoyilgandgi  umum narxi: ")
    r = input("Mahsulot donasi yoki kilosini narxi: ")
    g = int(input("Mahsulot sotilish narxi: "))

    if b and c and d:  # Faqat b, c va d to'g'ri kiritilganda qo'shib boriladi
        mahsulot = f"Nomi: {b},\nMahsulot kelgan Sanasi:{r},\nYarog'lilik muddati: {c},\nMahsulot donasi-blogi: {d},\nMahulot qabul qilingan narxi:{f},\nMahsulot donasi yoki kilosini narxi:{r},\nMahsulot sotilish narxi:{g},\nKegan Mahsulotni umumiy % qoyilgandgi  umum narxi:{h}"
        mahsulotlar.append(mahsulot)
        fayl.write(mahsulot + "\n")
        print("\nMahsulot qo'shildi:")
        print(mahsulot)
    else:
        print("Noto'g'ri ma'lumotlar!")

def mahsulotlarni_korish(mahsulotlar):
    if not mahsulotlar:
        print("Ro'yxat bo'sh.")
    else:
        for mahsulot in mahsulotlar:
            print(mahsulot)

def sotish(mahsulotlar, fayl):
    ret, rasm = kamera.read()

    if not ret:
        print("Error: Kameradan ma'lumot o'qib bo'lmadi.")
        return

    barcodes = decode(rasm)

    if not barcodes:
        print("Error: QR-kod topilmadi.")
        return

    for barcode in barcodes:
        barcode_data = barcode.data.decode("utf-8")
        for mahsulot in mahsulotlar:
            if barcode_data in mahsulot:
                foydalanuvchi_sotib_oldi(fayl, barcode_data, mahsulot)
                print(f"{barcode_data} sotib olindi.")
                return
    print(f"{barcode_data} ro'yxatda mavjud emas.")

def foydalanuvchi_sotib_oldi(fayl, barcode_data, mahsulot):
    narx = mahsulot.split("Mahsulot sotilish narxi:")[1].strip()
    sotib_olindi = f"Sotildi:{barcode_data},\tNarxi:{narx}"
    fayl.write(sotib_olindi + "\n")

def kunlik_savdo_hisoboti(mahsulotlar, fayl):
    ns = int(input("Inkasatsiya ajratilgan Mablagni Krting: "))
    nd = int(input("Terminal Xumo dan tushgan summani ktring: "))
    nf = int(input("Terminal Uzcard dan tushgan summani ktring: "))
    gf = input("Bugungi sana: ")
    df = ns + nd + nf + umumiy_sotish(mahsulotlar)  # Umumiy sotishlarni hisoblash
    gf = f"Bugungi sana:{gf}, Shu kun ichida - Umumiy Bolgan Savdo:{df}"
    fayl.write(gf + "\n")
    print(gf)

def umumiy_sotish(mahsulotlar):
    umumiy = 0
    for mahsulot in mahsulotlar:
        umumiy += int(mahsulot.split("Kegan Mahsulotni umumiy % qoyilgandgi  umum narxi:")[1].strip())
    return umumiy

qoshish()

import cv2
from pyzbar.pyzbar import decode
i = []
def foydalanuvchi_sotib_oldi(fayl, barcode_data, mahsulot):
    with open("sotilgan.txt", "a") as f:
        f.write(f"Sotib alindi: {barcode_data}, Mahsulot: {mahsulot}\n")

def qrcode(mahsulotlar):
    kamera = cv2.VideoCapture("http://10.20.0.235:8080/video") 
    ret, rasm = kamera.read()
    # mahsulot = 
    if not ret:
        print("Error: Kameradan ma'lumot o'qib bo'lmadi.")
        return

    barcodes = decode(rasm)

    if not barcodes:
        print("Error: QR-kod topilmadi.")
        return

    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(rasm, (x, y), (x + w, y + h), (1, 300, 1), 3)

        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        cv2.putText(rasm, str(barcode_data), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        print(f"QR-kod turi: {barcode_type}, ma'lumot: {barcode_data}")

        for mahsulot in i:
            if barcode_data in mahsulot:
                foydalanuvchi_sotib_oldi("sotilgan.txt", barcode_data, mahsulot)
                print(f"{barcode_data} sotib olindi.")
                break

        else:
            print(f"{barcode_data} ro'yxatda mavjud emas.")

    cv2.imshow("QR-kod skanneri", rasm)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # cv2.exit()

def qoshish():
   
    t = open("Malumot.txt", "a")  # Faylni "qo'shish" rejimida ochish uchun
    p = 0  # Astatkani saqlash uchun o'zgaruvchi
    y = open("sotish.txt", "a")
    v = open("Kunlik Savdo Hisoboti.txt","a")
    mahsulotlar = []  # Define mahsulotlar list here

    while True:
        print("Mahsulot qoshing!\nMahsulot qoshish uchun 1 tanlang")
        print("Mahsulotlarini ko'rish uchun 2 tanlang")
        print("Sotish uchun 6 ni tanlang")
        print("QR kod skanlash uchun 7 ni tanlang")
        a = input("Tanlang (exit to quit): ")

        if a.lower() == "exit":
            print("Muvaffaqiyatli chiqildi! Xayr.")
            break
        elif a == "2":
            if not i:
                print("Ro'yxat bo'sh.")
            else:
                for item in i:
                    print(item)
        elif a == "6":
            qrcode(mahsulotlar)
        elif a == "1":
            b = input("Mahsulot nomi: ")
            r = input("Mahsulotlar kelgan Sanasi (yyyy.mm.dd): ")
            c = input("Mahsulot yaroqliligi muddati (yyyy.mm.dd): ")
            d = input("Mahsulot donasi-blogi (blog db yoki dona db): ")
            f = input("Mahsulot qabul qilingan narxi: ")
            h = input("Kegan Mahsulotni umumiy % qoyilgandgi  umum narxi:")
            r = input("Mahsulot donasi yoki kilosini narxi: ")
            g = int(input("Mahsulot sotilish narxi: "))

            if b and c and d:
                item_str = f"Nomi: {b},\nMahsulot kelgan Sanasi:{r},\nYarog'lilik muddati: {c},\nMahsulot donasi-blogi: {d},\nMahulot qabul qilingan narxi:{f},\nMahsulot donasi yoki kilosini narxi:{r},\nMahsulot sotilish narxi:{g},\nKegan Mahsulotni umumiy % qoyilgandgi  umum narxi:{h}"
                i.append(item_str)
                # i.(item_str)
                t.write(item_str + "\n")
                mahsulotlar.append(item_str)  # Append item_str to mahsulotlar list
                print("\nMahsulot qo'shildi:")
                print(item_str)
            else:
                print("Noto'g'ri ma'lumotlar!")
        else:
            print("Noto'g'ri tanlov!")
            input("Qayta kriting:")

    t.close()

qoshish()

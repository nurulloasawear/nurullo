import cv2
from pyzbar.pyzbar import decode

def qoshish():
    i = []  # Mahsulotlar ro'yxati
    t = open("Malumot.txt", "a")  # Fayl ma'lumotlarini qo'shish uchun ochilgan
    capture = cv2.VideoCapture(0)  # Kamera videoni olish

    while True:
        print("Mahsulot qo'shish!")
        print("1 - Mahsulot qo'shish")
        print("2 - Mahsulotlarni ko'rish")
        print("3 - Mahsulot qidirish")
        print("4 - Prihodni aniqlash")
        print("5 - Rasxodni ayrish")
        print("6 - Sotish")
        print("7 - Kuni Tugatish Z va X hisobini Olish")
        choice = input("Tanlang (exit to quit): ")

        if choice.lower() == "exit":
            print("Chiqildi! Xayr.")
            break
        elif choice == "2":
            if len(i) == 0:
                print("Ro'yxat bo'sh.")
            else:
                for item in i:
                    print(item)

        elif choice == "6":
            while True:
                ret, frame = capture.read()  # Kamerani o'qish
                if ret:
                    decoded_objects = decode(frame)  # QR kodlarni aniqlash
                
                    if decoded_objects:
                        for obj in decoded_objects:
                            points = obj.polygon
                            data = obj.data.decode('utf-8')  # QR-kodning tekst ma'lumotini olish

                            print("QR-kod:", data)

                            for point in points:
                                cv2.circle(frame, point, 10, (0, 0, 255), -1)  # QR-kodning joylashgan joylarini ko'rsatish

                            cv2.imshow("QR-kod skanneri", frame)  # Ekran bo'yicha QR kodlarni chiqarish

                            for item in i:
                                if data in item:
                                    item_str = item.split("Mahsulot sotilish narxi:")[1].strip()
                                    item_str = f"Sotildi:{frame},\tNarxi:{item_str}"
                                    print("Sotilgan narxi summasini:", item_str)
                                    break
                            else:
                                print(f"{data} ro'yxatda mavjud emas.")
                    
                if cv2.waitKey(1) & 0xFF == ord('q'):  # Chiqish uchun 'q' tugmasi
                    break
           
        elif choice == "7":
            ns = int(input("Inkasatsiya ajratilgan Mablagni Kiriting:"))
            nd = int(input("Terminal Xumo dan tushgan summani ktring:"))
            nf = int(input("Terminal Uzcard dan tushgan summani ktring:"))
            gf = input("Bugungi sana:")
            df = ns + nd + nf
            gf = f"Bugungi sana:{gf},Shu kun ichida - Umumiy Bolgan Savdo:{df}"
            print(gf)
        elif choice == "3":
            s = input("Qidirayotgan narsangizni kriting: ")
            if any(s in item for item in i):
                print(f"{s} ro'yxatda mavjud.")
            else:
                print(f"{s} ro'yxatda mavjud emas.")
        elif choice == "4":
            g = int(input("Qancha prihodni aniqlamoqchisiz: "))
            print("Astatkani summasini:", g)
        elif choice == "5":
            d = int(input("Qancha arymoqchi bolgan summani ktring:"))
            print(f"Bajarildi:{d}")
        elif choice == "1":
            b = input("Mahsulot nomi: ")
            r = input("Mahsulotlarning Kelgan Sanasi (yyyy.mm.dd): ")
            c = input("Mahsulot yaroqliligi muddati (yyyy.mm.dd): ")
            d = input("Mahsulot donasi-blogi (blog db yoki dona db): ")
            f = input("Mahsulot qabul qilingan narxi: ")
            h = input("Kegan Mahsulotni umumiy % qoyilgandgi  umum narxi:")
            r = input("Mahsulot donasi yoki kilosini narxi: ")
            g = int(input("Mahsulot sotilish narxi: "))

            if b and c and d:
                item_str = f"Nomi: {b},\nMahsulot kelgan Sanasi:{r},\nYarog'lilik muddati: {c},\nMahsulot donasi-blogi: {d},\nMahulot qabul qilingan narxi:{f},\nMahsulot donasi yoki kilosini narxi:{r},\nMahsulot sotilish narxi:{g},\nKegan Mahsulotni umumiy % qoyilgandgi  umum narxi:{h}"
                i.append(item_str)
                t.write(item_str + "\n")
                print("\nMahsulot qo'shildi:")
                print(item_str)
            else:
                print("Noto'g'ri ma'lumotlar!")
        else:
            print("Noto'g'ri tanlov!")
            input("Qayta kriting:")

    t.close()

qoshish()

def mahsulot_qoshish():
    b = input("Mahsulot nomi: ")
    r = input("Mahsulotlarning Kelgan Sanasi (yyyy.mm.dd): ")
    c = input("Mahsulot yaroqliligi muddati (yyyy.mm.dd): ")
    d = input("Mahsulot donasi-blogi (blog db yoki dona db): ")
    f = input("Mahsulot qabul qilingan narxi: ")
    r = input("Mahsulot donasi yoki kilosini narxi: ")
    # g o'zgaruvchisini tanlash
    g = int(input("Mahsulot sotilish narxi: "))

    if b != "" and c != "" and d != "":
        item_str = f"Nomi: {b},\nMahsulot kelgan Sanasi:{r},\nYarog'lilik muddati: {c},\nMahsulot donasi-blogi: {d},\nMahulot qabul qilingan narxi:{f},\nMahsulot donasi yoki kilosini narxi:{r},\nMahsulot sotilish narxi:{g}"
        i.append(item_str)
        t.write(item_str + "\n")
        print("\nMahsulot qo'shildi:")
        print(item_str)
    else:
        print("Noto'g'ri ma'lumotlar!")

def qoshish():
    i = []
    t = open("Malumot.txt", "a")  # Faylni "qo'shish" rejimida ochish uchun
    p = 0  # Astatkani saqlash uchun o'zgaruvchi

    while True:
        print("Mahsulot qoshing!\nMahsulot qoshish uchun 1 tanlang")
        print("Mahsulotlarini ko'rish uchun 2 tanlang")
        print("Mahsulot qidirish uchun 3 ni tanlang")
        print("Qancha prihodni aniqlash uchun 4 ni bosing:")
        print("Rasxodni ayrish uchun bosing 5: ")
        a = input("Tanlang (exit to quit): ")

        if a.lower() == "exit":
            print("Muvaffaqiyatli chiqildi! Xayr.")
            break
        elif a == "2":
            for item in i:
                print(item)
        elif a == "3":
            s = input("Qidirayotgan narsangizni kriting: ")
            if any(s in item for item in i):
                print(f"{s} ro'yxatda mavjud.")
            else:
                print(f"{s} ro'yxatda mavjud emas.")
        elif a == "4":
            # g o'zgaruvchisini aniqlash
            g = int(input("Qancha prihodni aniqlamoqchisiz: "))
            
            # p o'zgaruvchisini yaratish
            p = 0
            for x in i:
                # Har bir elementni hisoblash va p ga qo'shish
                p += int(x.split("Mahsulot sotilish narxi:")[1].strip())
            p += g
            print("Astatkani summasini:", p)
        elif a == "5":
            d = int(input("Qancha arymoqchi bolgan summani ktring:"))
            f = d - p
            print(f"Bajarildi:{d}")
            print("Qolgan holati:", p)
        elif a == "1":
            mahsulot_qoshish()
        else:
            print("Noto'g'ri tanlov!")
            input("Qayta kriting:")

    t.close()

qoshish()

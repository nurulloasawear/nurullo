# def qoshish():
#     i = []
#     t = open("Malumot.txt", "w")
    
#     while True:
#         print("Mahsulot qoshing!\nMahsulot qoshish uchun 1 tanlang")
#         print("Mahsulotlarini ko'rish uchun 2 tanlang")
#         print("Mahsulot qidirish uchun 3 ni tanlang")
#         print("Qancha mol qolganini  aniqlash uchun 4 ni bosing:")
#         a = input("Mahsulot qoshish (exit to quit): ")

#         if a.lower() == "exit":
#             print("Muvaffaqiyatli chqilidi! Xayr")
#             break
#         elif a == "2":
#             print(i)
#         elif a == "3":
#             s = input("Qidirayotgan narsangiz kriting: ")
#             if any(s in item for item in i):
#                 print(f"{s} ro'yxatda mavjud.")
#             else:
#                 print(f"{s} ro'yxatda mavjud emas.")

#         if a == "1":
#             b = input("Mahsulot nomi: ")
#             r = input("Mahsulotlning Kelgan Sanasi (yyyy.mm.dd):")
#             c = input("Mahsulot yarog'liligi (yyyy.mm.dd): ")
#             d = input("Mahsulot donasi-blogi (blog bolsa blog db dona bolsa dona db yozb keting!): ")
#             f = input("Mahsulotlarini qabul qilgan narxi:")
#             r = input("Mahsulotlning donsi yoki kilosini  narxi:")
#             g = int(input("Mahsulotlning sotilish narxi:"))

#             elif g == int():
#                 c =  g + g
#                 if a == "4":
#                     print(c)

#             if b != "" and c != "" and d != "":
#                 # i.write(f"Nomi: {b}, Yarog'lilik muddati: {c}, Mahsulot donasi-blogi: {d},Mahulot qabul qilingan narxi:{f},Mahsulot donasi yoki kilosini narxi:{r},Mahsulot sotilish narxi:{g}")
#                 i.append(f"Nomi: {b},\nMahsulot kelgan Sanasi:{r},\n Yarog'lilik muddati: {c}, Mahsulot donasi-blogi: {d},Mahulot qabul qilingan narxi:{f},Mahsulot donasi yoki kilosini narxi:{r},Mahsulot sotilish narxi:{g}")
#                 t.write(f"Nomi: {b},\n Mahsulot kelgan Sanasi:{r},\n Yarog'lilik muddati: {c},\n Mahsulot donasi-blogi: {d},\nMahulot qabul qilingan narxi:{f},\nMahsulot donasi yoki kilosini narxi:{r},\nMahsulot sotilish narxi:{g}\n")
#                 print("\nMahsulot qoshildi:")
#                 print(f"Nomi: {b},\nMahsulot kelgan Sanasi:{r},\n Yarog'lilik muddati: {c}\nMahsulot donasi-blogi: {d},Mahulot qabul qilingan narxi:{f},Mahsulot donasi yoki kilosini narxi:{r},Mahsulot sotilish narxi:{g}")
#             else:
#                 print("Noto'g'ri ma'lumotlar!")

#         else:
#             print("Noto'g'ri tanlov!")
#             input("Qayta kritin:")

#     t.close()

# qoshish()
def birleshtir(*args):
    yeni_sozluk = {}
    for sozluk in args:
        yeni_sozluk.update(sozluk)
    return yeni_sozluk

d1 = {"a": 3, "b": 9}
d2 = {"c": 7, "d": 11}
d3 = {"e": 15, "f": 21}

birlesmis_sozluk = birleshtir(d1, d2, d3)
print(birlesmis_sozluk)

# Kullanıcıdan 3 değer alınması
deger1 = input("Birinci değeri girin: ")
deger2 = input("İkinci değeri girin: ")
deger3 = input("Üçüncü değeri girin: ")

# Değerlerin bir listeye kaydedilmesi
liste = [deger1, deger2, deger3]

# Liste elemanlarının bir küme oluşturularak çiftleştirilmesi
yeni_set = set(liste)

print("Oluşturulan küme:", yeni_set)
def set_isle(setim, deger):
    if deger in setim:
        setim.remove(deger)
    else:
        setim.add(deger)
    return setim

# Kullanıcıdan bir set ve bir değer alınması
setim = set(input("Bir set girin (örneğin, {1, 2, 3}): "))
deger = input("Bir değer girin: ")

# Kullanıcı girdilerinin uygun formata dönüştürülmesi (set ve değer)
setim = set(eval(setim))
deger = eval(deger)

# Fonksiyonun çağrılması ve sonucun yazdırılması
yenilenen_set = set_isle(setim, deger)
print("Yenilenen set:", yenilenen_set)
def ortalama_hesapla(sozluk):
    toplam = sum(sozluk.values())
    ortalama = toplam / len(sozluk)
    return ortalama

# Verilen Dictionary
fanning_baholari = {"matematika": 85, "fizika": 78, "kimyo": 90, "biologiya": 88, "tarix": 80}

# Ortalama hesaplanması
ortalama = ortalama_hesapla(fanning_baholari)

# Yeni anahtarın eklenmesi
fanning_baholari["avg"] = ortalama

print("Fanning baho Dictionarysi:", fanning_baholari)

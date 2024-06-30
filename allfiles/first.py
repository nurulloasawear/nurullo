# import cv2
# from pyzbar.pyzbar import decode

# def scan_qr_code():
#     # Kamera obyektini ochish
#     cap = cv2.VideoCapture(0)

#     while True:
#         # Kameradan rasm olish
#         ret, frame = cap.read()

#         # QR-kodlarni aniqlash
#         decoded_objects = decode(frame)

#         # Agar QR-kod topilgan bo'lsa
#         if decoded_objects:
#             for obj in decoded_objects:
#                 # QR-kodlarni joylashgan joylarini yasash
#                 points = obj.polygon

#                 # QR-kodning tekst ma'lumotini olish
#                 data = obj.data.decode('utf-8')
                
#                 # Ma'lumotlarni terminalga chiqarish
#                 print("QR-kod:", data)

#                 # QR-kodning joylashgan joylarini ko'rsatish
#                 for point in points:
#                     cv2.circle(frame, point, 10, (0, 0, 255), -1)

#             # Ekran bo'yicha chiqarish
#             cv2.imshow("QR-kod skanneri", frame)

#         # Ekran bosilganda chiqish
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Kamerani to'xtatish va ekranlarni yopish
#     cap.release()
#     cv2.destroyAllWindows()

# # Dasturni ishga tushirish
# if __name__ == "__main__":
#     scan_qr_code()

users = ["jasur","karim","nurullo", True]
emply=["bank"]
emply.insert(2,"bobur")

emply.extend(users)
users.append("nurulo")
print("bobur" in users)
print(users[2])
print(users.index(True))
print(users)
print(emply)
print(emply)

emply[3]="rahhim"
print(emply)
users[2:2] = emply
print(users)
users.remove("jasur")
print(users)
ochir = users.pop()
print(ochir)
print(users)
del users[2]
print(users)
users.clear()
print(users)
del users
# print(users)
num = [33,45,-6,0 ,607]
num.sort()
print(num)
num1= [33,45,-6,0 ,607]
num1.sort(reverse=True)
print(num1)
num1= [33,45,-6,0 ,607]
num1.sort(reverse=True)
print(num1)
 
my_tuple1 = tuple(["gafur",43,True])
my_tuple2_2 = ("Qolgan",12,False)
print(my_tuple1)
print(my_tuple2_2)
new_tuple = (5,5,5,5,10,4,5,8)
print(new_tuple.count(5))
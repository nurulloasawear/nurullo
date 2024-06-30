# import sqlite3
# conn = sqlite3.connect("tutorial.db") # tutorial.db nomli ma'lumotlar bazasini yaratish yoki ochish
# c = conn.cursor() # ma'lumotlar bazasi bilan ishlash uchun kursor yaratish

# class ota:
#     def __init__(self,name ,age):
#         self.name = name
#         self.age = age
        
    
# class bola(ota):
#     def __init__(self,name,age,number,region):
#         super().__init__(name,age)
#         self.number = number
#         self.region = region
    

# class nevara(bola):
#     def __init__(self,name,age,number,region,merrid,sun):
#         super().__init__(name,age,number,region)
#         self.merrid = merrid
#         self.sun = sun 
#     def bag(self):
#         return f"ismi:{self.name},yoshi:{self.age},telefon raqami:{self.number},region:{self.region},uylaganmi:{self.merrid},bolasi bormi:{self.sun}"   

    
 
# name = input("ism:")
# age = input("yoshi:")
# number = input("telefon raqami:")
# region = input("region:")
# merrid = input("uylanganmi:")
# sun = input("bolasi bormi:")

# tub = nevara(name,age,number,region,merrid,sun)
# c.execute("CREATE TABLE IF NOT EXISTS nevara (name, age, number, region, merrid, sun)") # nevara nomli jadval yaratish
# c.execute("INSERT INTO nevara VALUES (?,?,?,?,?,?)", (tub.name, tub.age, tub.number, tub.region, tub.merrid, tub.sun)) # obyekt ma'lumotlarini jadvalga qo'shish
# conn.commit() # o'zgarishlarni saqlash
# print(tub.bag())
new = [1,2,3,45,67,8]
def qarash(input,num):
    for  i in range(0,len(input)):
        if input[i]==num:
            return i
qarash(new,67)

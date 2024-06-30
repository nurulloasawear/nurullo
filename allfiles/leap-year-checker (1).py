# class Oyinchi:
#     def __init__(self, boyi ,eni, vazn ,sochi):
#         self.boyi = boyi
#         self.eni = eni
#         self.vazn = vazn
#         self.sochi = sochi

#     def korish(self):
#         print('Oyinchini Korish Boshladi!')
#     def ogahlantrish(self):
#         print('\nVahtingiz Kam qoldi!!')
#     def tugadi(self):
#         print('\n\nEtiboringiz uchun Raxmat!!!')

# u = Oyinchi(185,50,95,"qora")
# print(u.boyi)

 
# u.korish()
# u.ogahlantrish()
# u.tugadi()

# def nurullo():
 
#     print("Oneni Omi!!!")
#     # return nurullo

# my = nurullo()
# print(my)
# x = "nurullo"
# c = 25  
# print("%s is %d years old" % (x,c))
# class Par1:
#     def Nurullo(self):
#         return Par1
# class Par2:
#     def Abduvalli(self):
#         return Par2
# class child:
#     def chil(self):
#         return Par1,Par2

# def nurullo():
#     print("nurullo")
# n = nurullo()
# print(n )                    
# class OOP:
#     c = "Nurullo"
# p1 = OOP()
# print(p1.c) 
# import abc   
# class Person:
#     def __init__(my,name ,age):
#         my.name = name
#         my.age = age

#     # def __str__(self):
#     #     return f"{self.name}({self.age})"    
#     def n(abc):
#         print("Hello My name is\t"+abc.name)
# p1 = Person("John",36)
# p1.n()
# print(p1.age)    
# import random
 
# class Dondonziki:
#         def don(self,oyinchin,comp_hisob) :
#             self.oyinchin =oyinchin
#             self.bot = bot
# for x in p1.random():
#     oyinchi = input("Tosh, Qog'oz, Qaychi?\n").capitalize()
#     computer = random.choice(tanlov)
#     if oyinchi == computer:
#         print("Durrang!")
#         comp_hisob+=1
#         oyinchi_hisob+=1
#     elif oyinchi == "Tosh":
#         if computer == "Qog'oz":
#             print("Yutqazdingiz!", computer, " yopdi ", oyinchi, "ni")
#             comp_hisob+=1
#         else:
#             print("Yutdingiz!", oyinchi, " ustun ", computer, "dan")
#             oyinchi_hisob+=1
#     elif oyinchi == "Qog'oz":
#         if computer == "Qaychi":
#             print("Yutqazdingiz!", computer, " kesdi ", oyinchi, "ni")
#             comp_hisob+=1
#         else:
#             print("Yutdingiz!", oyinchi, "yopib qo'ydi ", computer, "ni")
#             oyinchi_hisob+=1
#     elif oyinchi == "Qaychi":
#         if computer == "Tosh":
# #             print("Yutqazdingiz...", computer, " sindirdi ", oyinchi, "ni")
#             comp_hisob+=1
#         else:
#             print("Yutdingiz!", oyinchi, "kesdi", computer, "ni")
#             oyinchi_hisob+=1
#     elif oyinchi=='Tugat' or oyinchi=="Stop":
#         print("Yakuniy hisob: \n")
#         print(f"Computer:{comp_hisob}")
#         print(f"O'yinchi:{oyinchi_hisob}")
#         if comp_hisob>oyinchi_hisob:
#             print("Kompyuter yutdi! Afsus... Yana urinib ko'ring.")
#         elif comp_hisob<oyinchi_hisob:
#             print("O'yinchi g'olib! Tabriklaymiz!")
#         else:
#             print("Durrang!")
#         break

                         



# p1 = Dondonziki("Tosh","qaychi","qogoz")
# comp_hisob = 0
# oyinchi_hisob = 0
# print(p1)
# import random

# class Dondonziki:
#     def __init__(self, oyinchi, qogoz, qaychi):
#         self.oyinchi = oyinchi
#         self.tanlov = [qogoz, "Qog'oz", qaychi]

#     def don(self, comp_hisob, oyinchi_hisob):
#         while True:
#             oyinchi = input("Tosh, Qog'oz, Qaychi?\n").capitalize()
#             computer = random.choice(self.tanlov)
            
#             if oyinchi == computer:
#                 print("Durrang!")
#                 comp_hisob += 1
#                 oyinchi_hisob += 1
#             elif oyinchi == "Tosh":
#                 if computer == "Qog'oz":
#                     print("Yutqazdingiz!", computer, " yopdi ", oyinchi, "ni")
#                     comp_hisob += 1
#                 else:
#                     print("Yutdingiz!", oyinchi, " ustun ", computer, "dan")
#                     oyinchi_hisob += 1
#             elif oyinchi == "Qog'oz":
#                 if computer == "Qaychi":
#                     print("Yutqazdingiz!", computer, " kesdi ", oyinchi, "ni")
#                     comp_hisob += 1
#                 else:
#                     print("Yutdingiz!", oyinchi, "yopib qo'ydi ", computer, "ni")
#                     oyinchi_hisob += 1
#             elif oyinchi == "Qaychi":
#                 if computer == "Tosh":
#                     print("Yutqazdingiz...", computer, " sindirdi ", oyinchi, "ni")
#                     comp_hisob += 1
#                 else:
#                     print("Yutdingiz!", oyinchi, "kesdi", computer, "ni")
#                     oyinchi_hisob += 1
#             elif oyinchi == 'Tugat' or oyinchi == "Stop":
#                 print("Yakuniy hisob: \n")
#                 print(f"Computer:{comp_hisob}")
#                 print(f"O'yinchi:{oyinchi_hisob}")
#                 if comp_hisob > oyinchi_hisob:
#                     print("Kompyuter yutdi! Afsus... Yana urinib ko'ring.")
#                 elif comp_hisob < oyinchi_hisob:
#                     print("O'yinchi g'olib! Tabriklaymiz!")
#                 else:
#                     print("Durrang!")
#                 break

# p1 = Dondonziki("Tosh", "qogoz", "qaychi")
# comp_hisob = 0
# oyinchi_hisob = 0
# p1.don(comp_hisob, oyinchi_hisob)

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def print_ingredients(self):
        print(f"Список продуктов для приготовления блюда '{self.name}':")
        for i, ingredient in enu e(self.ingredients):
            print(f"{i+1}. {ingredient}")

    def cook(self):
        print(f"Вы приготовили блюдо '{self.name}'! Приятного аппетита!")

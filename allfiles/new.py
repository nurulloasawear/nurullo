# a = [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# a = [ x for x in a if x not in [7, 13]]
# for i in a:
#     print(i)
# #2-task
# def hisoblash(s):
#     takrorlar = {}
#     for harf in s:
#         if harf in takrorlar:
#             takrorlar[harf] += 1
#         else:
#             takrorlar[harf] = 1
#     return
#      takrorlar

# s = input("String kiriting: ")
# takrorlar = hisoblash(s)
# print(takrorlar)
# 3-part
a = [4,8,6,2]
def newlist(a):
	d = []
	c = sum(a) / len(a)
	for x  in a :
		if x >= c:
			 d.append(x)
	return d
b =  newlist(a)
print('katta list da:',b)
#4-part
# def asd():
# 	c = {"Mahsulot":""}
# 	x = input("add product:")
# 	x.append(c)
# 	print(x)
# 	d =input("sale product:")
# 		if d  == cs:
# 		d.remove(c)
# 		print("Sotilgan Mahsulot",d)
# asd()		
# def asd():
# 	while True:
#     		c = {"Mahsulot": ""}
#     		x = [c]  # Ro'yxat ichida lug'at
#     		product_name = input("Mahsulotni qo'shing: ")
#     		c["Mahsulot"] = product_name
#     		print(x)
#     		sale_product = input("Mahsulotni sotib olish: ")
#     		if sale_product == c["Mahsulot"]:
#      		   x.remove(c)
#       		   print("Sotilgan Mahsulot", c)
        
# asd()

def manage_inventory(inventory):
    # Foydalanuvchidan yangi mahsulotlar va ularning miqdorini so'raymiz
    new_items = input("Yangi mahsulotlar va ularning miqdorini kiriting (mahsulot miqdori bilan ajrating): ").split()
    
    # Yangi mahsulotlarni inventoriyaga qo'shamiz
    for i in range(0, len(new_items), 2):
        product = new_items[i]
        quantity = int(new_items[i+1])
        if product in inventory:
            inventory[product] += quantity
        else:
            inventory[product] = quantity
    
    # Sotilgan mahsulotlarni inventoriyadan o'chiramiz
    sold_items = input("Sotilgan mahsulotlarni kiriting (mahsulot nomi bilan ajrating): ").split()
    for item in sold_items:
        if item in inventory:
            sold_quantity = int(input(f"Mahsulot {item} necha miqdorda sotilgan? "))
            if sold_quantity >= inventory[item]:
                del inventory[item]
            else:
                inventory[item] -= sold_quantity
    
    print("Yangilangan inventoriya:", inventory)

# Test qilish uchun boshlang'ich inventoriya
inventory = {"olma": 10, "banan": 20, "anor": 15}

# inventoriyani boshqarish
manage_inventory(inventory)
	
	



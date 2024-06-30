# # # # import phonenumbers
# # # # import opencage
# # # # import folium
# # # # from myphone import number
# # # # from phonenumbers import geocoder

# # # # pepnumbers  = phonenumbers.parse(number)
# # # # location = geocoder.description_for_number(pepnumbers,"uz")
# # # # print(location)

# # # # from phonenumbers import carrier
# # # # service_pro = phonenumbers.parse(number)
# # # # print(carrier.name_for_number(service_pro,"uz"))

# # # # from opencage.geocoder import OpenCageGeocode
# # # # key = "afc9f767e8d14451b1bb2d893a521ec0"
# # # # geocoder = OpenCageGeocode(key)
# # # # query = str(location)
# # # # results = geocoder.geocode(query)
# # # # # print(results)
# # # # lat = results[0]["geometry"]["lat"]
# # # # lng = results[0]["geometry"]["lng"]
# # # # print(lat,lng)
# # # # myMap =  folium.Map(location=[lat,lng],zoom_start=9)
# # # # folium.Marker([lat,lng],popup=location).add_to(myMap)
# # # # myMap.save("mylacatiton.html")

# # # import phonenumbers
# # # from phonenumbers import geocoder, carrier
# # # from opencage.geocoder import OpenCageGeocode
# # # import folium

# # # # Assuming `number` is correctly defined in your `myphone` module
# # # from myphone import number

# # # # Parse the phone number
# # # pepnumbers = phonenumbers.parse(number)

# # # # Get location information
# # # location = geocoder.description_for_number(pepnumbers, "en")

# # # # Print location
# # # print("Location:", location)

# # # # Get carrier information
# # # service_provider = carrier.name_for_number(pepnumbers, "en")

# # # # Print carrier information
# # # print("Service Provider:", service_provider)

# # # # Initialize OpenCageGeocode with your API key
# # # key = "afc9f767e8d14451b1bb2d893a521ec0"
# # # geocoder = OpenCageGeocode(key)

# # # # Get geolocation coordinates
# # # query = str(location)
# # # results = geocoder.geocode(query)

# # # if results and len(results):
# # #     # Extract latitude and longitude
# # #     lat = results[1]["geometry"]["lat"]
# # #     lng = results[1]["geometry"]["lng"]

# # #     # Print latitude and longitude
# # #     print("Latitude:", lat)
# # #     print("Longitude:", lng)

# # #     # Create a map
# # #     myMap = folium.Map(location=[lat, lng], zoom_start=9)

# # #     # Add a marker for the location
# # #     folium.Marker([lat, lng], popup=location).add_to(myMap)

# # #     # Save the map to an HTML file
# # #     myMap.save("mylocation.html")
# # # else:
# # #     print("No results found for the given location query.")
# # #first-task
# # class Phone:
# #     def init(self, name, price, stock_quantity):
# #         self.name = name
# #         self.price = price
# #         self.stock_quantity = stock_quantity

# # def get_phones_with_price_higher_than(phones, price):
# #     return list(filter(lambda phone: phone.price > price, phones))

# # def get_out_of_stock_phones(phones):
# #     return list(filter(lambda phone: phone.stock_quantity == 0, phones))

# # def apply_new_year_discount(phones):
# #     for phone in phones:
# #         phone.price *= 0.85  # Apply 15% discount
# #     return phones

# # def calculate_total_cost(phones):
# #     return sum(phone.price * phone.stock_quantity for phone in phones)
# # ####2-ttask
# # from phone_store import *

# # def main_func():
# #     phones = [
# #         Phone('Phone 1', 1000, 5),
# #         Phone('Phone 2', 1500, 0),
# #         Phone('Phone 3', 800, 10),
# #         Phone('Phone 4', 1200, 2)
# #     ]

# #     phones_with_higher_price = get_phones_with_price_higher_than(phones, 1000)
# #     print('Phones with price higher than 1000:', phones_with_higher_price)

# #     out_of_stock_phones = get_out_of_stock_phones(phones)
# #     print('Out of stock phones:', out_of_stock_phones)

# #     phones_with_discount = apply_new_year_discount(phones)
# #     print('Phones with discount:', phones_with_discount)

# #     total_cost = calculate_total_cost(phones)
# #     print('Total cost of phones:', total_cost)

# # if name == "main":
# #     main_func()
# #     ###2-task
# #     # main.py

# # phones = [
# #     {"name": "Phone1", "price": 100, "stock_quantity": 5},
# #     {"name": "Phone2", "price": 200, "stock_quantity": 0},
# #     {"name": "Phone3", "price": 300, "stock_quantity": 10},
# #     {"name": "Phone4", "price": 400, "stock_quantity": 3},
# # ]

# # # Task 1
# # def find_higher_price_phones(price):
# #     return [phone["name"] for phone in phones if phone["price"] > price]

# # # Task 2
# # def find_out_of_stock_phones():
# #     return [phone["name"] for phone in phones if phone["stock_quantity"] == 0]

# # # Task 3
# # def calculate_discount_price():
# #     discount = 0.15
# #     return {phone["name"]: phone["price"] * (1 - discount) for phone in phones}

# # # Task 4
# # def calculate_total_price():
# #     return sum([phone["price"] for phone in phones])

# # def main_func():
# #     # Task 1
# #     user_input_price = float(input("Iltimos, kiriting: "))
# #     higher_price_phones = find_higher_price_phones(user_input_price)
# #     print("Higher Price Phones:", higher_price_phones)

# #     # Task 2
# #     out_of_stock_phones = find_out_of_stock_phones()
# #     if out_of_stock_phones:
# #         print("Out of Stock Phones:", out_of_stock_phones)
# #     else:
# #         print("ALL PHONES ARE IN STOCK")

# #     # Task 3
# #     discount_price = calculate_discount_price()
# #     print("Discount Price for New Year:", discount_price)

# #     # Task 4
# #     total_price = calculate_total_price()
# #     print("Total Price of all Phones:", total_price)

# # if __name__ == "__main__":
# #     main_func()

# # #3-task
# # def calculate_average(*args):
# #     if not args:
# #         return None
# #     total = sum(args)
# #     average = total / len(args)
# #     return total, average

# # # Test
# # print(calculate_average(1, 2, 3, 4, 5))  # Output: (15, 3.0)
# # print(calculate_average(10, 20, 30))     # Output: (60, 20.0)
# # print(calculate_average())               # Output: None
# # #4-task
# # def process_numbers(numbers):
# #     squared_list = [num ** 2 for num in numbers]
# #     even_list = [num for num in numbers if num % 2 == 0]
# #     odd_list = [num for num in numbers if num % 2 != 0]
# #     return squared_list, even_list, odd_list

# # numbers = [5, 9, 13, 0, 1, 7, 21, 25, 3]

# # squared, even, odd = process_numbers(numbers)

# # print("Squared elements list:", squared)
# # print("Even numbers list:", even)
# # print("Odd numbers list:", odd)

# # def calcute(**args):
# #     if len(args) == 0:
# #         return None
# #     aum = sum(args)
# #     a = aum / len(args)
# #     return (aum,a)
# # r1,r2 = calcute(1,2,3,4,5)
# # r3,r4 = ca
# import socket
# import subprocess
# import sys
# from datetime import datetime
# subprocess.call('clear',shell=True)
# remoteServer = input("ip:")
# remoteServerIP = socket.gethostbyname(remoteServer)

# print("-"*60)
# print("Iltmos kuting!")
# print("-"*60)
# t1= datetime.now()

# try:
#     for port in range(1,1025):
#         sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#         result = sock.connect_ex((remoteServerIP,port)) # Bu yerda ',' belgisi kerak, chunki bu ikkita argument.
#         if result == 0:
#             print("port {}".format(port)) # Bu yerda port raqamini chiqarish kerak.
#         sock.close()
# except KeyboardInterrupt:
#     print('You pressed Ctrl+c')        
#     sys.exit()
# except socket.gaierror:
#     print('hostname could not be resolved.Exiting')  
#     sys.exit()
# except socket.error:
#     print('Couldnt connect to server')     
#     sys.exit()   
# t2 = datetime.now()
# total = t2 -t1
# print("Scanning  Complete in",total)
# import os
# os.system("color a")
# print("                                                          _____")
# print(" \t                                         ________|chose|___          ")
# print("    \t  \t                                    1.|login/sign'up   |.2|          ")
# a = input("                                               chosing:")

# if  a == "1":
#     print("\n\n\t                                      please enterance  ")
#     c = input("                                       login:")
#     b = input("                                       password:")
#     print("connecting server....../")
#     os.system("ping 8.8.8.8")
#     print("\n\nconnecting server....../...../")
#     os.system("ping 8.8.8.8")
#     print("\n\nconnecting server....../...../..../.../../")
#     os.system("ping 8.8.8.8")
#     print("\n\nconnecting server....../...../..../.../../")
#     os.system("ping 8.8.8.8")
#     print("\n\nconnecting server....../...../..../.../../")
#     os.system("ping 8.8.8.8")
#     print("\n\nconnecting server....../...../..../.../../")
#     os.system("ping 8.8.8.8")
#     print("\n\nconnecting server....../...../..../.../../")
#     os.system("ping 8.8.8.8")
#     print("\n\nconnecting server....../...../..../.../../")
#     os.system("ping 8.8.8.8")
#     print("\n\nconnecting server....../...../..../.../../")

#     os.system("ping 8.8.8.8")
#     print("\n\nconnecting server....../")
#     os.system("ping 8.8.8.8")
#     print("\n\nconnecting server....../...../")
#     os.system("ping 8.8.8.8")
#     print("\n\nconnecting server....../...../..../.../../")
#     os.system("ping 8.8.8.8")
#     print("\n\nconnecting server....../...../..../.../../")
#     os.system("ping 8.8.8.8")
#     print("\n\nconnecting server....../...../..../.../../")
#     os.system("ping 8.8.8.8")
#     print("\n\nconnecting server....../...../..../.../../")
#     os.system("ping 8.8.8.8")
#     if c == "nurullo" and b == "nurullo2@2":
#         print("you can doit!")
#         os.system("telnet")
#     else:
#         print("good by!")    
# else:
#     print("good by!")

import os

def connect_to_server():
    print("connecting server....../")
    os.system("ping 8.8.8.8")
    print("\n\nconnecting server....../...../")
    os.system("ping 8.8.8.8")
    print("\n\nconnecting server....../...../..../.../../")
    os.system("ping 8.8.8.8")
    print("\n\nconnecting server....../...../..../.../../")
    os.system("ping 8.8.8.8")
    print("\n\nconnecting server....../...../..../.../../")
    os.system("ping 8.8.8.8")

def login():
    c = input("login: ")
    b = input("password: ")
    if c == "nurullo" and b == "nurullo2@2":
        print("You can do it!")
        os.system("telnet")
    else:
        print("Goodbye!")
        os.system("Exit   ")

def main():
    os.system("color a")
    print("                                                          _____")
    print(" \t                                         ________|chose|___          ")
    print("    \t  \t                                    1.|login/sign'up   |.2|          ")
    a = input("                                               choosing: ")

    if a == "1":
        print("\n\n\t                                      please enterance  ")
        login()
        connect_to_server()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()

    
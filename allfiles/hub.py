# import tkinter as tk

# def qoshish():
#     i = []
#     p = 0
#     t = open("Malumot.txt", "a")
#     y = open("sotish.txt", "a")
#     v = open("Kunlik Savdo Hisoboti.txt", "a")

#     def sell_item():
#         nonlocal p
#         s = entry_sell.get()
#         for item in i:
#             if s in item:
#                 item_str = item.split("Mahsulot sotilish narxi:")[1].strip()
#                 item_str = f"Sotildi:{s},\tNarxi:{item_str}"
#                 y.write(item_str + "\n")
#                 p += int(''.join(filter(str.isdigit, item_str.split("Narxi:")[1].strip())))
#                 label_result.config(text=f"Sotilgan narxi summasini: {item_str}")
#                 break
#         else:
#             label_result.config(text=f"{s} ro'yxatda mavjud emas.")

#     def calculate_total_sales():
#         ns = int(entry_ns.get())
#         nd = int(entry_nd.get())
#         nf = int(entry_nf.get())
#         gf = entry_gf.get()
#         df = ns + nd + nf + p + p
#         gf_str = f"Bugungi sana:{gf}, Shu kun ichida - Umumiy Bolgan Savdo:{df}"
#         v.write(gf_str + "\n")
#         label_result.config(text=gf_str)

#     def search_item():
#         s = entry_search.get()
#         if any(s in item for item in i):
#             label_result.config(text=f"{s} ro'yxatda mavjud.")
#         else:
#             label_result.config(text=f"{s} ro'yxatda mavjud emas.")

#     def calculate_profit():
#         g = int(entry_profit.get())
#         for item in i:
#             p += int(item.split("Kegan Mahsulotni umumiy % qoyilgandgi  umum narxi:")[1].strip())
#         p += g
#         label_result.config(text=f"Astatkani summasini: {p}")

#     def calculate_expenses():
#         d = int(entry_expenses.get())
#         f = d - p
#         p -= d
#         label_result.config(text=f"Bajarildi:{d}\nQolgan holati:{p}")

#     def add_item():
#         b = entry_name.get()
#         r = entry_date.get()
#         c = entry_duration.get()
#         d = entry_blog.get()
#         f = entry_initial_price.get()
#         h = entry_percentage.get()
#         r = entry_price.get()
#         g = int(entry_sell_price.get())

#         if b != "" and c != "" and d != "":
#             item_str = f"Nomi: {b},\nMahsulot kelgan Sanasi:{r},\nYarog'lilik muddati: {c},\nMahsulot donasi-blogi: {d},\nMahulot qabul qilingan narxi:{f},\nMahsulot donasi yoki kilosini narxi:{r},\nMahsulot sotilish narxi:{g},\nKegan Mahsulotni umumiy % qoyilgandgi  umum narxi:{h}"
#             i.append(item_str)
#             t.write(item_str + "\n")
#             label_result.config(text="\nMahsulot qo'shildi:\n" + item_str)
#         else:
#             label_result.config(text="Noto'g'ri ma'lumotlar!")

#     root = tk.Tk()
#     root.title("Savdo Hisoblash")

#     # Create and place Entry widgets and Labels for user input and output
#     entry_sell = tk.Entry(root)
#     entry_ns = tk.Entry(root)
#     entry_nd = tk.Entry(root)
#     entry_nf = tk.Entry(root)
#     entry_gf = tk.Entry(root)
#     entry_search = tk.Entry(root)
#     entry_profit = tk.Entry(root)
#     entry_expenses = tk.Entry(root)
#     entry_name = tk.Entry(root)
#     entry_date = tk.Entry(root)
#     entry_duration = tk.Entry(root)
#     entry_blog = tk.Entry(root)
#     entry_initial_price = tk.Entry(root)
#     entry_percentage = tk.Entry(root)
#     entry_price = tk.Entry(root)
#     entry_sell_price = tk.Entry(root)

#     label_result = tk.Label(root, text="Result will be displayed here")

#     button_sell = tk.Button(root, text="Sell Item", command=sell_item)
#     button_calculate_total_sales = tk.Button(root, text="Calculate Total Sales", command=calculate_total_sales)
#     button_search_item = tk.Button(root, text="Search Item", command=search_item)
#     button_calculate_profit = tk.Button(root, text="Calculate Profit", command=calculate_profit)
#     button_calculate_expenses = tk.Button(root, text="Calculate Expenses", command=calculate_expenses)
#     button_add_item = tk.Button(root, text="Add Item", command=add_item)

#     # Place the widgets using grid or pack as per your design
#     entry_sell.grid(row=0, column=1)
#     entry_ns.grid(row=1, column=1)
#     entry_nd.grid(row=2, column=1)
#     entry_nf.grid(row=3, column=1)
#     entry_gf.grid(row=4, column=1)
#     entry_search.grid(row=5, column=1)
#     entry_profit.grid(row=6, column=1)
#     entry_expenses.grid(row=7, column=1)
#     entry_name.grid(row=8, column=1)
#     entry_date.grid(row=9, column=1)
#     entry_duration.grid(row=10, column=1)
#     entry_blog.grid(row=11, column=1)
#     entry_initial_price.grid(row=12, column=1)
#     entry_percentage.grid(row=13, column=1)
#     entry_price.grid(row=14, column=1)
#     entry_sell_price.grid(row=15, column=1)

#     label_result.grid(row=16, column=0, columnspan=2)

#     button_sell.grid(row=0, column=2)
#     button_calculate_total_sales.grid(row=1, column=2)
#     button_search_item.grid(row=2, column=2)
#     button_calculate_profit.grid(row=3, column=2)
#     button_calculate_expenses.grid(row=4, column=2)
#     button_add_item.grid(row=5, column=2)

#     root.mainloop()

#     t.close()

# qoshish()
import random
while True:
    a = {'salom':['Assalomu alaykum','Qaleysiz','nima-gap!']}
    b = input("sorov:")
    if b in a:
        # replay = a.random.choices()
        # print(replay)
        print('Assalomu alaykum')
    elif b  == 'saloms' :
        print('qaleysiz!')   

    else:
        print('sizni chunmadm!zr')     

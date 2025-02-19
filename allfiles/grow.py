import tkinter as tk
from tkinter import simpledialog

def qoshish():
    i = []

    def display_items():
        result_text.delete(1.0, tk.END)
        for item in i:
            result_text.insert(tk.END, item + "\n")

    def search_item():
        search_text = simpledialog.askstring("Qidirish", "Qidirayotgan narsangizni kriting:")
        if any(search_text in item for item in i):
            result_text.insert(tk.END, f"{search_text} ro'yxatda mavjud.\n")
        else:
            result_text.insert(tk.END, f"{search_text} ro'yxatda mavjud emas.\n")

    def calculate_income():
        global p
        income_text = simpledialog.askinteger("Prihod", "Qancha prihodni aniqlamoqchisiz:")
        p = 0
        for x in i:
            p += int(x.split("Mahsulot sotilish narxi:")[1].strip())
        p += income_text
        result_text.insert(tk.END, f"Astatkani summasini: {p}\n")

    def calculate_expenses():
        global p
        expenses_text = simpledialog.askinteger("Rasxod", "Qancha arymoqchi bolgan summani ktring:")
        result_text.insert(tk.END, f"Bajarildi: {expenses_text}\n")
        result_text.insert(tk.END, f"Qolgan holati: {p}\n")

    def add_item():
        b = simpledialog.askstring("Yangi mahsulot", "Mahsulot nomi:")
        r = simpledialog.askstring("Yangi mahsulot", "Mahsulotlarning Kelgan Sanasi (yyyy.mm.dd):")
        c = simpledialog.askstring("Yangi mahsulot", "Mahsulot yaroqliligi muddati (yyyy.mm.dd):")
        d = simpledialog.askstring("Yangi mahsulot", "Mahsulot donasi-blogi (blog db yoki dona db):")
        f = simpledialog.askstring("Yangi mahsulot", "Mahsulot qabul qilingan narxi:")
        r = simpledialog.askstring("Yangi mahsulot", "Mahsulot donasi yoki kilosini narxi:")
        g = simpledialog.askinteger("Yangi mahsulot", "Mahsulot sotilish narxi:")

        if b != "" and c != "" and d != "":
            item_str = f"Nomi: {b},\nMahsulot kelgan Sanasi:{r},\nYarog'lilik muddati: {c},\nMahsulot donasi-blogi: {d},\nMahulot qabul qilingan narxi:{f},\nMahsulot donasi yoki kilosini narxi:{r},\nMahsulot sotilish narxi:{g}"
            i.append(item_str)
            result_text.insert(tk.END, "\nMahsulot qo'shildi:\n")
            result_text.insert(tk.END, item_str + "\n")
        else:
            result_text.insert(tk.END, "Noto'g'ri ma'lumotlar!\n")

    def on_button_click():
        result_text.delete(1.0, tk.END)
        action = option_var.get()
        if action == "1":
            add_item()
        elif action == "2":
            display_items()
        elif action == "3":
            search_item()
        elif action == "4":
            calculate_income()
        elif action == "5":
            calculate_expenses()

    root = tk.Tk()
    root.title("Mahsulotlar Bazasi")

    option_var = tk.StringVar()
    option_var.set("1")  # default option

    option_menu = tk.OptionMenu(root, option_var, "1", "2", "3", "4", "5")
    option_menu.pack()

    button = tk.Button(root, text="Bajarish", command=on_button_click)
    button.pack()

    result_text = tk.Text(root, height=10, width=50)
    result_text.pack()

    root.mainloop()

qoshish()


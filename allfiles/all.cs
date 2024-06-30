using System;
using System.Collections.Generic;

class Mahsulot {
    public string nomi;
    public double narxi;
    public int miqdori;

    public Mahsulot(string nomi, double narxi, int miqdori) {
        this.nomi = nomi;
        this.narxi = narxi;
        this.miqdori = miqdori;
    }
}

class Ombor {
    public List<Mahsulot> mahsulotlar = new List<Mahsulot>();

    public void MahsulotQo'shish(Mahsulot mahsulot) {
        mahsulotlar.Add(mahsulot);
        Console.WriteLine($"{mahsulot.nomi} mahsuloti omborga qo'shildi.");
    }

    public Mahsulot MahsulotQidirish(string nomi) {
        foreach (Mahsulot mahsulot in mahsulotlar) {
            if (mahsulot.nomi == nomi) {
                return mahsulot;
            }
        }
        return null;
    }

    public void MahsulotlarRo'yhati() {
        Console.WriteLine("Ombordagi mahsulotlar:");
        foreach (Mahsulot mahsulot in mahsulotlar) {
            Console.WriteLine($"{mahsulot.nomi} - {mahsulot.narxi} so'm, qolgan miqdori: {mahsulot.miqdori}");
        }
    }

    public void QolmaganMahsulotlar() {
        Console.WriteLine("Qolmagan mahsulotlar ro'yhati:");
        bool qolmaganMavjud = false;
        foreach (Mahsulot mahsulot in mahsulotlar) {
            if (mahsulot.miqdori == 0) {
                qolmaganMavjud = true;
                Console.WriteLine($"{mahsulot.nomi} - {mahsulot.narxi} so'm");
            }
        }
        if (!qolmaganMavjud) {
            Console.WriteLine("Omborda qolmagan mahsulotlar yo'q");
        }
    }

    public void MahsulotniUpdateQilish(string nomi, double yangiNarx, int yangiMiqdori) {
        Mahsulot mahsulot = MahsulotQidirish(nomi);
        if (mahsulot != null) {
            mahsulot.narxi = yangiNarx;
            mahsulot.miqdori = yangiMiqdori;
            Console.WriteLine($"{mahsulot.nomi} mahsuloti muvaffaqiyatli yangilandi.");
        }
        else {
            Console.WriteLine("Mahsulot topilmadi.");
        }
    }
}

class Program {
    static void Main(string[] args) {
        Ombor ombor = new Ombor();

        while (true) {
            Console.WriteLine("\nMahsulotlar ombori");
            Console.WriteLine("1. Mahsulot qo'shish");
            Console.WriteLine("2. Mahsulot qidirish");
            Console.WriteLine("3. Mahsulotlar ro'yhatini ko'rish");
            Console.WriteLine("4. Qolmagan mahsulotlar ro'yhatini ko'rish");
            Console.WriteLine("5. Mahsulotni yangilash");
            Console.WriteLine("6. Chiqish");

            Console.Write("Tanlang: ");
            string tanlov = Console.ReadLine();

            if (tanlov == "1") {
                Console.Write("Mahsulot nomini kiriting: ");
                string nomi = Console.ReadLine();
                Console.Write("Mahsulot narxini kiriting: ");
                double narxi = double.Parse(Console.ReadLine());
                Console.Write("Mahsulot miqdorini kiriting: ");
                int miqdori = int.Parse(Console.ReadLine());
                Mahsulot mahsulot = new Mahsulot(nomi, narxi, miqdori);
                ombor.MahsulotQo'shish(mahsulot);
            }
            else if (tanlov == "2") {
                Console.Write("Qidirilayotgan mahsulot nomini kiriting: ");
                string nomi = Console.ReadLine();
                Mahsulot mahsulot = ombor.MahsulotQidirish(nomi);
                if (mahsulot != null) {
                    Console.WriteLine($"{mahsulot.nomi} - {mahsulot.narxi} so'm, qolgan miqdori: {mahsulot.miqdori}");
                }
                else {
                    Console.WriteLine("Mahsulot topilmadi.");
                }
            }
            else if (tanlov == "3") {
                ombor.MahsulotlarRo'yhati();
            }
            else if (tanlov == "4") {
                ombor.QolmaganMahsulotlar();
            }
            else if (tanlov == "5") {
                Console.Write("Yangilayotgan mahsulot nomini kiriting: ");
                string nomi = Console.ReadLine();
                Console.Write("Yangi narxni kiriting: ");
                double yangiNarx = double.Parse(Console.ReadLine());
                Console.Write("Yangi miqdorni kiriting: ");
                int yangiMiqdori = int.Parse(Console.ReadLine());
                ombor.MahsulotniUpdateQilish(nomi, yangiNarx, yangiMiqdori);
            }
            else if (tanlov == "6") {
                Console.WriteLine("Dastur tugadi.");
                break;
            }
            else {
                Console.WriteLine("Noto'g'ri tanlov! Qaytadan urinib ko'ring.");
            }
        }
    }
}

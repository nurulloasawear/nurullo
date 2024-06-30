using System;
using System.Collections.Generic;

class Program
{
    static List<string> ombor = new List<string>();

    static void MahsulotQo'shish(string mahsulot)
    {
        ombor.Add(mahsulot);
        Console.WriteLine($"{mahsulot} omborga qo'shildi.");
    }

    static void MahsulotYangilash(string mahsulot, string yangiMaqsad)
    {
        if (ombor.Contains(mahsulot))
        {
            ombor.Remove(mahsulot);
            ombor.Add(yangiMaqsad);
            Console.WriteLine($"{mahsulot} mahsuloti {yangiMaqsad} ga o'zgartirildi.");
        }
        else
        {
            Console.WriteLine($"{mahsulot} mahsuloti topilmadi.");
        }
    }

    static void QolmaganMahsulotlarRo'yxatiniChiqarish()
    {
        Console.WriteLine("Qolmagan mahsulotlar:");
        foreach (string mahsulot in ombor)
        {
            Console.WriteLine(mahsulot);
        }
    }

    static void Main(string[] args)
    {
        MahsulotQo'shish("Olma");
        MahsulotQo'shish("Banan");
        MahsulotQo'shish("Anor");
        
        MahsulotYangilash("Olma", "Nok");
        
        QolmaganMahsulotlarRo'yxatiniChiqarish();
    }
}

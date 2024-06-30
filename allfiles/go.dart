bool isPalindrome(int number) {
  int temp = number; // asl sonni saqlab qo'yamiz
  int reverse = 0; // teskari sonni saqlash uchun o'zgaruvchi
  while (number > 0) { // son noldan katta bo'lguncha
    reverse = reverse * 10 + number % 10; // sonni teskari tartibda yozamiz
    number = number ~/ 10; // sonni 10 ga bo'lamiz
  }
  return temp == reverse; // asl son bilan teskari sonni solishtiramiz
}

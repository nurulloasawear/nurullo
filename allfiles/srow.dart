// import 'dart:math';
// import 'dart:io';

// void main() {
//   final random = Random();
//   final level = 2; // Darajani bu yerda o'zgartiring (0, 1, yoki 2)
//   final numQuestions = 10;
//   final maxNumber = 12;

//   int score = 0;

//   for (int i = 0; i < numQuestions; i++) {
//     int num1 = random.nextInt(maxNumber) + 1;
//     int num2 = random.nextInt(maxNumber) + 1;
//     String operator = getRandomOperator();

//     int result = calculateResult(num1, num2, operator);

//     print('Savol ${i + 1}: $num1 $operator $num2 nechchi?');

//     int answer = int.parse(stdin.readLineSync() ?? '');

//     if (answer == result) {
//       score++;
//       print('To‘g‘ri!');
//     } else {
//       print('Noto‘g‘ri. To‘g‘ri javob: $result');
//     }
//   }

//   print('Sizning ballaringiz: $score/$numQuestions');
// }

// String getRandomOperator() {
//   final operators = ['+', '-', '*', '/'];
//   final random = Random();
//   return operators[random.nextInt(operators.length)];
// }

// int calculateResult(int num1, int num2, String operator) {
//   switch (operator) {
//     case '+':
//       return num1 + num2;
//     case '-':
//       return num1 - num2;
//     case '*':
//       return num1 * num2;
//     case '/':
//       return num1 ~/ num2;
//     default:
//       throw Exception('Noto‘g‘ri amal');
//   }
// }
import 'aa.dart';
void main() {
  var sanya = Human(name: "Nurullo", age: 23, height: 190);
  print(sanya.age);
  sanya.grewUp(1);
  print(sanya.age);
}



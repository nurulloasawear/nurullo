// void main(){
//   final students = <String,double> {
//     "nurullo":5.5,
//     "ruhullo":6.5,
//     "nuridin":6.7,
//   };
//   print(students);
//   students["Sasha"]=5.0;
//   print(students);
//   students.remove("nuridin");
//   print(students);
//   students.addAll({
//    " katya":3.5,
//     "jenya":4.4,
//   });
//   print(students);
//    print(students.length);
//    print(students.keys.toList());
//   print(students.values.toList());

//     print(students.containsValue(4.4));
//     print(students.containsKey("nurullo"));
//   //  final a ={1:5.5};
//   //  final b  = {5.5:"Qaysi satr","Qaysi satr":5.6}
// }
import 'dart:io';

void main() {
  a();
  String ad = stdin.readLineSync();
  b();
  String bd = stdin.readLineSync();
  var oy = "husan";
  var by = "husa1n";
  
  if (ad == oy && bd == by) {
    print("Successfully Completed!");
  } else {
    print("xayr");
  }
}

void a() {
  print("login");
}

void b() {
  print("password:");
}

// // void main(){
// //   var  a = 2;
// //   var b  = 2;
// //   var rusult = a ;
// //   for (var i = a;i < b ;i++){
// //     // print("salom hammaga!"+i.toString());
// //     rusult = rusult * a;
// //   }
// //   print(rusult);
// // }
// // void main(){
// //   final students = ["nurullo","lera","Masha"];
// //   print(students);
// //   for (final student in students ){
// //     print(student);

// //   }
// //   for (var i =0; i < students.length; i++) {
// //     students[i] = students[i] + " " + i.toString();
// //   }
// //   print(students);

// //   while (students.isNotEmpty) {
// //     students.removeLast();
// //     print("#########");
    
// //   }
// //   print(students);
// // }
// import 'dart:ffi';

// void main(){
//   var a =1000;
//   do{
//     a =a + 1;
//     print(a);
//   }
//   while (a <= 1000);
  
// }
// import 'dart:convert';
// import 'dart:ffi';
import "dart:io";
// String qara(qara){
//   return "salom login krting: ";
  
// }
// void main(){
//   var a = "salom";
//  var b = "dunyo";
//   print(qara(""));
//   var d = stdin.readLineSync();
//   var f = stdin.readLineSync();
//   if (d == a){
//     if (f == b){
//       print("Salom hush kelibsiz!");
//     }
//     else{
//       print("xayr!");

//     }
//   }
//   else{
//     print("xayr!");
//   }



// }
// import "dart:io";
String sora(){
  return "amalni tanlang:";
 
}
String ga(){
  return "ikkinchi sonni  krting:";
}
int javob(int f ,int b){
  return f+b;

}
int javo(int f ,int b){
  return f-b;

}
int jav(int f ,int b){
  return f*b;

}
int javf(int f ,int b){
  return f ~/ b;

}
void main(){
  while (true) {
    print(sora());
   print("/+_*:");
  var a = stdin.readLineSync();
  print("1-chi son kriting:");
  var f = int.parse(stdin.readLineSync()!);
  print(ga());
  var b = int.parse(stdin.readLineSync()!);
  
  if (a == "+"){
    var c = javob(f,b);
  print("javob:$c");
  }
  else if (a == "*"){
     var c = jav(f,b);
  print("javob:$c");
  }
else if (a == "-"){
     var c = javo(f,b);
  print("javob:$c");
  }
else if (a == "/"){
     var c = javf(f,b);
  print("javob:$c");
  }
  else{
    print("notori tanlov!");
  }
  }
  
}
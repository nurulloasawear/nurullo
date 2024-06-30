

// void main(){
 
//  var result= square(7);
//  result = square(result); 
//  print(tori(result));
//  var result1= square(5,);
//  result1 = square(result1); 
//  print(tori(result1));
// }
// int square(int number ){

//    return number*number;
// }
// String tori(int number){
//   return "sizning javobingiz:$number";

// }
import 'dart:io';

String login(){
  return "login:";
}
String password(){
  return "password:";
}
String welcome(){
  return " welcome to office ser!";
}

void main(){
  var list =["nurullo","asadbe k","jasur","axror"];
  var pslist =["12345678i","87654321n","nurullo2@"];
  print(list[0]);
  print(list[1]);
  print(login());
  var a = stdin.readLineSync();
  print(password());
  var b = stdin.readLineSync();
  for (var i in list ) {
     
    
    if (a == i){
      print(welcome());
    break;
  
    }
 
  
}
else{
      print("by!");
    break;
  }
 for (var a in pslist ) {
     
    
    if (b == a){
      print(welcome());
     break;
  
    }
 else{
      print("by!");
    break;
  }
  
}}
import 'dart.io';
 String a(){
  print("login")
 }
 String b(){
  print("passsword:")
 }
void main(){
  a()
  <String> ad = stdin.readLineSync()
  b()
  <String> bd = stdin.readLineSync()
  var oy= <String> "husan"
  var by= <String> "husa1n"
  if (ad==oy){
    if (bd==by){
      print("sucsessfuly Completed!")
    }
     else{
    print("xayr")
  }
  }
  else{
    print("xayr")
  }
}

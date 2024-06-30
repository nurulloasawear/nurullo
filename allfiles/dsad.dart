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
  var list = ["nurullo", "asadbek", "jasur", "axror"];
  var pslist = ["12345678i", "87654321n", "nurullo2@"];
  print(list[0]);
  print(list[1]);
  print(login());
  var a = stdin.readLineSync();
  print(password());
  var b = stdin.readLineSync();
  var loggedIn = false; // Track if login successful
  for (var i in list) {
    if (a == i){
      loggedIn = true;
      print(welcome());
      break;
    }
  }
  if (!loggedIn) {
    print("by!");
  }

  var passwordCorrect = false; // Track if password correct
  for (var ps in pslist) {
    if (b == ps){
      passwordCorrect = true;
      print(welcome());
      break;
    }
  }
  if (!passwordCorrect) {
    print("by!");
  }
}

// class Account {
//   String _accountNumber; // maxfiy ma'lumot
//   double _balance; // maxfiy ma'lumot

//   // constructor
//    Account(String accountNumber, double balance) {
//     this._accountNumber = accountNumber;
//     this._balance = balance;
//   }

//   // ma'lumotlarni olish uchun metodlar
//   String getAccountNumber() {
//     return _accountNumber;
//   }

//   double getBalance() {
//     return _balance;
//   }

//   // ma'lumotlarni o'zgartirish uchun metodlar
//   void deposit(double amount) {
//     if (amount > 0) {
//       _balance += amount;
//     }
//   }

//   void withdraw(double amount) {
//     if (amount > 0 && amount <= _balance) {
//       _balance -= amount;
//     }
//   }
// }

// void main() {
//   // Account sinfi obyekti yaratish va ma'lumotlarni o'rnating
//   Account myAccount = Account('123456789', 1000.0);

//   // Ma'lumotlarga murojaat qilish
//   print('Hisob raqami: ${myAccount.getAccountNumber()}');
//   print('Balans: ${myAccount.getBalance()}');

//   // Balansga qo'shimcha mablag' qo'shish
//   myAccount.deposit(500.0);
//   print('Balans: ${myAccount.getBalance()}');

//   // Balansdan pul yechish
//   myAccount.withdraw(200.0);
//   print('Balans: ${myAccount.getBalance()}');
// }

// import 'dart:async';

// void main(){
//   try {
//     print(tasho(2,0));
//   print("xammasi yaxshi ukam!");
//   } on Exception  catch(e){
//     print("xato keti!"+e.toString());
//   }
//     on Error catch(e){
//       print(a()+e.toString());


//   }
//   finally{
//     print(a());
//   }
// }
// dynamic tasho(dynamic a, dynamic b){
//   // throw UnimplementedError();
//   if (b == 0){
//     throw Exception("bolbomid ukam!");
//   }
//   // return (a + b)*c*c*c;
//   return a / b;
//  }
//  String a(){
//   return "Qse boldi!\n";
//  }
// enum Pet { dog, cat, bird }

// void main() {
//   final nuri = Pet.bird;

 
//   print(nuri.index);

//   switch (nuri) {
//     case Pet.dog:
//       print("Nuri is a dog");
//       break;
//     case Pet.cat:
//       print("Nuri is a cat");
//       break;
//     case Pet.bird:
//       print("Nuri is a bird");
//       break;
//   }
// }
// import 'dart:ffi';

// void main() {
//  var Nurullo = Odam(ismi:"Nurullo",yoshi:19,boyi:180.2);
// // print(Nurullo);
//  var Muhlis  = Muhlisa(ismi:"Muhlisa",yoshi:18,boyi:174.2,feli:"yomon");
//  var povar  = Povar(ismi:"Muhlisa",yoshi:28,boyi:174.3,shef:"yoq");
//  var Mexan  = Mexanik(ismi:"Muhlisa",yoshi:28,boyi:174.4,ishi:"50/50");
//   Mexan.Togirla();
//   Muhlis.Oqish();
//   povar.pishir();
//   print(Nurullo.Olchov(Muhlis));
//  print(Muhlis);
//  print(povar);
//  print(Mexan);
//  print( Muhlis is Muhlisa? 'haa':'yoq');
  // print(Nurullo.Olchov(Muhlisa));s
  // print(Nurullo);
  // Nurullo.osish(2 );
  // print(Nurullo);
//  print(Nurullo.ismi);
//  print(Nurullo.boyi);
// //  Nurullo.yoshi =25;
//  print(Nurullo.yoshi);
// }
// class Odam{
//   final String ismi;
//    int  yoshi;
//   double boyi;
//   void  osish(int yil){
//     yoshi + yil;
//   }
//   Odam({
//     required this.ismi ,
//      required this.yoshi,
//     required this.boyi,
//   });
//   bool  Olchov(Odam Muhlis){
//     return this.boyi > Muhlis.boyi;
//   }
//  @override
//  String toString(){
//   return 'Mani ismim:$ismi,Mani yoshim:$yoshi,Mani boyim:$boyi';
//  }
// }
// class Muhlisa extends Odam{
//    String feli;
//   Muhlisa({
//     required super.ismi,
//     required super.yoshi,
//     required super.boyi,
//     required this.feli,
//   });


// void Oqish(){
//   print('Muhlis yaxshilab oqmoqda!');
// }

// @override
//   String toString(){
//     return super.toString() + ' ' + 'Uni feli:$feli';
//   }

// }
// class Mexanik extends Odam{
//    String ishi;
//   Mexanik({
//     required super.ismi,
//     required super.yoshi,
//     required super.boyi,
//     required this.ishi,
//   });
// void Togirla(){
//   print('Mexanik nimadurni tuzatmoqda!');
// }



// @override
//   String toString(){
//     return 'Mexanik' + super.toString() + ' ' + 'Uni ishi:$ishi';
//   }

// }
// class Povar extends Odam{
//    String shef;
//   Povar({
//     required super.ismi,
//     required super.yoshi,
//     required super.boyi,
//     required this.shef,
//   });


// void pishir(){
//   print('Povar kechlik Tayarlamoqda!');
  
// }

// @override
//   String toString(){
//     return 'Povar'  +  super.toString() + ' ' + 'Uni bosh  povar mi:$shef';
//   }

// }

// class Human {
//   final String name;
//   int _age; // Private field for age
//   double height;

//   Human({
//     required this.name,
//     required int age, // Renamed parameter
//     required this.height,
//   }) : _age = age; // Initialize _age with the value of the parameter age

//   void grewUp(int years) {
//     _age += years;
//   }

//   // Getter for age
//   int get age => _age;

//   // Setter for age

//   }
// void main(){
  // var  sanya = Human(name:"sasha",age:23,height:190);
  // print(sanya.name);
// print(Human.count);
//   var  sany = Human(name:"saha",age:23,height:190);
//   print(sany.name);
// print(Human.count);
// }
// class Human {
//   final String name;
// int age;
// double height;

//   Human ({
//     required this.name,
//   required this.age,
//   required this.height
//   }){
//     count +=1;
//   }

//   static int count = 0;
// }
// // 
// void main(){
//   final wolf  = Wolf(5);
//   final tiger = Tiger(7);
//   wolf.MakeSound();
//   tiger.sirk();
//   print(wolf.age);
// }
// abstract interface class Animal{
//   int get age;
//   void  MakeSound();
// }

// class  Wolf implements Animal{
//    int age ;
//   Wolf(this.age);
//   @override
//   void MakeSound(){
//     print("Auuuuuuuuuuu");
//   }
  
// }

// class  Tiger implements Animal{
//     int age ;
//   Tiger(this.age);
//     @override
//   void MakeSound(){
//       print("rrrrrrrr");
//   }
//   void sirk(){
//     print("sirka da oynid");
//   }
// }
// void main(){
//   final wolf  = Wolf(5);
//   final tiger = Tiger(7);
//   wolf.MakeSound();
//   tiger.sirk();
//   print(wolf.age);
// }
abstract interface class Animal{
  int get age;
  void  MakeSound();
}

class  Wolf implements Animal{
   int age ;
  Wolf(this.age);
  @override
  void MakeSound(){
    print("Auuuuuuuuuuu");
  }
  
}

class  Tiger implements Animal{
    int age ;
  Tiger(this.age);
    @override
  void MakeSound(){
      print("rrrrrrrr");
  }
  void sirk(){
    print("sirka da oynid");
  }
}

// Hayvon sinfi
// class Hayvon {
//   void yemek() {
//     print('Hayvon yemakda');
//   }
// }

// // It sinfi
// class It extends Hayvon {
//   @override
//   void yemek() {
//     print('It yutuqda');
//   }
// }

// // Qo'y sinfi
// class Qoy extends Hayvon {
//   @override
//   void yemek() {
//     print('Qo\'y ot yeydi');
//   }
// }

// // Polimorfizmni namoyish qilish
// void main() {
//   List<Hayvon> hayvonlar = [It(), Qoy()];

//   for (var hayvon in hayvonlar) {
//     hayvon.yemek();
//   }
// }
// // Abstrakt Shape sinfi
// // Abstract klass yaratish
// abstract class Hayvon {
//   // Abstract metod yaratish
//   void yemek();

//   // Odatiy metod yaratish
//   void uyqu() {
//     print('Hayvon uyqda');
//   }
// }

// // Abstract klassdan miras oluvchi klass
// class It extends Hayvon {
//   // Abstract metodni qayta yozish
//   @override
//   void yemek() {
//     print('It yutuqda');
//   }
// }

// void main() {
//   var it = It();
//   it.yemek(); // It yutuqda
//   it.uyqu();  // Hayvon uyqda
// }

// class Car {
//   String _make;
//   String _model; 
//   int _year; 

//   Car(this._make, this._model, this._year);

//   String get make => _make;
//   set make(String make) => _make = make;

//   String get model => _model;
//   set model(String model) => _model = model;

//   int get year => _year;
//   set year(int year) => _year = year;
// }

// void main() {
//   var myCar = Car("Toyota", "Corolla", 2020);
//   print(myCar.make); 
//  myCar.model = "Camry";
//   print(myCar.model); 
// }


class Dog {
  String _name;
  String _model;
  Int _age;
  Dog(this._name, this._model, this._age);

  String get _name => name;
  set name(String name) => _name = name;

  String get _model => model;
  set model(String model) => _model = model;

  Int get _age =>
  


}
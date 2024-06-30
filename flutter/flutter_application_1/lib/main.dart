import 'package:flutter/material.dart';

void main() {
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          backgroundColor: Color(0xFF17212b),
          title: Text(
            "Telegram",
            style: TextStyle(
              fontSize: 20,
              fontWeight: FontWeight.bold,
              color: Colors.white,
            ),
          ),
        ),
        body: Container(
          color: Color(0xFF17212b),
          child: Center(
            child: Container(
              width: 280,
              height: 400,
              padding: EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: Color(0xFF17212b),
                borderRadius: BorderRadius.circular(16),
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Image(image: AssetImage('assets/img1.svg'),width: 60,),
                  Text("\nPhone Number\n", style: TextStyle(color: Colors.white)),
                  Text("Please Type code for enterency \n\t\tThis page created by Nurullo!\n", style: TextStyle(color: Colors.white)),
                  SizedBox(height: 10), // Adding some space between text fields
                  TextField(
                    decoration: InputDecoration(
                      hintText: "Country \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t               >",
                      hintStyle: TextStyle(color: Colors.white),
                      border: OutlineInputBorder(borderSide: BorderSide(color: Colors.white)),
                      filled: true,
                      fillColor: Colors.white.withOpacity(0.1),
                      contentPadding: EdgeInsets.symmetric(vertical: 12, horizontal: 10),
                    ),
                    style: TextStyle(color: Colors.white),
                  ),
                  SizedBox(height: 10), // Adding some space between text fields
                  TextField(
                    decoration: InputDecoration(
                      hintText: "\t+\t\t\t\t\t\t\t\t\t\t |",
                      hintStyle: TextStyle(color: Colors.white),
                      border: OutlineInputBorder(borderSide: BorderSide(color: Colors.white)),
                      filled: true,
                      fillColor: Colors.white.withOpacity(0.1),
                      contentPadding: EdgeInsets.symmetric(vertical: 12, horizontal: 10),
                    ),
                    style: TextStyle(color: Colors.white),
                  ),
                  SizedBox(height: 20), // Adding some space below the text fields
                  ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(5),
                      ),
                      minimumSize: Size(200, 50),
                      // Set background color directly
                      backgroundColor: Color(0xFF2f6ea5),
                    ),
                    onPressed: () {},
                    child: Container(
                      width: double.infinity,
                      height: 50,
                      alignment: Alignment.center,
                      child: Text(
                        "Continue",
                        style: TextStyle(fontSize: 18,color: Colors.white),
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}

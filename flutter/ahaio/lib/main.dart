import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Mobile Game',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: LandingPage(),
    );
  }
}

class LandingPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Landing Page'),
      ),
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => InitiatePage()),
            );
          },
          child: Text("O'yinni boshlash"),
        ),
      ),
    );
  }
}

class InitiatePage extends StatefulWidget {
  @override
  _InitiatePageState createState() => _InitiatePageState();
}

class _InitiatePageState extends State<InitiatePage> {
  TextEditingController player1Controller = TextEditingController();
  TextEditingController player2Controller = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Initiate Page'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: player1Controller,
              decoration: InputDecoration(labelText: "Player 1 ismi"),
            ),
            TextField(
              controller: player2Controller,
              decoration: InputDecoration(labelText: "Player 2 ismi"),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => GamePage(
                      player1Name: player1Controller.text,
                      player2Name: player2Controller.text,
                    ),
                  ),
                );
              },
              child: Text("O'yin"),
            ),
          ],
        ),
      ),
    );
  }
}

class GamePage extends StatefulWidget {
  final String player1Name;
  final String player2Name;

  GamePage({required this.player1Name, required this.player2Name});

  @override
  _GamePageState createState() => _GamePageState();
}

class _GamePageState extends State<GamePage> {
  int min = 1;
  int max = 100;
  int correctNumber = 50; // Bu tasodifiy sonni keyinchalik dinamik qilish mumkin
  bool isPlayer1Turn = true;
  TextEditingController guessController = TextEditingController();

  void checkGuess() {
    int guess = int.parse(guessController.text);
    setState(() {
      if (guess < correctNumber) {
        min = guess + 1;
      } else if (guess > correctNumber) {
        max = guess - 1;
      } else {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => ResultPage(
              winner: isPlayer1Turn ? widget.player1Name : widget.player2Name,
            ),
          ),
        );
      }
      isPlayer1Turn = !isPlayer1Turn;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Game Page'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Text("Oraliq: $min -> $max"),
            TextField(
              controller: guessController,
              decoration: InputDecoration(labelText: "Taxminingizni kiriting"),
            ),
            SizedBox(height: 20),
            Text(
                "${isPlayer1Turn ? widget.player1Name : widget.player2Name} navbati"),
            ElevatedButton(
              onPressed: checkGuess,
              child: Text("Tekshirish"),
            ),
          ],
        ),
      ),
    );
  }
}

class ResultPage extends StatelessWidget {
  final String winner;

  ResultPage({required this.winner});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Result Page'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text("$winner g'olib bo'ldi!"),
            ElevatedButton(
              onPressed: () {
                Navigator.pushAndRemoveUntil(
                  context,
                  MaterialPageRoute(builder: (context) => GamePage(player1Name: '', player2Name: '')),
                  (route) => false,
                );
              },
              child: Text("Yana o'ynash"),
            ),
          ],
        ),
      ),
    );
  }
}

using System;

class Program {
  static void Main() {
    string a = Console.ReadLine();
    int b = int.Parse(a);

    if (b % 2 == 0) {
      Console.WriteLine("Bob");
    } else {
      Console.WriteLine("Alice");
    }
  }
}
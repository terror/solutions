using System;
using System.Linq;

class Program {
  static void Main() {
    int l = int.Parse(Console.ReadLine());
    int d = int.Parse(Console.ReadLine());
    int x = int.Parse(Console.ReadLine());

    for (int i = l; i <= d; i++) {
      if (i.ToString().Sum(c => c - '0') == x) {
        Console.WriteLine(i);
        break;
      }
    }

    for (int j = d; j >= l; j--) {

      if (j.ToString().Sum(c => c - '0') == x) {
        Console.WriteLine(j);
        break;
      }
    }
  }
}
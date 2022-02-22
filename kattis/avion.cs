using System;
using System.Collections.Generic;
using System.Linq;

namespace HelloWord {
class Program {
  static void Main() {
    int i = 1;
    List<int> linesWithFBI = new List<int>();

    while (i <= 5) {
      string line = Console.ReadLine();

      if (line.Contains("FBI")) {
        linesWithFBI.Add(i);
      }
      i++;
    }

    bool isEmpty = !linesWithFBI.Any();
    if (isEmpty) {
      Console.WriteLine("HE GOT AWAY!");
    } else {
      foreach (int num in linesWithFBI) {
        Console.Write(num + " ");
      }
    }
  }
}
}
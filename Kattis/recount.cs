using System;
using System.Collections.Generic;
using System.Linq;

namespace Solution {

class Program {
  static void Main(string[] args) {
    Dictionary<string, int> dict = new Dictionary<string, int>();

    int max = 0;
    string line;
    while ((line = Console.ReadLine()) != "***") {
      if (dict.ContainsKey(line)) {
        dict.TryGetValue(line, out int currentCount);
        dict[line] = currentCount + 1;
      } else {
        dict.Add(line, 1);
      }
      if (dict[line] > max) {
        max = dict[line];
      }
    }

    int count = 0;
    foreach (KeyValuePair<string, int> entry in dict) {
      if (entry.Value == max) {
        count++;
      }
    }

    if (count > 1) {
      Console.WriteLine("Runoff!");
    } else {
      Console.WriteLine(
          dict.Aggregate((x, y) => x.Value > y.Value ? x : y).Key);
    }
  }
}
}

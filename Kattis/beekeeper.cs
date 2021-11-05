using System;
using System.Collections.Generic;
using System.Linq;

namespace Solution {
class Program {
  static void Main(string[] args) {

    char[] vowels = { 'a', 'e', 'i', 'o', 'u', 'y' };
    Dictionary<string, int> dict = new Dictionary<string, int>();

    int n;
    while ((n = int.Parse(Console.ReadLine())) != 0) {
      int i = 0;
      while (i < n) {
        string word = Console.ReadLine();
        int j, k;
        int counter = 0;
        for (j = 0; j < word.Length; j++) {
          for (k = 0; k < vowels.Length; k++) {
            if (j <= word.Length - 2) {
              if (word[j] == vowels[k] && word[j + 1] == vowels[k]) {
                counter++;
              }
            }
          }
        }
        if (!dict.ContainsValue(counter)) {
          dict.Add(word, counter);
        }
        i++;
      }
      Console.WriteLine(
          dict.Aggregate((x, y) => x.Value > y.Value ? x : y).Key);
      dict.Clear();
    }
  }
}
}

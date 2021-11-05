using System;
using System.Text;

namespace Solution {
class Program {
  static void Main(string[] args) {
    char[] abc = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                   'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                   's', 't', 'u', 'v', 'w', 'x', 'y', 'z' };
    StringBuilder sb = new StringBuilder();
    int n = int.Parse(Console.ReadLine());
    int i = 0;

    while (i < n) {
      string line = Console.ReadLine().ToLower();

      foreach (char c in abc)
        if (!line.Contains(c))
          sb.Append(c);

      if (sb.Length != 0)
        Console.WriteLine("missing " + sb.ToString());
      else
        Console.WriteLine("pangram");

      sb.Clear();
      i++;
    }
  }
}
}

using System;

namespace Solution {
class Program {
  static void Main(string[] args) {
    int n = int.Parse(Console.ReadLine());
    int i = 0;
    int sum = 0;
    while (i < n) {
      string num = Console.ReadLine();
      string power = num.Substring(num.Length - 1);
      num = num.Substring(0, num.Length - 1);
      sum += (int)Math.Pow(Convert.ToDouble(num), Convert.ToDouble(power));
      i++;
    }

    Console.WriteLine(sum);
  }
}
}

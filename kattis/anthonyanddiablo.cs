using System;

namespace Solution {
class Program {
  static void Main(string[] args) {
    // input
    string input = Console.ReadLine();
    string[] nums = input.Split(' ');
    float a = float.Parse(nums[0]);
    float n = float.Parse(nums[1]);

    // circle check

    // compute radius C/2PI, n = c
    float radius = n / ((float)Math.PI * 2);

    // compute area pi r squared
    float area = (float)Math.PI * (float)Math.Pow(radius, 2);

    if (area >= a) {
      Console.WriteLine("Diablo is happy!");
    } else {
      Console.WriteLine("Need more materials!");
    }
  }
}
}
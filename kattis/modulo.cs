using System;
using System.Collections.Generic;
using System.Linq;

namespace HelloWord {
class Program {
  static void Main(string[] args) {
    List<int> nums = new List<int>();
    int i = 0;
    while (i < 10) {
      int input = int.Parse(Console.ReadLine());
      nums.Add(input % 42);
      i++;
    }

    Console.WriteLine(nums.Distinct().Count());
  }
}

}
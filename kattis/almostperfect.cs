using System;

namespace Solution {
class Program {
  static void Main(string[] args) {
    string n;
    while ((n = (Console.ReadLine())) != null) {
      int num = int.Parse(n);
      int sum = ComputeSum(num);
      Console.WriteLine(sum == num                ? num + " perfect"
                        : Math.Abs(sum - num) < 3 ? num + " almost perfect"
                                                  : num + " not perfect");
    }
  }

  static int ComputeSum(int num) {
    int sum = 1;

    double sqrt = Math.Sqrt(num);
    if ((int)sqrt == sqrt) {
      sum += (int)sqrt;
    }

    for (int j = 2; j < sqrt; j++) {
      if (num % j == 0) {
        sum += j + (num / j);
      }
    }

    return sum;
  }
}
}

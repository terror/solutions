using System;

class Program {
  static void Main() {
    int num = int.Parse(Console.ReadLine());

    int i = 0;
    while (i < num) {
      string line = Console.ReadLine();
      string[] split = line.Split(new char[] { ' ' }, StringSplitOptions.None);
      int a = int.Parse(split[0]);
      int b = int.Parse(split[1]);
      int c = int.Parse(split[2]);

      if (b > a && (b - c) > a) {
        Console.WriteLine("advertise");
      } else if ((b - c) == a) {
        Console.WriteLine("does not matter");
      } else {
        Console.WriteLine("do not advertise");
      }

      i++;
    }
  }
}
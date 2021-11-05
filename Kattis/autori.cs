using System;
using System.Text;

class Program {
  static void Main() {
    string a = Console.ReadLine();
    StringBuilder sb = new StringBuilder();

    for (int i = 0; i < a.Length; i++) {
      if (Char.IsUpper(a[i])) {
        sb.Append(a[i].ToString());
      }
    }

    Console.WriteLine(sb);
  }
}
using System;
using System.Linq;

namespace HelloWord
{
    class Program
    {
        static void Main(string[] args)
        {
            int val = int.Parse(Console.ReadLine());
            int binaryReverse = Convert.ToInt32(new String(Convert.ToString(val, 2).Reverse().ToArray()), 2);
            Console.WriteLine(binaryReverse);
        }
    }

}
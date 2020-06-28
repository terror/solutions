using System;
using System.Collections.Generic;
using System.Linq;

namespace Solution
{
    class Program
    {
        static void Main(string[] args)
        {

            int numBattles = int.Parse(Console.ReadLine());
            int i = 0;
            int counter = 0;

            while (i < numBattles)
            {
                string ab = Console.ReadLine();

                if (!ab.Contains("CD"))
                {
                    counter++;
                }

                i++;
            }

            Console.WriteLine(counter);
        }
    }

}
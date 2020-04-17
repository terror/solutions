using System;
using System.Collections.Generic;
using System.Linq;

namespace HelloWord
{
    class Program
    {
        static void Main()
        {
            string input = Console.ReadLine();
            string[] nums = input.Split(' ');
            int e = int.Parse(nums[0]);
            int f = int.Parse(nums[1]);
            int c = int.Parse(nums[2]);

            int empty = e + f;
            int total = 0;

            while (empty >= c)
            {
                empty -= c;
                total++;
                empty++;
            }

            Console.WriteLine(total);
        }
    }
}
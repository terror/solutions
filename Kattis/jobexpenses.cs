using System;
using System.Collections.Generic;
using System.Linq;

namespace Solution
{
    class Program
    {
        static void Main(string[] args)
        {

            int num = int.Parse(Console.ReadLine());
            int i;
            string expenses = Console.ReadLine();
            string[] nums = expenses.Split(' ');
            List<int> intnums = new List<int>();

            for (i = 0; i < num; i++)
            {
                intnums.Add(int.Parse(nums[i]));
            }

            int numExpenses = 0;

            for (int j = 0; j < intnums.Count; j++)
            {
                if (intnums[j] < 0)
                {
                    numExpenses += intnums[j];
                }
            }

            Console.WriteLine(Math.Abs(numExpenses));
        }

    }
}
using System;
using System.Collections.Generic;

namespace Solution
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            List<int> times = new List<int>();

            string input = Console.ReadLine();
            string[] nums = input.Split(' ');

            for (int i = 0; i < n; i++)
            {
                times.Add(int.Parse(nums[i]));
            }

            Console.WriteLine(times.IndexOf(times.Min()));
        }
    }
}

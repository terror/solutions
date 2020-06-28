using System;

namespace Solution
{
    class Program
    {
        static void Main(string[] args)
        {
            // input mess
            string input = Console.ReadLine();
            string[] nums = input.Split(' ');
            int items = int.Parse(nums[0]);
            int price = int.Parse(nums[1]);
            string prices = Console.ReadLine();
            string[] pricesNums = prices.Split(' ');
            int[] vals = new int[items];

            // append items to array
            for (int i = 0; i < items; i++)
            {
                vals[i] = int.Parse(pricesNums[i]);
            }

            Array.Sort(vals);
            int j = 1;

            // look through sorted, can pick j items if statement is true
            for (; j < items; j++)
            {
                if (vals[j] + vals[j - 1] > price)
                {
                    break;
                }
            }
            Console.WriteLine(j);
        }

    }
}
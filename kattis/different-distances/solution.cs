using System;

namespace Solution
{
    class Program
    {
        static void Main(string[] args)
        {
            string line;
            while ((line = Console.ReadLine()) != "0")
            {
                string[] nums = line.Split(' ');

                // gathering points & p
                double x1 = double.Parse(nums[0]);
                double y1 = double.Parse(nums[1]);
                double x2 = double.Parse(nums[2]);
                double y2 = double.Parse(nums[3]);
                double p = double.Parse(nums[4]);

                // the almighty formula
                double pnorm = Math.Pow(Math.Pow(Math.Abs(x1 - x2), p) + Math.Pow(Math.Abs(y1 - y2), p), 1.0 / p);
                Console.WriteLine(Math.Round(pnorm, 10));
            }




        }

    }
}
using System;
using System.Collections.Generic;
using System.Linq;

namespace Solution
{
    class Program
    {
        static void Main(string[] args)
        {
            int numCases = int.Parse(Console.ReadLine());
            List<int> times = new List<int>();

            while (numCases-- > 0)
            {
                int numCustomers = int.Parse(Console.ReadLine());
                int k = 0;
                while (k < numCustomers)
                {
                    string w = Console.ReadLine();
                    string[] wnums = w.Split(' ');

                    int timesTotal = 0;
                    // skip first index
                    foreach (string s in wnums.Skip(1))
                    {
                        timesTotal += int.Parse(s);
                    }
                    times.Add(timesTotal);
                    k++;
                }
                times.Sort();
                int sum = 0;
                long total = 0;

                for (int x = 0; x < times.Count; x++)
                {
                    sum += times[x];
                    total += sum;
                }

                double avg = total / (double)times.Count;
                Console.WriteLine((decimal)avg + 0.0000000000m);
                times.Clear();
            }
        }
    }
}

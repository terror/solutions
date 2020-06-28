using System;

namespace Solution
{
    class Program
    {
        static void Main(string[] args)
        {

            int numCases = int.Parse(Console.ReadLine());
            int i = 0;

            while (i < numCases)
            {
                string space = Console.ReadLine();
                long numStudents = long.Parse(Console.ReadLine());
                int j = 0;
                long sum = 0;
                while (j < numStudents)
                {
                    sum += long.Parse(Console.ReadLine());
                    if (sum > numStudents)
                    {
                        sum %= numStudents;
                    }
                    j++;
                }

                if (sum % numStudents == 0 || sum == numStudents)
                {
                    Console.WriteLine("YES");
                }
                else
                {
                    Console.WriteLine("NO");
                }
                i++;
            }

        }
    }
}

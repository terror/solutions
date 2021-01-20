using System;

namespace HelloWord
{
    class Program
    {
        static void Main()
        {
            string input = Console.ReadLine();
            int a = 1;
            int b = 0;
            int c = 0;
            int d;

            for (int i = 0; i < input.Length; i++)
            {
                if (input[i] == 'A')
                {
                    d = a;
                    a = b;
                    b = d;
                }

                if (input[i] == 'B')
                {
                    d = b;
                    b = c;
                    c = d;
                }

                if (input[i] == 'C')
                {
                    d = c;
                    c = a;
                    a = d;
                }
            }

            if (a == 1)
            {
                Console.WriteLine(1);
            }
            else if (b == 1)
            {
                Console.WriteLine(2);
            }
            else
            {
                Console.WriteLine(3);
            }
        }
    }
}
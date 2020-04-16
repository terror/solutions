using System;

class Program
{
    static void Main()
    {
        string a = Console.ReadLine();
        int b = int.Parse(a);
        for (int i = 1; i <= b; i++)
        {
            Console.WriteLine(i + " Abracadabra");
        }
    }
}
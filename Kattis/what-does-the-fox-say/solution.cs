using System;
using System.Collections.Generic;
using System.Linq;

namespace Solution
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = int.Parse(Console.ReadLine());
            int i = 0;
            List<string> sounds = new List<string>();

            while (i < n)
            {
                List<string> list = new List<string>(Console.ReadLine().Split(' ').ToList());
                string line;
                while ((line = Console.ReadLine()) != null)
                {
                    string[] a = line.Split(' ');

                    if (a.Length == 3)
                        sounds.Add(a[2]);
                    else
                    {
                        foreach (string s in sounds)
                            list.RemoveAll(item => item == s);
                        break;
                    }
                }
                foreach (string s in list)
                    Console.Write(s + " ");
                i++;
            }


        }
    }
}

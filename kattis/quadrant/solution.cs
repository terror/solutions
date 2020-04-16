using System;

public class Program 
{
    public static void Main() 
    {
            long x = Int64.Parse(Console.ReadLine());
            long y = Int64.Parse(Console.ReadLine());
            
            if(x < 0 && y < 0) {
                Console.WriteLine(3);
            } else if(x < 0 && y > 0) {
                Console.WriteLine(2);
            } else if(x > 0 && y < 0) {
                Console.WriteLine(4);
            } else {
                Console.WriteLine(1);
            }
    }
        
        
}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ElsoHazi
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int max = Convert.ToInt32(Console.ReadLine());
            int num2 = Convert.ToInt32(Console.ReadLine());
            max = Math.Abs(num2) > Math.Abs(max) ? num2 : Math.Abs(num2) < Math.Abs(max) ? max : (num2 > max) ? num2 : max;
            int num3 = Convert.ToInt32(Console.ReadLine());
            max = Math.Abs(num3) > Math.Abs(max) ? num3 : Math.Abs(num2) < Math.Abs(max) ? max : (num3 > max) ? num2 : max;
            Console.WriteLine(max);
        }
    }
}

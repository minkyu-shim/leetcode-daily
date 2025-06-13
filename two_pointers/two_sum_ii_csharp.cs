using System;

namespace MyFirstCSharp
{
    class Program
    {
        public static void Main(string[] args)
        {
            
        }

        public int[] TwoSum(int[] numbers, int target)
        {
            int l = 0;
            int r = numbers.Length - 1;

            while (l < r)
            {
                if (numbers[l] + numbers[r] > target)
                {
                    r--;
                }
                else if (numbers[l] + numbers[r] < target)
                {
                    l++;
                }
                else
                {
                    break;
                }
            }

            return [l + 1, r + 1];
        }
    }
}
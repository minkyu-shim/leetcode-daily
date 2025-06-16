using System;

namespace MyFirstCSharp
{
    class Program
    {
        public static void Main(string[] args)
        {
            Solution solution = new Solution();

            int a = solution.MaxArea(new int[] {1, 8, 6, 2, 5, 4, 8, 3, 7});
            Console.WriteLine(a);

        }
    }

    public class Solution
    {
        public int MaxArea(int[] height)
        {
            int l = 0;
            int r = height.Length - 1;
            int maxArea = 0;

            while (l < r)
            {
                int currentArea = (r - l) * Math.Min(height[l], height[r]);
                maxArea = Math.Max(maxArea, currentArea);

                if (height[l] < height[r])
                {
                    l++;
                }
                else if (height[l] > height[r])
                {
                    r--;
                }
                else
                {
                    if (height[l + 1] > height[r + 1])
                    {
                        l++;
                    }
                    else
                    {
                        r--;
                    }
                }
                
            }
            return maxArea;
        }
    }
}
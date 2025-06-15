# Level: Medium
# Date: 2025-06-15

class Solution:
    def max_area(self, height):
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                if height[l + 1] > height[r - 1]:
                    l += 1
                else:
                    r -= 1

        return max_area

if __name__ == "__main__":
    example = Solution()
    example.max_area([1,8,6,2,5,4,8,3,7])
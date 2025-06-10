# Level: medium
# Date: 2025-06-10

class Solution:
    def product_except_self_first_ver(self, nums):
        right = [1] * len(nums)
        left = [1] * len(nums)

        for i, num in enumerate(nums):
            for x in nums[i + 1:]:
                right[i] *= x
            for x in nums[0 : i]:
                left[i] *= x

        return [x * y for x, y in zip(right, left)]

    def product_except_self(self, nums):
        n = len(nums)

        left = [1] * n
        for i in range(1, n):
            left[i] *= left[i - 1] * nums[i - 1]

        right = [1] * n
        for i in range(n - 2, -1, -1):
            right[i] *= right[i + 1] * nums[i + 1]

        return [left[i] * right[i] for i in range(n)]

if __name__ == "__main__":
    testcase = Solution()
    print(testcase.product_except_self([-1,1,0,-3,3]))
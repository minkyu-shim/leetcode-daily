# Problem: 238. Product of Array Except Self
# Link: https://leetcode.com/problems/product-of-array-except-self/
# Level: Medium
# Date: May 28th 2025
# Approach: Hash Map

def brute_force_product_array_except_self(nums):
    n = len(nums)
    res = []

    for i in range(n):
        mult = 1
        for num in nums[:i] + nums[i +1:]:
            mult *= num
        res.append(mult)
    return res

def with_division_product_array_except_self(nums):
    res = []
    for i in range(len(nums)):
        if i == 0:
            val = 1
            for j in nums[i+1:]:
                val *= j
            res.append(val)
        else:
            res.append(int(res[-1] * nums[i - 1] / nums[i]))
    return res


def product_array_except_self(nums):
    n = len(nums)
    res = [1] * n  # Output array initialized with 1's

    # First pass: calculate left products
    left = 1
    for i in range(n):
        res[i] = left
        left *= nums[i]

    # Second pass: calculate right products and multiply with left products
    right = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right
        right *= nums[i]

    return res

print(brute_force_product_array_except_self([1, 2, 3, 4, 5]))
print(with_division_product_array_except_self([1, 2, 3, 4, 5]))
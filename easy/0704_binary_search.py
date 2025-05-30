# Problem: 704 Binary Search
# Link: https://leetcode.com/problems/binary-search/description/
# Level: Easy
# Date: May 30th 2025
# Approach: Binary Search

def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        current_mid = nums[(left + right) // 2]

        if current_mid < target:
            left = ((left + right) // 2) + 1
        elif current_mid > target:
            right = ((left + right) // 2) - 1
        else:
            return (left + right) // 2
    return -1

ex1 = search([-1,0,3,5,9,12], 2)
print(ex1)
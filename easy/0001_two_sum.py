# Problem: 1. Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Level: Easy
# Date: May 26th 2025
# Approach: Hash Map

# O(n**2) approach
def two_sum(nums: list, target:int):
    n = len(nums)
    for i in range(n-1):
        to_find = target - nums[i]
        for j in range(i+1, n):
            if nums[j] == to_find:
                return i, j

# O(n) approach using hashmap
def re_two_sum(nums, target):
    hashmap = {} # num : index

    for i, nb in enumerate(nums):
        diff = target - nb
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[nb] = i


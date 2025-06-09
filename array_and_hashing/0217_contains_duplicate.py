# Level: easy
# Date: 2025-06-09

class Solution:
    def contains_duplicate(self, nums):
        return len(set(nums)) != len(nums)
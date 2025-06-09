# Level: easy
# Date: 2025-06-09

class Solution:
    def two_sum(self, nums, target):
        visited = {}

        for i, num in enumerate(nums):
            find = target - num

            if find in visited:
                return visited[find], i
            else:
                visited[num] = i
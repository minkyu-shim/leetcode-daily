# Level: medium
# Date: 2025-06-13

class Solution:
    def two_sum(self, numbers, target):
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                break

        return l + 1, r + 1

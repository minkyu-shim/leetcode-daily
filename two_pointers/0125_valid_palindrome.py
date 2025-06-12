# Level: easy
# Date: 2025-06-12

class Solution:
    def is_palindrome(self, s: str):
        l, r = 0, len(s) - 1
        lower_s = s.lower()

        while l < r:
            while not lower_s[l].isalnum() and l < r:
                l += 1
            while not lower_s[r].isalnum() and l < r:
                r -= 1
            if lower_s[l] != lower_s[r]:
                return False

            l += 1
            r -= 1

        return True
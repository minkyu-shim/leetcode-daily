# Level: easy
# Date: 2025-06-09

class Solution:
    def is_anagram(self, s: str, t: str):
        hashmap = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char not in hashmap:
                hashmap[char] = 0
            hashmap[char] += 1

        for char in t:
            if char not in hashmap:
                return False
            hashmap[char] -= 1

        return all(value == 0 for value in hashmap.values())

if __name__ == '__main__':
    ex = Solution()
    print(ex.is_anagram("aacc", "ccac"))
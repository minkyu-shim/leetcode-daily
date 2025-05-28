# Problem: 242 Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/description/
# Level: Easy
# Date: May 28th 2025
# Approach: Hash Map

def valid_anagram(s: str, t:str) -> bool:
    count_s, count_t = {}, {}

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    for char in count_s:
        if count_s[char] != count_t.get(char, 0):
            return False
    return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        split_s = [char for char in s]

        for char in t:
            if char in split_s:
                split_s.remove(char)
            else:
                return False

        return not split_s

print(valid_anagram('rat', 'car'))
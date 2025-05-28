# Problem: 49 Group Anagram
# Link: https://leetcode.com/problems/group-anagrams/description/
# Level: Medium
# Date: May 27th 2025
# Approach: Hash Map

def group_anagram(strs: list) -> list:
    result = {}

    for word in strs:
        count = [0] * 26 # a to z

        for char in word:
            count[ord(char) - ord('a')] += 1

        if tuple(count) not in result:
            result[tuple(count)] = []

        result[tuple(count)].append(word)

    return list(result.values())

ex1 = group_anagram(["eat","tea","tan","ate","nat","bat"])
pass
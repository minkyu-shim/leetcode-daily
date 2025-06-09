# Level: medium
# Date: 2025-06-09

class Solution:
    def group_anagram(self, strs):
        hashmap = {}

        for s in strs:
            s_id = [0] * 26

            for char in s:
                s_id[ord(char) - ord("a")] += 1

            if tuple(s_id) not in hashmap:
                hashmap[tuple(s_id)] = []

            hashmap[tuple(s_id)].append(s)

        return list(hashmap.values())
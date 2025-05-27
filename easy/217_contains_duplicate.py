# Problem: 217 Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/description/
# Level: Easy
# Date: May 27th 2025
# Approach: Hash Map

def contains_duplicate(nums: list) -> bool:
    hashmap = {}

    for nb in nums:
        if str(nb) not in hashmap.keys():
            hashmap[str(nb)] = 0
        else:
            return True

    return False




ex1 = contains_duplicate([1, 2, 3, 1])
ex2 = contains_duplicate([1, 2, 3, 4])
ex3 = contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])

print(ex1, ex2, ex3)

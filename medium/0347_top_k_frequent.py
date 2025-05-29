# Problem: 347 Top K Frequent Elements
# Link: https://leetcode.com/problems/top-k-frequent-elements/description/
# Level: Medium
# Date: May 29th 2025
# Approach: Hash Map

def top_k_frequent(nums, k: int):
    hashmap ={}

    for nb in nums:
        hashmap[nb] = hashmap.get(nb, 0) + 1

    sorted_hashmap = sorted(hashmap.items(), key=lambda item: item[1], reverse=True)

    return [nb[0] for nb in sorted_hashmap][0:k]

ex1 = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
print(ex1)

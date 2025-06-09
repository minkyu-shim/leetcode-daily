# Level: medium
# Date: 2025-06-09

class Solution:
    def top_k_frequent(self, nums, k):
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0

            hashmap[num] += 1

        return [nb[0] for nb in sorted(hashmap.items(), key=lambda item: item[1], reverse=True)][0:k]


if __name__ == "__main__":

    def sorted_hashmap(nums):
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0

            hashmap[num] += 1
        return sorted(hashmap.items(), key=lambda item: item[1], reverse=True)

    print(sorted_hashmap([1,1,1,2,2,3]))
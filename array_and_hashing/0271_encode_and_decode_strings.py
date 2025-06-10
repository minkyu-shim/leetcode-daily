# Level: medium
# Date: 2025-06-09

class Solution:
    def encode(self, strs):
        result = ""
        for word in strs:
            result += str(len(word)) + "$" + word
        return result

    def decode(self, str):
        result, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "$":
                j += 1
            length = int(str[i : j])
            result.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        
        return result
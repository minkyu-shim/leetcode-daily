# Level: easy
# Date: 2025-06-16

class Solution:
    def is_valid(self, s):
        stack = []
        close_to_open = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
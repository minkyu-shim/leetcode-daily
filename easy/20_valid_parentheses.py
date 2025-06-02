def is_valid(s):
    my_stack = []
    for c in s:
        if c in '({[':
            my_stack.append(c)
        else:
            compare = my_stack.pop(-1)
            if c == ')' and compare != '(':
                return False
            elif c == '}' and compare != '{':
                return False
            elif c == ']' and compare != '[':
                return False
    return not my_stack

def re_is_valid(s):
    stack = []
    close_to_open = {')' : '(', '}': '{', ']' : '['}

    for c in s:
        if c in close_to_open:
            if stack and stack[-1] == close_to_open[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False
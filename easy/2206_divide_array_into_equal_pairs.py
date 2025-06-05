def divide_array(nums):
    hashmap = {}
    for num in nums:
        hashmap[num] = hashmap.get(num, 0) + 1

    return all(x % 2 == 0 for x in hashmap.values())


def divide_array_stack(nums):
    stack = []
    for num in nums:
        if num in stack:
            stack.remove(num)
        else:
            stack.append(num)
    return not stack

def min_eating_speed(piles : list, h: int) -> int:
    left, right = 1, max(piles)
    result = right

    while left <= right:
        k = (left + right) // 2
        hours = 0
        for pile in piles:
            if pile % k == 0:
                hours += pile // k
            else:
                hours += (pile // k) + 1

        if hours <= h:
            result = min(result, k)
            right = k - 1
        else:
            left = k + 1

    return result

ex1 = min_eating_speed(piles = [3,6,7,11], h = 8)
ex2 = min_eating_speed(piles = [30,11,23,4,20], h = 5)
ex3 = min_eating_speed([30,11,23,4,20], h = 6)
ex4 = min_eating_speed([312884470], 312884469)
print(ex1)
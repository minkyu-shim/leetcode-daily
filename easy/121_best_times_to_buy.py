def max_profit_brute_force(prices):
    n = len(prices)
    profit = 0

    for buy in range(n - 1):
        for sell in range(buy + 1, n):
            if prices[sell] - prices[buy] > profit:
                profit = prices[sell] - prices[buy]

    return profit

def max_profit(prices):
    b = 0
    profit = 0
    for s in range(1, len(prices)):
        if prices[s] - prices[b] > profit:
            profit = prices[s] - prices[b]
        if prices[s] < prices[b]:
            b = s
    return profit


ex1 = max_profit([7,1,5,3,6,4])
ex2 = max_profit([7,6,4,3,1])
print(ex1)
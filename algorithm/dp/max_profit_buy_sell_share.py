"""
Maximum profit by buying and selling a share at most twice.
1)Create a table profit[0,..,n-1] and initialize all values in it 0.
2)Traverse price from right to left and update profit[i] such that profit[i] stores maximum profit achievable from one
transaction in subarray price[i,n-1].
3)Traverse price from right to left and update profit[i] such that profit[i] stores maximum profit[i] contains maximum
achievable profit from two transactions in subarray price[0,i].
4)Return profit[n-1].
"""


def max_profit(price):
    n = len(price)
    profit = [0]*n
    max_price = price[n-1]
    # do one transaction, find the maximum profit[i] in [i, n-1]
    for i in range(n-2, 0, -1):
        if price[i] > max_price:
            max_price = price[i]
        profit[i] = max(profit[i+1], max_price-price[i])
    min_price = price[0]
    for i in range(1, n):
        if price[i] < min_price:
            min_price = price[i]
        profit[i] = max(profit[i-1], profit[i] + price[i]-min_price)
    return profit[n-1]


p = [2, 30, 15, 10, 8, 25, 80]
print(max_profit(p))
p = [10, 22, 5, 75, 65, 80]
print(max_profit(p))
p = [100, 30, 15, 10, 8, 25, 80]
print(max_profit(p))
p = [90, 80, 70, 60, 50]
print(max_profit(p))
p = [112, 15, 80]
print(max_profit(p))
"""
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. Determine
the maximum value obtainable by cutting up the rod and selling the pieces.

We can get the best price by making a cut at different positions and comparing the values obtained after a cut. We can
recursively call the same function for a piece after a cut.
Let cutRod(n) be the required(best prices) value for a rod of length n, then cutRod(n) can be writen as follow:
cutRod(n) = max(price(i} + cutRod(n-i-1)) for i in {0, 1, 2, ... n}
"""


def cut_rod_recur(price, n):
    if n <= 0:
        return 0
    max_val = 0
    for i in range(n):
        v = price[i] + cut_rod_recur(price, n - i - 1)
        if v > max_val:
            max_val = v
    return max_val


def cut_rod_dp(price, n):
    p = [0] * (n + 1)
    for i in range(1, n + 1):
        max_val = 0
        for j in range(i):
            v = price[j] + p[i - j - 1]
            if v > max_val:
                max_val = v
        p[i] = max_val
    return p[n]


arr = [1, 5, 8, 9, 10, 17, 17, 20]
print("Maximum obtainable value is", cut_rod_recur(arr, len(arr)))
print(cut_rod_dp(arr, len(arr)))

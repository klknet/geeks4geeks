"""
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the
knapsack.
Solution:
To consider all subsets of n items, there can be two cases for every item: (1)the item is included in the optimal subset
(2)not included in the optimal subset.
Therefore, the maximum value that can be obtained from n items is max of following two values.
1)Maximum value obtained by n-1 items and W weight(excluding nth item)
2)Value of nth item plus maximum value obtained by n-1 items and W minus weight of nth item(including nth item).

"""


def knapsack_recur(item, n, W):
    # Base case
    if n == 0 or W == 0:
        return 0
    # If weight of the nth item is more than knapsack of capacity W, then this item cannot be included in the optimal
    # solution.
    if item[n - 1][0] > W:
        return knapsack_recur(item, n - 1, W)
    # return the maximum of two case:
    # (1)nth item included
    # (2)nth item not included
    return max(knapsack_recur(item, n - 1, W), item[n - 1][1] + knapsack_recur(item, n - 1, W - item[n - 1][0]))


def knapsack_dp(item, W):
    n = len(item)
    K = [[0] * (n + 1) for i in range(W + 1)]
    for w in range(1, W + 1):
        for j in range(1, n + 1):
            if item[j - 1][0] <= w:
                K[w][j] = max(K[w - item[j - 1][0]][j - 1] + item[j - 1][1], K[w][j - 1])
            else:
                K[w][j] = K[w][j - 1]
    return K[W][n]


# space optimal, we can calculate total value of knapsack with capacity of W weight using only one dimension array.
def knapsack_opt(item, W):
    n = len(item)
    F = [0] * (W+1)
    for i in range(n):
        for w in range(W, item[i][0], -1):
            # for ith loop, current F[i][w] stored the (i-1)th F[i-1][w]value, F[i][w-c[i]] stored the (i-1)th
            # F[i-1][w-c[i] value. So F[w] = max(F[w], F[w-c[i] + c[i])
            # The loop is in decreasing order, because some item will be loaded more than once, as V > V - C(i), if in
            # ascending order, F[w-c[i]] is ith value, not (i-1)th value.
            F[w] = max(F[w], item[i][1] + F[w - item[i][0]])
    return F[W]


item = [[10, 60], [20, 100], [30, 50], [15, 80]]
W = 55
print("Maximum value of the knapsack can taken is {}", knapsack_recur(item, len(item), W))
print(knapsack_dp(item, W))
print(knapsack_opt(item, W))

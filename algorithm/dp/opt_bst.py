"""
Given a sorted array keys[0..n-1] of search keys and an array freq[0..n-1] of frequency counts, where freq[i] is the
number of searches to keys[i]. Construct a binary search tree of all keys such that the total cost of all the searches
is as small as possible.
The optimal cost for freq[0..n-1] can be recursively calculated using following formula.
optCost(i,j) = ∑(k=i,j)freq[k] + min(r=i,j)[optCost(i,r-1)+optCost(r+1,j)]
We need to calculate optCost(0,n-1) to find the result.
The idea of above formula is simple, we one by one try all nodes as root(r varies from i to j in second term). When we
make rth node as root, we recursively calculate optimal cost from i to r-1 and r+1 to j. We add sum of frequencies from
i to j(see first term in above formula), this is added because every search will go through root and one comparison will
be done for every search.
"""

import sys


def opt_bst(keys, freq, i, j):
    if i > j:
        return 0
    if i == j:
        return freq[i]
    f = sum(freq[i:j + 1])
    min_cost = sys.maxsize
    for r in range(i, j + 1):
        cost = opt_bst(keys, freq, i, r - 1) + opt_bst(keys, freq, r + 1, j)
        if cost < min_cost:
            min_cost = cost
    return f + min_cost


def opt_bst_dp(keys, freq):
    n = len(freq)
    t = [[0 for col in range(n)] for row in range(n)]
    for i in range(n):
        t[i][i] = freq[i]
    for k in range(2, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            min_cost = sys.maxsize
            s = sum(freq[i:j + 1])
            for r in range(i, j + 1):
                left = t[i][r - 1] if r > i else 0
                right = t[r + 1][j] if r < j else 0
                cost = left + right + s
                if cost < min_cost:
                    min_cost = cost
            t[i][j] = min_cost
    return t[0][n - 1]


keys = [10, 12, 20]
freq = [34, 8, 50]
print('Cost of Optimal BST is', opt_bst(keys, freq, 0, len(freq) - 1))
print(opt_bst_dp(keys, freq))

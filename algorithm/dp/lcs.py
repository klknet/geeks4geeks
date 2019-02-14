"""
Given two sequences, find the length of longest common sub sequences.
Solution:
Let x[0,m-1] and y[0,n-1] be the input sequences of length m, n respectively, L(x[0,m-1], y[0,n-1]) be the length of the
lcs of x and y
1)if the last character of x and y is equal, x[m-1] == y[n-1],
then L(x[0,m-1], y[0,n-1]) = 1 + L(x[0,m-2], y[0,n-2])
else L([x[0,m-1], y[0,n-1]) = max(L(x[0,m-2], y[0,n-1]), L(x[0,m-1], y[0,n-2]))
"""


def lcs_recur(a, b, n, m):
    if n > 0 and m > 0:
        if a[n - 1] == b[m - 1]:
            return 1 + lcs_recur(a, b, n - 1, m - 1)
        else:
            return max(lcs_recur(a, b, n, m - 1), lcs_recur(a, b, n - 1, m))
    return 0


def lcs_recur_driven(a, b):
    length = lcs_recur(a, b, len(a), len(b))
    print("lcs of ", a, b, "is", length)


def lcs_dp(a, b):
    m = len(a)
    n = len(b)
    lcs = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                lcs[i][j] = 0
            elif a[i-1] == b[j-1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    return lcs[m][n]


a = "abcdefg"
b = "bdgef"
lcs_recur_driven(a, b)
print(lcs_dp(a, b))

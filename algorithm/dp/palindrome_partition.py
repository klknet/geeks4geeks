"""
Given a string, a partitioning of the string is a palindrome partitioning if every substring of the partition is a
palindrome. Determine the fewest cuts needed for palindrome partitioning
If the string is palindrome, then we simply return 0. Else, like the Matrix Chain Multiplication problem, we try making
cuts at all possible positions, recursively calculate the cost for each cut and return the minimum value.
Let the given string be str and minPalPartition() be the function that returns the fewest cuts needed for palindrome
partitioning. Following is optimal substructure property.
minPalPartition(str, i, j)=0 if i==j, only one character.
minPalPartition(str, i, j)=0 if str[i...j] is palindrome.
Else
minPalPartition(str, i, j) = Min( minPalPartition(str, i, k)+1+minPalPartition(str, k+1, j) ) where k varies from i to
j-1
"""


def min_pal_partition(s):
    n = len(s)
    # store p[i,j] is palindrome
    p = [[False for j in range(n)] for i in range(n)]
    d = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        p[i][i] = True
    # L is substring length. Build the solution in bottom up manner by considering all substrings of length starting
    # from 2 to n.
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            if L == 2:
                p[i][j] = (s[i] == s[j])
            else:
                p[i][j] = (s[i] == s[j]) and p[i + 1][j - 1]
            if not p[i][j]:
                d[i][j] = 999999
                for k in range(i, j):
                    d[i][j] = min(d[i][j], d[i][k] + 1 + d[k + 1][j])
    return d[0][n - 1]


def min_pal_partition_opt(s):
    n = len(s)
    # store palindrome state p[i][j] is true if s[i...j] is palindrome substring.
    p = [[False for j in range(n)] for i in range(n)]
    d = [0] * n
    # substring of length 1 is palindrome string
    for i in range(n):
        p[i][i] = True
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            if L == 2:
                p[i][j] = s[i] == s[j]
            else:
                p[i][j] = (s[i] == s[j]) and p[i + 1][j - 1]
    for i in range(n):
        if p[0][i]:
            d[i] = 0
        else:
            d[i] = 9999999
            for j in range(i):
                if p[j + 1][i] and 1 + d[j] < d[i]:
                    d[i] = 1 + d[j]
    return d[n - 1]


s = "ababbbabbababa"
print(min_pal_partition(s))
print(min_pal_partition_opt(s))

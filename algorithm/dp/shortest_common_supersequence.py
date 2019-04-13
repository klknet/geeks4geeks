"""
Shortest Common Supersequence.
Given two strings str1 and str2, find the shortest string that has both str1 and str2 as subsequences.
We need to find a string that has both strings as subsequences and is shortest such string. If both strings have all
characters different, then result is sum of lengths of given two strings. If there are common characters, we don't want
them multiple times as the task is to minimize length. Therefore, we first find the longest common subsequence, take one
occurrence of this subsequence and add extra characters.
"""


def shortest_common_str(str1, str2):
    t = len(str1) + len(str2)
    c = lcs(str1, str2)
    return t - c


def lcs(str1, str2):
    n1, n2 = len(str1), len(str2)
    dp = [[0 for i in range(n2 + 1)] for j in range(n1 + 1)]
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            if i == 0 or j == 0:
                dp[i][j] == 0
            else:
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[n1][n2]


def lcs2(str1, str2):
    n1, n2 = len(str1), len(str2)
    dp = [[0 for i in range(n2 + 1)] for j in range(n1 + 1)]
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            else:
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j])
    return dp[n1][n2]


def lcs3(str1, str2):
    """
    1)Construct L[m+1][n+1] using dynamic programming.
    2)The value of L[m][n] contains the length of lcs. Create a character array lcs[] of length equals to lcs.
    3)Traverse the 2D array starting from L[m][n]. Do following for every cell[i][j].
     a)If characters (in X and Y) corresponding to L[i][j] are same, then include this character as part of lcs.
     b)Else compare values of L[i][j-1] and L[i-1][j] and go indirection of greater value.
    """
    n1, n2 = len(str1), len(str2)
    dp = [[0 for i in range(n2 + 1)] for j in range(n1 + 1)]
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            if i == 0 or j == 0:
                dp[i][j] == 0
            else:
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    scs = n1 + n2 - dp[n1][n2]
    common = []
    supersuq = []
    i, j = n1, n2
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            common.insert(0, str1[i - 1])
            supersuq.insert(0, str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i][j - 1] >= dp[i - 1][j]:
            supersuq.insert(0, str2[j - 1])
            j -= 1
        else:
            supersuq.insert(0, str1[i - 1])
            i -= 1
    while i > 0:
        supersuq.insert(0, str1[i - 1])
        i -= 1
    while j > 0:
        supersuq.insert(0, str2[j - 1])
        j -= 1
    return ''.join(common), ''.join(supersuq)


X = "AGGTAB"
Y = "GXTXAYB"
# X = 'geek'
# Y = 'eke'
# print(shortest_common_str(X, Y))
# print(lcs2(X, Y))
print(lcs3(X, Y))

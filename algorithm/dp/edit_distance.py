"""
Given two strings str1 and str2 and below operations that can be performed on str1, Find minimum number of edits required
for convert str1 into str2.
Insert, Delete, Replace
The idea is process all characters one by one starting from either from left or right side of both strings, Let us traverse
from right corners, there are two possibilities for every pair of character being traverse.
m: Length of str1 (first string)
n: Length of str2 (second string)
1)If last character of both strings are same, nothing much to do, Ignore last character and get count for remaining strings,
so we recur for length m-1 and n-1
2)Else(last characters not same), Consider all operations on str1, three operations on last character of first string,
recursively compute minimum cost for all three operations and take minimum of three values.
1.Insert: Recur for m and n-1.
2.Delete: Recur for m-1 and n.
3.Replace: Recur for m-1 and n-1.
"""


def edit_recur(s1, s2, m, n):
    # if first string is empty, the only operation is insert second string into first string
    if m == 0:
        return n
    # if second string is empty, the only operation is delete all first string
    if n == 0:
        return m
    if s1[m - 1] == s2[n - 1]:
        return edit_recur(s1, s2, m - 1, n - 1)
    else:
        return 1 + min(edit_recur(s1, s2, m, n - 1), edit_recur(s1, s2, m - 1, n), edit_recur(s1, s2, m - 1, n - 1))


def edit_dp(s1, s2):
    m = len(s1)
    n = len(s2)
    tab = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                tab[i][j] = j
            elif j == 0:
                tab[i][j] = i
            elif s1[i-1] == s2[j-1]:
                tab[i][j] = tab[i-1][j-1]
            else:
                tab[i][j] = 1+min(tab[i][j-1], tab[i-1][j], tab[i-1][j-1])
    return tab[m][n]


s1 = 'geeks'
s2 = 'gesek'
print(edit_recur(s1, s2, len(s1), len(s2)))
print(edit_dp(s1, s2))

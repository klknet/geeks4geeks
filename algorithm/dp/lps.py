"""
Given a sequence, find the length of the longest palindromic subsequence in it.
Let X[0,1,..n-1] be the sequence of length n, L[0,n-1] be the length of the longest palindromic sebsequence of X[0, n-1].
If last and first characters of X are same, then L[0,n-1] = 2 + L[1,n-2]
else L[0,n-1] = max(L(0, n-2), L(1, n-1))
"""


def lps_recur(s, f, l):
    if f == l:
        return 1
    if s[f] == s[l] and f + 1 == l:
        return 2
    if s[f] == s[l]:
        return 2 + lps_recur(s, f + 1, l - 1)
    return max(lps_recur(s, f, l - 1), lps_recur(s, f + 1, l))


def lps_dp(s, f, l):
    t = [[1] * l for i in range(l)]
    for i in range(l, -1, -1):
        for j in range(i+1, l):
            if s[i] == s[j] and i + 1 == j:
                t[i][j] = 2
            elif s[i] == s[j]:
                t[i][j] = 2 + t[i + 1][j - 1]
            else:
                t[i][j] = max(t[i][j - 1], t[i + 1][j])
    return t[f][l - 1]


def lps_dp2(s, f, l):
    t = [[1]*l for i in range(l)]
    for cl in range(2, l+1):
        for i in range(l-cl+1):
            j = i+cl-1
            if s[i] == s[j] and cl == 2:
                t[i][j] = 2
            elif s[i] == s[j]:
                t[i][j] = 2 + t[i+1][j-1]
            else:
                t[i][j] = max(t[i+1][j], t[i][j-1])
    return t[f][l-1]


def lps_dp_opt(s):
    n = len(s)
    t = [0]*n
    for i in range(n-1, -1, -1):
        back_up = 0
        for j in range(i, n):
            if i==j:
                t[j] = 1
            # like t[i][j]= [i+1][j-1] + 2
            elif s[i] == s[j]:
                temp = t[j]
                t[j] = back_up + 2
                back_up = temp
            else:
                # t[i][j] = max(t[i][j-1], t[i+1][j])
                back_up = t[j]
                t[j] = max(t[j-1], t[j])
    return t[n-1]


seq = "aababab"
# seq = "GEEKSFORGEEKSabcdeffedcbaefa"
# print(lps_recur(seq, 0, len(seq) - 1))
print(lps_dp(seq, 0, len(seq)))
print(lps_dp2(seq, 0, len(seq)))
print(lps_dp_opt(seq))
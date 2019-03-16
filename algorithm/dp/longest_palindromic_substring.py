"""
Given a string, find the longest substring which is palindromic.
We maintain a boolean table[n][n] that is filled in bottom up manner. The value of table[i][j] is true if the substring
is palindrome, otherwise false. To calculate table[i][j], we first check the value of table[i+1][j-1], if the value is
true and str[j] is same as str[i], then we make table[i][j] true. Otherwise, the value of table[i][j] is made false.
"""


def lps(s):
    reverse_s = s[::-1]
    m = 1
    count = 0
    end = 0
    for i in range(len(s)):
        if s[i] == reverse_s[i]:
            count += 1
        else:
            count = 0
        if count > m:
            end = i
            m = count
    print(s[end - m + 1:end + 1])
    return m


def lps_dp(s):
    n = len(s)
    t = [[False for i in range(n)] for j in range(n)]
    for i in range(n):
        t[i][i] = True
    m = 1
    start = end =0
    for K in range(2, n + 1):
        for i in range(n - K + 1):
            j = i + K - 1
            if K == 2:
                t[i][j] = s[i] == s[j]
            else:
                t[i][j] = s[i] == s[j] and t[i + 1][j - 1]
            if t[i][j] and j-i+1>m:
                m = j-i+1
                start = i
                end = j
    print(s[start:end+1])
    print(m)



s = "forgeeksskeegfor"
print(lps(s))
lps_dp(s)

"""
Consider a situation where all characters of pattern are different.
When all characters of pattern are different, we can slide the pattern by more than 1. When a mismatch occurs after j
match, we know that the first character of pattern will not match the j matched characters because all the characters of
pattern are different. So we can always slide the pattern by j shifts without missing any valid shifts.
"""


def native_search(txt, pat):
    n, m = len(txt), len(pat)
    i = j = 0
    while i <= n - m:
        for j in range(m):
            if txt[i + j] != pat[j]:
                break
            j += 1
        if j == m:
            print(i)
            i += m
        elif j == 0:
            i += 1
        else:
            i += j


txt = "ABCEABCDABCEABCD"
pat = "ABCD"
native_search(txt, pat)

"""
Native algorithm for pattern searching.
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(pat[], txt[]) that prints all occurrences of
pat[] in txt[]. You may assume that n>m.
"""


def pattern_search(pat, txt):
    m, n = len(pat), len(txt)
    for i in range(n - m +1):
        for j in range(m):
            if pat[j] != txt[i + j]:
                break
            if j == m - 1:
                print(i)


pat = 'AABA'
txt = 'AABAACAADAABAABA'
pattern_search(pat, txt)

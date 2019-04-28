"""
KMP algorithm for pattern searching.
KMP algorithm preprocesses pat[] and construct an auxiliary array lps[] of size m(same of size pat) which is used to
skip characters while matching.
Name of lps indicates longest proper prefix which is also suffix.

1)We start comparision of pat[j] with j=0 with characters of current window of text.
2)We keep matching characters txt[i] and pat[j] and keep incrementing i and j while pat[j] and txt[i] keep matching.
3)When we see a mismatch.
  a)We know that characters pat[0..j-1] match with txt[i-j..i-1](Note that j starts with 0 and only increment it when
  there is a match)
  b)We also know that lps[0..j-1] is count of characters of pat[0..j-1] that are both proper prefix and suffix.
  c)From above two points, we can conclude that we do not need to match lps[j-1] characters with txt[i-j..i-1] because
  we know these characters will anyway match.

"""


def kmp_search(txt, pat):
    n, m = len(txt), len(pat)
    lps = [0] * m
    build_lps(pat, m, lps)
    i = j = 0
    while i < n:
        if txt[i] == pat[j]:
            i += 1
            j += 1
        if j == m:
            print(i - j)
            j = lps[j-1]
        if i < n and txt[i] != pat[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def build_lps(pat, m, lps):
    k = 0
    i = 1
    while i<m:
        if pat[i] == pat[k]:
            k += 1
            lps[i] = k
            i += 1
        else:
            if k != 0:
                k = lps[k-1]
            else:
                lps[i] = 0
                i += 1

pat = 'AABA'
txt = 'AABAACAADAABAABA'
kmp_search(txt, pat)


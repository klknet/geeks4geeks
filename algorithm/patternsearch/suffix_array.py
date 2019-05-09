"""
A suffix array is a sorted array of all suffixes of a given string.
"""


# Because the array is sorted, we can use binary search.
def search(pat, txt):
    m, n = len(pat), len(txt)
    sa = build_sa(txt, n)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) >> 1
        res = strncmp(pat, sa[mid].suff, m)
        if res == 0:
            print(sa[mid].index)
            return
        elif res < 0:
            r = mid-1
        else:
            l = mid + 1


# compare pattern with suffix, return 0 if match.
def strncmp(pat, suffix, m):
    # if the length of pattern is longer than suffix, then return 1
    if len(suffix) < m:
        return 1
    for i in range(m):
        if ord(pat[i])-ord(suffix[i]) != 0:
            return ord(pat[i])-ord(suffix[i])
    return 0


# build a suffix array.
def build_sa(txt, n):
    sa = [0] * n
    for i in range(n):
        sa[i] = Suffix(i, txt[i:])
    sa.sort(key=lambda s: s.suff)
    return sa


class Suffix(object):
    def __init__(self, i, suff):
        self.index = i
        self.suff = suff


pat = 'nan'
txt = 'banana'
search(pat, txt)

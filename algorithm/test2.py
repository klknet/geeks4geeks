"""
Print all permutation of a string.
"""


def permutation(s, l, res):
    if l == len(s):
        print(res)
        return
    for cur in range(l, len(s)):
        s[l], s[cur] = s[cur], s[l]
        permutation(s, l + 1, res + s[l])
        s[l], s[cur] = s[cur], s[l]


s = ['A', 'B', 'C']
permutation(s, 0,  "")

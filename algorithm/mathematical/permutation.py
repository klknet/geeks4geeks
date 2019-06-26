"""
Write a program to print all permutations of a given string
"""


def permutation(s, l, r):
    if l == r:
        print("".join(s))
        return
    for i in range(l, r):
        s[l], s[i] = s[i], s[l]
        permutation(s, l+1, r)
        s[i], s[l] = s[l], s[i]


s = ['A', 'B', 'C', 'D']
permutation(s, 0, len(s))
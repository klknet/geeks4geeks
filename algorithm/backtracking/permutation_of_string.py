"""
Write a program to print all permutations of a given string.
"""


def permutation(s, l, r):
    if l == r:
        print("".join(s))
        return
    for i in range(l, r+1):
        s[l], s[i] = s[i], s[l]
        permutation(s, l + 1, r)
        s[i], s[l] = s[l], s[i] # backtrack


s = ['a', 'b', 'c']
permutation(s, 0, len(s) - 1)

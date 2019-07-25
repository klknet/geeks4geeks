"""
Print all permutations in sorted(lexicographic) order.
1.Sort the given string in non-decreasing order and print it. The first permutation is always the string sorted in
non-decreasing order.
2.Start generating next higher permutation. Do it util next higher permutation is not possible. If we reach a permutation
where all characters are sorted in non-increasing order, the that permutation is the last permutation.

Steps to generate the next higher permutation:
1.Take the previously printed permutation and find the rightmost character in it, which is smaller than its next character.
Let us call this character as 'first character'.
2.Now find the ceiling of the first character. Let us call the ceil character as 'second character'.
3.Swap the two characters found in above 2 steps.
4.Sort the substring(in non-decreasing order) after the original index of 'first character'.
"""


def permutations(s, cur, n, r):
    if cur == n:
        print(r)
        return
    for i in range(cur, n):
        ch = s[i]
        s[cur], s[i] = s[i], s[cur]
        permutations(s, cur + 1, n, r + ch)
        s[i], s[cur] = s[cur], s[i]


def perm(s):
    s.sort(key=lambda x: x)
    while True:
        print(s)
        i = len(s) - 2
        while i >= 0:
            if s[i + 1] > s[i]:
                break
            i -= 1
        if i == -1:
            break
        j = 0
        smallest_big = 9999
        for k in range(i, len(s)):
            if ord(s[i]) < ord(s[k]) < smallest_big:
                smallest_big = ord(s[k])
                j = k
        s[i], s[j] = s[j], s[i]
        # s[i + 1:].sort(key=lambda x: x)
        s1 = s[:i+1]
        s2 = s[i+1:]
        s2.reverse()
        s = s1+s2


s = ['A', 'B', 'C', 'D']
permutations(s, 0, len(s), '')
perm(s)

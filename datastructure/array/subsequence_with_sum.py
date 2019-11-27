"""
Find the subsequence with given sum in a superincreasing sequence.
Using Greedy Algorithm.
"""


def subsequence(arr, s):
    res = []
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] <= s:
            res.insert(0, arr[i])
            s -= arr[i]
    return res


print(subsequence([17, 25, 46, 94, 201, 400], 272))
print(subsequence([1, 2, 4, 8, 16], 12))

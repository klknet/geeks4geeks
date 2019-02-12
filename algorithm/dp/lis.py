"""
given a sequence, find the longest increasing sub sequence
let arr[0,1,...n] be the input array and L(i) be the length of lis ending at index i such that arr[i] is the last element
of lis
Then L(i) can be recursively writen as:
L(i) = 1+max(L(j)) where 0<j<i and arr[j]<arr[i]
or L(i)=1 if not exist this j
"""

max_lis = 1


# Simple recursive implementation
def lis_recur(arr):
    global max_lis
    _lis(arr, len(arr))
    print(max_lis)


def _lis(arr, n):
    global max_lis
    if n == 1:
        return 1
    n_lis = 1
    for i in range(1, n):
        i_lis = _lis(arr, i)
        if arr[n - 1] > arr[i - 1] and n_lis < i_lis + 1:
            n_lis = i_lis + 1
    max_lis = max(max_lis, n_lis)
    return n_lis


# using dp by bottom up tabulation
def lis_dp(arr):
    n = len(arr)
    li = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and li[i] < li[j] + 1:
                li[i] = li[j] + 1
    return max(li)


arr = [5, 20, 6, 4, 3, 8, 10, 9]
arr = [5, 6]
lis_recur(arr)
print(lis_dp(arr))

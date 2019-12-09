"""
Rearrange an array such that arr[i]=i
"""
import copy


def rearrange(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] != -1 and arr[i] != i:
            x = arr[i]
            while arr[x] != -1 and arr[x] != x:
                y = arr[x]
                arr[x] = x
                x = y
            arr[x] = x
            if arr[i] != i:
                arr[i] = -1
    return arr


def rearrange1(arr):
    """
    This is a programing taste.
    :param arr:
    :return:
    """
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] != -1 and arr[i] != i:
            t = arr[i]
            arr[i] = arr[t]
            arr[t] = t
        else:
            i += 1
    return arr


def rearrange2(arr):
    unique = set(arr)
    for i in range(len(arr)):
        if i in unique:
            arr[i] = i
        else:
            arr[i] = -1
    return arr


arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
print(rearrange(copy.copy(arr)))
print(rearrange1(copy.copy(arr)))
print(rearrange2(copy.copy(arr)))

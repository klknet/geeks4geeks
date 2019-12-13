"""
Rearrange array such that arr[i] >= arr[j] if i is even and arr[i] <= arr[j] if i is odd and j<i;
"""
import math


def rearrange(arr):
    arr.sort()
    idx = math.ceil(len(arr) / 2)
    odd = arr[:idx]
    even = arr[idx:]
    odd_idx = len(odd) - 1
    even_idx = 0
    for i in range(0, len(arr), 2):
        arr[i] = odd[odd_idx]
        odd_idx -= 1
    for i in range(1, len(arr), 2):
        arr[i] = even[even_idx]
        even_idx += 1
    return arr


def rearrange1(arr):
    pos = split(arr)
    neg = 0
    while neg < len(arr) and pos < len(arr) and arr[neg] < 0:
        arr[pos], arr[neg] = arr[neg], arr[pos]
        pos += 1
        neg += 2
    return arr


def move_zero_to_end(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1
    return arr


def move_zero_to_end1(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < len(arr):
        arr[count] = 0
        count += 1
    return arr


def rearrange2(arr):
    tmp = [-1] * len(arr)
    arr.sort()
    mid = int(len(arr)/2)
    i, j = 0, len(arr)-1
    k=0
    while i < mid or mid <= j:
        if k<len(arr):
            tmp[k] = arr[i]
            k += 1
        if k<len(arr):
            tmp[k] = arr[j]
            k += 1
        i += 1
        j -= 1
    return tmp


def split(arr):
    pivot = 0
    i = j = 0
    for j in range(0, len(arr)):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return i


print(rearrange([1, 2, 3, 4, 5, 6, 7]))
print(rearrange([1, 2, 1, 4, 5, 6, 8, 8]))
print(rearrange1([-1, 2, -3, 4, 5, 6, -7, 8, 9]))
print(move_zero_to_end([1, 2, 0, 4, 3, 0, 5, 0]))
print(move_zero_to_end1([1, 2, 0, 4, 3, 0, 5, 0]))
print(rearrange2([5, 8, 1, 4, 2, 9, 3, 7, 6]))
print(rearrange2([5, 8, 1, 4, 2, 9, 3, 7, 6, 10]))

"""
Rearrange array such that arr[i] >= arr[j] if i is even and arr[i] <= arr[j] if i is odd and j<i;
"""
import math


def rearrange(arr):
    arr.sort()
    idx = math.ceil(len(arr)/2)
    odd = arr[:idx]
    even = arr[idx:]
    tmp = [-1] * len(arr)
    odd_idx = len(odd) - 1
    even_idx = 0
    for i in range(0, len(arr), 2):
        arr[i] = odd[odd_idx]
        odd_idx -= 1
    for i in range(1, len(arr), 2):
        arr[i] = even[even_idx]
        even_idx += 1
    return arr


print(rearrange([1, 2, 3, 4, 5, 6, 7]))
print(rearrange([1, 2, 1, 4, 5, 6, 8, 8]))




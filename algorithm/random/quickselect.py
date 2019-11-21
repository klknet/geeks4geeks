"""
K'th smallest elements in unsorted array.
"""
import random


def k_smallest(arr, k):
    return quick_select(arr, 0, len(arr) - 1, k-1)


def quick_select(arr, l, r, k):
    pivot_idx = partition(arr, l, r)
    if pivot_idx == k:
        return arr[pivot_idx]
    elif pivot_idx > k:
        return quick_select(arr, l, pivot_idx-1, k)
    elif pivot_idx < k:
        return quick_select(arr, pivot_idx+1, r, k)


def partition(arr, l, r):
    idx = random.randint(l, r)
    pivot = arr[idx]
    arr[idx], arr[r] = arr[r], arr[idx]
    i, j = l, l
    while j < r:
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


print(k_smallest([12, 3, 5, 7, 4, 19, 26], 3))

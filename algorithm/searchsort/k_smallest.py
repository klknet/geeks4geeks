# Find k'th smallest elemnt in unsorted array
import random
import sys


def k_smallest(arr, l, r, k):
    if l <= r:
        pos = partition(arr, l, r)
        if pos - l == k - 1:
            return arr[pos]
        # go to left subarray if pivot is greater than k
        if pos - l > k - 1:
            return k_smallest(arr, l, pos - 1, k)
        return k_smallest(arr, pos + 1, r, k - (pos - l + 1))
    return sys.maxsize


def k_smallest_itr(arr, k):
    n = len(arr)
    l, r = 0, n - 1
    while l <= r:
        pos = partition_dual(arr, l, r)
        if pos == k - 1:
            return arr[pos]
        elif pos > k - 1:
            r = pos - 1
        else:
            l = pos + 1
    return sys.maxsize


def partition(arr, l, r):
    rid = random.randint(l, r)
    pivot = arr[rid]
    arr[r], arr[rid] = pivot, arr[r]
    i = l
    for j in range(l, r, 1):
        if arr[j] <= pivot:
            if i != j:
                arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[r], arr[i] = arr[i], pivot
    return i


def partition_dual(arr, l, r):
    """
    Use dual pointer l, r, let leftest element as pivot, find the first element that greater than pivot from left to right, let arr[r]
    =arr[l], find the first element that smaller than pivot from right to left, let arr[l]=arr[r], if l<r, at last assign
    arr[l] = pivot
    :param arr:
    :param l:
    :param r:
    :return:
    """
    pivot = arr[r]
    while l < r:
        while l < r:
            if arr[l] > pivot:
                break
            else:
                l += 1
        arr[r] = arr[l]
        r -= 1
        while l < r:
            if arr[r] < pivot:
                break
            else:
                r -= 1
        arr[l] = arr[r]
    arr[l] = pivot
    return l


if __name__ == '__main__':
    arr = [12, 3, 5, 7, 4, 19, 26, 10]
    for i in range(len(arr)):
        # print(k_smallest(arr, 0, len(arr) - 1, i + 1))
        print(k_smallest_itr(arr, i + 1), end=' ')

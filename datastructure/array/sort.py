"""
Sorting
"""
import heapq
import copy


def ksorted_array(arr, k):
    """
    Sort a nearly sorted(k sorted) array.
    :param arr:
    :param k:
    :return:
    """
    for i in range(1, len(arr)):
        e = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > e:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = e
    return arr


def ksorted_array_heap(arr, k):
    """
    Sort a nearly sorted(k sorted) array using minimum heap.
    :param arr:
    :param k:
    :return:
    """
    h = arr[:k + 1]
    heapq.heapify(h)
    index = 0
    for i in range(k + 1, len(arr)):
        arr[index] = heapq.heappop(h)
        index += 1
        heapq.heappush(h, arr[i])
    while len(h) > 0:
        arr[index] = heapq.heappop(h)
        index += 1
    return arr


def wave_sort(arr):
    """
    Sort an array in wave form.
    Traverse the array of even positions, if previous element is greater than current element, swap each other,
    if next element is greater than current element, swap each other.
    :param arr:
    :return:
    """
    i = 0
    while i < len(arr):
        if i - 1 > 0 and arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
        if i + 1 < len(arr) and arr[i + 1] > arr[i]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i += 2
    return arr


def wave_sort1(arr):
    """
    Sort an array in wave form.
    Sort the array first, then swap all adjacent elements.
    :param arr:
    :return:
    """
    arr.sort()
    for i in range(0, len(arr)-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


def merge_n_arr(arr1, arr2):
    idx1 = len(arr1)
    for i in range(len(arr1)-1, -1, -1):
        if arr1[i] != -1:
            idx1 -= 1
            arr1[idx1] = arr1[i]
    idx = idx2 = 0
    while idx1 < len(arr1) and idx2 < len(arr2):
        if arr1[idx1] < arr2[idx2]:
            arr1[idx] = arr1[idx1]
            idx1 += 1
        else:
            arr1[idx] = arr2[idx2]
            idx2 += 1
        idx += 1
    while idx1 < len(arr1):
        arr1[idx] = arr1[idx1]
        idx1 += 1
        idx += 1
    while idx2 < len(arr2):
        arr1[idx] = arr2[idx2]
        idx2 += 1
        idx += 1
    return arr1


def sort_arr_contains_1_n(arr):
    """
    Sort an array which contains 1 to n values.
    :param arr:
    :return:
    """
    n = len(arr)
    for i in range(n):
        idx = i
        val = arr[i]
        while idx+1 != val:
            idx = val-1
            arr[val-1], val = val, arr[val-1]
    return arr


def sort_1_n_adj_swap(arrA, arrB):
    """
    Given an array, A of size n consisting of elements 1 to n. A boolean array B consisting of n-1 elements indicates
    that if B[i] is 1, then A[i] can be swapped with A[i+1].
    Find out if A can be sorted by swapping elements.
    :param arrA:
    :param arrB:
    :return:
    """
    for i in range(len(arrB)):
        if arrA[i] != i+1:
            arrA[i], arrA[i+1] = arrA[i+1], arrA[i]
    for i in range(len(arrA)):
        if arrA[i] != i+1:
            return False
    return True


if __name__ == "__main__":
    arr = [6, 5, 3, 2, 8, 10, 9]
    print("ksorted array is", ksorted_array(copy.deepcopy(arr), 3))
    print("ksorted array is", ksorted_array_heap(arr, 3))
    arr = [10, 5, 6, 3, 2, 20, 100, 80]
    print("wave sort", wave_sort(copy.deepcopy(arr)))
    print("wave sort", wave_sort1(copy.deepcopy(arr)))
    arr1 = [2, -1, 7, -1, -1, 10, -1]
    arr2 = [5, 8, 12, 14]
    print("merge one array of size n into another one of size mn", merge_n_arr(arr1, arr2))
    arr = [10, 7, 9, 2, 8,
                 3, 5, 4, 6, 1]
    print("sort an array which contains 1 to n values", sort_arr_contains_1_n(arr))
    arrA = [2, 3, 1, 4, 5, 6]
    arrB = [0, 1, 1, 1, 1]
    print("arrA can be sorted?", sort_1_n_adj_swap(arrA, arrB))

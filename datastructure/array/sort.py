"""
Sorting
"""
import heapq
import copy
import sys


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
    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


def merge_n_arr(arr1, arr2):
    idx1 = len(arr1)
    for i in range(len(arr1) - 1, -1, -1):
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
        while idx + 1 != val:
            idx = val - 1
            arr[val - 1], val = val, arr[val - 1]
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
        if arrA[i] != i + 1:
            arrA[i], arrA[i + 1] = arrA[i + 1], arrA[i]
    for i in range(len(arrA)):
        if arrA[i] != i + 1:
            return False
    return True


def partition_sort(arr):
    """
    Sort an array containing two types of elements.
    :param arr:
    :return:
    """
    i = j = 0
    while j < len(arr):
        if arr[j] < 1:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    return arr


def sort_by_frequency(arr):
    """
    Sort elements by frequency, if frequency is same than keep the origin order.
    1. Sort the element.
    2. Scan the sorted array and construct a 2D array of element and count.
    3. Sort the 2D array according to count.
    :param arr:
    :return:
    """

    class Element:
        def __init__(self, index, count, val):
            self.index = index
            self.count = count
            self.val = val

    n = len(arr)
    eles = [Element(i, 0, arr[i]) for i in range(n)]
    eles.sort(key=lambda e: e.val)
    eles[0].count = 1
    for i in range(1, n):
        if eles[i].val == eles[i - 1].val:
            eles[i].count = eles[i - 1].count + 1
            eles[i - 1].count = -1
            eles[i].index = eles[i - 1].index
        else:
            eles[i].count = 1
    eles.sort(key=lambda e: (-e.count, e.index))
    idx = 0
    for i in range(n):
        if eles[i].count != -1:
            for j in range(eles[i].count):
                arr[idx] = eles[i].val
                idx += 1
    return arr


def count_inversion(arr):
    """
    Count inversions in an array.
    Inversion Count for an array indicates--how far(close) the array from being sorted.
    Formally speaking, two elements form an inversion if arr[i]>arr[j] and i<j.
    :param arr:
    :return:
    """
    return merge_sort(arr, 0, len(arr) - 1, [0] * len(arr))


def merge_sort(arr, left, right, tmp):
    if left >= right:
        return 0
    mid = (left + right) // 2
    c_left = merge_sort(arr, left, mid, tmp)
    c_right = merge_sort(arr, mid + 1, right, tmp)
    cross = merge(arr, left, right, tmp)
    return c_left + c_right + cross


def merge(arr, left, right, tmp):
    mid = (left + right) // 2
    i, j = left, mid + 1
    count = 0
    idx = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tmp[idx] = arr[i]
            i += 1
        else:
            tmp[idx] = arr[j]
            j += 1
            count += (mid - i + 1)
        idx += 1
    while i <= mid:
        tmp[idx] = arr[i]
        idx += 1
        i += 1
    while j <= right:
        tmp[idx] = arr[j]
        idx += 1
        j += 1
    idx = 0
    for i in range(left, right + 1):
        arr[i] = tmp[idx]
        idx += 1
    return count


def two_ele_sum_closest_zero(arr):
    """
    Find the two elements whose sum is closet to zero.
    1. Sort the array.
    2. Use two index variables i and j from left and right ends respectively. Initialize i as 0 and j as n-1.
    3. sum = a[i]+a[j].
    4. Keep track of abs min sum.
    5. if sum is -ev, i++.
    6. if sum is +ev, l--.
    7. Repeat 3,4,5,6 while i<l.
    :param arr:
    :return:
    """
    arr.sort()
    i, j = 0, len(arr) - 1
    s = sys.maxsize
    a = b = 0
    while i < j:
        cur_sum = arr[i] + arr[j]
        if abs(cur_sum) < s:
            s = abs(cur_sum)
            a, b = arr[i], arr[j]
        if cur_sum < 0:
            i += 1
        else:
            j -= 1
    return a, b, s


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
    arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
    arr = [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1]
    print("Sort is", partition_sort(arr))
    arr = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
    print("Sort by frequency", sort_by_frequency(arr))
    arr = [1, 20, 6, 4, 5]
    print("Inversion count", count_inversion(arr))
    arr = [1, 60, -10, 70, -80, 85]
    print("Closest to zero elements is %s, %s, sum is %s" % two_ele_sum_closest_zero(arr))

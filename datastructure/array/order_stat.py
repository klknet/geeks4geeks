import sys
import heapq
from datastructure.array.max_heap import MaxHeap


def kth_smallest(arr, k):
    """
    Find the kth smallest element.
    :param arr:
    :param k:
    :return:
    """
    return quick_select(arr, 0, len(arr) - 1, k)


def quick_select(arr, l, r, k):
    if l <= r:
        p = partition(arr, l, r)
        if p == k - 1:
            return arr[p]
        elif p < k - 1:
            return quick_select(arr, p + 1, r, k)
        else:
            return quick_select(arr, l, p - 1, k)


def partition(arr, l, r):
    p = arr[r]
    i = j = l
    while j < r:
        if arr[j] < p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def largest_3_elements(arr):
    """
    Find the largest 3 elements in an array.
    :param arr:
    :return:
    """
    f = s = t = -sys.maxsize
    for i in range(len(arr)):
        if arr[i] > f:
            t = s
            s = f
            f = arr[i]
        elif arr[i] > s:
            t = s
            s = arr[i]
        elif arr[i] > t:
            t = arr[i]
    return f, s, t


def median_of_stream(arr):
    """
    Median of Stream of Running integers.
    Using maximum heap and minimum heap. Left array storing min part using maximum heap, Right array storing max part using
    minimum heap, if left.size == right.size, then cur is median.
    :param arr:
    :return:
    """
    median = 0
    # max heap
    left = []
    # min heap
    right = []
    res = []
    for ele in arr:
        if len(left) == len(right):
            if ele > median:
                heapq.heappush(right, ele)
                median = right[0]
                res.append(median)
            else:
                heapq.heappush(left, -ele)
                median = -left[0]
                res.append(median)
        elif len(left) > len(right):
            if ele > median:
                heapq.heappush(right, ele)
            else:
                heapq.heappush(right, -heapq.heappop(left))
                heapq.heappush(left, -ele)
            median = (right[0] - left[0]) / 2
            res.append(median)
        else:
            if ele > median:
                heapq.heappush(left, -heapq.heappop(right))
                heapq.heappush(right, ele)
            else:
                heapq.heappush(left, -ele)
            median = (right[0] - left[0]) / 2
            res.append(median)
    return res


def k_max_combination(arr1, arr2, k):
    """
    K maximum sum combinations from two arrays.
    :param arr1:
    :param arr2:
    :param k:
    :return:
    """
    unique = set()
    heap = MaxHeap()
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            s = arr1[i] + arr2[j]
            if s not in unique:
                unique.add(s)
                heap.push(s)
    while k > 0:
        print(heap.pop())
        k -= 1


def k_smallest_order(arr, k):
    """
    K smallest elements in same order using O(1) extra space.
    Using insert sort
    :param arr:
    :param k:
    :return:
    """
    for i in range(k, len(arr)):
        max_val = 0
        pos = k - 1
        j = pos
        while j >= 0:
            if arr[j] > max_val:
                max_val = arr[j]
                pos = j
            j -= 1
        if arr[i] < max_val:
            while pos < k - 1:
                arr[pos] = arr[pos + 1]
                pos += 1
            arr[pos] = arr[i]
    print(arr[:k])


def second_largest_element(arr):
    """
    Find second largest element in an array.
    :param arr:
    :return:
    """
    first = second = -sys.maxsize
    for data in arr:
        if data > first:
            second = first
            first = data
        elif data > second:
            second = data
    return second


def k_num_occurrence(arr, k):
    """
    Find k numbers with most occurrences in the given array.
    :param arr:
    :param k:
    :return:
    """
    freq = {}
    for key in arr:
        if key in freq:
            freq[key] += 1
        else:
            freq[key] = 1

    def orderby_val(item):
        return -item[1], -item[0]

    return list(map(lambda item: item[0], sorted(freq.items(), key=orderby_val)[:k]))


def smallest_second_arr(arr):
    """
    Find smallest and second smallest element in an array.
    :param arr:
    :return:
    """
    first = second = sys.maxsize
    for d in arr:
        if first > d:
            second = first
            first = d
        elif second > d != first:
            second = d
    return first, second


def find_smallest_missing_num(arr):
    """
    Find the first missing number.
    :param arr:
    :return:
    """
    return binary_search(arr, 0, len(arr) - 1)


def binary_search(arr, l, r):
    if l > r:
        return r + 1
    if arr[l] != l:
        return l
    m = int((l + r) / 2)
    if arr[m] > m:
        return binary_search(arr, l, m)
    else:
        return binary_search(arr, m + 1, r)


def max_no_adjacent(arr):
    """
    Maximum sum such that no two elements are adjacent.
    :param arr:
    :return:
    """
    incl = arr[0]
    excl = 0
    for i in range(1, len(arr)):
        incl, excl = excl + arr[i], max(incl, excl)
    return max(incl, excl)


def get_min_max(arr):
    if len(arr) == 0:
        return
    if len(arr) == 1:
        return arr[0], arr[0]
    if len(arr) & 1 == 0:
        if arr[0] < arr[1]:
            s, c = arr[0], arr[1]
        else:
            s, c = arr[1], arr[0]
        idx = 2
    else:
        s = c = arr[0]
        idx = 1
    for i in range(idx, len(arr)-1, 2):
        if arr[i] > arr[i+1]:
            if arr[i] > c:
                c = arr[i]
            if arr[i+1] < s:
                s = arr[i+1]
        else:
            if arr[i] < s:
                s = arr[i]
            if arr[i+1] > c:
                c = arr[i+1]
    return s,c



print(kth_smallest([12, 3, 5, 7, 19], 4))
print(largest_3_elements([12, 13, 1, 10, 34, 1]))
print(median_of_stream([-5, -10, 5, -8, 8]))
k_max_combination([1, 4, 2, 3], [2, 5, 1, 6], 4)
k_smallest_order([1, 5, 8, 9, 6, 7, 3, 4, 2, 0], 5)
print(second_largest_element([12, 35, 1, 10, 34, 1]))
print(k_num_occurrence([7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9], 4))
print(smallest_second_arr([12, 13, 1, 10, 34, 1]))
print(find_smallest_missing_num([4, 5, 10, 11]))
print(find_smallest_missing_num([0, 1, 3, 6, 9]))
print(max_no_adjacent([5, 5, 10, 100, 10, 5]))
print(get_min_max([1000, 11, 445, 1, 330, 3000]))
print("你好啊！abc"[5:])

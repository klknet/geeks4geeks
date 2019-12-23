import sys
import heapq


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


print(kth_smallest([12, 3, 5, 7, 19], 4))
print(largest_3_elements([12, 13, 1, 10, 34, 1]))
print(median_of_stream([-5, -10, 5, -8, 8]))
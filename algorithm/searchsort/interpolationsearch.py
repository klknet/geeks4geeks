def interpolation_search(arr, x):
    """
    Given a sorted array of n uniformly distributed values arr[],  we can use slope formula
    pos = lo + (x2-x1)/(y2-y1)*(x-y1)
    :param arr:
    :param x:
    :return:
    """
    n = len(arr)
    lo, hi = 0, n - 1
    while lo <= hi and arr[lo] <= x <= arr[hi]:
        pos = lo + int((hi - lo) / (arr[hi] - arr[lo]) * (x - arr[lo]))
        print('#', x, pos, '#')
        # int(((float(hi - lo) /(arr[hi] - arr[lo])) * (x - arr[lo])))
        if arr[pos] < x:
            lo = pos + 1
        elif arr[pos] > x:
            hi = pos - 1
        else:
            return pos
    return -1


if __name__ == '__main__':
    arr = list(range(0, 30, 2))
    print(arr)
    for i in range(-3, 33):
        # print(binary_search_recur(arr, i, 0, len(arr) - 1), end=" ")
        print(interpolation_search(arr, i), end=' ')
    print()
    arr = [10, 12, 13, 16, 18, 19, 20, 21, \
                22, 23, 24, 33, 35, 42, 47]
    print(interpolation_search(arr, 18))

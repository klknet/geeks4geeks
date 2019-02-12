def ternarysearch(arr, x):
    n = len(arr)
    l, r = 0, n - 1
    while l <= r:
        mid1, mid2 = l + (r - l) // 3, r - (r - l) // 3
        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2
        if arr[mid1] > x:
            r = mid1 - 1
        elif arr[mid2] < x:
            l = mid2 + 1
        else:
            l, r = mid1 + 1, mid2 - 1
    return -1


def ternarysearch_recr(arr, x, l, r):
    if l <= r:
        mid1, mid2 = l + (r - l) // 3, r - (r - l) // 3
        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2
        if arr[mid1] > x:
            return ternarysearch_recr(arr, x, l, mid1 - 1)
        elif arr[mid2] < x:
            return ternarysearch_recr(arr, x, mid2 + 1, r)
        else:
            return ternarysearch_recr(arr, x, mid1 + 1, mid2 - 1)
    return -1


if __name__ == '__main__':
    arr = list(range(0, 30, 3))
    for i in range(-3, 33):
        # print(binary_search_recur(arr, i, 0, len(arr) - 1), end=" ")
        print(ternarysearch_recr(arr, i, 0, len(arr) - 1), end=" ")
        # print(ternarysearch(arr, i), end=" ")

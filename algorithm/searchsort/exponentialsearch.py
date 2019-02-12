import algorithm.searchsort.binarysearch as bs


def exponentialsearch(arr, x):
    if arr[0] == x:
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] <= x:
        i *= 2
    return bs.binary_search_itr(arr, x, i >> 1, min(i, n)-1)


if __name__ == '__main__':
    arr = list(range(0, 30, 2))
    # print(exponentialsearch(arr, 4))
    for i in range(-3, 33):
        print(exponentialsearch(arr, i))

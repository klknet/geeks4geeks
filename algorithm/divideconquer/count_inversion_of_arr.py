"""
Count inversions in an array.
Enhance merge sort:
Suppose we know the number of inversions in the left half and right half of the array(let be inv1 and inv2), what kinds
of inversions are not accounted for in inv1+inv2? The answer is - the inversions we have to count in the merge step.
Therefore, to get the number of inversions, we need to add number of inversions in left subarray, right subarray and merge().
How to get number of inversions in merge()?
In merge process, let i is used for indexing left subarray and j for right subarray. At any step in merge(), if a[i] is
greater than a[j], then there are (mid-i+1) inversions. Because left and right subarrays are sorted, so all the remaining
elements in left subarray a[i..n/2] will be greater than a[j].
"""


def merge_count(arr, l, r, temp):
    if l == r:
        return 0
    m = (l + r) >> 1
    inv1 = merge_count(arr, l, m, temp)
    inv2 = merge_count(arr, m + 1, r, temp)
    cross_inv = merge(arr, l, r, m, temp)
    return inv1 + inv2 + cross_inv


def merge(arr, l, r, m, temp):
    i, j = l, m+1
    c = 0
    k = l
    while i <= m and j <= r:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            c += m - i + 1
            j += 1
        k += 1
    while i <= m:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= r:
        temp[k] = arr[j]
        j += 1
        k += 1
    for i in range(l, r + 1):
        arr[i] = temp[i]
    return c


arr = [1, 20, 6, 4, 5]
temp = [0] * len(arr)
print(merge_count(arr, 0, len(arr) - 1, temp))

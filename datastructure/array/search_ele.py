"""
Search an element in a sorted and rotated array.
"""


def pivot_index(arr, low, high):
    if low > high:
        return -1
    mid = int((low + high) / 2)
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid-1
    if arr[low] > arr[mid]:
        return pivot_index(arr, mid+1, high)
    return pivot_index(arr, low, mid - 1)


def binary_search(arr, low, high, e):
    while low <= high:
        mid = int((low + high) / 2)
        if arr[mid] < e:
            low = mid + 1
        elif arr[mid] > e:
            high = mid - 1
        else:
            return mid
    return -1


def search_ele(arr, e):
    p = pivot_index(arr, 0, len(arr) - 1)
    # the array doesn't rotate at all.
    if p == -1:
        return binary_search(arr, 0, len(arr)-1, e)
    if arr[p] == e:
        return p
    if arr[0] > e:
        return binary_search(arr, p+1, len(arr) - 1, e)
    return binary_search(arr, 0, p-1, e)


arr = [5, 6, 1, 2, 3, 4]
# arr = [1, 2, 3, 4, 5, 6, 7]
print(search_ele(arr, 10))
for i in arr:
    print(search_ele(arr, i))

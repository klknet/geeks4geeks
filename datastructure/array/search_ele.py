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


def search_ele1(arr, e):
    return search(arr, 0, len(arr)-1, e)


def search(arr, low, high, e):
    if low > high:
        return -1
    mid = int((low + high)/2)
    if arr[mid] == e:
        return mid
    # left arr[l...mid] is sorted.
    if arr[low] <= arr[mid]:
        # As this subarray is sorted, we can quickly check if key lies in half or other half.
        if arr[low] <= e < arr[mid]:
            return search(arr, low, mid-1, e)
        else:
            return search(arr, mid+1, high, e)
    #If arr[l...mid] is not sorted, then arr[mid...high] must be sorted subarray.
    if arr[mid] < e <= arr[high]:
        return search(arr, mid+1, high, e)
    return search(arr, low, mid-1, e)



arr = [5, 6, 1, 2, 3, 4]
# arr = [1, 2, 3, 4, 5, 6, 7]
# print(search_ele(arr, 10))
for i in arr:
    # print(search_ele(arr, i))
    print(search_ele1(arr, i))

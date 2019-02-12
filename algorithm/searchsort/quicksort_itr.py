import random


def quick_sort(arr):
    n = len(arr)
    stack = [0]*n
    top = -1
    l, r = 0, n-1
    top += 1
    stack[top] = l
    top += 1
    stack[top] = r
    while top>=0:
        r = stack[top]
        top -= 1
        l = stack[top]
        top -= 1
        p = _partition(arr, l, r)
        if p-1>l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p-1
        if p+1<r:
            top += 1
            stack[top] = p+1
            top += 1
            stack[top] = r


def _partition(arr, l, r):
    r_idx = random.randint(l, r)
    pivot = arr[r_idx]
    arr[r_idx], arr[r] = arr[r], pivot
    # index of small ele
    i = l-1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            if i != j:
                arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[r] = pivot, arr[i+1]
    return i+1


if __name__ == '__main__':
    arr = [4, 3, 5, 2, 1, 3, 2, 3]
    quick_sort(arr)
    print(arr)
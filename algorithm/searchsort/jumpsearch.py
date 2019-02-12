import math


def jump_search(arr, x, step):
    n = len(arr)
    if arr[0] > x or arr[n - 1] < x:
        return -1
    i = 0
    while i < n:
        if arr[i] == x:
            return i
        elif arr[i] > x:
            for j in range(i - step + 1, i):
                if arr[j] == x:
                    return j
            break
        elif i + step >= n:
            for j in range(i, n):
                if arr[j] == x:
                    return j
            break
        i += step
    return -1


def jump_search_1(arr, x, n):
    if arr[0] > x or arr[n - 1] < x:
        return -1
    step = s = math.sqrt(n)
    prev = 0
    # find the block in which x place
    while arr[min(int(step), n) - 1] < x:
        prev = step
        step += s
    # Doing a linear search for x in block beginning with prev
    while arr[int(prev)] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[int(prev)] == x:
        return int(prev)
    return -1


if __name__ == '__main__':
    arr = list(range(0, 32, 2))
    step = int(math.sqrt(len(arr)))
    for i in range(-3, 35):
        print(i, '=', jump_search_1(arr, i, len(arr)))
        # print(jump_search(arr, i, step))

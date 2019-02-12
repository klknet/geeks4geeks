# Find k closest elements to a given value
def cross_over_pt(arr, x):
    """
    Find the cross over point
    the point before which elements is smaller than or equal to x and after which elements is greater than x
    :param arr:
    :param x:
    :return:
    """
    n = len(arr) - 1
    l, r = 0, n
    if x < arr[l]:
        return l
    if x >= arr[r]:
        return r
    while l <= r:
        mid = (l + r) >> 1
        if arr[mid] <= x < arr[mid + 1]:
            return mid
        elif x > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def find_k_closest(arr, k, x):
    """
    Find cross over point, search before and after, fill up the smaller element
    :param arr:
    :param k:
    :param x:
    :return:
    """
    idx = cross_over_pt(arr, x)
    v = arr[idx]
    if idx == -1:
        pass
    res = []
    total, n = 0, len(arr)
    l, r = idx, idx + 1
    if arr[idx] == x:
        l = idx - 1
    while l >= 0 and r < n and total < k:
        total += 1
        if x - arr[l] < arr[r] - x:
            res.append(arr[l])
            l -= 1
        else:
            res.append(arr[r])
            r += 1
    while total < k and l >= 0:
        res.append(arr[l])
        l -= 1
        total += 1
    while total < k and r < n:
        res.append(arr[r])
        r += 1
        total += 1
    return res


if __name__ == '__main__':
    arr = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
    print(arr)
    print(find_k_closest(arr, 4, 12))

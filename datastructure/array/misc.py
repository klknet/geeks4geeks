def subsequence(arr):
    """
    Find all subsequences of a string.
    :param arr:
    :return:
    """
    res = []
    subsequence_util(arr, len(arr) - 1, res)
    return res


def subsequence_util(arr, n, res):
    if n == 0:
        res.append(arr[n])
        return
    subsequence_util(arr, n - 1, res)
    tmp = len(res)
    for i in range(tmp):
        res.append(res[i] + arr[n])
    res.append(arr[n])


def subsequence_bit(arr):
    n = len(arr)
    total = 2 ** n - 1
    res = []
    for counter in range(1, total + 1):
        r = ''
        for i in range(n):
            if counter & (1 << i):
                r += arr[i]
        res.append(r)
    return res


def num_of_product_k(arr, k):
    """
    Number of subarrays with given product.
    :param arr:
    :param k:
    :return:
    """
    if k == 1:
        return find_ones(arr)
    else:
        return find_num_subarray_product(arr, k)


def find_num_product(arr):
    s = e = -1
    res = 0
    for i in range(len(arr)):
        if arr[i] == 1 and s == -1:
            s = i
            e = i
        elif arr[i] == 1:
            e += 1
        elif s != -1:
            res += (e - s + 1) * (e - s + 2) // 2
            s = e = -1
    return res


def find_ones(arr):
    i = 0
    res = 0
    while i < len(arr):
        if arr[i] == 1:
            total = 0
            while i < len(arr) and arr[i] == 1:
                i += 1
                total += 1
            res += total * (total + 1) // 2
        i += 1
    return res


def find_num_subarray_product(arr, k):
    s = e = 0
    p = 1
    res = 0
    countOnes = 0
    while e < len(arr):
        while e < len(arr) and p < k:
            p *= arr[e]
            e += 1
        while s < e and p > k:
            p //= arr[s]
            s += 1
        if p == k:
            while e < len(arr) and arr[e] == 1:
                countOnes += 1
                e += 1
            res += countOnes + 1
            while s < e and arr[s] == 1:
                s += 1
                res += countOnes + 1
            p //= arr[s]
            countOnes = 0
    return res


if __name__ == '__main__':
    arr = ['1', '2', '3', '4']
    print("subsequence", subsequence(arr))
    print("subsequence", subsequence_bit(arr))
    arr = [2, 1, 1, 1, 4, 5]
    k = 4
    print("Number of subarrays", num_of_product_k(arr, k))
    arr = [1, 2, 3, 4, 1]
    arr = [2, 1, 1, 1, 3, 1, 1, 4]
    k = 24
    k = 1
    print("Number of subarrays", num_of_product_k(arr, k))

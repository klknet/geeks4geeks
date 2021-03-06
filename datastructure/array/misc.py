import sys


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


def find_arr_sub_arr(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i = j = 0
    equal_count = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            i += 1
            j += 1
            equal_count += 1
        elif arr1[i] < arr2[j]:
            j += 1
        else:
            i += 1
    return equal_count == len(arr2)


def check_consecutive(arr):
    n = len(arr)
    min_v = min(arr)
    max_v = max(arr)
    if max_v - min_v + 1 == n:
        visited = [False] * n
        for i in arr:
            if not visited[i - min_v]:
                visited[i - min_v] = True
            else:
                return False
        return True
    return False


def find_complement(arr1, arr2):
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            print(arr1[i], end='  ')
            i += 1
        else:
            j += 1
    if i < len(arr1):
        print(arr1[i:])


def minimum_incr_operation(arr, k):
    """
    Minimum increment by k operations to make all elements equal.
    :param arr:
    :param k:
    :return:
    """
    m = max(arr)
    t = 0
    for i in arr:
        if (m - i) % k == 0:
            t += (m - i) // k
        else:
            return -1
    return t


def minimum_difference_max_min(A, B, C):
    """
    Minimum min(max(A[i],B[j],C[k])-min(A[i],B[j],C[k])) of three different sorted arrays.
    :param A:
    :param B:
    :param C:
    :return:
    """
    i, j, k = len(A) - 1, len(B) - 1, len(C) - 1
    d = sys.maxsize
    while i >= 0 and j >= 0 and k >= 0:
        max_v = max(A[i], B[j], C[k])
        min_v = min(A[i], B[j], C[k])
        d = min(d, max_v - min_v)
        if A[i] == max_v:
            i -= 1
        elif B[j] == max_v:
            j -= 1
        else:
            k -= 1
    return d


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
    arr = [5, 4, 2, 3, 1, 6]
    print("consecutive", check_consecutive(arr))
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]
    print(find_arr_sub_arr(arr1, arr2))
    find_complement(arr1, arr2)
    arr = [4, 7, 19, 16]
    arr = [4, 2, 6, 8]
    k = 3
    print('minimum increment operation', minimum_incr_operation(arr, k))
    A = [1, 4, 5, 8, 10]
    B = [6, 9, 15]
    C = [2, 3, 6, 6]
    print(minimum_difference_max_min(A, B, C))

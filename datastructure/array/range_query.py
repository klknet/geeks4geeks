"""
Range Queries.
"""
import math

lookup = None
lookup1 = None
frequency = None


def sparse_table(arr, l, r):
    """
    build a lookup[i][j] table where i is range in [0, n] and j is range in [0, sqrt(n)],
    and respond in arr[i] to arr[i+2^j -1]
    :param arr:
    :param l:
    :param r:
    :return:
    """
    global lookup
    sqrt = math.floor(math.sqrt(len(arr)))
    if lookup is None:
        lookup = [[0 for i in range(sqrt)] for j in range(len(arr))]
        for i in range(len(arr)):
            lookup[i][0] = arr[i]
        for j in range(1, sqrt):
            i = 0
            while i + (1 << j) - 1 < len(arr):
                if lookup[i][j - 1] < lookup[i + (1 << (j - 1))][j - 1]:
                    lookup[i][j] = lookup[i][j - 1]
                else:
                    lookup[i][j] = lookup[i + (1 << (j - 1))][j - 1]
                i += 1
    j = math.floor(math.log(r - l + 1, 2))
    if lookup[l][j] < lookup[r - (1 << j) + 1][j]:
        return lookup[l][j]
    return lookup[r - (1 << j) + 1][j]


def sparse_table_sum(arr, l, r):
    global lookup1
    k = 16
    if lookup1 is None:
        lookup1 = [[0 for i in range(k)] for j in range(len(arr))]
        n = len(arr)
        for i in range(n):
            lookup1[i][0] = arr[i]
        for j in range(1, k + 1):
            i = 0
            while i + (1 << j) - 1 < n:
                lookup1[i][j] = lookup1[i][j - 1] + lookup1[i + (1 << (j - 1))][j - 1]
                i += 1
    res = 0
    for i in range(k, -1, -1):
        if l + (1 << i) - 1 <= r:
            res += lookup1[l][i]
            l += (1 << i)
    return res


def range_frequencies(arr, l, r, ele):
    """
    using a map store element's occurrence position, find lower_bound of l and upper_bound of r,
    then result is r-l
    :param arr:
    :param l:
    :param r:
    :param ele:
    :return:
    """
    global frequency
    if frequency is None:
        frequency = {}
        for i in range(len(arr)):
            if arr[i] in frequency:
                frequency[arr[i]].append(i)
            else:
                frequency[arr[i]] = [i]
    ran = frequency[ele]
    return binary_search_greater(ran, 0, len(ran) - 1, r) - binary_search(ran, 0, len(ran) - 1, l)


def binary_search(arr, l, r, e):
    if l <= r:
        m = int((l + r) / 2)
        if m > l and arr[m - 1] < e <= arr[m]:
            return m
        if m == l and arr[m] >= e:
            return m
        if arr[m] < e:
            return binary_search(arr, m + 1, r, e)
        else:
            return binary_search(arr, l, m, e)
    return -1


def binary_search_greater(arr, l, r, e):
    if arr[r] <= e:
        return r + 1
    if l <= r:
        m = int((l + r) / 2)
        if m > l and arr[m - 1] <= e < arr[m]:
            return m
        if m == l and arr[m] > e:
            return m
        if arr[m] <= e:
            return binary_search_greater(arr, m + 1, r, e)
        else:
            return binary_search_greater(arr, l, m, e)
    return -1


def constant_add(arr, l, r, delta):
    n = len(arr)
    arr[l] += delta
    if r + 1 < n:
        arr[r + 1] -= delta


def update_arr(arr):
    for i in range(1, len(arr)):
        arr[i] += arr[i - 1]
    return arr


tree = [0] * 1000


def lcm_build(arr, node, start, end):
    """
    find lcm in range queries.
    using segment tree.
    :param arr:
    :param node:
    :param start:
    :param end:
    :return:
    """
    global tree
    if start == end:
        tree[node] = arr[start]
        return arr[start]
    mid = int((end + start) / 2)
    left_lcm = lcm_build(arr, node * 2, start, mid)
    right_lcm = lcm_build(arr, node * 2 + 1, mid + 1, end)
    tree[node] = lcm(left_lcm, right_lcm)
    return tree[node]


def query_lcm(node, start, end, l, r):
    global tree
    if start > r or end < l:
        return 1
    if start >= l and r >= end:
        return tree[node]
    mid = int((start + end) / 2)
    left_lcm = query_lcm(node * 2, start, mid, l, r)
    right_lcm = query_lcm(node * 2 + 1, mid + 1, end, l, r)
    return lcm(left_lcm, right_lcm)


def lcm(a, b):
    """
    lowest common multiple
    lcm(a,b) = a*b/gcd(a,b)
    :param a:
    :param b:
    :return:
    """
    return int(a * b / gcd(max(a, b), min(a, b)))


def gcd(a, b):
    """
    greatest common divisor.
    gcd(a,b) = gcd(b, a%b) a>b
    :param a:
    :param b:
    :return:
    """
    if a < b:
        return gcd(b, a)
    return a if b == 0 else gcd(b, a % b)


gcd_tree = None


def gcd_construct(arr, node, start, end):
    global gcd_tree
    if gcd_tree is None:
        n = 2 ** ((math.ceil(math.log(len(arr), 2))) + 1)
        gcd_tree = [0] * n
    if start == end:
        gcd_tree[node] = arr[start]
        return arr[start]
    mid = int((start + end) / 2)
    left_gcd = gcd_construct(arr, node * 2 + 1, start, mid)
    right_gcd = gcd_construct(arr, node * 2 + 2, mid + 1, end)
    gcd_tree[node] = gcd(left_gcd, right_gcd)
    return gcd_tree[node]


def gcd_query(node, start, end, l, r):
    global gcd_tree
    # out of range
    if end < l or start > r:
        return 0
    # inside range
    if l <= start and r >= end:
        return gcd_tree[node]
    mid = (start + end) // 2
    left_gcd = gcd_query(node * 2 + 1, start, mid, l, r)
    right_gcd = gcd_query(node * 2 + 2, mid + 1, end, l, r)
    return gcd(left_gcd, right_gcd)


prefix_tree = None
suffix_tree = None


def build_out_range_gcd(arr):
    global prefix_tree
    global suffix_tree
    if prefix_tree is None or suffix_tree is None:
        prefix_tree = [0] * len(arr)
        suffix_tree = [0] * len(arr)
        prefix_tree[0] = arr[0]
        suffix_tree[-1] = arr[-1]
        for i in range(1, len(arr)):
            prefix_tree[i] = gcd(prefix_tree[i - 1], arr[i])
        for i in range(len(arr) - 2, -1, -1):
            suffix_tree[i] = gcd(suffix_tree[i + 1], arr[i])


def query_out_range_gcd(arr, l, r):
    global prefix_tree
    global suffix_tree
    n = len(arr)
    if l == 0:
        return suffix_tree[r + 1]
    if r == n - 1:
        return prefix_tree[l - 1]
    return gcd(prefix_tree[l - 1], suffix_tree[r + 1])


def count_ele(arr, l, r):
    arr.sort()
    return upper_bin(arr, r) - lower_bin(arr, l) + 1


def lower_bin(arr, x):
    l, h = 0, len(arr) - 1
    while l <= h:
        m = (l + h) // 2
        if arr[m] >= x:
            h = m - 1
        else:
            l = m + 1
    return l


def upper_bin(arr, x):
    l, h = 0, len(arr) - 1
    while l <= h:
        m = (l + h) // 2
        if arr[m] <= x:
            l = m + 1
        else:
            h = m - 1
    return h


if __name__ == '__main__':
    arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]
    print(sparse_table(arr, 0, 4))
    print(sparse_table(arr, 4, 7))
    print(sparse_table(arr, 7, 8))

    arr = [3, 7, 2, 5, 8, 9]
    assert sparse_table_sum(arr, 0, 5) == 34
    assert sparse_table_sum(arr, 3, 5) == 22
    assert sparse_table_sum(arr, 2, 4) == 15

    arr = [2, 8, 6, 9, 8, 6, 8, 2, 11]
    assert range_frequencies(arr, 0, 5, 2) == 1
    assert range_frequencies(arr, 3, 8, 8) == 2

    arr = [0] * 6
    constant_add(arr, 0, 2, 100)
    constant_add(arr, 1, 5, 100)
    constant_add(arr, 2, 3, 100)

    print(update_arr(arr))
    arr = [5, 7, 5, 2, 10, 12, 11, 17, 14, 1, 44]
    lcm_build(arr, 1, 0, len(arr) - 1)
    print(query_lcm(1, 0, len(arr) - 1, 2, 5))
    print(query_lcm(1, 0, len(arr) - 1, 5, 10))
    print(query_lcm(1, 0, len(arr) - 1, 0, 10))

    arr = [2, 3, 6, 9, 5]
    gcd_construct(arr, 0, 0, len(arr) - 1)
    print(gcd_query(0, 0, len(arr) - 1, 1, 3))
    print(gcd_query(0, 0, len(arr) - 1, 2, 3))

    arr = [2, 6, 9]
    build_out_range_gcd(arr)
    print(query_out_range_gcd(arr, 0, 0))
    print(query_out_range_gcd(arr, 1, 1))
    print(query_out_range_gcd(arr, 1, 2))

    arr = [1, 4, 4, 9, 10, 3]
    print(count_ele(arr, 1, 4))
    print(count_ele(arr, 9, 12))
"""
Longest even length substring such that Sum of First and Second half is same.
"""


def find_length(arr):
    n = len(arr)
    max_len = 0
    for i in range(n):
        for j in range(i + 1, n, 2):
            l, r = i, j
            left_sum = right_sum = 0
            while l < r:
                left_sum += int(arr[l])
                right_sum += int(arr[r])
                l += 1
                r -= 1
            if left_sum == right_sum:
                max_len = max(max_len, j - i + 1)
    return max_len


def find_length_dp(arr):
    n = len(arr)
    Sum = [0] * (n + 1)
    for i in range(1, n + 1):
        Sum[i] += Sum[i - 1] + int(arr[i - 1])
    max_len = 0
    for length in range(2, n + 1, 2):
        for i in range(0, n - length + 1):
            j = i + length - 1
            if Sum[i + length // 2] - Sum[i] == Sum[j + 1] - Sum[i + length // 2]:
                max_len = max(max_len, length)
    return max_len


def find_length_opt(arr):
    """
    O(n^2) and O(1) extra space
    :param arr:
    :return:
    """
    n = len(arr)
    max_len = 0
    for i in range(0, n - 1):
        l, r = i, i + 1
        lsum = rsum = 0
        while l >= 0 and r < n:
            lsum += int(arr[l])
            rsum += int(arr[r])
            if lsum == rsum:
                max_len = max(max_len, r - l + 1)
            l -= 1
            r += 1
    return max_len


s = '123123'
print(find_length(s))
print(find_length_dp(s))
print(find_length_opt(s))
s = '1538023'
print(find_length(s))
print(find_length_dp(s))
print(find_length_opt(s))

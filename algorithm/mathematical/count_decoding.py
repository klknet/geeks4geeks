"""
Count possible decodings of a given digit sequence.
"""


def count_decodings(arr, n):
    if n < 1:
        return 1
    res = 0
    if arr[n] != 0:
        res += count_decodings(arr, n - 1)
    if (arr[n-1] == 1 or arr[n-1] == 2) and arr[n] < 7:
        res += count_decodings(arr, n - 2)
    return res


def count_decoding_dp(arr, n, dp):
    if n < 1:
        return 1
    if dp[n] != -1:
        return dp[n]
    res = 0
    if arr[n] != 0:
        res += count_decoding_dp(arr, n - 1, dp)
    if (arr[n-1] == 1 or arr[n-1] == 2) and arr[n] < 7:
        res += count_decoding_dp(arr, n - 2, dp)
    dp[n] = res
    return res


arr = [1, 2, 2, 0, 4]
print(count_decodings(arr, len(arr) - 1))
print(count_decoding_dp(arr, len(arr) - 1, [-1] * len(arr)))

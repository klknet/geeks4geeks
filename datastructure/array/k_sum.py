"""
Count of subarrays with sum at least K.
Approach: For a fixed left index say l, try to find the first index on the right of l(say r) such that (arr[l]+arr[l+1]
+...+arr[r])>=k. Then add N-r+1 to the required answer. Repeat this process for all the left indices.
"""


def k_sum(arr, k):
    ans = 0
    r = 0
    s = 0
    for l in range(len(arr)):
        while s < k:
            if r == len(arr):
                break
            s += arr[r]
            r += 1
        if s < k:
            break
        ans += len(arr) - r + 1
        s -= arr[l]
    return ans


print(k_sum([6, 1, 2, 7], 10))

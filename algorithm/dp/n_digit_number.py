"""
Given two integers n and sum, find count of all n digit numbers with sum of digits as 'sum'. Leading 0's are not counted
as digits.
1<=n<=100 and 1<=sum<=500
The idea is simple, we subtract all values from 0 to 9 from given sum and recur for sum minus that digit. Below is
recursive formula.
countRec(n, sum) = ∑countRec(n-1, sum-i) where i varies from 0 to 9.
"""

lookup = [[-1 for col in range(501)] for row in range(101)]


# lookup[0][0] = 1


def count_dp(n, s):
    if n == 0:
        return 1 if s == 0 else 0
    if s == 0:
        return 1
    if lookup[n][s] != -1:
        return lookup[n][s]
    ans = 0
    for i in range(10):
        if s - i >= 0:
            ans += count_dp(n - 1, s - i)
    lookup[n][s] = ans
    return ans


def count_dp_driver(n, s):
    ans = 0
    for i in range(1, 10):
        if s - i >= 0:
            ans += count_dp(n - 1, s - i)
    return ans


def count_recur(n, s):
    if n == 0:
        return s == 0
    if s == 0:
        return 1
    ans = 0
    for i in range(10):
        if s - i >= 0:
            ans += count_recur(n - 1, s - i)
    return ans


def count_driver(n, s):
    ans = 0
    for i in range(1, 10):
        if s - i >= 0:
            ans += count_recur(n - 1, s - i)
    return ans


def find_count(n, s):
    start = 10 ** (n - 1)
    end = 10 ** n - 1
    count = 0
    i = start
    while i <= end:
        temp = i
        cur = 0
        while temp != 0:
            cur += (temp % 10)
            temp //= 10
        if cur == s:
            count += 1
            i += 9
        else:
            i += 1
    return count


n, s = 90, 15
# print(count_driver(n, s))
print(count_dp_driver(n, s))
# print(find_count(n, s))
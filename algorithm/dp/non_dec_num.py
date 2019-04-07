"""
Total number of non-decreasing numbers with n digits.
A number is non-decreasing if every digit is greater than or equal to previous digit. So given the number of digits n, you
are required to find the count of total non-decreasing numbers with n digits.
One way to look at the problem is, count of numbers is equal to count n digit number ending with 9 plus count of ending
with 8 plus count for 7 and so on. How to count ending with a particular digit? We can recur for n-1 length and digits
smaller than or equal to the last digit. So below is the recursive formula.

"""


def total_non_decreasing(n, d):
    if n == 1:
        return 1
    count = 0
    for k in range(d+1):
        count += total_non_decreasing(n - 1, d - k)
    return count


def total_driver(n):
    count = 0
    for k in range(10):
        count += total_non_decreasing(n, k)
    return count


def total_num_dp(n):
    t = [[0 for col in range(10)] for row in range(n)]
    for i in range(10):
        t[0][i] = 1
    for i in range(1, n):
        for j in range(10):
            for k in range(j+1):
                t[i][j] += t[i-1][k]
    res = t[n-1]
    return sum(res)


n = 20
# print(total_driver(n))
print(total_num_dp(n))

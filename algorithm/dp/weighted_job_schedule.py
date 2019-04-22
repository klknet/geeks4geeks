"""
Given N jobs where every job is represented by following three elements of it:
1.Start time
2.End time
3.Profit or value associated

The above problem can solved using following recursive solution:
1)First sort jobs according to finish time.
2)Now applying following recursive process.
 maxProfit(arr, n) = max( maxProfit(arr, n-1), arr[n]+maxProfit(arr, prev)
 where prev is first job that ending time is before current starting time.

 The idea is to find the latest job before the current job that doesn't conflict with current job.
"""


def max_profit_schedule(arr, n):
    if n == 0:
        return arr[n].profit
    prev = prev_job(arr, n)
    incl = arr[n].profit
    if prev != -1:
        incl += max_profit_schedule(arr, prev)
    excl = max_profit_schedule(arr, n - 1)
    return max(incl, excl)


def max_profit_dp(arr):
    dp = [0]*len(arr)
    dp[0] = arr[0].profit
    for i in range(1, len(arr)):
        incl = arr[i].profit
        prev = prev_job(arr, i)
        if prev != -1:
            incl += dp[prev]
        excl = dp[i-1]
        dp[i] = max(incl, excl)
    return dp[-1]


def prev_job(arr, n):
    start = arr[n].start
    i, j = 0, n
    while i <= j:
        mid = (i + j) >> 1
        if arr[mid].end > start:
            j = mid - 1
        elif arr[mid].end <= start < arr[mid + 1].end:
            return mid
        else:
            i = mid + 1
    return -1


class Job:
    def __init__(self, start, end, profit):
        self.start = start
        self.end = end
        self.profit = profit

    def __le__(self, other):
        return self.end < other.end

    def __eq__(self, other):
        return self.end == other.end


arr = [Job(1, 2, 50), Job(3, 5, 20), Job(6, 19, 100), Job(2, 100, 200)]
# print(prev_job(arr, len(arr)))
print(max_profit_schedule(arr, len(arr) - 1))
print(max_profit_dp(arr))

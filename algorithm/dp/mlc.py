"""
Maximum Length Chain of Pairs
You are given n pairs of numbers. In every pair, the first number is always smaller then the second number. A pair(c,d)
can follow another pair(a,b) if c<a. Chain of pairs can be formed in this fashion. Find the longest chain which can be
formed from a given set of pairs.

"""
m = 0


def mic_recur(arr, n):
    global m
    if n == 1:
        return 1
    mlc = 1
    for i in range(1, n):
        i_mlc = mic_recur(arr, i)
        if arr[i - 1][1] < arr[n - 1][0] and i_mlc + 1 > mlc:
            mlc = i_mlc + 1
    if m < mlc:
        m = mlc
    return mlc


def mic_recur_dp(arr):
    arr.sort(key=lambda  a: a[0])
    n = len(arr)
    p = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j][1] < arr[i][0] and p[j] + 1 > p[i]:
                p[i] = 1 + p[j]
    return max(p)


def mic_recur_greedy(arr):
    # sorted by second argument. so the first element will always in the optimal solution as first element
    arr.sort(key=lambda a: a[1])
    n = len(arr)
    res = [arr[0]]
    i = 0
    for j in range(1, n):
        if arr[i][1] < arr[j][0]:
            i = j
            res.append(arr[j])
    print(res)


arr = [[5, 24], [15, 25], [27, 40], [50, 60], [42, 48]]
mic_recur(arr, len(arr))
# print(m)
print(mic_recur_dp(arr))
mic_recur_greedy(arr)

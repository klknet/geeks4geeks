"""
Random number generator in arbitrary probability distribution fashion.
1.Take an auxiliary array of size n.
2.Populate it with prefix sum, such that prefix[i] represents sum of numbers from 0 to i.
3.Generate a random number between 1 and sum,where sum represents summation of input frequency array.
4.Find index of ceil of random number generated in step#3 in the prefix array. Let the index be idxC.
5.Return the random number arr[idxC].
"""
import random

prefix = []


def random_check(arr, freq):
    global prefix
    if len(prefix) == 0:
        s = 0
        for i in freq:
            s += i
            prefix.append(s)
    v = random.randint(1, prefix[-1])
    l, r = 0, len(prefix) - 1
    while l < r:
        mid = l + ((r - l) >> 1)
        if v > prefix[mid]:
            l = mid + 1
        else:
            r = mid
    return arr[l]


arr = [10, 50, 40, 20]
freq = [2, 19, 3, 4]
stat = {}
for i in arr:
    stat[i] = 0
n = 1000
for i in range(n):
    res = random_check(arr, freq)
    stat[res] += 1
for i in range(len(arr)):
    print(arr[i], stat[arr[i]], round(freq[i]/sum(freq),4), stat[arr[i]]/n)

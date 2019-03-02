"""
Given an array arr[0,1,...n] containing n positive integers, a subsequence is called bitonic if it is first increasing
then decreasing. Write a function that takes a array as argument and returns the length of the longest bitonic subsequence.

Let the input array be arr[] of length n. We need to construct two arrays lis[] and lds[] using dynamic programming solution
of lis problem, lis[i] stores the length of the longest increasing subsequence ending with i, lds[i] stores the length
of the longest decreasing subsequence starting with i. Finally we return the max value of lis[i]+lds[i]-1 where i is from
0 to n-1.
"""


def lbs(arr):
    n = len(arr)
    lis = [1] * (n)
    lds = [1] * (n)
    for i in range(1, n):
        for j in range(i + 1):
            if arr[j] < arr[i] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if arr[j] < arr[i] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1
    m = 0
    for i in range(n):
        s = lis[i]+lds[i]-1
        if m<s:
            m = s
    return m


arr = [1, 5, 2, 6]
arr = [0 , 8 , 4, 12, 2, 10 , 6 , 14 , 1 , 9 , 5 , 13,
        3, 11 , 7 , 15]
print(lbs(arr))

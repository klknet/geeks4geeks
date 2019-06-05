"""
Given a set of n integers, divide the set in two subsets of n/2 sizes each such that the difference of the sum of two
subsets is as minimum as possible. If n is even, then sizes of two subsets must be strictly n/2 and if n is odd, then size
of one subset must be (n-1)/2 and size of other subset must be (n+1)/2.
"""

import sys

diff = sys.maxsize


def tugOfWar(arr):
    n = len(arr)
    sol = [False] * n
    curr_elems = [False] * n
    Sum = sum(arr)
    tugOfWarUtil(arr, n, 0, curr_elems, sol, 0, Sum, 0)
    print("The first subset: ", end='')
    for i in range(n):
        if sol[i]:
            print(arr[i], end=' ')
    print("\nThe second subset: ", end='')
    for i in range(n):
        if not sol[i]:
            print(arr[i], end=' ')


def tugOfWarUtil(arr, n, no_selected, curr_elems, sol, curr_sum, Sum, pos):
    global diff
    # reach the end, return
    if pos == n:
        return
    # checks that the number of elements left are not less than the number of elements required to form the solution.
    if n // 2 - no_selected > n - pos:
        return
    # exclude current element
    tugOfWarUtil(arr, n, no_selected, curr_elems, sol, curr_sum, Sum, pos + 1)
    # include current element
    curr_sum += arr[pos]
    no_selected += 1
    curr_elems[pos] = True

    if n // 2 == no_selected:
        if abs(Sum / 2 - curr_sum) < diff:
            diff = abs(Sum / 2 - curr_sum)
            for i in range(n):
                sol[i] = curr_elems[i]
    else:
        tugOfWarUtil(arr, n, no_selected, curr_elems, sol, curr_sum, Sum, pos + 1)
    curr_elems[pos] = False


arr = [23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]
tugOfWar(arr)
print('\nMinimum difference is', diff)

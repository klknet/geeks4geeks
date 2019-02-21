"""
given n eggs and k floors, find the minimum number of droppings that break the egg
When we drop an egg from a floor x, there can be two cases (1)the egg breaks (2)the egg doesn't break
1)If the egg breaks after dropping from xth floor, then we only need to check for floors lower than x with remaining eggs,
so the problem reduces to n-1 eggs and x-1 floors.
2)If the egg doesn't break after dropping from the xth floor, then we only need to check for floors higher than x, so the
problem reduces to n eggs and k-x floors
Since we need to minimize the number of trials in worst case, we take the maximum of the two cases, we consider the max
of above cases for every floor and choose the floor which yields minimum number of trials.
f(n, k) = 1 + min{ max( f(n-1, x-1), f(n, k-x) ) } for 1<=x<=k
"""

import sys


def num_droppings(n, k):
    # if only 1 floor, then 1 trial needed, 0 floor, 0 trial needed
    if k == 1 or k == 0:
        return k
    # if remaining 1 egg, we need try every floor.
    if n == 1:
        return k
    min_num = sys.maxsize
    for x in range(1, k + 1):
        droppings = 1 + max(num_droppings(n - 1, x - 1), num_droppings(n, k - x))
        if droppings < min_num:
            min_num = droppings
    return min_num


def num_droppings_dp(n, k):
    t = [[0] * (k + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i == 1 or j == 1:
                t[i][j] = j
            else:
                min_num = sys.maxsize
                for x in range(1, j + 1):
                    droppings = 1 + max(t[i - 1][x - 1], t[i][j - x])
                    if droppings < min_num:
                        min_num = droppings
                t[i][j] = min_num
    return t[n][k]


n, k = 3, 36
# print("Minimum number of trials in worst case with %d eggs and %d floors is %d" % (n, k, num_droppings(n, k)))
print(num_droppings_dp(n, k))

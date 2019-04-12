"""
Collect maximum points in a grid using two traversals.
Given a matrix where every cell represents points. How to collect maximum points using two traversals under following
conditions.
Let the dimensions of given grid be R*C:
1)The first traversal starts from top left corner, i.e.,(0,0) and should reach left bottom corner, i.e.,(R-1,0). The
second traversal starts from top right corner, i.e(0, C-1), and should reach right bottom corner, i.e, (R-1,C-1).
2)From a point(i,j), we can move to (i+1,j-1) (i+1,j) (i+1,j+1).
3)A traversal gets all points of a particular cell through which it passes. If one traversal has already collected points
of a cell, then the other traversal gets no points if goes through that cell again.

The important thing to note is, at any particular step both traversals will be in same row as in all possible tree moves,
row number is increased. Let (x1,y1) and (x2,y2) denote current positions of first and second traversals respectively.
Thus at any time x1 will be equal to x2 as both of them move forward but variation is possible alone y. Since variation
in y could occur in 3 ways, no change(y), go left(y-1), go right(y+1). So in total 9 combinations among y1, y2 are
possible.
maxPoints(grid, x, y1, y2) = max(maxPoints(grid, x+1, y1+i, y2+i)+grid[x][y1]+grid[x][y2] or grid[x][y1])
where i is combination of [-1,0,1]
"""

import sys

y = [-1, 0, 1]


def max_points(grid, x, y1, y2):
    r, c = len(grid), len(grid[0])
    # invalid position, return infinite
    if y1 < 0 or y2 < 0 or y1 >= c or y2 >= c:
        return -sys.maxsize
    if x == 0:
        if y1 != 0 or y2 != c - 1:
            return -sys.maxsize
        else:
            # base case, initial position
            return grid[0][0] + grid[0][c - 1]
    m = -sys.maxsize
    for i in y:
        for j in y:
            v = max_points(grid, x - 1, y1 + i, y2 + j)
            if v != -sys.maxsize:
                if y1 != y2:
                    v += (grid[x][y1] + grid[x][y2])
                else:
                    v += grid[x][y1]
                m = max(m, v)
    return m


def max_points_util(grid, x, y1, y2, dp):
    r, c = len(grid), len(grid[0])
    if y1 < 0 or y1 >= c or y2 < 0 or y2 >= c:
        return -sys.maxsize
    if x == r - 1 and y1 == 0 and y2 == c - 1:
        return grid[x][y1] + grid[x][y2]
    if x == r - 1:
        return -sys.maxsize
    if dp[x][y1][y2] != -1:
        return dp[x][y1][y2]
    m = -sys.maxsize
    for i in y:
        for j in y:
            c = max_points_util(grid, x+1, y1+i, y2+j, dp)
            if c != -sys.maxsize:
                if y1 == y2:
                    c += grid[x][y1]
                else:
                    c += (grid[x][y1]+grid[x][y2])
                m = max(m, c)
    dp[x][y1][y2] = m
    return m


def max_point_dp(grid):
    r, c = len(grid), len(grid[0])
    dp = [[[-1 for i in range(c)] for j in range(c)] for k in range(r)]
    return max_points_util(grid, 0, 0, c-1, dp)


arr = [[3, 6, 8, 2],
       [5, 2, 4, 3],
       [1, 1, 20, 10],
       [1, 1, 20, 10],
       [1, 1, 20, 10],
       ]
print(max_points(arr, len(arr) - 1, 0, len(arr[0]) - 1))
print(max_point_dp(arr))

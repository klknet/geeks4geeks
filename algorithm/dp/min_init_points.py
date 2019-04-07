"""
Minimum Initial Points to Reach Destination.
Given a grid with each cell consisting of positive, negative or no points i.e zero points. We can move across a cell only
if we have positive points(>0). Whenever we pass through a cell, points in that cell are added to our overall points. We
need to find the minimum initial points to reach cell(m-1,n-1) from (0,0).
Constraints:
1.From a cell(i,j), we can move to (i+1,j) or (i,j+1).
2.We can not move from (i,j) if your overall points at (i,j) is <=0.
3.We have to reach at (m-1,n-1) with minimum positive points i.e., > 0.
"""

m, n = 3, 3


def min_init_points(point):
    dp = [[0 for col in range(n)] for row in range(m)]
    if point[m-1][n-1] < 0:
        dp[m-1][n-1] = 1-point[m-1][n-1]
    else:
        dp[m-1][n-1] = 1

    for i in range(m-2, -1, -1):
        dp[i][n-1] = max(dp[i+1][n-1]-point[i][n-1], 1)
    for i in range(n-2, -1, -1):
        dp[m-1][i] = max(dp[m-1][i+1]-point[m-1][i], 1)

    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            min_Points_on_exit = min(dp[i+1][j], dp[i][j+1])
            dp[i][j] = max(min_Points_on_exit-point[i][j], 1)
    return dp[0][0]


p = [[-2, -3, 3],
     [-5, -10, 1],
     [10, 30, -5]]
print(min_init_points(p))
"""
Count number of ways to reach a given score in a game.
Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n, find number of ways to
reach the given score.
The idea is to create a table of size n+1 to store counts of all scores from 0 to n. For every possible move(3,5,and10)
increment values in table.
"""


def count_num(n):
    dp = [0]*(n+1)
    # base case
    dp[0] = 1
    for i in range(3, n+1):
        dp[i] += dp[i-3]
    for i in range(5, n+1):
        dp[i] += dp[i-5]
    for i in range(10, n+1):
        dp[i] += dp[i-10]
    return dp[n]


# print(count_num(13))
print(count_num(20))
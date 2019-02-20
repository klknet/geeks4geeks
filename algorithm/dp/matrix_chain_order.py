"""
Problem:
Given a sequence of matrices, find the most efficient way to multiply these matrices together. The problem is not actually
to perform the multiplications, but merely to decide in which order to perform the multiplications.

Solution:
A simple solution is to place parenthesis at all possible places, calculate the cost for each placement and return the
minimum value. In a chain of matrices of size n, we can place the first set of parenthesis in n-1 ways. For example, if
the given chain is of 4 matrices. Let the chain be ABCD, then there are 3 ways to place the first set of parenthesis:
(A)(BCD) (AB)(CD) (ABC)(D). So when we place a set of parenthesis, we divide the problem into subproblems of smaller size.
Therefore, the problem has optimal substructure property and can be easily solved using recursion.

Minimum number of multiplication needed to multiply a chain of size n = Minimum of all n-1 placements(These placements
create subproblems of smaller size).
"""

import sys


def matrix_chain_order(p, i, j):
    if i == j:
        return 0
    min_num = sys.maxsize
    for k in range(i, j):
        count = matrix_chain_order(p, i, k) + matrix_chain_order(p, k + 1, j) \
                + p[i - 1] * p[k] * p[j]
    if min_num > count:
        min_num = count
    return min_num


def matrix_chain_order_dp(p, n):
    # t[i,j] is the minimum num of scalar multiplications needed to compute the matrix p[i]p[i+1]...p[j]=p[i..j] where
    # dimension of p[i] is p[i-1]*p[i]
    m = [[0] * n for i in range(n)]
    # L is the length of matrix chain.
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                count = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if m[i][j] > count:
                    m[i][j] = count
    return m[1][n - 1]


arr = [1, 2, 3, 4, 3]
print(matrix_chain_order(arr, 1, len(arr) - 1))
print(matrix_chain_order_dp(arr, len(arr)))

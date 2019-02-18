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


arr = [1, 2, 3, 4, 3]
print(matrix_chain_order(arr, 1, len(arr) - 1))

"""
Maximum size square sub-matrix with all 1s.
Given a binary matrix, find out the maximum size square sub-matrix with all 1s.
Let the given binary matrix be M[R][C]. The idea of the algorithm is to construct an auxiliary size matrix S[][] in which
each entry S[i][j] represents size of the square sub-matrix with all 1s including M[i][j] where M[i][j] is the rightmost
and bottommost entry in sub-matrix.
1)Construct a sum matrix S[R][C] for the given M[R][C].
 a)Copy first row and first column as it is from M[][] to S[][].
 b)For other entries, use following expressions to construct S[][].
 If M[i][j] is 1 then
    S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1])+1
 Else
    S[i][j] = 0
2)Find the maximum entry in S[R][C]
3)Using the value and coordinates of maximum entry in S[i][j], print sub-matrix M[][]
"""


def max_square_matrix(m):
    r = len(m)
    c = len(m[0])
    s = [[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        s[i][0] = m[i][0]
    for j in range(c):
        s[0][j] = m[0][j]
    for i in range(1, r):
        for j in range(1, c):
            if m[i][j] == 1:
                s[i][j] = 1+min(s[i-1][j], s[i][j-1], s[i-1][j-1])
    return max(max(s))


M = [[0, 1, 1, 0, 1],
     [1, 1, 0, 1, 0],
     [0, 1, 1, 1, 0],
     [1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0]]
print(max_square_matrix(M))
"""
Given a matrix of characters. Find the length of the longest path from a given character, such that all characters in the
path are consecutive to each other. It is allowed to move in all 8 directions from a cell.
The idea is to first search given starting character in the given matrix. Do Depth First Search(DFS) from all occurrences
to find all consecutive paths. While do DFS, we may encounter many subproblems again and again. So we use dynamic programming
to store results of subproblems.
"""

C, R = 3, 3
dp = [[0 for col in range(C)] for row in range(R)]
# tool matrices to recur for adjacent cells.
x = [0, -1, -1, -1, 0, 1, 1, 1]
y = [-1, -1, 0, 1, 1, 1, 0, -1]


def longest_path(mat, s):
    ans = 0
    for i in range(R):
        for j in range(C):
            if mat[i][j] == s:
                for k in range(8):
                    ans = max(ans, 1+longest_path_util(mat, i+x[k], j+y[k], s))
    return ans


# it calls recursive DFS based function to find max length path.
def longest_path_util(mat, i, j, prev):
    if not isvalid(i, j) or not isconsecutive(mat[i][j], prev):
        return 0
    if dp[i][j]>0:
        return dp[i][j]
    ans = 0
    for k in range(8):
        ans = max(ans, 1+longest_path_util(mat, i+x[k], j+y[k], mat[i][j]))
    dp[i][j] = ans
    return ans



# whether current position is valid
def isvalid(i, j):
    if i < 0 or j < 0 or i >= R or j >= C:
        return False
    return True


# whether current character is next to prev.
def isconsecutive(cur, prev):
    return ord(cur) - ord(prev) == 1


mat = [['a', 'c', 'd'],
       ['h', 'b', 'a'],
       ['i', 'g', 'f']]

print(longest_path(mat, 'a'))
print(longest_path(mat, 'e'))
print(longest_path(mat, 'b'))
print(longest_path(mat, 'f'))

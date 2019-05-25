"""
N Queen Problem.
"""
import copy


class ChessBoard(object):
    def __init__(self, n):
        self.n = n
        self.t = 0
        self.board = [[0 for col in range(n)] for row in range(n)]

    def print_chess(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end="\t")
            print("")

    def isSafe(self, x, y):
        # check for row in column y, because columns left than y are already place a queeen.
        for i in range(y):
            if self.board[x][i] == 1:
                return False
        # check for upper diagonal
        for i, j in list(zip(range(x, -1, -1), range(y, -1, -1))):
            if self.board[i][j] == 1:
                return False
        # check for down diagonal
        for i, j in list(zip(range(x, self.n, 1), range(y, -1, -1))):
            if self.board[i][j] == 1:
                return False
        return True


def n_queen_util(cb, queen):
    if queen == cb.n:
        cb.t += 1
        print(cb.t, '--')
        cb.print_chess()
        return True
    res = False
    for i in range(cb.n):
        if cb.isSafe(i, queen):
            cb.board[i][queen] = 1
            res = n_queen_util(cb, queen + 1) or res
            cb.board[i][queen] = 0
    return res


def n_queen(cb):
    if not n_queen_util(cb, 0):
        print("no solution exists.")


n = 8
cb = ChessBoard(n)
n_queen(cb)

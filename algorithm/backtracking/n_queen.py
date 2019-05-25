"""
N Queen Problem.
"""


class ChessBoard(object):
    def __init__(self, n):
        self.n = n
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
        return True
    for i in range(cb.n):
        if cb.isSafe(i, queen):
            cb.board[i][queen] = 1
            if n_queen_util(cb, queen + 1):
                return True
            cb.board[i][queen] = 0
    return False


def n_queen(cb):
    for i in range(cb.n):
        if n_queen_util(cb, i):
            cb.print_chess()
            break


cb = ChessBoard(5)
n_queen(cb)

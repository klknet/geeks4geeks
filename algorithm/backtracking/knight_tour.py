"""
The Knight's tour problem.
If all squares are visited
    print the solution
Else
    a)Add one of the next moves to the solution vector and recursively check if this move leads to the solution. (A knight
    can make maximum 8 moves. We choose one of the 8 moves in this step)
    b)If the move chosen in the above step doesn't lead to a solution then remove this move from the solution vector and
    try other alternative moves.
    c)If none of the alternatives work then return false(Returning false will remove the previously added item in
    recursion and if false is return by the initial call of recursion then "no solution exists")
"""

xMove = [-2, -2, -1, 1, 2, 2, 1, -1]
yMove = [-1, 1, 2, 2, 1, -1, -2, -2]


def knight_tour(cb):
    x, y = 0, 0
    cb.board[x][y] = 0
    if knight_util(cb, x, y, 1):
        cb.print_solution()


def knight_util(cb, x, y, move):
    if move == 64:
        return True
    moves = cb.moves(x, y)
    moves.sort(key=lambda x: x[0])
    for k in range(cb.n):
        next_x = moves[k][1][0]
        next_y = moves[k][1][1]
        if cb.isSafe(next_x, next_y):
            cb.board[next_x][next_y] = move
            if knight_util(cb, next_x, next_y, move + 1):
                return True
            cb.board[next_x][next_y] = -1
    return False


class ChessBoard(object):
    def __init__(self, n):
        self.n = n
        self.board = [[-1 for col in range(n)] for row in range(n)]
        self.step = 0

    def print_solution(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end='\t')
            print('')

    def isSafe(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n and self.board[x][y] == -1

    def countNext(self, x, y):
        c = 0
        for k in range(self.n):
            next_x = x + xMove[k]
            next_y = y + yMove[k]
            if self.isSafe(next_x, next_y):
                c += 1
        return c

    def moves(self, x, y):
        moves = []
        for k in range(self.n):
            next_x = x + xMove[k]
            next_y = y + yMove[k]
            if self.isSafe(next_x, next_y):
                c = self.countNext(next_x, next_y)
                moves.append((c, (next_x, next_y)))
        return moves


knight_tour(ChessBoard(8))

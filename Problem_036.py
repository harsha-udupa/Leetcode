"""

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def row_check(board):
            for i in board:
                td = {}
                for j in i:
                    if j != '.' and j not in td:
                        td[j] = 1
                    elif j in td:
                        return False
            return True

        def col_check(board):
            for i in range(9):
                td = {}
                for j in range(9):
                    if board[j][i] != '.' and board[j][i] not in td:
                        td[board[j][i]] = 1
                    elif board[j][i] in td:
                        return False
            return True

        def box_check(board):

            for k in range(3):
                for l in range(3):
                    td = {}
                    for i in range(3):
                        for j in range(3):
                            x,v = (3*k+i),(3*l+j)
                            if board[x][v] != '.' and board[x][v] not in td:
                                td[board[x][v]] = 1
                            elif board[x][v] in td:
                                return False
            return True

        if not row_check(board) or not col_check(board) or not box_check(board):
            return False
        return True

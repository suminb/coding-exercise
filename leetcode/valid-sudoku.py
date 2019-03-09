# 36. Valid Sudoku
# difficulty: medium

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.valid_rows(board) and self.valid_cols(board) and self.valid_subboxes(board)

    def valid_rows(self, board):
        valid = True
        for i in range(9):
            valid = valid and self.is_valid_section(board[i])
        return valid

    def valid_cols(self, board):
        valid = True
        for j in range(9):
            valid = valid and self.is_valid_section([board[i][j] for i in range(9)])
        return valid

    def valid_subboxes(self, board):
        valid = True
        for y in range(0, 9, 3):
            for x in range(0, 9, 3):
                xs = [board[y + i][x + j] for i in range(3) for j in range(3)]
                valid = valid and self.is_valid_section(xs)
        return valid

    def is_valid_section(self, elements):
        xs = [int(x) for x in elements if x != '.']
        return len(xs) == len(set(xs))


def test_valid():
    s = Solution()
    assert s.isValidSudoku([
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ])


def test_invalid():
    s = Solution()
    assert not s.isValidSudoku([
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ])

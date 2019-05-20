# 48. Rotate Image
# difficulty: medium
# https://leetcode.com/problems/rotate-image/

from typing import List

import pytest


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 0:
            return

        m = len(matrix[0])
        assert n == m, 'Invalid input'

        transpose(matrix)
        flip_horizontally(matrix)

# CW: Transpose and flip left-right
# CCW: Transpose and flip up-down

def transpose(matrix):
    """Looks like we're only expecting NxN matrices."""
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def flip_horizontally(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n // 2):
            k = n - j - 1
            matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]


@pytest.mark.parametrize('matrix, expected', [
    ([], []),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]), 
    ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]], 
     [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]), 
])
def test_rotate(matrix, expected):
    s = Solution()
    s.rotate(matrix)
    assert expected == matrix
# 85. Maximal Rectangle
# difficulty: hard
# https://leetcode.com/problems/maximal-rectangle/

from typing import List

import pytest


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        return maximal_rectangle(matrix)


def maximal_rectangle(matrix):
    if not matrix:
        return 0

    width = len(matrix[0])
    heights = [0] * width
    max_area = 0
    for row in matrix:
        heights = accumulate_heights(heights, row)
        area = calc_max_area(heights)
        max_area = max(max_area, area)

    return max_area


def accumulate_heights(heights, row):
    return [h + 1 if r == '1' else 0
            for h, r in zip(heights, row)]


def calc_max_area(heights):
    left_indices, right_indices = calc_max_indices(heights)
    max_area = 0
    for i, h in enumerate(heights):
        width = right_indices[i] - left_indices[i] - 1
        max_area = max(max_area, width * h)
    return max_area


def calc_max_indices(heights):
    n = len(heights)
    left_indices = [0] * n
    right_indices = [0] * n

    for i in range(n):
        j = i - 1
        while j >= 0 and heights[j] >= heights[i]:
            j = left_indices[j]
        left_indices[i] = j

    for i in range(n - 1, -1, -1):
        j = i + 1
        while j < n and heights[j] >= heights[i]:
            j = right_indices[j]
        right_indices[i] = j

    return left_indices, right_indices


def test_maximal_rectangle():
    matrix = [
        ['1','0','1','0','0'],
        ['1','0','1','1','1'],
        ['1','1','1','1','1'],
        ['1','0','0','1','0']
    ]
    assert 6 == maximal_rectangle(matrix)


if __name__ == '__main__':
    pytest.main([__file__])
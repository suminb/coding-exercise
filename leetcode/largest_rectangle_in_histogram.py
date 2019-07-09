# 84. Largest Rectangle in Histogram
# difficulty: hard
# https://leetcode.com/problems/largest-rectangle-in-histogram/

from typing import List

import pytest


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return largest_rectangle_area(heights)


def largest_rectangle_area(heights):
    n = len(heights)
    min_left, min_right = calc_min_indices(heights)

    max_area = 0
    for i, h in enumerate(heights):
        w = min_right[i] - min_left[i] - 1
        max_area = max(max_area, w * h)

    return max_area


def calc_min_indices(heights):
    n = len(heights)
    min_left, min_right = [0] * n, [0] * n

    for i in range(n):
        j = i - 1
        while j >= 0 and heights[j] >= heights[i]:
            j = min_left[j]
        min_left[i] = j

    for i in range(n - 1, -1, -1):
        j = i + 1
        while j < n and heights[j] >= heights[i]:
            j = min_right[j]
        min_right[i] = j

    return min_left, min_right


@pytest.mark.parametrize('heights, expected', [
    ([], 0), 
    ([3], 3), 
    ([2, 1, 5, 6, 2, 3], 10), 
    ([1, 1, 1, 7, 1, 1, 1], 7),
    ([1, 1, 1, 9, 1, 1, 1], 9),
    ([1, 1, 1, 1, 7, 1, 1, 1], 8),
    ([2, 2, 0, 3, 1, 3, 0, 1], 4),
])
def test_largest_rectangle_area(heights, expected):
    actual = largest_rectangle_area(heights)
    assert expected == actual


if __name__ == '__main__':
    pytest.main([__file__])
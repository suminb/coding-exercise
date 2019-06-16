# 42. Trapping Rain Water
# difficulty: hard
# https://leetcode.com/problems/trapping-rain-water/

from typing import List

import pytest


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # TODO: Perhaps we could do some code refactoring
        max_left, max_right = 0, 0
        max_to_right = [0] * n
        max_to_left = [0] * n
        for i in range(1, n):
            max_left = max(height[i - 1], max_left)
            max_to_left[i] = max_left

            j = n - i - 1
            max_right = max(height[j + 1], max_right)
            max_to_right[j] = max_right

        volume = 0
        for i in range(0, n):
            wall = min(max_to_left[i], max_to_right[i])
            volume += max(wall - height[i], 0)

        return volume



@pytest.mark.parametrize('height, expected', [
    ([0], 0),
    ([9, 0, 0], 0),
    ([0, 0, 8], 0),
    ([3, 0, 3], 3),
    ([3, 0, 5, 0, 3], 6),
    ([1, 9, 7, 6, 3, 3, 2, 2, 0, 6, 1], 20),
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6), 
])
def test_trapping_rain_water(height, expected):
    s = Solution()
    actual = s.trap(height)
    assert expected == actual


if __name__ == '__main__':
    pytest.main(['-v', __file__])
# 75. Sort Colors
# difficulty: medium
# https://leetcode.com/problems/sort-colors/


from typing import List

import pytest


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_counts = [0, 0, 0]
        for x in nums:
            color_counts[x] += 1

        color_index = 0
        for i, x in enumerate(nums):
            while color_counts[color_index] <= 0:
                color_index += 1
            nums[i] = color_index
            color_counts[color_index] -= 1


@pytest.mark.parametrize('values, expected', [
    ([], []),
    ([1], [1]),
    ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]), 
    ([2, 0, 2, 1, 1, 0, 2, 1, 0, 1, 2, 1, 2, 1, 2, 1, 2, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
])
def test(values, expected):
    s = Solution()
    s.sortColors(values)
    assert expected == values


if __name__ == '__main__':
    pytest.main(['-v', 'sort-colors.py'])
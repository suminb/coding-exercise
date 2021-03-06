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
        one_pass_solution(nums)

def two_pass_solution(nums):
    color_counts = [0, 0, 0]
    for x in nums:
        color_counts[x] += 1

    color_index = 0
    for i, x in enumerate(nums):
        while color_counts[color_index] <= 0:
            color_index += 1
        nums[i] = color_index
        color_counts[color_index] -= 1


def one_pass_solution(nums):
    """NOTE: Lomuto partition"""
    j = k = 0
    for i, v in enumerate(nums):
        nums[i] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[k] = 0
            k += 1


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
    pytest.main(['-v', __file__])

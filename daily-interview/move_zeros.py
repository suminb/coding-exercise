# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
#
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
#
# Here is a starting point:
#
# class Solution:
# def moveZeros(self, nums):
#     # Fill this in.
#
# nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
# Solution().moveZeros(nums)
# print(nums)
# # [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]

import pytest


def move_zeros(nums):
    leader = follower = 0
    n = len(nums)

    while leader < n:
        if nums[leader] != 0:
            nums[follower] = nums[leader]
            follower += 1
        leader += 1
    while follower < n:
        nums[follower] = 0
        follower += 1


@pytest.mark.parametrize("nums, expected", [
    ([], []),
    ([0], [0]),
    ([1], [1]),
    ([0, 0, 0, 0], [0, 0, 0, 0]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 0], [1, 2, 3, 4, 0]),
    ([0, 1, 2, 3, 4], [1, 2, 3, 4, 0]),
    ([0, 0, 0, 2, 0, 1, 3, 4, 0, 0], [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]),
])
def test(nums, expected):
    move_zeros(nums)
    assert expected == nums
# You are given an array of integers. Return the smallest positive integer that is not present in the array. The array may contain duplicate entries.
#
# For example, the input [3, 4, -1, 1] should return 2 because it is the smallest positive integer that doesn't exist in the array.
#
# Your solution should run in linear time and use constant space.
#
# Here's your starting point:
#
# def first_missing_positive(nums):
#   # Fill this in.
#
# print first_missing_positive([3, 4, -1, 1])
# # 2

import pytest


def first_missing_positive(nums):
    n = len(nums)
    # TODO: Can we do this with O(1) space?
    buf = [0] * n
    for i, x in enumerate(nums):
        if x > 0:
            buf[x - 1] = x
    i = 0
    while i < n and buf[i] == i + 1:
        i += 1
    return i + 1


@pytest.mark.parametrize("nums, expected", [
    ([0], 1),
    ([1], 2),
    ([1, 2], 3),
    ([3, 4, -1, 1], 2),
    ([3, 4, -1, 1, -1], 2),
    ([0, 1, 2, 3], 4),
    ([-1, -2, -3], 1),
])
def test_first_missing_positive(nums, expected):
    actual = first_missing_positive(nums)
    assert expected == actual
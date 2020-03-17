# You are given an array of integers. Return an array of the same size where
# the element at each index is the product of all the elements in the original
# array except for the element at that index.
#
# For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].
#
# You cannot use division in this problem.
#
# Here's a start:
#
# def products(nums):
#   # Fill this in.
#
# print products([1, 2, 3, 4, 5])
# # [120, 60, 40, 30, 24]

import pytest


def products(nums):
    n = len(nums)
    left = [1] * (n + 2)
    right = [1] * (n + 2)

    i, j = 0, n - 1
    while i < n:
        left[i + 1] = left[i] * nums[i]
        i += 1

        right[j + 1] = right[j + 2] * nums[j]
        j -= 1

    i = 0
    while i < n:
        nums[i] = left[i] * right[i + 2]
        i += 1


@pytest.mark.parametrize("nums, expected", [
    ([1], [1]),
    ([2, 3], [3, 2]),
    ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
])
def test_products(nums, expected):
    products(nums)
    assert expected == nums
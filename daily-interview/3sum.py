# [Daily Problem] 3 Sum
#
# Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c) in nums such that a + b + c = 0. Note that there may not be any triplets that sum to zero in nums, and that the triplets must not be duplicates.
#
# Example:
# Input: nums = [0, -1, 2, -3, 1]
# Output: [0, -1, 1], [2, -3, 1]
# Here's a starting point:
#
# class Solution(object):
#   def threeSum(self, nums):
#     # Fill this in.
#
# # Test Program
# nums = [1, -2, 1, 0, 5]
# print(Solution().threeSum(nums))
# # [[-2, 1, 1]]

import pytest


# TODO: Come up with a faster solution
def threesum_bruteforce(nums):
    i, j, k = 0, 1, 2
    n = len(nums)
    triples = []

    while i < n:
        j = i + 1
        while j < n:
            k = j + 1
            while k < n:
                x, y, z = nums[i], nums[j], nums[k]
                if x + y + z == 0:
                    triples.append([x, y, z])
                k += 1
            j += 1
        i += 1

    return triples


@pytest.mark.parametrize("nums, expected", [
    ([0, -1, 2, -3, 1], [[0, -1, 1], [2, -3, 1]]),
])
def test_threesum(nums, expected):
    actual = threesum_bruteforce(nums)
    assert expected == actual
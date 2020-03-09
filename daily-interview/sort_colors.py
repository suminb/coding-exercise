# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library’s sort function for this problem.
#
# Can you do this in a single pass?
#
# Example:
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Here's a starting point:
#
# class Solution:
#   def sortColors(self, nums):
#     # Fill this in.
#
# nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
# print("Before Sort: ")
# print(nums)
# # [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
#
# Solution().sortColors(nums)
# print("After Sort: ")
# print(nums)
# # [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]

import pytest


# TODO: This is a two-pass solution. Can we do this in one pass?
def sort_colors(nums):
    counts = [0, 0, 0]
    for x in nums:
        counts[x] += 1
    i = 0
    while i < counts[0]:
        nums[i] = 0
        i += 1
    j = i
    while j - i < counts[1]:
        nums[j] = 1
        j += 1
    k = j
    while k - j < counts[2]:
        nums[k] = 2
        k += 1


@pytest.mark.parametrize("nums, expected", [
    ([], []),
    ([0, 1, 2], [0, 1, 2]),
    ([2, 2, 0, 1], [0, 1, 2, 2]),
    ([0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1], [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]),
])
def test_sort_colors(nums, expected):
    sort_colors(nums)
    assert expected == nums
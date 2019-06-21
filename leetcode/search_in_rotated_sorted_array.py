#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
# difficulty: medium
# https://leetcode.com/problems/search-in-rotated-sorted-array/
#

from typing import List

import pytest


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        return search(nums, target, left, right)


def search(nums, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if target == nums[mid]:
        return mid
    elif nums[left] <= nums[mid]:
        # if left half is sorted
        if nums[left] <= target < nums[mid]:
            return search(nums, target, left, mid - 1)
        else:
            return search(nums, target, mid + 1, right)
    else:
        # if right half is sorted
        if nums[mid] < target <= nums[right]:
            return search(nums, target, mid + 1, right)
        else:
            return search(nums, target, left, mid - 1)


@pytest.mark.parametrize('nums, target, expected', [
    ([0], 0, 0),
    ([1], 2, -1),
    ([2, 3, 4, 5, 1], 0, -1),
    ([2, 3, 4, 5, 1], 1, 4),
    ([2, 3, 4, 5, 1], 2, 0),
    ([2, 3, 4, 5, 1], 3, 1),
    ([2, 3, 4, 5, 1], 4, 2),
    ([2, 3, 4, 5, 1], 5, 3),
    ([5, 1, 2, 3, 4], 1, 1),
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([4, 5, 6, 7, 0, 1, 2], 1, 5),
    ([4, 5, 6, 7, 0, 1, 2], 2, 6),
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ([4, 5, 6, 7, 0, 1, 2], 4, 0),
    ([4, 5, 6, 7, 0, 1, 2], 5, 1),
    ([4, 5, 6, 7, 0, 1, 2], 6, 2),
    ([4, 5, 6, 7, 0, 1, 2], 7, 3),
])
def test_rotated_array_search(nums, target, expected):
    actual = Solution().search(nums, target)
    assert expected == actual


if __name__ == '__main__':
    pytest.main(['-v', __file__])
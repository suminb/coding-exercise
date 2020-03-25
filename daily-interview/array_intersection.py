# [Daily Problem] Given two arrays, write a function to compute their
# intersection.
#
# Hi, here's your problem today. This problem was recently asked by Amazon:
#
# Given two arrays, write a function to compute their intersection - the
# intersection means the numbers that are in both arrays.
#
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:
# Each element in the result must be unique.
# The result can be in any order.
#
# Here's a starting point:
#
# class Solution:
#   def intersection(self, nums1, nums2):
#     # Fill this in.
#
# print Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4])
# # [9, 4]

import pytest


def intersection_bruteforce(nums1, nums2):
    """Runtime of O(m * n), no extra space."""
    intersect = []
    for x in nums1:
        if x in nums2 and x not in intersect:
            intersect.append(x)
    return intersect


def intersection_oneliner(nums1, nums2):
    """Linear runtime, requires two extra sets."""
    return [x for x in set(nums1) if x in set(nums2)]


def intersection_with_dict(nums1, nums2):
    """Linear runtime, requires only one extra dict."""
    counter = {}
    for x in nums1:
        counter[x] = 1
    for y in nums2:
        if y in counter:
            counter[y] = 2

    return [k for k, v in counter.items() if v == 2]


@pytest.mark.parametrize("nums1, nums2, expected", [
    ([], [], []),
    ([1], [2], []),
    ([1], [1], [1]),
    ([1, 2, 3], [4, 5, 6], []),
    ([1, 2, 2, 1], [2, 2], [2]),
    ([4, 9, 5], [9, 4, 9, 8, 4], [9, 4]),
])
def test_intersection(nums1, nums2, expected):
    actual = intersection_bruteforce(nums1, nums2)
    assert set(expected) == set(actual)

    actual = intersection_oneliner(nums1, nums2)
    assert set(expected) == set(actual)

    actual = intersection_with_dict(nums1, nums2)
    assert set(expected) == set(actual)
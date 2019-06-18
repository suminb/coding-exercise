# 53. Maximum Subarray
# difficulty: easy
# https://leetcode.com/problems/maximum-subarray/

from typing import List

import pytest


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_a =  max_b = nums[0]
        for x in nums[1:]:
            max_a = max(x, max_a + x)
            max_b = max(max_a, max_b)
        return max_b


@pytest.mark.parametrize('array, expected', [
    ([0], 0),
    ([1, 2, 3], 6),
    ([1, -2, 3], 3),
    ([-3, -2, -1], -1),
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
])
def test_max_subarray(array, expected):
    s = Solution()
    actual = s.maxSubArray(array)
    assert expected == actual

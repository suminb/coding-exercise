# 1. Two Sum
# difficulty: easy
# https://leetcode.com/submissions/detail/202462306/

import pytest


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache = {}
        for i in range(len(nums)):
            m = nums[i]
            if m in cache:
                return [cache[m], i]
            else:
                cache[target - m] = i


@pytest.mark.parametrize('nums, target, expected', [
    ([2, 7, 11, 15], 9, [0, 1]),
])
def test_two_sum(nums, target, expected):
    s = Solution()
    assert expected == s.twoSum(nums, target)

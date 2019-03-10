# 53. Maximum Subarray

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_a =  max_b = nums[0]
        for x in nums[1:]:
            max_a = max(x, max_a + x)
            max_b = max(max_a, max_b)
        return max_b


def test():
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

# 179. Largest Number
# difficulty: medium
# https://leetcode.com/problems/largest-number/

from typing import List

import pytest


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return ''.join(sorted([str(x) for x in nums], reverse=True))


@pytest.mark.parametrize('nums, expected', [
    ([10,2], '210'),
    ([[3,30,34,5,9], '9534330'])
])
def test(nums, expected):
    s = Solution()
    assert expected == s.largestNumber(nums)


if __name__ == '__main__':
    pytest.main(['-v', 'largest-number.py'])
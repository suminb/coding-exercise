# 179. Largest Number
# difficulty: medium
# https://leetcode.com/problems/largest-number/

from typing import List

import pytest


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return largest_number(nums)


def largest_number(nums):
    if len(nums) < 2:
        return ''.join([str(x) for x in nums])
    else:
        return max(expand(nums))

def expand(nums):
    for i, x in enumerate(nums):
        rest = nums[:i] + nums[i+1:]
        yield str(x) + largest_number(rest)


@pytest.mark.parametrize('nums, expected', [
    ([], ''),
    ([5], '5'),
    ([10, 2], '210'), 
    ([[3, 30, 34, 5, 9], '9534330']),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], '9876543210'),
    ([93, 5, 3, 1, 3, 412, 45, 6151823579123, 3752], '9361518235791235454123752331'),
])
def test(nums, expected):
    s = Solution()
    assert expected == s.largestNumber(nums)


if __name__ == '__main__':
    pytest.main(['-v', 'largest-number.py'])
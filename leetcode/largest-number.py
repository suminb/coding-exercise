# 179. Largest Number
# difficulty: medium
# https://leetcode.com/problems/largest-number/

from functools import partial
from typing import List

import pytest


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        return ''.join(
            sorted([str(x) for x in nums], key=partial(key, n=n), reverse=True))


def key(x: str, n: int):
    """We would like to compare numbers as if there is some sort of place
    holders.
    """
    return x + '0' * (n - len(x))


@pytest.mark.parametrize('nums, expected', [
    ([], ''),
    ([5], '5'),
    ([10, 2], '210'),
    ([121, 12], '12121'),
    ([[3, 30, 34, 5, 9], '9534330']),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], '9876543210'),
    ([93, 5, 3, 1, 3, 412, 45, 6151823579123, 3752], '9361518235791235454123752331'),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6], '9876655443322110'),
])
def test(nums, expected):
    s = Solution()
    assert expected == s.largestNumber(nums)


if __name__ == '__main__':
    pytest.main(['-v', 'largest-number.py'])
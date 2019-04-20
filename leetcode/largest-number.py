# 179. Largest Number
# difficulty: medium
# https://leetcode.com/problems/largest-number/

from typing import List

import pytest


class CustomString(str):
    def __gt__(self, other):
        return self + other > other + self

    def __lt__(self, other):
        return self + other < other + self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        number = ''.join(sorted([CustomString(x) for x in nums], reverse=True))

        while len(number) > 1 and number[0] == '0':
            number = number[1:]

        return number


def test_compare():
    assert CustomString('12') > CustomString('121')
    assert CustomString('12') > CustomString('120')
    assert CustomString('122') > CustomString('121')
    assert CustomString('121') > CustomString('120')


@pytest.mark.parametrize('nums, expected', [
    ([], ''),
    ([5], '5'),
    ([0, 0], '0'),
    ([0, 0, 0], '0'),
    ([10, 2], '210'),
    ([10, 0, 0], '1000'),
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
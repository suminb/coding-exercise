# 137. Single Number II
# difficulty: medium
# https://leetcode.com/problems/single-number-ii/

from typing import List

import pytest


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return single_number(nums)


def single_number(nums):
    """The basic idea is to count the number of 1-bit for each digit for each
    element in nums. If the number of 1-bits is not multiple of three, that
    is our clue for the exceptional element.

    As far as the time complexity is concerned, it is O((d + 1)n) where d is
    the number of bits occupied by each element in nums and n is the number
    of elements of nums. The value of d is dependent of the underlying CPU
    architecture (e.g., 32bit/64bit processor) and thus we could consider it
    as constant. Therefore, O((d + 1)n) is contained in O(n).
    """
    n = len(nums)
    m = max(nums)
    mask = 1
    res = 0
    while mask <= m:
        count = count_bits(nums, mask)
        if count % 3 != 0:
            res |= mask
        mask = mask << 1
    return res


def count_bits(nums, mask):
    return sum([1 for n in nums if n & mask != 0])


def test_count_bits():
    assert 4 == count_bits([5, 5, 5, 9], 1)
    assert 0 == count_bits([5, 5, 5, 9], 2)
    assert 3 == count_bits([5, 5, 5, 9], 4)
    assert 1 == count_bits([5, 5, 5, 9], 8)


@pytest.mark.parametrize('nums, expected', [
    ([1], 1),
    ([2, 2, 3, 2], 3), 
    ([0, 1, 0, 1, 0, 1, 99], 99),
])
def test_single_number(nums, expected):
    actual = single_number(nums)
    assert expected == actual
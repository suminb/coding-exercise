# 260. Single Number III
# difficulty: medium
# https://leetcode.com/problems/single-number-iii/

from functools import reduce
from typing import List

import pytest


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return single_number(nums)


def xor(x, y):
    return x ^ y


def single_number(xs):
    xs_xor = reduce(xor, xs)
    set_bit = find_set_bit(xs_xor)

    first = reduce(xor, find_group(xs, set_bit, set_bit))
    second = reduce(xor, find_group(xs, set_bit, 0))

    return [first, second]


def find_set_bit(xor):
    mask = 1
    while xor & mask == 0:
        mask = mask << 1
    return mask


def find_group(xs, set_bit, expected):
    """The problem description states that the space complexity must be O(1),
    so we avoid making a new list.
    """
    for x in xs:
        if x & set_bit == expected:
            yield x


@pytest.mark.parametrize('xs, expected', [
    ([1, 2], [1, 2]),
    ([1, 2, 1, 2, 3, 4], [3, 4]),
    ([1, 2, 1, 3, 2, 5], [3, 5]), 
])
def test_single_number_iii(xs, expected):
    actual = single_number(xs)
    assert expected == actual
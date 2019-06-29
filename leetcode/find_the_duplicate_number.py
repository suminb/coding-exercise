# 287. Find the Duplicate Number
# difficulty: medium
# https://leetcode.com/problems/find-the-duplicate-number/

from typing import List

import pytest


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return find_duplicate(nums)


def find_duplicate(xs):
    """This uses O(n) space which violates one of the requirements."""
    s = set()
    for x in xs:
        if x in s:
            return x
        else:
            s.update([x])
    return 0


def find_duplicate_tortoise(xs):
    """FIXME: This code does not cover all cases."""
    ptr1 = ptr2 = xs[0]
    for i in range(len(xs)):
        ptr1 = xs[ptr1]
        ptr2 = xs[xs[ptr2]]
        if xs[ptr1] == xs[ptr2]:
            return ptr1
    return 0


def find_duplicate_xor(xs):
    """This won't work in cases like [2, 2, 2]."""
    n = len(xs)
    s = 0
    for i, x in enumerate(xs, 1):
        s ^= x
        s ^= i
    s ^= n
    return s


@pytest.mark.parametrize('xs, expected', [
    ([0], 0),
    ([1, 1, 2, 3], 1),
    ([1, 3, 4, 2, 2], 2), 
    ([3, 1, 3, 4, 2], 3), 
    ([2, 2, 2, 2, 2], 2), 
    ([2, 5, 9, 6, 9, 3, 8, 9, 7, 1], 9), 
])
def test_find_duplicate(xs, expected):
    actual = find_duplicate(xs)
    assert expected == actual
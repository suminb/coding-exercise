#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/

from functools import reduce
from typing import List

import pytest


class Solution:
    table = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        candidates = [self.table[d] for d in digits]
        return [''.join(p) for p in cartesian_product(*candidates)]


def cartesian_product_of_two(xs, ys):
    for x in xs:
        for y in ys:
            if isinstance(x, tuple):
                yield (*x, y)
            else:
                yield (x, y)


def cartesian_product(*sets):
    """NOTE: We could've used itertools.product(), but it is worth implementing
    this ourselves for educational purposes.
    """
    return reduce(lambda x, y: cartesian_product_of_two(x, y), sets)


@pytest.mark.parametrize('digits, expected', [
    ('', []),
    ('23', ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']),
    # TODO: We need more test cases
])
def test_letter_combinations(digits, expected):
    actual = Solution().letterCombinations(digits)
    assert expected == actual

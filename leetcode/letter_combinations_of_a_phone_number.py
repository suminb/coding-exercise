#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/

from itertools import product
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
        # FIXME: Could we do this without itertools.product()?
        return [''.join(p) for p in product(*candidates)]


@pytest.mark.parametrize('digits, expected', [
    ('', []),
    ('23', ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']),
])
def test_letter_combinations(digits, expected):
    actual = Solution().letterCombinations(digits)
    assert expected == actual

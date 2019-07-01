#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
# difficulty: easy
# https://leetcode.com/problems/excel-sheet-column-title/description/
#

import pytest


class Solution:
    def convertToTitle(self, n: int) -> str:
        return convert(n)


def convert(n, base=26):
    buf = []
    while n > 0:
        d = (n - 1) % base + 1
        n = (n - d) // base
        buf.append(digit(d))
    return ''.join([str(x) for x in buf[::-1]])


def digit(n):
    """An one-based index."""
    return chr(n + ord('A') - 1)


@pytest.mark.parametrize('n, expected', [
    (1, 'A'),
    (2, 'B'),
    (3, 'C'),
    (26, 'Z'),
    (27, 'AA'),
    (28, 'AB'),
    (701, 'ZY'),
    (702, 'ZZ'),
    (703, 'AAA'),
    (123456, 'FZPH'),
])
def test_convert(n, expected):
    actual = convert(n)
    assert expected == actual


if __name__ == '__main__':
    pytest.main([__file__])
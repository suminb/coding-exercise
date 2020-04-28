# [Daily Problem] Consecutive Ones
#
# Hi, here's your problem today. This problem was recently asked by Microsoft:
#
# Return the longest run of 1s for a given integer n's binary representation.
#
# Example:
# Input: 242
# Output: 4
# 242 in binary is 0b11110010, so the longest run of 1 is 4.
#
# def longest_run(n):
#   # Fill this in.
#
# print longest_run(242)
# # 4

import pytest


def longest_run(n):
    count, max_count = 0, 0
    while n > 0:
        if n & 1 != 0:
            print(n)
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
        n = n >> 1
    return max(max_count, count)


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 1),
    (5, 1),
    (6, 2),
    (7, 3),
    (8, 1),
    (9, 1),
    (242, 4),
    (255, 8),
])
def test_longest_run(n, expected):
    actual = longest_run(n)
    assert expected == actual
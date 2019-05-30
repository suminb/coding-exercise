# This is not from LeetCode
# https://www.geeksforgeeks.org/next-greater-element/

import pytest

from typing import List


def next_greater_element(xs: List[int]) -> List[int]:
    """NOTE: This is a brute-force solution."""
    n = len(xs)
    j = 0
    res = []
    for i, curr in enumerate(xs):
        j = i
        while j < n and xs[j] <= curr:
            j += 1
        res.append(xs[j] if j < n else -1)

    return res


@pytest.mark.parametrize('xs, expected', [
    ([4, 5, 2, 25], [5, 25, 25, -1]),
    ([13, 7, 6, 12], [-1, 12, 12, -1]),
])
def test_next_greater_element(xs, expected):
    actual = next_greater_element(xs)
    assert expected == actual

if __name__ == '__main__':
    pytest.main(['-v', __file__])


# Looks like we could solve this in linear time: https://www.ideserve.co.in/learn/next-great-element-in-an-array
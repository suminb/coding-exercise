# [Daily Problem] Subarray With Target Sum
#
# def find_continuous_k(list, k):
#   # Fill this in.
#
# print find_continuous_k([1, 3, 2, 5, 7, 2], 14)
# # [2, 5, 7]

import pytest


def find_continuous_k(xs, k):
    left, right = 0, 0  # (inclusive, exclusive)
    n = len(xs)
    s = 0

    while s != k:
        if s > k and left < n:
            s -= xs[left]
            left += 1
        elif s < k and right < n:
            s += xs[right]
            right += 1
        else:
            left = right = n
            # TODO: Could we do this without the break statement?
            break

    return xs[left:right]


@pytest.mark.parametrize("xs, k, expected", [
    ([], 0, []),
    ([1], 1, [1]),
    ([1], 2, []),
    ([1, 2], 2, [2]),
    ([1, 2, 3], 2, [2]),
    ([1, 3, 5, 7, 9], 12, [5, 7]),
    ([1, 3, 5, 7, 9], 13, []),
    ([1, 3, 2, 5, 7, 2], 14, [2, 5, 7]),
])
def test_find_continuous_k(xs, k, expected):
    actual = find_continuous_k(xs, k)
    assert expected == actual
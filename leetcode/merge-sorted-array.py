# 88. Merge Sorted Array
# difficulty: easy

from typing import List

import pytest


class Solution:
    def merge(self, xs: List[int], m: int, ys: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n - 1
        i = m - 1
        j = n - 1
        while k >= 0:
            # print('before', xs, ys, i, j, k)
            if i < 0:
                xs[k] = ys[j]
                j -= 1
            elif j < 0:
                xs[k] = xs[i]
                i -= 1
            elif xs[i] > ys[j]:
                xs[k] = xs[i]
                i -= 1
            else:
                xs[k] = ys[j]
                j -= 1
            k -= 1
            # print('after ', xs, ys, i, j, k)


@pytest.mark.parametrize('xs, m, ys, n, expected', [
    (
        [1, 0], 1,
        [1], 1,
        [1, 1]
    ), (
        [2, 0], 1,
        [1], 1,
        [1, 2]
    ), (
        [1, 3, 5, 0, 0, 0], 3,
        [2, 4], 2,
        [1, 2, 3, 4, 5, 0]
    ), (
        [1, 2, 3, 0, 0, 0], 3,
        [2, 5, 6], 3,
        [1, 2, 2, 3, 5, 6]
    )
])
def test_merge(xs, m, ys, n, expected):
    s = Solution()
    s.merge(xs, m, ys, n)
    assert xs == expected

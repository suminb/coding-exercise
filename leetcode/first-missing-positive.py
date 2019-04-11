# 41. First Missing Positive
# difficulty: hard
# https://leetcode.com/problems/first-missing-positive/

from typing import List

import pytest


class Solution:
    def firstMissingPositive(self, xs: List[int]) -> int:
        """Found a magical algorithm on https://leetcode.com/problems/first-missing-positive/discuss/17080/Python-O(1)-space-O(n)-time-solution-with-explanation
        """
        # We will need in case of xs is consist of all consecutive positive
        # numbers.
        xs.append(0)
        n = len(xs)

        # Given a list of length of n, the first missing positive will be in
        # [1, n + 1] range. So we can ignore all other values out of this
        # range.
        for i, x in enumerate(xs):
            if x < 0 or x >= n:
                xs[i] = 0

        for i, x in enumerate(xs):
            xs[x % n] += n

        for i, x in enumerate(xs):
            if x // n == 0:
                return i

        return n


@pytest.mark.parametrize('xs, expected', [
    ([], 1),
    ([1,2,0], 3),
    ([3,4,-1,1], 2),
    ([7,8,9,11,12], 1),
    ([1, 1], 2),
    ([1, 1000], 2),
    ([0, 3], 1),
])
def test(xs, expected):
    s = Solution()
    assert expected == s.firstMissingPositive(xs)

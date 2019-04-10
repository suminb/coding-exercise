# 41. First Missing Positive
# difficulty: hard
# https://leetcode.com/problems/first-missing-positive/

import pytest


class Solution:
    def firstMissingPositive(self, xs: List[int]) -> int:
        # FIMXE: Your algorithm should run in O(n) time and uses constant extra space.
        ps = [x for x in set(xs) if x > 0]
        if not ps:
            return 1

        pmin, pmax, psum = min(ps), max(ps), sum(ps)
        
        if pmin > 1:
            return 1
        else:
            fullsum = pmax * (pmax + 1) // 2
            if psum == fullsum:
                return pmax + 1
            else:
                return fullsum - psum


@pytest.mark.parametrize('xs, expected', [
    ([], 1),
    ([1,2,0], 3),
    ([3,4,-1,1], 2),
    ([7,8,9,11,12], 1),
    ([1, 1], 2),
    ([1, 1000], 2),
])
def test(xs, expected):
    s = Solution()
    assert expected == s.firstMissingPositive(xs)
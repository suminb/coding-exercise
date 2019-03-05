# 47. Permutations II

from typing import List


class Solution:
    def permuteUnique(self, xs: List[int]) -> List[List[int]]:
        if not xs:
            return [[]]
        else:
            r, s = [], set()
            for i, x in enumerate(xs):
                if x not in s:
                    s.add(x)
                    for p in self.permuteUnique(xs[:i] + xs[i + 1:]):
                        r.append([x] + p)
            return r


def test(assert_list_equals):
    s = Solution()

    p = s.permuteUnique([])
    assert p == [[]]

    p = s.permuteUnique([1, 2, 3])
    assert_list_equals(p, [
        [1, 2, 3], [1, 3, 2],  [2, 1, 3], [2, 3, 1],  [3, 1, 2], [3, 2, 1]])

    p = s.permuteUnique([1, 1, 2])
    assert_list_equals(p, [[1, 1, 2], [1, 2, 1], [2, 1, 1]])

    p = s.permuteUnique([3, 3, 0, 3])
    assert_list_equals(p, [
        [0, 3, 3, 3], [3, 0, 3, 3], [3, 3, 0, 3], [3, 3, 3, 0]])

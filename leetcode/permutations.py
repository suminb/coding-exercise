# 46. Permutations

from typing import List

class Solution:
    def permute(self, xs: List[int]) -> List[List[int]]:
        if not xs:
            return [[]]
        else:
            r = []
            for i, x in enumerate(xs):
                for p in self.permute(xs[:i] + xs[i + 1:]):
                    r.append([x] + p)

            return r


def test():
    s = Solution()
    p = s.permute([1, 2, 3])
    assert p == [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

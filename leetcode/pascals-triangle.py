# 118. Pascal's Triangle
# difficulty: easy
# https://leetcode.com/problems/pascals-triangle/

from typing import List


class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n < 1:
            return []
        xs = [1]
        serieses = [xs]
        for i in range(1, n):
            xs = generate(xs)
            serieses.append(xs)
        return serieses


def generate(prev):
    return [x + y for x, y in zip([0] + prev, prev + [0])]

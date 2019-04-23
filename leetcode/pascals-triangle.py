# 118. Pascal's Triangle
# difficulty: easy
# https://leetcode.com/problems/pascals-triangle/

from typing import List

import pytest


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


@pytest.mark.parametrize('value, expected', [
    ([1], [1, 1]),
    ([1, 1], [1, 2, 1]),
    ([1, 2, 1], [1, 3, 3, 1]),
])
def test(value, expected):
    assert expected == generate(value)


if __name__ == '__main__':
    pytest.main(['-v', __file__])
# 69. Sqrt(x)
# difficulty: easy

import pytest


class Solution:
    def mySqrt(self, x: int) -> int:
        p = leading_one_position(x)
        sqrt = 0
        while p >= 0:
            mask = 1 << p
            print(f'sqrt={sqrt}, x={x}, p={p}, mask={mask}, masked={(x & mask) >> p}')
            sqrt = sqrt | ((x & mask) >> (p - p // 2))
            p -= 1
        return sqrt


def leading_one_position(x):
    i = -1
    while x != 0:
        x = x >> 1
        i += 1
    return i


@pytest.mark.parametrize('x, expected', [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2),
    (8, 2),
    (9, 3),
    (10, 3),
    (15, 3),
    (16, 4),
    (17, 4),
])
def test(x, expected):
    s = Solution()
    assert s.mySqrt(x) == expected


if __name__ == '__main__':
    pytest.main(['-v', 'sqrtx.py'])
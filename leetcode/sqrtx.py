# 69. Sqrt(x)
# difficulty: easy

import pytest


class Solution:
    def mySqrt(self, x: int) -> int:
        return binary_search_sqrt(x)


def binary_search_sqrt(x):
    left, right, v = 1, x, x // 2

    if x == 0:
        return 0

    while v >= 1:
        if v * v > x:
            right = v
            v //= 2
        elif v * v < x:
            left = max(left, v)
            v = (left + right) // 2
            if left == v:
                return v
        else:
            return v
    return left


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
    (19, 4),
    (1000, 31),
    (1234, 35),
    (12345, 111),
    (777777, 881),
])
def test(x, expected):
    s = Solution()
    assert s.mySqrt(x) == expected


if __name__ == '__main__':
    pytest.main(['-v', __file__])

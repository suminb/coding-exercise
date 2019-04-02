# 70. Climbing Stairs
# difficulty: easy

import pytest


class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        return climb_stairs_2(n, cache)


def climb_stairs_1(n, depth=1):
    """Brute force solution"""
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return climb_stairs_1(n - 1, depth+1) + climb_stairs_1(n - 2, depth+1)


def climb_stairs_2(n: int, cache: dict):
    """Saves intermediate results."""
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in cache:
        return cache[n]
    else:
        cache[n] = climb_stairs_2(n - 1, cache) + climb_stairs_2(n - 2, cache)
        return cache[n]


@pytest.mark.parametrize('n, x', [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 8),
    (8, 34),
    (15, 987),
])
def test(n, x):
    try:
        assert x == climb_stairs_1(n)
    except RecursionError:
        pass

    cache = {}
    assert x == climb_stairs_2(n, cache)


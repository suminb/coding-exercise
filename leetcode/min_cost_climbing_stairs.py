# 746. Min Cost Climbing Stairs
# difficulty: easy
# https://leetcode.com/problems/min-cost-climbing-stairs/submissions/

from typing import List

import pytest


class Solution:
    def __init__(self):
        self.cache = {}

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.min_cost(0, cost), self.min_cost(1, cost))

    def min_cost(self, index, costs):
        n = len(costs)
        if index >= n:
            return 0
        else:
            if index in self.cache:
                return self.cache[index]
            else:
                cost = costs[index] + min(
                    self.min_cost(index + 1, costs), self.min_cost(index + 2, costs))
                self.cache[index] = cost
                return cost


@pytest.mark.parametrize("costs, expected", [
    ([0, 0, 1, 1], 1), # NOTE: This should work, but in LeetCode says my code spits out '0' as a result
    ([10, 15, 20], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
])
def test_basic(costs, expected):
    actual = Solution().minCostClimbingStairs(costs)
    assert actual == expected
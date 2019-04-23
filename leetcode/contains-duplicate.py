# 217. Contains Duplicate
# difficulty: easy
# https://leetcode.com/problems/contains-duplicate/

from typing import List

import pytest


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return n_log_n_time_solution(nums)


def linear_time_solution(nums):
    """An O(n) time, O(n) space solution."""
    counts = {}
    for x in nums:
        counts.setdefault(x, 0)
        counts[x] += 1

    return any([x > 1 for x in counts.values()])


def n_log_n_time_solution(nums):
    """An O(n log n) time, O(1) space solution."""
    if len(nums) < 2:
        return False
    nums.sort()
    return any([x == y for x, y in zip(nums[:-1], nums[1:])])


@pytest.mark.parametrize('values, expected', [
    ([], False),
    ([0], False),
    ([1, 2, 3], False),
    ([1, 2, 3, 1], True),
])
def test(values, expected):
    assert expected == linear_time_solution(values)
    assert expected == n_log_n_time_solution(values)


if __name__ == '__main__':
    pytest.main(['-v', __file__])

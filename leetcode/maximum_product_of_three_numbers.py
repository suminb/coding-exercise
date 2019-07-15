# 628. Maximum Product of Three Numbers
# difficulty: easy
# https://leetcode.com/problems/maximum-product-of-three-numbers/

from functools import reduce

from typing import List

import pytest


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        return maximum_product_by_sorting(nums)


def maximum_product_by_sorting(nums):
    nums.sort(reverse=True)
    return max(product(nums[:3]), product([nums[0], nums[-1], nums[-2]]))


def product(nums):
    return reduce(lambda x, y: x * y, nums)


@pytest.mark.parametrize('nums, expected', [
    ([1, 2, 3], 6),
    ([1, 2, 3, 4], 24), 
    ([1, 2, 3, 7, 9, -1, -13, -11], 1287), 
])
def test_maximum_product(nums, expected):
    actual = maximum_product_by_sorting(nums)
    assert expected == actual


if __name__ == '__main__':
    pytest.main([__file__])
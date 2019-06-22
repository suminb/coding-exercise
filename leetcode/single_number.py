# 136. Single Number
# difficulty: easy
# https://leetcode.com/submissions/detail/202469273/

import pytest


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return single_number_without_extra_space(nums)


def single_number_with_set(nums):
    """Set creation can be done in linear time, as insertion to a hash set is
    a constant time operation. However, this solution inccurs extra memory of
    O(n).
    """
    return sum(set(nums)) * 2 - sum(nums)


def single_number_without_extra_space(nums):
    """Done with XOR operations.

    Provided that:

        x ^ 0 = x
        x ^ x = 0

    We can find a single number as follows:

        x ^ y ^ x = (x ^ x) ^ y = 0 ^ y = y

    Time complexity: O(n)
    Space complexity: O(1)
    """    
    x = 0
    for n in nums:
        x = x ^ n
    return x


@pytest.mark.parametrize('nums, expected', [
    ([1], 1),
    ([2, 2, 1], 1), 
    ([4, 1, 2, 1, 2], 4), 
    # TODO: Write more test cases
])
def test_single_number(nums, expected):
    actual = single_number_with_set(nums)
    assert expected == actual

    actual = single_number_without_extra_space(nums)
    assert expected == actual
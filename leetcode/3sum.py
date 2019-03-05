# 15. 3Sum

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return [c for c in self.generate_combinations(sorted(nums), 3) if sum(c) == 0]

    def generate_combinations(self, nums, k):
        if k == 0:
            return [[]]

        combs = []
        prev_n = None
        for i, n in enumerate(nums, 1):
            if n != prev_n:
                for c in self.generate_combinations(nums[i:], k - 1):
                    combs.append([n] + c)
                prev_n = n
        return combs


def test(assert_list_equals):
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    assert_list_equals(s.threeSum(nums), [[-1, 0, 1], [-1, -1, 2]])

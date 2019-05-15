# 15. 3Sum

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = 0
        n = len(nums)
        res = []
        nums.sort()

        while l < n - 2:
            while 0 < l < n - 2 and nums[l] == nums[l - 1]:
                l += 1

            m, r = l + 1, n - 1
            while m < r:
                comb = [nums[l], nums[m], nums[r]]
                s = sum(comb)
                if s < 0:
                    m += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append(comb)
                    while m < r and nums[m] == nums[m + 1]:
                        m += 1
                    while m < r and nums[r] == nums[r - 1]:
                        r -= 1
                    m += 1
                    r -= 1
            l += 1

        return res


def test(assert_list_equals):
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum(nums))
    assert_list_equals(s.threeSum(nums), [[-1, 0, 1], [-1, -1, 2]])

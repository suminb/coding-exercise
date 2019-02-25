# 35. Search Insert Position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, n = 0, len(nums)
        while i < n:
            x = nums[i]
            if x == target:
                return i
            elif x > target:
                return i
            i += 1
        return i

# Took me less than 5min
# https://leetcode.com/submissions/detail/210566050/

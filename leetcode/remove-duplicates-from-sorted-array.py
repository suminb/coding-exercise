class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        last = nums[0]
        offset = 1
        for x in nums:
            if last != x:
                last = x
                nums[offset] = x
                offset += 1

        return offset


# https://leetcode.com/submissions/detail/204019073/

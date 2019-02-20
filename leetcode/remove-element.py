class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        offset = 0
        # n = len(nums)
        # for i in range(n):
        for i, x in enumerate(nums):
            # nums[offset] = nums[i]
            # if nums[i] != val:
            if x != val:
                nums[offset] = x
                offset += 1

        return offset


# https://leetcode.com/submissions/detail/207426040/

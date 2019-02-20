class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cache = {}
        for i in range(len(nums)):
            m = nums[i]
            if m in cache:
                return [cache[m], i]
            else:
                cache[target - m] = i


# https://leetcode.com/submissions/detail/202462306/

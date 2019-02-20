INITIAL = 0
ACCEPTING = 1
NOT_ACCEPTING = 2

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        state = INITIAL
        offset = 0
        last = None

        for x in nums:
            nums[offset] = x
            state, offset = self.next_state(state, x == last, offset)
            last = x

        return offset

    def next_state(self, state, equals, offset):
        if state == INITIAL:
            return ACCEPTING, offset + 1
        elif state == ACCEPTING:
            if equals:
                return NOT_ACCEPTING, offset + 1
            else:
                return ACCEPTING, offset + 1
        elif state == NOT_ACCEPTING:
            if equals:
                return NOT_ACCEPTING, offset
            else:
                return ACCEPTING, offset + 1


# https://leetcode.com/submissions/detail/204260146/

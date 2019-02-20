class Solution:
    OPENING = '({['
    CLOSING = ')}]'
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for p in s:
            if p in OPENING:
                stack.append(p)
            elif p in CLOSING:
                q = stack.pop()
                if p != q:
                    return False
            else:
                raise ValueError('Invalid input')

        return True


# https://leetcode.com/submissions/detail/204489842/

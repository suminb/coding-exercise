class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        offset = 0
        for xs in zip(*strs):
            t = all([x == xs[0] for x in xs[1:]])
            if t:
                offset += 1
            else:
                break

        return strs[0][:offset]


# https://leetcode.com/submissions/detail/203576287/

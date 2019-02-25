vs = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

ss = {
    # X can be placed after Y (denoting Y - X)
    'V': 'I',
    'X': 'I',
    'L': 'X',
    'C': 'X',
    'D': 'C',
    'M': 'C',
}

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value, prev = 0, None
        for i, curr in enumerate(s):
            if curr in ss and prev == ss[curr]:
                value += vs[curr] - vs[prev] * 2
            else:
                value += vs[curr]
            prev = curr
        return value

# https://leetcode.com/submissions/detail/210563927/

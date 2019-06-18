# 9. Palindrome Number
# difficulty: easy
# https://leetcode.com/problems/palindrome-number/submissions/

import pytest


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        n = len(s)
        return all([(s[i] == s[n-i-1]) for i in range(0, n//2)])
    
        # Even simpler solution would be possible, but this probably won't cut it for tech interviews.
        # return s == s[::-1]


@pytest.mark.parametrize('x, expected', [
    (0, True),
    (1, True),
    (121, True),
    (-121, False),
    (1234567, False),
    (10, False),
])
def test_palindrom_number(x, expected):
    s = Solution()
    actual = s.isPalindrome(x)
    assert expected == actual

# 125. Valid Palindrome
# difficulty: easy
# https://leetcode.com/problems/valid-palindrome/

import pytest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        xs = [x for x in s.lower() if x.isalnum()]
        n = len(xs)
        mid = n // 2
        return all([x == y for x, y in zip(xs[:mid + 1], xs[n:mid - 1:-1])])


@pytest.mark.parametrize('xs, expected', [
    ('', True),
    ('a', True),
    (';,.', True),
    ('A man, a plan, a canal: Panama', True),
    ('asdf', False),
    ('race a car', False),
])
def test(xs, expected):
    s = Solution()
    assert expected == s.isPalindrome(xs)


if __name__ == '__main__':
    pytest.main(['-v', 'valid-palindrome.py'])

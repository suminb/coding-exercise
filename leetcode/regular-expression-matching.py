# 10. Regular Expression Matching
# difficulty: hard
# https://leetcode.com/problems/regular-expression-matching/

import pytest


class Solution:
    def isMatch(self, string: str, pattern: str) -> bool:
        i = j = 0
        state = 'ACCEPTING'

        ss = string + '$$'
        ps = tokenize_pattern(pattern)
        n, m = len(ss) - 1, len(ps)

        while i < n and j < m:
            state, i, j = next_state(state, ss[i], ss[i + 1], ps[j], i, j)

            if state == 'ACCEPTED':
                return True
            elif state == 'REJECTED':
                return False
        return False


def tokenize_pattern(pattern):
    i, n = 0, len(pattern)
    tokens = []
    while i < n:
        if i + 1 < n and pattern[i + 1] == '*':
            tokens.append(pattern[i:i + 2])
            i += 2
        else:
            tokens.append(pattern[i])
            i += 1
    tokens.append('$')
    return tokens


def next_state(state, string, next_string, pattern, i, j):
    if is_asterisk(pattern):
        if next_string == pattern[0]:
            return 'ACCEPTING', i + 1, j + 1
        elif string != '$' and pattern[0] in ('.', string):
            return 'ACCEPTING', i + 1, j
        else:
            return 'ACCEPTING', i, j + 1
    else:
        if string == pattern == '$':
            return 'ACCEPTED', i, j
        if pattern in ('.', string):
            return 'ACCEPTING', i + 1, j + 1
        else:
            return 'REJECTED', i, j


def is_asterisk(pattern):
    return len(pattern) == 2 and pattern[1] == '*'


@pytest.mark.parametrize('pattern, tokens', [
    ('a', ['a', '$']),
    ('ab', ['a', 'b', '$']),
    ('a*', ['a*', '$']),
    ('a*bbc*', ['a*', 'b', 'b', 'c*', '$']),
    ('a.*b', ['a', '.*', 'b', '$']),
])
def test_tokenize_pattern(pattern, tokens):
    assert tokenize_pattern(pattern) == tokens


@pytest.mark.parametrize('string, pattern', [
    ('', ''),
    ('', '.*'),
    ('aa', 'a*'),
    ('ab', '.*'),
    ('mississippi', 'mis*is*ip*.'),
])
def test_match(string, pattern):
    s = Solution()
    assert s.isMatch(string, pattern)


@pytest.mark.parametrize('string, pattern', [
    ('a', ''),
    ('aa', 'a'),
    ('abc', 'x'),
    ('abc', 'abd'),
    ('mississippi', 'mis*is*p*.'),
])
def test_non_match(string, pattern):
    s = Solution()
    assert not s.isMatch(string, pattern)


def test():
    s = Solution()
    assert s.isMatch('aaa', 'a*a')


if __name__ == '__main__':
    pytest.main(['-v', 'regular-expression-matching.py'])

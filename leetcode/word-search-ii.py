# 212. Word Search II
# difficulty: hard
# https://leetcode.com/problems/word-search-ii/

from collections import deque
from typing import List

import pytest


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        return sorted([word for word in words if contains_word(board, word)])


def contains_word(board, word):
    n, m = len(board), len(board[0])
    for i in range(n):
        for j in range(m):
            visited = {}
            if contains_word_from(board, word, i, j, 0, visited):
                return True
    return False


def contains_word_from(board, word, i, j, k, visited):
    n, m = len(board), len(board[0])
    word_len = len(word)

    if not (0 <= i < n and 0 <= j < m):
        return False
    if k >= word_len:
        return False
    if (i, j) in visited:
        return False

    char = board[i][j]

    if char == word[k]:
        if k + 1 == word_len:
            return True
        params = [
            (i - 1, j),
            (i, j + 1),
            (i + 1, j),
            (i, j - 1),
        ]
        visited[(i, j)] = True
        for ii, jj in params:
            if contains_word_from(board, word, ii, jj, k + 1, visited):
                return True
        del visited[(i, j)]

    return False


def test_contains_word_1():
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    assert contains_word(board, 'o')
    assert contains_word(board, 'oa')
    assert contains_word(board, 'oat')
    assert contains_word(board, 'oath')
    assert contains_word(board, 'eta')
    assert not contains_word(board, 'ra')
    assert not contains_word(board, 'xyz')


def test_contains_word_2():
    board = [
        ['a', 'a']
    ]
    assert contains_word(board, 'aa')
    assert not contains_word(board, 'aaa')


def test_find_words_1():
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    words = ['oath', 'pea', 'eat', 'rain']
    expected = ['eat', 'oath']

    s = Solution()
    assert expected == s.findWords(board, words)


def test_find_words_2():
    board = [
        ['a', 'b'],
        ['a', 'a'],
    ]
    words = ['aba', 'baa', 'bab', 'aaab', 'aaa', 'aaaa', 'aaba']
    expected = ['aaa', 'aaab', 'aaba', 'aba', 'baa']

    # NOTE: One of the important keys is to use DFS, otherwise it won't catch
    # an edge case like 'aaba'.

    s = Solution()
    assert expected == s.findWords(board, words)


def test_find_words_3():
    board = [
        ['a', 'b'],
        ['c', 'd'],
    ]
    words = ['acdb']
    expected = ['acdb']

    s = Solution()
    assert expected == s.findWords(board, words)


def test_find_words_4():
    board = [
        ['a', 'b'],
        ['c', 'd'],
    ]
    words = ['ab', 'cb', 'ad', 'bd', 'ac', 'ca', 'da', 'bc', 'db', 'adcb', 'dabc', 'abb', 'acb']
    expected = ['ab', 'ac', 'bd', 'ca', 'db']

    s = Solution()
    assert expected == s.findWords(board, words)


def test_find_words_5():
    board = [
        ['a', 'b', 'c'], 
        ['a', 'e', 'd'], 
        ['a', 'f', 'g'], 
    ]
    words = ['abcdefg', 'gfedcbaaa', 'eaabcdgfa', 'befa', 'dgc', 'ade']
    expected = ['abcdefg', 'befa', 'eaabcdgfa', 'gfedcbaaa']

    s = Solution()
    assert expected == s.findWords(board, words)


def test_find_words_6():
    board = [
        ['b', 'a', 'a', 'b', 'a', 'b'], 
        ['a', 'b', 'a', 'a', 'a', 'a'], 
        ['a', 'b', 'a', 'a', 'a', 'b'], 
        ['a', 'b', 'a', 'b', 'b', 'a'], 
        ['a', 'a', 'b', 'b', 'a', 'b'], 
        ['a', 'a', 'b', 'b', 'b', 'a'], 
        ['a', 'a', 'b', 'a', 'a', 'b'], 
    ]
    words = [
        'bbaabaabaaaaabaababaaaaababb',
        'aabbaaabaaabaabaaaaaabbaaaba',
        'babaababbbbbbbaabaababaabaaa',
        'bbbaaabaabbaaababababbbbbaaa',
        'babbabbbbaabbabaaaaaabbbaaab',
        'bbbababbbbbbbababbabbbbbabaa',
        'babababbababaabbbbabbbbabbba',
        'abbbbbbaabaaabaaababaabbabba',
        'aabaabababbbbbbababbbababbaa',
        'aabbbbabbaababaaaabababbaaba',
        'ababaababaaabbabbaabbaabbaba',
        'abaabbbaaaaababbbaaaaabbbaab',
        'aabbabaabaabbabababaaabbbaab',
        'baaabaaaabbabaaabaabababaaaa',
        'aaabbabaaaababbabbaabbaabbaa',
        'aaabaaaaabaabbabaabbbbaabaaa',
        'abbaabbaaaabbaababababbaabbb',
        'baabaababbbbaaaabaaabbababbb',
        'aabaababbaababbaaabaabababab',
        'abbaaabbaabaabaabbbbaabbbbbb',
        'aaababaabbaaabbbaaabbabbabab',
        'bbababbbabbbbabbbbabbbbbabaa',
        'abbbaabbbaaababbbababbababba',
        'bbbbbbbabbbababbabaabababaab',
        'aaaababaabbbbabaaaaabaaaaabb',
        'bbaaabbbbabbaaabbaabbabbaaba',
        'aabaabbbbaabaabbabaabababaaa',
        'abbababbbaababaabbababababbb',
        'aabbbabbaaaababbbbabbababbbb',
        'babbbaabababbbbbbbbbaabbabaa',
    ]
    expected = [
        'aabbbbabbaababaaaabababbaaba',
        'abaabbbaaaaababbbaaaaabbbaab',
        'ababaababaaabbabbaabbaabbaba'
    ]

    s = Solution()
    assert expected == s.findWords(board, words)

if __name__ == '__main__':
    pytest.main(['-v', __file__])

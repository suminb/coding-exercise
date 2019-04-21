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
            if contains_word_from(board, word, i, j):
                return True
    return False


def contains_word_from(board, word, i, j):
    k = 0
    n, m = len(board), len(board[0])
    visited = {}
    queue = deque([(i, j)])

    while queue:
        i, j = queue.popleft() 
        if not (0 <= i < n and 0 <= j < m):
            continue
        if (i, j) in visited:
            continue

        char = board[i][j]

        if k < len(word) and char == word[k]:
            if k + 1 == len(word):
                return True
            queue.append((i - 1, j))
            queue.append((i + 1, j))
            queue.append((i, j - 1))
            queue.append((i, j + 1))
            visited[(i, j)] = True
            k += 1

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


if __name__ == '__main__':
    pytest.main(['-v', 'word-search-ii.py'])
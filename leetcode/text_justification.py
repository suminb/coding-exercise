#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
# difficulty: hard
# https://leetcode.com/problems/text-justification/
#

import pytest

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        return list(full_justify(words, maxWidth))


def full_justify(words, max_width):
    lines = list(break_down_to_lines(words, max_width))
    n = len(lines)

    for i, line in enumerate(lines):
        if i == n - 1:
            # If last line
            yield left_justify_line(line, max_width)
        else:
            yield full_justify_line(line, max_width)


def left_justify_line(words, max_width):
    line = ' '.join(words)
    space_length = max_width - len(line)

    return line + (' ' * space_length)


def full_justify_line(words, max_width):
    words_length = sum([len(w) for w in words])
    word_count = len(words)
    space_length = max_width - words_length
    space_count = word_count - 1

    res = [words[0]]
    for word in words[1:]:
        # TODO: Deal with edge cases
        res.append(' ' * (space_length // space_count))
        res.append(word)

    # FIXME: Logically correct, but very inefficient
    index = 1
    while sum([len(w) for w in res]) < max_width:
        res.insert(index, ' ')
        index += 3

    return ''.join(res)


def break_down_to_lines(words, max_width):
    line = []
    line_width = 0
    for word in words:
        word_width = len(word)
        space_width = 1 if line else 0
        if line_width + word_width + space_width > max_width:
            yield line
            line = []
            line_width = 0
        space_width = 1 if line else 0
        line.append(word)
        line_width += word_width + space_width
    if line:
        yield line


@pytest.mark.parametrize('words, max_width, expected', [
    (["This", "is", "an", "example", "of", "text", "justification."], 16,
     ["This    is    an","example  of text","justification.  "]),
    (["What","must","be","acknowledgment","shall","be"], 16,
     ["What   must   be", "acknowledgment  ", "shall be        "]),
    (["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20,
     ["Science  is  what we","understand      well","enough to explain to","a  computer.  Art is","everything  else  we","do                  "]),
    # TODO: Write more test cases
])
def test_full_justify(words, max_width, expected):
    actual = Solution().fullJustify(words, max_width)
    assert expected == actual
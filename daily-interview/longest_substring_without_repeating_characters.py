# Hi, here's your problem today. This problem was recently asked by Microsoft:
#
# Given a string, find the length of the longest substring without repeating
# characters.
#
# Here is an example solution in Python language. (Any language is OK to use in
# an interview, though we'd recommend Python as a generalist language utilized
# by companies like Google, Facebook, Netflix, Dropbox, Pinterest, Uber, etc.,)
#
# Can you find a solution in linear time?

import pytest


def length_of_longest_substring(s):
    """Linear time, linear space solution."""
    n = len(s)
    left, right = 0, 0
    max_len = 0
    counts = {}

    while right < n and left <= right:
        ch = s[right]
        counts.setdefault(ch, 0)
        if counts[ch] == 0:
            counts[ch] += 1
            right += 1
        else:
            counts[s[left]] -= 1
            left += 1

        max_len = max(right - left, max_len)

    return max_len


@pytest.mark.parametrize("s, expected", [
    ("", 0),
    ("a", 1),
    ("abcde", 5),
    ("abrkaabcdefghijjxxx", 10),
    ("zzz", 1),
    ("aabcccccdddeeffff", 3),
    ("1234512312312345612345", 6),
])
def test(s, expected):
    assert expected == length_of_longest_substring(s)
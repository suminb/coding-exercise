# Reverse Words in a String
#
# Given a string, you need to reverse the order of characters in each word
# within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "The cat in the hat"
# Output: "ehT tac ni eht tah"
# Note: In the string, each word is separated by single space and there will
# not be any extra space in the string.
#
# Here's a starting point:
#
# class Solution:
#   def reverseWords(self, str):
#     # Fill this in.
#
# print Solution().reverseWords("The cat in the hat")
# # ehT tac ni eht tah

import pytest


def reverse_words(s):
    return " ".join([w[::-1] for w in s.split()])


@pytest.mark.parametrize("s, expected", [
    ("", ""),
    ("w", "w"),
    ("word", "drow"),
    ("The cat in the hat", "ehT tac ni eht tah"),
])
def test_reverse_words(s, expected):
    actual = reverse_words(s)
    assert expected == actual
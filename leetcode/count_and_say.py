#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
# difficulty: easy
# https://leetcode.com/problems/count-and-say
#

import pytest


class Solution:
    def countAndSay(self, n: int) -> str:
        return count_and_say(n)


def count_and_say(n):
    if n == 1:
        return '1'
    else:
        prev_seq = count_and_say(n - 1)
        curr_seq = []
        prev = None
        for p in prev_seq:
            if prev != p:
                curr_seq.append([p, 1])
                prev = p
            else:
                curr_seq[-1][1] += 1
        return ''.join([str(c) + str(v) for v, c in curr_seq])
        

@pytest.mark.parametrize('n, expected', [
    (1, '1'),
    (2, '11'),
    (3, '21'),
    (4, '1211'),
    (5, '111221'),
    (6, '312211'),
    (7, '13112221'),
    (20, '11131221131211132221232112111312111213111213211231132132211211131221131211221321123113213221123113112221131112311332211211131221131211132211121312211231131112311211232221121321132132211331121321231231121113112221121321133112132112312321123113112221121113122113121113123112112322111213211322211312113211'),
])
def test_count_and_say(n, expected):
    actual = count_and_say(n)
    assert expected == actual

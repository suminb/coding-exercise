# 49. Group Anagrams
# difficulty: medium
# https://leetcode.com/problems/group-anagrams/

from typing import List

import pytest


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return group_anagrams(strs)


def group_anagrams(strs):
    res = {}
    for s in strs:
        key = tuple(sorted(s))
        res.setdefault(key, [])
        res[key].append(s)
    return [sorted(v) for k, v in res.items()]


@pytest.mark.parametrize('strs, expected', [
    ([], []),
    (["eat", "tea", "tan", "ate", "nat", "bat"], [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]),
])
def test_group_anagrams(strs, expected):
    actual = group_anagrams(strs)
    assert expected == actual
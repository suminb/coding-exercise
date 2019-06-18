# 763. Partition Labels
# difficulty: medium
# submissions:
# https://leetcode.com/problems/partition-labels/
# - https://leetcode.com/submissions/detail/211196386/ (33min, 35.62%)
# - https://leetcode.com/submissions/detail/211198527/

from typing import List

import pytest


class Solution:
    def partitionLabels(self, xs: str) -> List[int]:
        max_indices = {x: i for i, x in enumerate(xs)}
        max_index = 0
        indices = [-1]
        for i, x in enumerate(xs):
            max_index = max(max_index, max_indices[x])
            if i == max_index:
                indices.append(max_index)
        return [i2 - i1 for i1, i2 in zip(indices[:-1], indices[1:])]


@pytest.mark.parametrize('string, expected', [
    ('aaaa', [4]),
    ('xyz', [1, 1, 1]),
    ('ababcbacadefegdehijhklij', [9, 7, 8]),
])
def test_partition_labels(string, expected):
    s = Solution()
    actual = s.partitionLabels(string)
    assert expected == actual

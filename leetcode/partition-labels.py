# 763. Partition Labels
# difficulty: medium
# submissions:
# - https://leetcode.com/submissions/detail/211196386/ (33min, 35.62%)

from typing import List


class Solution:
    def partitionLabels(self, xs: str) -> List[int]:
        max_indices = {x: i for i, x in enumerate(xs)}
        bucket = set()
        indices = [-1]
        for i, x in enumerate(xs):
            bucket.add(x)
            max_index = max([max_indices[b] for b in bucket])
            if i == max_index:
                indices.append(max_index)
                bucket = set()
        return [i2 - i1 for i1, i2 in zip(indices[:-1], indices[1:])]


def test_solution():
    s = Solution()
    indicies = s.partitionLabels('ababcbacadefegdehijhklij')
    assert indicies == [9, 7, 8]

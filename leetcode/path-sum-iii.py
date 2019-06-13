# 437. Path Sum III
# difficulty: easy

from typing import List

import pytest

from leetcode import build_binary_tree, TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> int:
        return path_sum(root, 0, sum_)


def path_sum(node, subtotal, target):
    if node:
        new_subtotal = subtotal + node.val
        ret = 1 if new_subtotal == target else 0
        print(subtotal, new_subtotal, target, ret)
        return ret + \
            path_sum(node.left, new_subtotal, target) + \
            path_sum(node.right, new_subtotal, target)
    else:
        return 0


@pytest.mark.skip
def test():
    s = Solution()

    root = build_binary_tree(
        [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    assert s.pathSum(root, 8) == 3

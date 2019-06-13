# 113. Path Sum II
# difficulty: medium

from typing import List

from leetcode import build_binary_tree, TreeNode


class Solution:
    def __init__(self):
        self.paths = []

    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        # TODO: Could we make this more elegant?
        self.path_sum(root, [], sum_)
        return self.paths

    def path_sum(self, node, path, target):
        if is_leaf(node):
            if sum(path) + node.val == target:
                self.paths.append(path + [node.val])
        elif node is not None:
            self.path_sum(node.left, path + [node.val], target)
            self.path_sum(node.right, path + [node.val], target)


def is_leaf(node):
    return node and node.left is None and node.right is None


def test():
    s = Solution()

    root = build_binary_tree(
        # NOTE: Looks like LeetCode builds trees differently
        # [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1])
    assert s.pathSum(root, 22) == [
        [5, 4, 11, 2],
        [5, 8, 4, 5]
    ]

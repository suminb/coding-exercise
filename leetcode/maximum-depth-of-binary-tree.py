# 104. Maximum Depth of Binary Tree
# difficulty: easy

from leetcode import build_binary_tree, TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.max_depth(root, 0)

    def max_depth(self, node, depth):
        if node:
            return max(self.max_depth(node.left, depth + 1), self.max_depth(node.right, depth + 1))
        else:
            return depth


def test():
    s = Solution()

    root = build_binary_tree([])
    assert s.maxDepth(root) == 0

    root = build_binary_tree([0])
    assert s.maxDepth(root) == 1

    root = build_binary_tree([1, 2, 3])
    assert s.maxDepth(root) == 2

    root = build_binary_tree([3, 9, 20, None, None, 15, 7])
    assert s.maxDepth(root) == 3

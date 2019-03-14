# 104. Maximum Depth of Binary Tree
# difficulty: easy

from common import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.max_depth(root, 0)

    def max_depth(self, node, depth):
        if node:
            return max(self.max_depth(node.left, depth + 1), self.max_depth(node.right, depth + 1))
        else:
            return depth

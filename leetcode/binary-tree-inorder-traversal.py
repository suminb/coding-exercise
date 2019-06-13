# 94. Binary Tree Inorder Traversal

from typing import List

from leetcode import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        # self.recursive(root, res)
        self.iterative(root, res)
        return res

    def recursive(self, node, res):
        if node is not None:
            self.recursive(node.left)
            res.append(node.val)
            self.recursive(node.right)

    def iterative(self, node, res):
        stack = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

    # NOTE: Not a requirement, but just out of curiosity

    def iterative_preorder(self, node, res):
        stack = []
        while node or stack:
            while node:
                stack.append(node)
                res.append(node.val)
                node = node.left
            node = stack.pop()
            node = node.right
        return res

    def iterative_postorder(self, node, rest):
        pass
        # TODO: Fill this in

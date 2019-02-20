# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        _, v = self.find(root, p, q)
        return v

    def find(self, node, p, q):
        if node is None:
            return (False, None)
        if node.val in (p.val, q.val):
            return (True, node)

        left = self.find(node.left, p, q)
        right = self.find(node.right, p, q)

        if left[0] and right[0]:
            return (True, node)
        elif left[0]:
            return (True, left[1])
        elif right[0]:
            return (True, right[1])
        else:
            return (False, None)


# https://leetcode.com/submissions/detail/209328300/
# 35min to solve
# Multiple 'Run Code' trials (without submissions)

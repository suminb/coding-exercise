# 98. Validate Binary Search Tree
# difficulty: medium

from common import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        xs = []
        self.in_order_traversal(root, xs)

        return all([x < y for x, y, in zip(xs[:-1], xs[1:])])

    def in_order_traversal(self, node, xs):
        if node is not None:
            self.in_order_traversal(node.left, xs)
            xs.append(node.val)
            self.in_order_traversal(node.right, xs)

# Test cases
# [1] = True
# [1, 1] = False
# [2, 1, 3] = True
# [2, 1, 2] = False
# [5,1,4,null,null,3,6] = False
# [10,5,15,null,null,6,20] = False

# 100. Same Tree

from common import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is None:
            return False
        elif q is None:
            return False
        else:
            return p.val == q.val \
                and self.isSameTree(p.left, q.left) \
                and self.isSameTree(p.right, q.right)

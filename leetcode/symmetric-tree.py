# 101. Symmetric Tree
# difficulty: easy

from collections import deque

from common import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return is_mirror(root, root)


def is_mirror(node1, node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    return node1.val == node2.val and \
            is_mirror(node1.left, node2.right) and \
            is_mirror(node1.right, node2.left)


def test_is_symmetric(build_binary_tree):
    s = Solution()
    root = build_binary_tree([])
    assert s.isSymmetric(root)

    root = build_binary_tree([1])
    assert s.isSymmetric(root)

    root = build_binary_tree([1, 2, 2, 3, 4, 4, 3])
    assert s.isSymmetric(root)

    root = build_binary_tree([1, 2])
    assert not s.isSymmetric(root)

    root = build_binary_tree([1, 2, 3])
    assert not s.isSymmetric(root)

    root = build_binary_tree([1, 2, 2, None, 3, None, 3])
    assert not s.isSymmetric(root)

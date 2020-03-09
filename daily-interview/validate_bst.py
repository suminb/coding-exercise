# You are given the root of a binary search tree. Return true if it is a valid binary search tree, and false otherwise. Recall that a binary search tree has the property that all values in the left subtree are less than or equal to the root, and all values in the right subtree are greater than or equal to the root.
#
# Here's a starting point:
#
# class TreeNode:
#   def __init__(self, key):
#     self.left = None
#     self.right = None
#     self.key = key
#
# def is_bst(root):
#   # Fill this in.
#
# a = TreeNode(5)
# a.left = TreeNode(3)
# a.right = TreeNode(7)
# a.left.left = TreeNode(1)
# a.left.right = TreeNode(4)
# a.right.left = TreeNode(6)
# print is_bst(a)
#
# #    5
# #   / \
# #  3   7
# # / \ /
# #1  4 6

from math import inf

import pytest

from common import build_binary_tree


def is_bst(root, left=-inf, right=inf):
    if root:
        return left <= root.val <= right and \
            is_bst(root.left, left, root.val) and \
            is_bst(root.right, root.val, right)
    else:
        return True


@pytest.mark.parametrize("root, expected", [
    ([], True),
    ([1], True),
    ([5, 3, 7, 1, 4, 6], True),
    ([1, 1, 1, 1, 1, 1, 1], True),
    ([1, 2, 3], False),
    ([2, 1, 3, 3, 2], False),
])
def test_is_bst(root, expected):
    actual = is_bst(build_binary_tree(root))
    assert expected == actual
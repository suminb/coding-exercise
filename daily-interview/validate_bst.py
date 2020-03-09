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

import pytest

from common import build_binary_tree


def is_bst(root):
    if root:
        lmin, lmax, lflag = is_bst(root.left)
        rmin, rmax, rflag = is_bst(root.right)
        lmin = coalesce(lmin, root.val)
        lmax = coalesce(lmax, root.val)
        rmin = coalesce(rmin, root.val)
        rmax = coalesce(rmax, root.val)
        return (lmin, rmax, lflag and rflag and lmax <= root.val <= rmin)
    else:
        return (None, None, True)


def coalesce(val1, val2):
    if val1:
        return val1
    else:
        return val2


@pytest.mark.parametrize("root, expected", [
    ([], True),
    ([1], True),
    ([5, 3, 7, 1, 4, 6], True),
    ([1, 2, 3], False),
])
def test_is_bst(root, expected):
    _, _, actual = is_bst(build_binary_tree(root))
    assert expected == actual
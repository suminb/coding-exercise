# Hi, here's your problem today. This problem was recently asked by Google:
#
# You are given the root of a binary tree. Return the deepest node (the furthest node from the root).
#
# Example:
#
#     a
#    / \
#   b   c
#  /
# d
#
# The deepest node in this tree is d at depth 3.
#
# Here's a starting point:
#
# class Node(object):
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
#
#   def __repr__(self):
#     # string representation
#     return self.val
#
#
# def deepest(node):
#   # Fill this in.
#
# root = Node('a')
# root.left = Node('b')
# root.left.left = Node('d')
# root.right = Node('c')
#
# print deepest(root)
# # (d, 3)

import pytest

from common import build_binary_tree, compare_binary_trees, TreeNode


def deepest(node):
    if node:
        left = deepest(node.left)
        right = deepest(node.right)
        if left[0] and right[0]:
            max_node = max(left, right, key=lambda x: x[1])
            return (max_node[0], max_node[1] + 1)
        elif left[0]:
            return (left[0], left[1] + 1)
        elif right[0]:
            return (right[0], right[1] + 1)
        else:
            return (node.val, 1)
    else:
        return (None, 0)


@pytest.mark.parametrize("root, expected", [
    ([], (None, 0)),
    (["x"], ("x", 1)),
    (["a", "b", "c", None, None, None, "g"], ("g", 3)),
    (["a", "b", "c", "d"], ("d", 3)),
    (["a", "b", "c", "d", "e", "f"], ("d", 3)),
    (["a", "b", "c", "d", "e", "f", None, "h"], ("h", 4)),
])
def test_deepest(root, expected):
    actual = deepest(build_binary_tree(root))
    assert expected == actual
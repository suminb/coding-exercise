# [Daily Problem] Tree Serialization
#
# You are given the root of a binary tree. You need to implement 2 functions:
#
# 1. serialize(root) which serializes the tree into a string representation
# 2. deserialize(s) which deserializes the string back to the original tree that it represents
#
# For this problem, often you will be asked to design your own serialization format. However, for simplicity, let's use the pre-order traversal of the tree. Here's your starting point:
#
# class Node:
#   def __init__(self, val, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right
#
#   def __str__(self):
#     # pre-order printing of the tree.
#     result = ''
#     result += str(self.val)
#     if self.left:
#       result += str(self.left)
#     if self.right:
#       result += str(self.right)
#     return result
#
# def serialize(root):
#   # Fill this in.
#
# def deserialize(data):
#   # Fill this in.
#
# #     1
# #    / \
# #   3   4
# #  / \   \
# # 2   5   7
# tree = Node(1)
# tree.left = Node(3)
# tree.left.left = Node(2)
# tree.left.right = Node(5)
# tree.right = Node(4)
# tree.right.right = Node(7)
#
# print serialize(tree)
# # 1 3 2 # # 5 # # 4 # 7 # #
# print deserialize('1 3 2 # # 5 # # 4 # 7 # #')
# # 132547

import pytest

from common import build_binary_tree, compare_binary_trees, TreeNode, print_binary_tree


def serialize(root):
    def traverse(root):
        if root:
            return [str(root.val)] + traverse(root.left) + traverse(root.right)
        else:
            return ["#"]
    return " ".join(traverse(root))


def deserialize(values):
    def traverse(it):
        v = next(it)
        if v == "#":
            return None
        node = TreeNode(v)
        node.left = traverse(it)
        node.right = traverse(it)
        return node

    return traverse(iter(values.split()))


@pytest.mark.parametrize("values, expected", [
    ([1], "1 # #"),
    ([1, 2], "1 2 # # #"),
    ([1, None, 3], "1 # 3 # #"),
    ([1, 2, 3], "1 2 # # 3 # #"),
    ([1, 3, 4, 2, 5, None, 7], "1 3 2 # # 5 # # 4 # 7 # #"),
])
def test_serialize(values, expected):
    def stringify(v):
        """We convert node values into string for easier comparison after
        deserialization.
        """
        if v is None:
            return v
        else:
            return str(v)
    root = build_binary_tree([stringify(v) for v in values])

    actual = serialize(root)
    assert expected == actual

    actual = deserialize(serialize(root))
    assert compare_binary_trees(root, actual)


# @pytest.mark.parametrize("serialized, expected", [
#     ("1 # #", [1]),
# ])
# def test_deserialize(serialized, expected):
#     actual = deserialize(serialized)
#     assert compare_binary_trees(build_binary_tree(expected), actual)
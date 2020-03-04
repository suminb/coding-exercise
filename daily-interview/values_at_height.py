# Given a binary tree, return all values given a certain height h.
#
# Here's a starting point:
#
# class Node():
#   def __init__(self, value, left=None, right=None):
#     self.value = value
#     self.left = left
#     self.right = right
#
# def valuesAtHeight(root, height):
#   # Fill this in.
#
# #     1
# #    / \
# #   2   3
# #  / \   \
# # 4   5   7
#
# a = Node(1)
# a.left = Node(2)
# a.right = Node(3)
# a.left.left = Node(4)
# a.left.right = Node(5)
# a.right.right = Node(7)
# print valuesAtHeight(a, 3)
# # [4, 5, 7]

from collections import deque

import pytest

from common import build_binary_tree, TreeNode


def values_at_height(root, height):
    queue = deque()
    queue.append((root, 1))
    values = []

    while queue:
        node, level = queue.popleft()
        if node:
            if level == height:
                values.append(node.val)
            elif level < height:
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))

    return values


@pytest.mark.parametrize("node_values, height, expected", [
    ([1], 1, [1]),
    ([1, 2, 3, 4, 5, None, 7], 1, [1]),
    ([1, 2, 3, 4, 5, None, 7], 2, [2, 3]),
    ([1, 2, 3, 4, 5, None, 7], 3, [4, 5, 7]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4, [8, 9, 10]),
])
def test_values_at_height(node_values, height, expected):
    root = build_binary_tree(node_values)
    actual = values_at_height(root, height)
    assert expected == actual
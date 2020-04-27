# [Daily Problem] Binary Tree Level with Minimum Sum
#
# You are given the root of a binary tree. Find the level for the binary tree
# with the minimum sum, and return that value.
#
# For instance, in the example below, the sums of the trees are 10, 2 + 8 = 10,
# and 4 + 1 + 2 = 7. So, the answer here should be 7.
#
# class Node:
#   def __init__(self, value, left=None, right=None):
#     self.val = value
#     self.left = left
#     self.right = right
#
# def minimum_level_sum(root):
#   # Fill this in.
#
# #     10
# #    /  \
# #   2    8
# #  / \    \
# # 4   1    2
# node = Node(10)
# node.left = Node(2)
# node.right = Node(8)
# node.left.left = Node(4)
# node.left.right = Node(1)
# node.right.right = Node(2)
#
# print minimum_level_sum(node)

from collections import deque

import pytest

from common import build_binary_tree


def minimum_level_sum(root):
    queue = deque()
    queue.append((root, 0))
    sums = {}

    while queue:
        node, level = queue.popleft()
        if node:
            sums.setdefault(level, 0)
            sums[level] += node.val

            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

    return min(sums.values())


@pytest.mark.parametrize("values, expected", [
    ([1], 1),
    ([1, 2], 1),
    ([1, None, 3], 1),
    ([10, 2, 8, 4, 1, 2], 7),
    ([10, 9, 8, 7, 6, 5, 4], 10),
])
def test_minimum_level_sum(values, expected):
    actual = minimum_level_sum(build_binary_tree(values))
    assert expected == actual
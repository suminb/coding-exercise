# Hi, here's your problem today. This problem was recently asked by LinkedIn:
#
# Given a sorted list of numbers, change it into a balanced binary search tree.
# You can assume there will be no duplicate numbers in the list.
#
# Here's a starting point:
#
# from collections import deque
#
# class Node:
#   def __init__(self, value, left=None, right=None):
#     self.value = value
#     self.left = left
#     self.right = right
#
#   def __str__(self):
#     # level-by-level pretty-printer
#     nodes = deque([self])
#     answer = ''
#     while len(nodes):
#       node = nodes.popleft()
#       if not node:
#         continue
#       answer += str(node.value)
#       nodes.append(node.left)
#       nodes.append(node.right)
#     return answer
#
#
# def createBalancedBST(nums):
#   # Fill this in.
#
# print createBalancedBST([1, 2, 3, 4, 5, 6, 7])
# # 4261357
# #   4
# #  / \
# # 2   6
# #/ \ / \
# #1 3 5 7

import pytest

from common import build_binary_tree, compare_binary_trees, TreeNode


def create_balanced_bst(values, n=None):
    if values:
        if n is None:
            n = len(values)
        m = n // 2
        node = TreeNode(
            values[m],
            create_balanced_bst(values[:m], m),
            create_balanced_bst(values[m + 1:], n - m - 1))
        return node
    else:
        return None


@pytest.mark.parametrize("values, expected", [
    ([], []),
    ([1], [1]),
    ([1, 2], [2, 1]),
    ([1, 2, 3], [2, 1, 3]),
    ([1, 2, 3, 4], [3, 2, 4, 1]),
    ([1, 2, 3, 4, 5, 6, 7], [4, 2, 6, 1, 3, 5, 7]),
])
def test_create_balanced_bst(values, expected):
    actual = create_balanced_bst(values)
    assert compare_binary_trees(build_binary_tree(expected), actual)
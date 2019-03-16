# 107. Binary Tree Level Order Traversal II
# difficulty: easy

# The solution is almost identical to that of 102. Binary Tree Level Order
# Traversal, except the result array is in a reverse-order.

from collections import deque
from typing import List

from common import TreeNode


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        queue = deque([(root, 0)])

        while queue:
            node, depth = queue.popleft()

            if node:
                if depth == len(levels):
                    levels.append([])
                levels[depth].append(node.val)

                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))

        return levels[::-1]


def test(build_binary_tree):
    s = Solution()

    root = build_binary_tree([3, 9, 20, None, None, 15, 7])
    assert s.levelOrder(root) == [[15, 7], [9, 20], [3]]

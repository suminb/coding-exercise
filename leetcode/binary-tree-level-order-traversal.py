# 102. Binary Tree Level Order Traversal
# difficulty: medium

from collections import deque
from typing import List

from leetcode import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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

        return levels


def test(build_binary_tree):
    s = Solution()

    root = build_binary_tree([3, 9, 20, None, None, 15, 7])
    assert s.levelOrder(root) == [[3], [9, 20], [15, 7]]

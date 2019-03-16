# 102. Binary Tree Level Order Traversal
# difficulty: medium

from collections import deque
from typing import List

from common import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        bucket = {}
        queue = deque([(root, 0)])

        while queue:
            node, depth = queue.popleft()

            if node:
                bucket.setdefault(depth, [])
                bucket[depth].append(node.val)

                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))

        return list(bucket.values())


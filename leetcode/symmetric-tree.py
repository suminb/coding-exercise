# 101. Symmetric Tree
# difficulty: easy

from collections import deque

from common import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return is_symmetric(root)


def is_symmetric(root):
    prev_depth = -1
    queue = deque([(root, 0)])
    single_level = []
    while queue:
        node, depth = queue.popleft()

        print(depth, single_level)

        if depth != prev_depth:
            if not is_symmetric_list(single_level, prev_depth):
                return False
            single_level = []
            prev_depth = depth
        single_level.append(node.val if node else None)

        if node:
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

    if not is_symmetric_list(single_level, depth):
        return False

    return True


def is_symmetric_list(xs, depth):
    if depth < 0:
        return True

    # expected length = 2 ** depth
    n = 2 ** depth
    mid = n // 2
    return len(xs) == n and all([x == y for x, y in zip(xs[:mid], xs[n:mid:-1])])


def test_is_symmetric_list():
    assert is_symmetric_list([], -1)
    assert is_symmetric_list([1], 0)
    assert is_symmetric_list([1, 1], 1)
    assert is_symmetric_list([1, 2, 2, 1], 2)
    assert is_symmetric_list([1, None, None, 1], 2)

    assert not is_symmetric_list([1, 2, 1, 2], 2)


def test_is_symmetric(build_binary_tree):
    root = build_binary_tree([])
    assert is_symmetric(root)

    root = build_binary_tree([1])
    assert is_symmetric(root)

    root = build_binary_tree([1, 2, 2, 3, 4, 4, 3])
    assert is_symmetric(root)

    root = build_binary_tree([1, 2])
    assert not is_symmetric(root)

    root = build_binary_tree([1, 2, 3])
    assert not is_symmetric(root)

    root = build_binary_tree([1, 2, 2, None, 3, None, 3])
    assert not is_symmetric(root)

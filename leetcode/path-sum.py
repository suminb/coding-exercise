# 112. Path Sum
# difficulty: easy

from common import build_binary_tree, TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, sum_: int) -> bool:
        return has_path_sum(root, 0, sum_)


def has_path_sum(node, subtotal, target):
    if not node:
        return False
    elif is_leaf(node):
        return subtotal + node.val == target
    else:
        subtotal += node.val
        return has_path_sum(node.left, subtotal, target) or \
            has_path_sum(node.right, subtotal, target)


def is_leaf(node):
    return node and node.left is None and node.right is None


def test():
    s = Solution()
    root = build_binary_tree(
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])

    assert s.hasPathSum(root, 27)
    assert s.hasPathSum(root, 22)

    # NOTE: Looks like LeetCode builds trees differently
    # assert s.hasPathSum(root, 26)
    # assert s.hasPathSum(root, 18)

    assert not s.hasPathSum(root, 0)
    assert not s.hasPathSum(root, -1)
    assert not s.hasPathSum(root, 5)
    assert not s.hasPathSum(root, 6)

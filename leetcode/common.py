class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_binary_tree(xs):
    """Builds a binary tree from a list of elements."""
    def build(root, xs, i, n):
        if i < n and xs[i] is not None:
            root = TreeNode(xs[i])
            root.left = build(root.left, xs, i * 2 + 1, n)
            root.right = build(root.right, xs, i * 2 + 2, n)
        return root

    if not xs:
        return None
    else:
        return build(None, xs, 0, len(xs))


def print_binary_tree(node, depth=0):
    if node:
        print(' ' * (depth * 2) + str(node.val))
        print_binary_tree(node.left, depth + 1)
        print_binary_tree(node.right, depth + 1)

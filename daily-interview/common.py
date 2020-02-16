class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def build_list(elements):
    root = None
    if len(elements) > 0:
        root = ListNode(elements[0])
        prev = root
        for x in elements[1:]:
            node = ListNode(x)
            prev.next = node
            prev = node
    return root


def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()


def compare_lists(l1, l2):
    n1, n2 = l1, l2
    while n1 and n2:
        if n1.val != n2.val:
            return False
        n1 = n1.next
        n2 = n2.next
    return not (n1 or n2)


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


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


def compare_binary_trees(tree1, tree2):
    if tree1 and tree2:
        return (tree1.val == tree2.val) \
            and compare_binary_trees(tree1.left, tree2.left) \
            and compare_binary_trees(tree1.right, tree2.right)
    else:
        return tree1 is None and tree2 is None
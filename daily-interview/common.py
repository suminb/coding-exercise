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
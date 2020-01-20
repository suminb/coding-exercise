# Hi, here's your problem today. This problem was recently asked by Microsoft:
#
# You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# Here is the function signature as a starting point (in Python):
#
# # Definition for singly-linked list.
# class ListNode(object):
#   def __init__(self, x):
#     self.val = x
#     self.next = None
# 
# class Solution:
#   def addTwoNumbers(self, l1, l2, c = 0):
#     # Fill this in.
#
# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)
#
# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)
#
# result = Solution().addTwoNumbers(l1, l2)
# while result:
#   print result.val,
#   result = result.next
# # 7 0 8

import pytest


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2, c=0):
    node = ListNode(0)
    if l1 and l2:
        v = l1.val + l2.val + c
        n1, n2 = l1.next, l2.next
    elif l1:
        v = l1.val + c
        n1, n2 = l1.next, None
    elif l2:
        v = l2.val + c
        n1, n2 = None, l2.next
    elif c:
        v = c
        n1, n2 = None, None
    else:
        return None

    c = v // 10
    v = v % 10

    node.val = v
    node.next = add_two_numbers(n1, n2, c)
    return node


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


@pytest.mark.parametrize("l1, l2, expected", [
    ([], [], []),
    ([0], [0], [0]),
    ([1], [2], [3]),
    ([9], [8], [7, 1]),
    ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ([9, 9, 9, 9], [1], [0, 0, 0, 0, 1])
])
def test(l1, l2, expected):
    actual = add_two_numbers(build_list(l1), build_list(l2))
    assert compare_lists(build_list(expected), actual)
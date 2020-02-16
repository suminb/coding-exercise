# Reverse a Linked List

# Given a singly-linked list, reverse the list. This can be done iteratively or recursively. Can you get both solutions?

# Example:
# Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
# Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL
# class ListNode(object):
#   def __init__(self, x):
#     self.val = x
#     self.next = None
  
#   # Function to print the list
#   def printList(self):
#     node = self
#     output = '' 
#     while node != None:
#       output += str(node.val)
#       output += " "
#       node = node.next
#     print(output)

#   # Iterative Solution
#   def reverseIteratively(self, head):
#     # Implement this.

#   # Recursive Solution      
#   def reverseRecursively(self, head):
#     # Implement this.

# # Test Program
# # Initialize the test list: 
# testHead = ListNode(4)
# node1 = ListNode(3)
# testHead.next = node1
# node2 = ListNode(2)
# node1.next = node2
# node3 = ListNode(1)
# node2.next = node3
# testTail = ListNode(0)
# node3.next = testTail

# print("Initial list: ")
# testHead.printList()
# # 4 3 2 1 0
# testHead.reverseIteratively(testHead)
# #testHead.reverseRecursively(testHead)
# print("List after reversal: ")
# testTail.printList()
# # 0 1 2 3 4

import pytest

from common import build_list, compare_lists, ListNode


def reverse_recursively(head):
    if not (head and head.next):
        return head
    node = reverse_recursively(head.next)
    head.next.next = head
    head.next = None
    return node


def reverse_iteratively(head):
    node = head
    prev = None
    while node:
        next = node.next
        node.next = prev
        prev = node
        node = next
    return prev


@pytest.mark.parametrize("root, expected", [
    ([], []),
    ([0], [0]),
    ([1, 2, 3, 4], [4, 3, 2, 1]),
])
def test(root, expected):
    actual = reverse_iteratively(build_list(root))
    assert compare_lists(build_list(expected), actual)

    actual = reverse_recursively(build_list(root))
    assert compare_lists(build_list(expected), actual)
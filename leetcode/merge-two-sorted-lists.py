# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            node = ListNode(l1.val)
            node.next = self.mergeTwoLists(l1.next, l2)
        else:
            node = ListNode(l2.val)
            node.next = self.mergeTwoLists(l1, l2.next)

        return node


# https://leetcode.com/submissions/detail/203407798/

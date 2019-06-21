#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
# difficulty: hard
# https://leetcode.com/problems/reverse-nodes-in-k-group/
#

from leetcode import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        return reverse(head, k)


def reverse(head, k):
    prev = None
    curr = head
    next = None
    count = 0

    # If the number of nodes is not a multiple of k then left-out nodes in the
    # end should remain as it is.
    if not proceed(head, k):
        return head

    while curr is not None and count < k:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1

    if next is not None:
        head.next = reverse(next, k)

    return prev


def proceed(head, k):
    curr = head
    count = 0
    while curr is not None and count < k:
        curr = curr.next
        count += 1
    return count >= k

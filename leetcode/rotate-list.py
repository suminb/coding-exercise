# 61. Rotate List

from common import ListNode, TreeNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k <= 0:
            return head
        n = self.len(head)
        if n == 0:
            return head
        p = n - (k % n)

        node, prev = head, None
        new_head, new_tail = head, None
        while node and node.next:
            prev = node
            node = node.next
            p -= 1
            if p == 0:
                new_head = node
                new_tail = prev

        if new_tail:
            node.next = head
            new_tail.next = None

        return new_head

    def len(self, node):
        k = 0
        while node:
            node = node.next
            k += 1
        return k

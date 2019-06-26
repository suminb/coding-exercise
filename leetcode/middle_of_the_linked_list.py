# 876. Middle of the Linked List
# difficulty: easy
# https://leetcode.com/problems/middle-of-the-linked-list/

from leetcode import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        front = behind = head
        while front is not None and front.next is not None:
            behind = behind.next
            front = front.next.next
        return behind

# TODO: Write some test cases

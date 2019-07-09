# 328. Odd Even Linked List
# difficulty: medium
# https://leetcode.com/problems/odd-even-linked-list/

from leetcode import ListNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        return odd_even_list(head)


def odd_even_list(head):
    if not head or not head.next:
        return head

    even = even_prev = head
    odd = odd_start = head.next

    while even and odd:
        if even.next:
            even.next = even.next.next
            even_prev = even
            even = even.next
        if odd.next:
            odd.next = odd.next.next
            odd = odd.next
    if even:
        even.next = odd_start
    else:
        even_prev.next = odd_start
    return head

# TODO: Write some test cases

# 2. Add Two Numbers
# difficulty: medium
# https://leetcode.com/problems/add-two-numbers/
# https://leetcode.com/submissions/detail/202465277/

from leetcode import ListNode


class Solution:
    def addTwoNumbers(self, l1, l2, p=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None and p == 0:
            return None

        x = l1.val if l1 is not None else 0
        y = l2.val if l2 is not None else 0
        s = x + y + p

        if s >= 10:
            p = s // 10
            s = s % 10
        else:
            p = 0

        node = ListNode(s)
        if l1 is not None and l2 is not None:
            node.next = self.addTwoNumbers(l1.next, l2.next, p)
        elif l1 is not None:
            node.next = self.addTwoNumbers(l1.next, None, p)
        elif l2 is not None:
            node.next = self.addTwoNumbers(None, l2.next, p)

        return node

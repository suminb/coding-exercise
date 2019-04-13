// 19. Remove Nth Node From End of List
// difficulty: medium
// https://leetcode.com/problems/remove-nth-node-from-end-of-list/

package leetcode

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	newHead, m := remove(head, n)
	// FIXME: Perhaps we could do it without this kind of special case handling
	if n == m {
		return newHead.Next
	} else {
		return newHead
	}
}

func remove(node *ListNode, n int) (*ListNode, int) {
	if node != nil {
		_, m := remove(node.Next, n)
		if n == m {
			node.Next = node.Next.Next
		}
		return node, m + 1
	} else {
		return nil, 0
	}
}

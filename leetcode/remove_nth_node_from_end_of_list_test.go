// 19. Remove Nth Node From End of List
// difficulty: medium
// https://leetcode.com/problems/remove-nth-node-from-end-of-list/

package leetcode

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	return removeIteratively(head, n)
	// newHead, m := removeRecursively(head, n)
	// // FIXME: Perhaps we could do it without this kind of special case handling
	// if n == m {
	// 	return newHead.Next
	// } else {
	// 	return newHead
	// }
}

func removeRecursively(node *ListNode, n int) (*ListNode, int) {
	if node != nil {
		_, m := removeRecursively(node.Next, n)
		if n == m {
			node.Next = node.Next.Next
		}
		return node, m + 1
	} else {
		return nil, 0
	}
}

func removeIteratively(head *ListNode, n int) *ListNode {
	i := 0
	m := length(head)
	node := head
	var prevNode *ListNode
	for node != nil {
		if i == m-n {
			if prevNode != nil {
				prevNode.Next = node.Next
			} else {
				head = node.Next
			}
		}
		prevNode = node
		node = node.Next
		i++
	}
	return head
}

func length(node *ListNode) int {
	n := 0
	for node != nil {
		node = node.Next
		n++
	}
	return n
}

// TODO: Write some test cases

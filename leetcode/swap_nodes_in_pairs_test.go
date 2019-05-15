// 24. Swap Nodes in Pairs
// difficulty: medium
// https://leetcode.com/problems/swap-nodes-in-pairs/

package leetcode

import (
	"fmt"
	"testing"
)

func swapPairs(head *ListNode) *ListNode {
	return swapPairsRecursive(head)
}

func swapPairsRecursive(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	node := head.Next
	head.Next = swapPairsRecursive(head.Next.Next)
	node.Next = head
	return node
}

func swapPairsIterative(head *ListNode) *ListNode {
	var prev *ListNode
	var newHead *ListNode
	index := 0
	node := head
	buffer := make([]*ListNode, 2)
	for node != nil {
		if index == 2 {
			swapNodes(prev, buffer[0], buffer[1], node)
			if newHead == nil {
				newHead = buffer[1]
			}
			prev = buffer[0]
			index = 0
		}

		buffer[index] = node

		node = node.Next
		index++
	}
	if index == 2 {
		swapNodes(prev, buffer[0], buffer[1], node)
		if newHead == nil {
			newHead = buffer[1]
		}
	}
	if newHead == nil {
		newHead = head
	}
	return newHead
}

func swapNodes(prev *ListNode, first *ListNode, second *ListNode, next *ListNode) {
	if prev != nil {
		prev.Next = second
	}
	second.Next = first
	first.Next = next
}

func TestSwapPairs(t *testing.T) {
	params := []struct {
		listElements []int
		expected     []int
	}{
		{[]int{}, []int{}},
		{[]int{1}, []int{1}},
		{[]int{1, 2}, []int{2, 1}},
		{[]int{1, 2, 3, 4}, []int{2, 1, 4, 3}},
		{[]int{1, 2, 3, 4, 5}, []int{2, 1, 4, 3, 5}},
	}

	for _, param := range params {
		root := BuildLinkedList(param.listElements)
		actual := BuildIntArrayFromLinkedList(swapPairs(root))
		assertTrue(t, compareIntArrays(param.expected, actual), fmt.Sprintf("Case %v", param.listElements))
	}
}

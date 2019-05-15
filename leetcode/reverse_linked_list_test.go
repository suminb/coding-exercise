// This is not a LeetCode problem; I made this up
package leetcode

import (
	"fmt"
	"testing"
)

func reverseLinkedList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	node := reverseLinkedList(head.Next)
	head.Next.Next = head
	head.Next = nil
	return node
}

func TestReverseLinkedList(t *testing.T) {
	params := []struct {
		listElements []int
		expected     []int
	}{
		{[]int{}, []int{}},
		{[]int{1}, []int{1}},
		{[]int{1, 2}, []int{2, 1}},
		{[]int{1, 2, 3}, []int{3, 2, 1}},
		{[]int{1, 2, 3, 4}, []int{4, 3, 2, 1}},
		{[]int{1, 2, 3, 4, 5}, []int{5, 4, 3, 2, 1}},
	}

	for _, param := range params {
		root := BuildLinkedList(param.listElements)
		actual := BuildIntArrayFromLinkedList(reverseLinkedList(root))
		assertTrue(t, compareIntArrays(param.expected, actual), fmt.Sprintf("Case %v", param.listElements))
	}
}

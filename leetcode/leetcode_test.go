package leetcode

import "testing"

func TestBuildLinkedList(t *testing.T) {
	head := BuildLinkedList([]int{1, 2, 3, 4, 5})
	PrintLinkedList(head)
}

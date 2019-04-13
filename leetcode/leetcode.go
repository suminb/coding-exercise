package leetcode

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func BuildLinkedList(elements []int) *ListNode {
	if len(elements) == 0 {
		return nil
	} else {
		var head, prev *ListNode
		for _, value := range elements {
			node := ListNode{Val: value, Next: nil}
			if head == nil {
				head = &node
			}
			if prev != nil {
				prev.Next = &node
			}
			prev = &node
		}
		return head
	}
}

func PrintLinkedList(head *ListNode) {
	node := head
	for node != nil {
		fmt.Printf("%d ", node.Val)
		node = node.Next
	}
	fmt.Println()
}

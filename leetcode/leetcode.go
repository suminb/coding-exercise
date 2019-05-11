package leetcode

import (
	"fmt"
	"testing"
)

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

func assertEquals(t *testing.T, expected interface{}, actual interface{}, errorMessage string) bool {
	if expected != actual {
		t.Errorf("%s (expected=%s, actual=%s)\n", errorMessage, expected, actual)
		return false
	} else {
		return true
	}
}

func assertTrue(t *testing.T, evaluated bool, errorMessage string) bool {
	if !evaluated {
		t.Errorf("Expected false, but got true: %s\n", errorMessage)
		return false
	}
	return true
}

func assertFalse(t *testing.T, evaluated bool, errorMessage string) bool {
	if evaluated {
		t.Errorf("Expected true, but got false: %s\n", errorMessage)
		return false
	}
	return true
}

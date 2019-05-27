package leetcode

import (
	"fmt"
	"testing"
)

// ListNode represents a node of a singly linked list
type ListNode struct {
	Val  int
	Next *ListNode
}

func (node ListNode) String() string {
	return fmt.Sprintf("ListNode(%d)", node.Val)
}

// BuildLinkedList builds a linked list from an array list
func BuildLinkedList(elements []int) *ListNode {
	if len(elements) == 0 {
		return nil
	}
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

// BuildIntArrayFromLinkedList turns a linked list into an array of integers
func BuildIntArrayFromLinkedList(head *ListNode) []int {
	array := make([]int, 0)
	node := head
	for node != nil {
		array = append(array, node.Val)
		node = node.Next
	}
	return array
}

// PrintLinkedList is pretty much self-explanatory
func PrintLinkedList(head *ListNode) {
	node := head
	for node != nil {
		fmt.Printf("%d ", node.Val)
		node = node.Next
	}
	fmt.Println()
}

func max(x int, y int) int {
	if x > y {
		return x
	}
	return y
}

func min(x int, y int) int {
	if x < y {
		return x
	}
	return y
}

func compareIntArrays(xs []int, ys []int) bool {
	if len(xs) != len(ys) {
		return false
	}
	for i, x := range xs {
		if x != ys[i] {
			return false
		}
	}
	return true
}

func assertEquals(t *testing.T, expected interface{}, actual interface{}, errorMessage string) bool {
	if expected != actual {
		t.Errorf("%s (expected=%s, actual=%s)\n", errorMessage, expected, actual)
		return false
	}
	return true
}

func assertTrue(t *testing.T, evaluated bool, errorMessage string) bool {
	if !evaluated {
		t.Errorf("Expected true, but got false: %s\n", errorMessage)
		return false
	}
	return true
}

func assertFalse(t *testing.T, evaluated bool, errorMessage string) bool {
	if evaluated {
		t.Errorf("Expected false, but got true: %s\n", errorMessage)
		return false
	}
	return true
}

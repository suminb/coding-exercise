// This is not from Leetcode

package leetcode

import (
	"fmt"
	"testing"
)

func LengthOfConsecutiveZeros(xs []int) int {
	length, maxLength := 0, 0
	for _, x := range xs {
		if x == 0 {
			length++
		} else {
			maxLength = max(length, maxLength)
			length = 0
		}
	}
	return max(length, maxLength)
}

func TestLengthOfConsecutiveZeros(t *testing.T) {
	params := []struct {
		xs       []int
		expected int
	}{
		{[]int{}, 0},
		{[]int{0}, 1},
		{[]int{1}, 0},
		{[]int{0, 0, 0, 1, 1, 0}, 3},
	}

	for _, param := range params {
		actual := LengthOfConsecutiveZeros(param.xs)
		assertEquals(t, param.expected, actual, fmt.Sprintf("Case xs = %v", param.xs))
	}
}

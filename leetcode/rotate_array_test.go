// 189. Rotate Array
// difficulty: easy
// https://leetcode.com/problems/rotate-array/

package leetcode

import (
	"fmt"
	"testing"
)

func rotate(nums []int, k int) {
	n := len(nums)

	// O(n) space complexity
	// Could we do it with O(1) space?
	res := make([]int, n)

	for i := 0; i < n; i++ {
		j := (i + k) % n
		res[j] = nums[i]
	}
	for i := 0; i < n; i++ {
		nums[i] = res[i]
	}
}

func TestRotateArray(t *testing.T) {
	nums := []int{1, 2, 3, 4, 5, 6, 7}
	rotate(nums, 3)
	fmt.Println(nums)
	// TODO: Write some test cases
}

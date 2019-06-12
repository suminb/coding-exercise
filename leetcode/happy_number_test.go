// 202. Happy Number
// difficulty: easy
// https://leetcode.com/problems/happy-number/

package leetcode

import (
	"testing"
)

func isHappy(n int) bool {
	seen := make(map[int]bool)
	seen[n] = true

	for n != 1 {
		digits := getDigits(n)
		n = sumOfSquareOfDigits(digits)
		if _, ok := seen[n]; ok {
			return false
		}
		seen[n] = true
	}
	return true
}

func getDigits(n int) []int {
	digits := []int{}
	for n > 0 {
		digit := n % 10
		digits = append(digits, digit)
		n = n / 10
	}
	return digits
}

func sumOfSquareOfDigits(digits []int) int {
	sum := 0
	for _, d := range digits {
		sum += d * d
	}
	return sum
}

func TestIsHappyNumber(t *testing.T) {
	params := []TestParam{
		{1, true},
		{2, false},
		{19, true},
		{999, false},
		{235234, false},
		// TODO: More test cases
	}

	f, _ := isHappy.(func(interface{}) interface{})
	(*Testing)(t).RunTestsWithParams(params, f)

	// for _, param := range params {
	// 	actual := isHappy(param.n)
	// 	assertEquals(t, param.expected, actual, "")
	// }
}

package leetcode

import "testing"

func TestSqrtx(t *testing.T) {
	params := []struct {
		input, expected int
	}{
		{0, 0}, {1, 1}, {2, 1}, {3, 1}, {4, 2}, {5, 2}, {8, 2}, {9, 3},
		{19, 4}, {1000, 31}, {1234, 35}, {12345, 111}, {777777, 881},
	}

	for _, param := range params {
		actual := mySqrt(param.input)
		assertEquals(t, param.expected, actual, "Incorrect value")
	}
}

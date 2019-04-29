// 54. Spiral Matrix
package leetcode

import (
	"fmt"
	"reflect"
	"testing"
)

const RIGHT = 0
const DOWN = 1
const LEFT = 2
const UP = 3

func spiralOrder(matrix [][]int) []int {
	orientation := RIGHT
	n := len(matrix)
	if n == 0 {
		return []int{}
	}
	m := len(matrix[0])
	i, j := 0, -1
	k, flatten := 0, make([]int, n*m)
	count := n * m

	n--
	p, q := n, m

	for k < count {
		if orientation%4 == RIGHT {
			j++
			q--
		} else if orientation%4 == DOWN {
			i++
			p--
		} else if orientation%4 == LEFT {
			j--
			q--
		} else {
			i--
			p--
		}

		if orientation%2 == 0 && q == 0 {
			// RIGHT or LEFT
			m--
			q = m
			orientation++
		} else if orientation%2 == 1 && p == 0 {
			// DOWN or UP
			n--
			p = n
			orientation++
		}

		flatten[k] = matrix[i][j]
		k++
	}

	return flatten
}

func TestSpiralOrder0(t *testing.T) {
	matrix := [][]int{}
	actual := spiralOrder(matrix)
	expected := []int{}
	assertTrue(t, reflect.DeepEqual(actual, expected),
		fmt.Sprintf("expected = %v, actual = %v", expected, actual))
}

func TestSpiralOrder1(t *testing.T) {
	matrix := [][]int{
		{1},
	}
	actual := spiralOrder(matrix)
	expected := []int{1}
	assertTrue(t, reflect.DeepEqual(actual, expected),
		fmt.Sprintf("expected = %v, actual = %v", expected, actual))
}

func TestSpiralOrder2(t *testing.T) {
	matrix := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}
	actual := spiralOrder(matrix)
	expected := []int{1, 2, 3, 6, 9, 8, 7, 4, 5}
	assertTrue(t, reflect.DeepEqual(actual, expected),
		fmt.Sprintf("expected = %v, actual = %v", expected, actual))
}

func TestSpiralOrder3(t *testing.T) {
	matrix := [][]int{
		{1, 2, 3, 4},
		{5, 6, 7, 8},
		{9, 10, 11, 12},
	}
	actual := spiralOrder(matrix)
	expected := []int{1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7}
	assertTrue(t, reflect.DeepEqual(actual, expected),
		fmt.Sprintf("expected = %v, actual = %v", expected, actual))
}

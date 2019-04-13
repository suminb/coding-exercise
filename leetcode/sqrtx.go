// 69. Sqrt(x)
// difficulty: easy
// https://leetcode.com/problems/sqrtx/

package leetcode

func mySqrt(x int) int {
	return binarySearchSqrt(x)
	// return bruteForceSqrt(x)
}

func binarySearchSqrt(x int) int {
	left, right, v := 1, x, x/2

	if x == 0 {
		return 0
	}

	for v >= 1 {
		if v*v > x {
			right = v
			v /= 2
		} else if v*v < x {
			left = max(v, left)
			v = (left + right) / 2
			if left == v {
				return left
			}
		} else {
			return v
		}
	}
	return left
}

func max(x int, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}

func bruteForceSqrt(x int) int {
	v := 0
	for v*v <= x {
		v++
	}
	return v - 1
}

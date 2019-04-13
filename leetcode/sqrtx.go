// 69. Sqrt(x)
// difficulty: easy
// https://leetcode.com/problems/sqrtx/

package leetcode

func mySqrt(x int) int {
	return bruteForce(x)
}

func bruteForce(x int) int {
	v := 0
	for v*v <= x {
		v++
	}
	return v - 1
}

// 5. Longest Palindromic Substring
// difficulty: medium
// https://leetcode.com/problems/longest-palindromic-substring/

package leetcode

import (
	"fmt"
	"testing"
)

func longestPalindrome(s string) string {
	n := len(s)
	if n == 0 {
		return s
	}
	m := 0       // max length so far
	x, y := 0, 0 // index of max length

	dp := make([][]bool, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]bool, n)
		dp[i][i] = true

		if i+1 < n && s[i] == s[i+1] {
			dp[i][i+1] = true
			m = 2
			x, y = i, i+1
		}
	}
	for i := n - 1; i >= 0; i-- {
		for j := i + 1; j < n; j++ {
			if s[i] == s[j] && dp[i+1][j-1] {
				dp[i][j] = true
				if j-i+1 >= m {
					m = j - i + 1
					x, y = i, j
				}
			}
		}
	}
	return s[x : y+1]
}

func TestLongestPalindrom(t *testing.T) {
	params := []struct {
		input    string
		expected string
	}{
		{"", ""},
		{"x", "x"},
		{"xx", "xx"},
		{"xxx", "xxx"},
		{"xxxx", "xxxx"},
		{"abcdcb", "bcdcb"},
		{"babad", "bab"},
		{"cbbd", "bb"},
		{"abcdcbaabcdc", "cdcbaabcdc"},
		{"abcba01210", "abcba"},
		{"::0x123456789876543210", "12345678987654321"},
	}
	for _, param := range params {
		actual := longestPalindrome(param.input)
		assertEquals(t, param.expected, actual, fmt.Sprintf("Case (%s)", param.input))
	}
}

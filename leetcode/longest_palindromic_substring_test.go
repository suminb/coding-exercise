// 5. Longest Palindromic Substring
// difficulty: medium
// https://leetcode.com/problems/longest-palindromic-substring/

package leetcode

import "testing"

func longestPalindrome(s string) string {
	n := len(s)
	if n <= 1 {
		return s
	}
	t, i, j := longestPalindromeAux(s, 0, n-1)
	if t {
		return s[i : j+1]
	}
	return ""
}

func longestPalindromeAux(s string, i int, j int) (bool, int, int) {
	if i > j {
		return false, i, i
	} else if i == j {
		return true, i, i
	}

	if s[i] == s[j] {
		if j-i == 1 {
			return true, i, j
		}
		t, _, _ := longestPalindromeAux(s, i+1, j-1)
		if t {
			return true, i, j
		}
	}

	t1, p1, q1 := longestPalindromeAux(s, i+1, j)
	t2, p2, q2 := longestPalindromeAux(s, i, j-1)

	if t1 && t2 {
		if q1-p1 > q2-p2 {
			return t1, p1, q1
		}
	} else if t1 {
		return t1, p1, q1
	}
	return t2, p2, q2
}

func TestLongestPalindrome(t *testing.T) {
	params := []struct {
		value    string
		expected string
	}{
		{"", ""},
		{"x", "x"},
		{"xx", "xx"},
		{"babad", "bab"},
		{"caba", "aba"},
		{"abacdfgdcaba", "aba"},
		{"asdf", "f"},
	}
	for _, param := range params {
		actual := longestPalindrome(param.value)
		assertEquals(t, param.expected, actual, "Invalid result")
	}
}

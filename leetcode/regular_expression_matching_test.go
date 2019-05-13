// 10. Regular Expression Matching
// difficulty: hard
// https://leetcode.com/problems/regular-expression-matching/

package leetcode

import (
	"fmt"
	"testing"
)

func isMatch(s string, p string) bool {
	return isMatchImpl(s, 0, len(s), p, 0, len(p))
}

func isMatchImpl(s string, i int, m int, p string, j int, n int) bool {
	slen, plen := m-i, n-j
	if plen == 0 {
		return slen == 0
	}

	firstMatch := slen > 0 && (p[j] == s[i] || p[j] == '.')

	// Cases
	// 1. single exact matching
	// 2. single wildcard matching
	// 3. exact star matching
	// 4. wildcard star matching
	if plen >= 2 && p[j+1] == '*' {
		return isMatchImpl(s, i, m, p, j+2, n) ||
			(firstMatch && isMatchImpl(s, i+1, m, p, j, n))
	}
	return firstMatch && isMatchImpl(s, i+1, m, p, j+1, n)
}

func TestIsMatch(t *testing.T) {
	params := []struct {
		str      string
		pattern  string
		expected bool
	}{
		{"", "", true},
		{"aa", "aa", true},
		{"aa", "a", false},
		{"aa", "a*", true},
		{"aa", ".*", true},
		{"ab", ".*", true},
		{"aab", "c*a*b", true},
		{"mississippi", "mis*is*p*.", false},
	}

	for _, param := range params {
		actual := isMatch(param.str, param.pattern)
		assertEquals(t, param.expected, actual, fmt.Sprintf("Case (%s, %s)", param.str, param.pattern))
	}
}

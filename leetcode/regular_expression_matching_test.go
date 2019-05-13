// 10. Regular Expression Matching
// difficulty: hard
// https://leetcode.com/problems/regular-expression-matching/

package leetcode

import (
	"fmt"
	"testing"
)

func isMatchRegex(s string, p string) bool {
	return isMatchRegexImpl(s, 0, len(s), p, 0, len(p))
}

func isMatchRegexImpl(s string, i int, m int, p string, j int, n int) bool {
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
		return isMatchRegexImpl(s, i, m, p, j+2, n) ||
			(firstMatch && isMatchRegexImpl(s, i+1, m, p, j, n))
	}
	return firstMatch && isMatchRegexImpl(s, i+1, m, p, j+1, n)
}

func TestIsMatchRegex(t *testing.T) {
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
		actual := isMatchRegex(param.str, param.pattern)
		assertEquals(t, param.expected, actual, fmt.Sprintf("Case (%s, %s)", param.str, param.pattern))
	}
}

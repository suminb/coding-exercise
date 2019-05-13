// 44. Wildcard Matching
// difficulty: hard
// https://leetcode.com/problems/wildcard-matching/

package leetcode

import (
	"fmt"
	"testing"
)

func isMatchWildcard(s string, p string) bool {
	return isMatchWildcardImpl(s, 0, len(s), p, 0, len(p))
}

func isMatchWildcardImpl(s string, i int, m int, p string, j int, n int) bool {
	slen, plen := m-i, n-j
	if plen == 0 {
		return slen == 0
	}

	if p[j] == '*' {
		if plen == 1 {
			return true
		}
		return (p[j+1] == '*' && isMatchWildcardImpl(s, i, m, p, j+1, n)) ||
			(slen >= 1 && p[j+1] == s[i] && isMatchWildcardImpl(s, i+1, m, p, j+2, n)) ||
			(slen >= 1 && isMatchWildcardImpl(s, i+1, m, p, j, n)) ||
			isMatchWildcardImpl(s, i, m, p, j+1, n)
	}
	return slen >= 1 && (p[j] == s[i] || p[j] == '?') && isMatchWildcardImpl(s, i+1, m, p, j+1, n)
}

func TestIsMatchWildcard(t *testing.T) {
	params := []struct {
		str      string
		pattern  string
		expected bool
	}{
		{"", "", true},
		{"", "*", true},
		{"", "?", false},
		{"aa", "aa", true},
		{"aa", "a", false},
		{"aa", "*", true},
		{"cb", "?a", false},
		{"adceb", "*a*b", true},
		{"acccb", "a*c?b", true},
		{"acdcb", "a*c?b", false},
		{"aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba", "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*", true},
		// {"aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b", true},
	}

	for _, param := range params {
		actual := isMatchWildcard(param.str, param.pattern)
		assertEquals(t, param.expected, actual, fmt.Sprintf("Case (%s, %s)", param.str, param.pattern))
	}
}

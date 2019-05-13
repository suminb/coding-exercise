// 44. Wildcard Matching
// difficulty: hard
// https://leetcode.com/problems/wildcard-matching/

package leetcode

import (
	"fmt"
	"testing"
)

func isMatchWildcard(s string, p string) bool {
	return isMatchWildcardLinear(s, 0, len(s), p, 0, len(p))
}

func isMatchWildcardLinear(s string, i int, m int, p string, j int, n int) bool {
	iMark, jMark := 0, -1
	for i < m {
		if j < n && (p[j] == '?' || p[j] == s[i]) {
			i++
			j++
		} else if j < n && p[j] == '*' {
			iMark = i
			jMark = j
			j++
		} else if jMark != -1 {
			j = jMark + 1
			iMark++
			i = iMark
		} else {
			return false
		}
	}
	for j < n && p[j] == '*' {
		j++
	}
	return j == n
}

type Pair struct {
	x int
	y int
}

// This works, but way too slow
func isMatchWildcardDFS(s string, i int, m int, p string, j int, n int) bool {
	slen, plen := m-i, n-j
	if plen == 0 {
		return slen == 0
	}

	if p[j] == '*' {
		if plen == 1 {
			return true
		}
		return (p[j+1] == '*' && isMatchWildcardDFS(s, i, m, p, j+1, n)) ||
			(slen >= 1 && p[j+1] == s[i] && isMatchWildcardDFS(s, i+1, m, p, j+2, n)) ||
			(slen >= 1 && isMatchWildcardDFS(s, i+1, m, p, j, n)) ||
			isMatchWildcardDFS(s, i, m, p, j+1, n)
	}
	return slen >= 1 && (p[j] == s[i] || p[j] == '?') && isMatchWildcardDFS(s, i+1, m, p, j+1, n)
}

func isMatchWildcardDP(s string, i int, m int, p string, j int, n int, cache map[Pair]bool) bool {
	if value, ok := cache[Pair{i, j}]; ok {
		return value
	}

	slen, plen := m-i, n-j
	res := false
	if plen == 0 {
		res = slen == 0
	} else if p[j] == '*' {
		if plen == 1 {
			res = true
		} else {
			res = (p[j+1] == '*' && isMatchWildcardDP(s, i, m, p, j+1, n, cache)) ||
				(slen >= 1 && p[j+1] == s[i] && isMatchWildcardDP(s, i+1, m, p, j+2, n, cache)) ||
				(slen >= 1 && isMatchWildcardDP(s, i+1, m, p, j, n, cache)) ||
				isMatchWildcardDP(s, i, m, p, j+1, n, cache)
		}
	} else {
		res = slen >= 1 && (p[j] == s[i] || p[j] == '?') && isMatchWildcardDP(s, i+1, m, p, j+1, n, cache)
	}

	cache[Pair{i, j}] = res
	return res
}

var params = []struct {
	str      string
	pattern  string
	expected bool
}{
	{"", "", true},
	{"", "*", true},
	{"", "**", true},
	{"", "?", false},
	{"aa", "aa", true},
	{"aa", "a", false},
	{"aa", "*", true},
	{"cb", "?a", false},
	{"adceb", "*a*b", true},
	{"acccb", "a*c?b", true},
	{"acccccb", "a*c?b", true},
	{"acccb", "a***c?b", true},
	{"acdcb", "a*c?b", false},
	{"aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba", "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*", true},
	{"aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b", false},
}

func TestIsMatchWildcardLinear(t *testing.T) {
	for _, param := range params {
		s, p := param.str, param.pattern
		actual := isMatchWildcardLinear(s, 0, len(s), p, 0, len(p))
		assertEquals(t, param.expected, actual, fmt.Sprintf("Case (%s, %s)", param.str, param.pattern))
	}
}

func TestIsMatchWildcardDP(t *testing.T) {
	for _, param := range params {
		cache := make(map[Pair]bool)
		s, p := param.str, param.pattern
		actual := isMatchWildcardDP(s, 0, len(s), p, 0, len(p), cache)
		assertEquals(t, param.expected, actual, fmt.Sprintf("Case (%s, %s)", param.str, param.pattern))
	}
}

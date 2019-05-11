// 79. Word Search
// difficulty: medium
// https://leetcode.com/problems/word-search/

package leetcode

import (
	"testing"
)

func exist(board [][]byte, word string) bool {
	m, n := len(board), 0
	if m > 0 {
		n = len(board[0])
	} else {
		return false
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if existsAt(board, word, i, j, m, n, 0) {
				return true
			}
		}
	}

	return false
}

func existsAt(board [][]byte, word string, i int, j int, m int, n int, k int) bool {
	if i < 0 || i >= m || j < 0 || j >= n {
		return false
	}
	char := board[i][j]
	if char == 0 {
		return false
	}
	wordLen := len(word)
	if k >= wordLen {
		return false
	}

	if char == word[k] {
		if k+1 == wordLen {
			return true
		}
		board[i][j] = 0
		params := []struct {
			i int
			j int
		}{
			{i, j + 1}, // right
			{i + 1, j}, // down
			{i, j - 1}, // left
			{i - 1, j}, // up
		}
		for _, param := range params {
			if existsAt(board, word, param.i, param.j, m, n, k+1) {
				board[i][j] = char
				return true
			}
		}
		board[i][j] = char
	}
	return false
}

func TestExist(t *testing.T) {
	board := [][]byte{
		[]byte{'A', 'B', 'C', 'E'},
		[]byte{'S', 'F', 'C', 'S'},
		[]byte{'A', 'D', 'E', 'E'},
	}
	assertTrue(t, exist(board, "ABCCED"), "Case = ABCCED")
	assertTrue(t, exist(board, "SEE"), "Case = SEE")
	assertFalse(t, exist(board, "ABCB"), "Case = ABCB")
}

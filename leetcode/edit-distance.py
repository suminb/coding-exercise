# 72. Edit Distance
# difficulty: hard
# https://leetcode.com/problems/edit-distance/

import pytest

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

        return dp[m][n]


@pytest.mark.parametrize('word1, word2, expected', [
    ('', '', 0),
    ('foo', '', 3),
    ('', 'bar', 3),
    ('git', 'hits', 2),
    ('saturday', 'sunday', 3),
])
def test_edit_distance(word1, word2, expected):
    s = Solution()
    actual = s.minDistance(word1, word2)
    assert expected == actual


if __name__ == '__main__':
    pytest.main(['-v', __file__])
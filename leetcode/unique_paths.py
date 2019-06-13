# 62. Unique Paths
# difficulty: medium
# https://leetcode.com/problems/unique-paths/

import pytest


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """The basic idea is that the number of paths to a particular point
        is the sum of the number of paths to the previous paths (left and
        up).
        """
        if m * n == 0:
            return 0
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]


@pytest.mark.parametrize('m, n, expected', [
    (1, 1, 1),
    # (2, 1, 2),
    # (1, 3, 3),
    # (3, 2, 6),
    (5, 3, 15),
    (7, 5, 210),
])
def test_unique_paths(m, n, expected):
    s = Solution()
    actual = s.uniquePaths(m, n)
    assert expected == actual


if __name__ == '__main__':
    pytest.main(['-v', __file__])
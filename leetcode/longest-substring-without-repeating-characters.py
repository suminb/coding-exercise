class Solution:
    def lengthOfLongestSubstring(self, xs: str) -> int:
        i, n = 0, len(xs)
        max_len = 0

        while i < n:
            max_len = max(max_len, self.longest_substr(xs[i:]))
            i += 1

        return max_len

    def longest_substr(self, xs):
        i, n, s = 0, len(xs), set()
        max_len = 0

        while i < n:
            s.add(xs[i])

            if len(s) != n - i:
                return max_len
            else:
                max_len = n - i

        return max_len

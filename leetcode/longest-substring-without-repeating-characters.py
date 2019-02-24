class Solution:
    def lengthOfLongestSubstring(self, xs: str) -> int:
        i, j, n, s = 0, 0, len(xs), set()
        max_len = 0

        while i < n and j < n:
            if xs[j] in s:
                s.remove(xs[i])
                i += 1
            else:
                s.add(xs[j])
                max_len = max(max_len, len(s))
                j += 1

        return max_len

class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0

        for i, x in enumerate(haystack):
            if n - i < m:
                return -1
            if x == needle[0]:
                if self.matches(haystack[i:], needle):
                    return i

        return -1

    def matches(self, xs, ys):
        for x, y in zip(xs, ys):
            if x != y:
                return False
        return True

# 97. Interleaving String
# difficulty: hard

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        i = j = 0
        n1, n2, n3 = [len(x) for x in (s1, s2, s3)]
        leftover = []
        while i < n1 and j < n3:
            if s1[i] == s3[j]:
                i += 1
                j += 1
            else:
                leftover.append(s3[j])
                j += 1
        leftover.extend(s3[j:])
        return leftover == s2

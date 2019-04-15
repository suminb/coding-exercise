from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True) # sort in-place
        # i = 0, n = len(candidates)

        while candidates[i] > target and i < n:
            i += 1

        if i >= n:
            return [[]]
        else:
            pass
            # return [candidates[i]] + ?


class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        res = [[]]
        for x in nums:
            res.extend([y + [x] for y in res])
        return res

print(Solution().subsets([1, 2, 3]))

# https://leetcode.com/submissions/detail/209573065/
# https://leetcode.com/submissions/detail/209571184/
# Took me more than an hour for some reason. (72min)

# class Solution:
#     def maxArea(self, height: 'List[int]') -> 'int':
#         max_area = 0
#         for i, h1 in enumerate(height):
#             for j, h2 in enumerate(height[i + 1:], i + 1):
#                 area = (j - i) * min(h1, h2)
#                 max_area = max(area, max_area)
#
#         return max_area

#
# Brute force solution timed out:
# https://leetcode.com/submissions/detail/209829829/
#

class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        max_area = 0
        i, j = 0, len(height) - 1
        while i < j:
            h1, h2 = height[i], height[j]
            area = (j - i) * min(h1, h2)
            max_area = max(max_area, area)

            if h1 < h2:
                i += 1
            else:
                j -= 1

        return max_area

# https://leetcode.com/submissions/detail/209834037/


# class Solution:
#     def maxArea(self, height: 'List[int]') -> 'int':
#         max_area = 0
#         i, j = 0, len(height) - 1
#         while i < j:
#             h1, h2 = height[i], height[j]
#             area = (j - i) * (h1 if h1 < h2 else h2)
#             if area > max_area:
#                 max_area = area

#             if h1 < h2:
#                 i += 1
#             else:
#                 j -= 1

#         return max_area

# NOTE: It is somewhat faster without using min() and max() built-in functions
# https://leetcode.com/submissions/detail/209836084/


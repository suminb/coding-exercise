# 56. Merge Intervals

from operator import attrgetter
from typing import List


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=attrgetter('start'))
        merged = [intervals[0]]
        for i2 in intervals[1:]:
            i1 = merged.pop()
            merged.extend(self.merge_two(i1, i2))
        return merged

    def merge_two(self, i1, i2):
        start, end = min(i1.start, i2.start), max(i1.end, i2.end)
        span = end - start
        span1, span2 = i1.end - i1.start, i2.end - i2.start

        if span > span1 + span2:
            return [i1, i2]
        else:
            return [Interval(start, end)]

#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
# difficulty: hard
# https://leetcode.com/problems/insert-interval
#

from typing import List

import pytest

LOWER = 0
UPPER = 1


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        return insert(intervals, newInterval)


def insert(intervals, new_interval):
    res = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][UPPER] < new_interval[LOWER]:
        res.append(intervals[i])
        i += 1

    while i < n and intervals[i][LOWER] <= new_interval[UPPER]:
        new_interval = merge(new_interval, intervals[i])
        i += 1
    res.append(new_interval)

    while i < n:
        res.append(intervals[i])
        i += 1

    return res


def merge(interval1, interval2):
    lower = min(interval1[LOWER], interval2[LOWER])
    upper = max(interval1[UPPER], interval2[UPPER])
    return (lower, upper)


@pytest.mark.parametrize('interval1, interval2, expected', [
    ((1, 2), (2, 3), (1, 3)),
    ((1, 3), (2, 5), (1, 5)),
])
def test_merge_intervals(interval1, interval2, expected):
    actual = merge(interval1, interval2)
    assert expected == actual


@pytest.mark.parametrize('intervals, new_interval, expected', [
    ([], (1, 2), [(1, 2)]),
    ([(1, 5)], (6, 8), [(1, 5), (6, 8)]),
    ([(1, 3), (6, 9)], (2, 5), [(1, 5), (6, 9)]),
    ([(1, 2), (3, 5), (6, 7), (8, 10), (12, 16)], (4, 8), [(1, 2), (3, 10), (12, 16)]),
])
def test_insert_interval(intervals, new_interval, expected):
    actual = insert(intervals, new_interval)
    assert expected == actual


if __name__ == '__main__':
    pytest.main([__file__])
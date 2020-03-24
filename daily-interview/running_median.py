# [Daily Problem] Running Median
#
# You are given a stream of numbers. Compute the median for each new element .
#
# Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]
#
# Here's a starting point:
#
# def running_median(stream):
#   # Fill this in.
#
# running_median([2, 1, 4, 7, 2, 0, 5])
# # 2 1.5 2 3.0 2 2.0 2

from heapq import heappop, heappush

import pytest


def running_mediam(stream):
    minheap, maxheap = [], []
    medians = []
    median = None

    for x in stream:
        if median is not None and x < median:
            heappush(minheap, -x)
        else:
            heappush(maxheap, x)

        rebalance(minheap, maxheap)

        median = get_median(minheap, maxheap)
        medians.append(median)

    return medians


def rebalance(minheap, maxheap):
    m, n = len(minheap), len(maxheap)
    if n > m + 1:
        p = heappop(maxheap)
        heappush(minheap, -p)
    elif m > n:
        p = heappop(minheap)
        heappush(maxheap, -p)


def get_median(minheap, maxheap):
    if len(maxheap) > len(minheap):
        return maxheap[0]
    else:
        p, q = maxheap[0], -minheap[0]
        return (p + q) / 2


@pytest.mark.parametrize("stream, expected", [
    ([], []),
    ([1], [1]),
    ([1, 2, 3], [1, 1.5, 2]),
    ([2, 1, 4, 7, 2, 0, 5], [2, 1.5, 2, 3.0, 2, 2.0, 2]),
])
def test_running_median(stream, expected):
    actual = running_mediam(stream)
    assert expected == actual
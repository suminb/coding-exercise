# [Daily Problem] Nth Fibonacci Number
#
# The Fibonacci sequence is the integer sequence defined by the recurrence
# relation: F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1. In other
# words, the nth Fibonacci number is the sum of the prior two Fibonacci
# numbers. Below are the first few values of the sequence:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
#
# Given a number n, print the n-th Fibonacci Number.
# Examples:
# Input: n = 3
# Output: 2
#
# Input: n = 7
# Output: 13
# Here's a starting point:
#
# class Solution():
#   def fibonacci(self, n):
#     # fill this in.
#
# n = 9
# print(Solution().fibonacci(n))
# # 34

import pytest


def fibonacci_recursive(n):
    cache = {
        0: 0,
        1: 1,
        2: 1,
    }
    def fibonacci(n):
        if n in cache:
            return cache[n]
        elif n < 2:
            return n
        else:
            p, q = fibonacci(n - 1), fibonacci(n - 2)
            cache[n] = p + q
            return p + q
    return fibonacci(n)


def fibonacci_iterative(n):
    if n < 0:
        raise ValueError
    elif n < 2:
        return n
    else:
        res, prev1, prev2, i = 1, 1, 1, 2
        while i < n:
            res = prev2 + prev1
            i += 1
            prev1 = prev2
            prev2 = res
        return res


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (30, 832040),
    (100, 354224848179261915075),
])
def test_fibonacci(n, expected):
    actual = fibonacci_recursive(n)
    assert expected == actual

    actual = fibonacci_iterative(n)
    assert expected == actual
# Former Coding Interview Question: Flatten an iterator of iterators (interleaved iteration)
# https://techdevguide.withgoogle.com/resources/former-coding-interview-question-flatten-an-iterator-of-iterators/?types=coding-interview-question#!

import pytest


class InterleavingFlattener:

    def __init__(self, itoit):
        """
        :param itoit: Iterator of iterator
        """
        self.itoit = itoit
        self.curr_iter = self._next_iterator(itoit)

    def _next_iterator(self, itoit):
        try:
            return next(itoit)
        except StopIteration:
            return None

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_iter is None:
            raise StopIteration

        try:
            return next(self.curr_iter)
        except StopIteration:
            self.curr_iter = self._next_iterator(self.itoit)
            return self.__next__()


def test_itoit_0():
    it = iter([])
    flattener = InterleavingFlattener(it)
    assert list(flattener) == []


def test_itoit_1():
    it = iter([
        iter([1, 2, 3]),
        iter([4, 5]),
        iter([6, 7, 8, 9]),
    ])

    flattener = InterleavingFlattener(it)
    assert list(flattener) == list(range(1, 10))


if __name__ == '__main__':
    pytest.main(['-v', __file__])
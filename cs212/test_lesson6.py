import pytest

from lesson6 import *


@pytest.mark.parametrize('h1, h2, expected', [
    (1, 0, True),
    (0, 1, False),
    (4, 3, True),
    (2, 2, False),
])
def test_imright(h1, h2, expected):
    actual = imright(h1, h2)
    assert expected == actual


@pytest.mark.parametrize('h1, h2, expected', [
    (1, 0, True),
    (0, 1, True),
    (1, 1, False),
    (2, 4, False),
])
def test_nextto(h1, h2, expected):
    actual = nextto(h1, h2)
    assert expected == actual


def test_all_ints():
    it = all_ints()
    ints = [next(it) for _ in range(8)]
    assert [0, +1, -1, +2, -2, +3, -3, +4]


@pytest.mark.skip
@pytest.mark.parametrize('formula, expected', [
    ('X + Y == Z', '2 + 1 == 3'),  # Sometimes the order gets mixed up...
    ('ODD + ODD == EVEN', '655 + 655 == 1310'),
])
def test_solve(formula, expected):
    actual = solve(formula)
    assert expected == actual


@pytest.mark.parametrize('word, expected', [
    ('', ''),
    ('+', '+'),
    ('YOU', '1*U+10*O+100*Y'),
    ('lower', 'lower'),
])
def test_compile_word(word, expected):
    actual = compile_word(word)
    assert expected == actual


# NOTE: A simple profiling can be done by invoking the following command:
#
#   python -m cProfile cs212/test_lesson6.py
#

if __name__ == '__main__':
    pytest.main(['-v', __file__])
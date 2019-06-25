import itertools
import re

#
# Part 1: Zebra Puzzle
#

houses = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(houses))


def imright(h1, h2):
    """House h1 is immediately right of h2 if h1-h2 == 1."""
    return h1 - h2 == 1


def nextto(h1, h2):
    """Two houses are next to each other if they differ by 1."""
    # We could do abs(h1 - h2) == 1 but this is for fun :-)
    return imright(h1, h2) or imright(h2, h1)


def ints(start, end=None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1


def all_ints():
    """Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."""
    sign = -1
    n = 1
    while True:
        yield n // 2 * sign
        sign *= -1
        n += 1


def zebra_puzzle():
    "Return a tuple (WATER, ZEBRA indicating their house numbers."
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses)) # 1
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in orderings
                if imright(green, ivory)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
                if Englishman is red
                if Norwegian is first
                if nextto(Norwegian, blue)
                for (coffee, tea, milk, oj, WATER) in orderings
                if coffee is green
                if Ukranian is tea
                if milk is middle
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Kools is yellow
                if LuckyStrike is oj
                if Japanese is Parliaments
                for (dog, snails, fox, horse, ZEBRA) in orderings
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )


#
# Part 2: Solving Cryptarithmetic
#


def fill_in(formula):
    """Generate all possible fillings-in of letters in formula with digits."""
    letters = ''.join(set([x for x in formula if x.isalpha()]))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = str.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            return f
    return None


def valid(f):
    """Formula f is valid if and only if it has no numbers with leading zero,
    and evals true."""

    # FIXME: eval() is slow. Use something else.
    try: 
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False


def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""

    if word.isupper():
        return '+'.join(
            ['{}*{}'.format(10 ** i, w) for i, w in enumerate(word[::-1])])
    else:
        return word
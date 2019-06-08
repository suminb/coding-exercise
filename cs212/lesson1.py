from operator import itemgetter


def poker(hands):
    """Return a list of winning hands: poker([hand,...]) => [hand,...]"""
    return allmax(hands, key=hand_rank)


def allmax(iterable, key=None):
    """Return a list of all items equal to the max of the iterable."""
    # Your code here.
    max_ = max(iterable, key=key)
    return [x for x in iterable if hand_rank(x) == hand_rank(max_)]


def hand_rank(hand):
    """Return a value indicating the ranking of a hand."""
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)


def card_ranks(hand):
    """Return a list of the ranks, sorted with higher first."""
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if ranks == [14, 5, 4, 3, 2] else ranks


def straight(ranks):
    """Return True if the ordered ranks form a 5-card straight."""
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


# def straight(ranks):
#     "Return True if the ordered ranks form a 5-card straight."
#     # Your code here.
#     return all(map(lambda x, y: y - x == 1, ranks[1:], ranks[:-1]))


def flush(hand):
    "Return True if all the cards have the same suit."
    # Your code here.
    return len(set([s for _, s in hand])) == 1


def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # Your code here.
    pair1 = kind(2, ranks)
    pair2 = kind(2, ranks[::-1])

    if pair1 != pair2:
        return (pair1, pair2)
    else:
        return None

    # if pair1 is None:
    #     return None

    # pair2 = kind(2, ranks[2:])
    # if pair2 is None:
    #     return None

    # return (pair1, pair2)


def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def best_hand(hand):
    """From a 7-card hand, return the best 5 card hand."""
    raise NotImplementedError

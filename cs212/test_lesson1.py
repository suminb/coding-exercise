import pytest

from lesson1 import best_hand, card_ranks, kind, poker, straight, two_pair


@pytest.fixture
def sf():
    return '6C 7C 8C 9C TC'.split()  # Straight Flush


@pytest.fixture
def fk():
    return '9D 9H 9S 9C 7D'.split()  # Four of a Kind


@pytest.fixture
def fh():
    return 'TD TC TH 7C 7D'.split()  # Full House


@pytest.fixture
def tp():
    return 'TD 9H TH 7C 3S'.split()  # Two Pair


@pytest.fixture
def al():
    return 'AC 2D 4H 3D 5S'.split()  # Ace-Low Straight


def test(fk):
    fkranks = card_ranks(fk)
    # tpranks = card_ranks(tp)

    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) is None
    assert kind(2, fkranks) is None
    assert kind(1, fkranks) == 7
    assert two_pair([10, 10, 5, 5, 2]) == (10, 5)


def test_ace_low_straight(al):
    assert straight(card_ranks(al)) is True


def test_draw(fk, fh):
    sf1 = '6C 7C 8C 9C TC'.split()  # Straight Flush
    sf2 = '6D 7D 8D 9D TD'.split()  # Straight Flush
    assert poker([sf1, sf2, fk, fh]) == [sf1, sf2]


@pytest.mark.skip
def test_best_hand():
    assert sorted(best_hand('6C 7C 8C 9C TC 5C JS'.split())) \
        == ['6C', '7C', '8C', '9C', 'TC']
    assert sorted(best_hand('TD TC TH 7C 7D 8C 8S'.split())) \
        == ['8C', '8S', 'TC', 'TD', 'TH']
    assert sorted(best_hand('JD TC TH 7C 7D 7S 7H'.split())) \
        == ['7C', '7D', '7H', '7S', 'JD']

import src.functions as fc


def test_first_crescent():
    assert fc.get_largest(3, 1, 2) == 3


def test_first_decrescent():
    assert fc.get_largest(3, 2, 1) == 3


def test_second_crescent():
    assert fc.get_largest(1, 3, 2) == 3


def test_second_decrescent():
    assert fc.get_largest(2, 3, 1) == 3


def test_third_crescent():
    assert fc.get_largest(1, 2, 3) == 3


def test_third_decrescent():
    assert fc.get_largest(2, 1, 3) == 3


def test_float():
    assert fc.get_largest(2.0, 1.4, 3.1) == 3.1


def test_negative():
    assert fc.get_largest(-2, -1, -3) == -1


def test_negative_positive():
    assert fc.get_largest(-2, 1, 0) == 1

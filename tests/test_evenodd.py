import src.functions as fc


def test_output_type():
    assert isinstance(fc.even_odd(5), str)


def test_even_small():
    assert fc.even_odd(4) == "Even"


def test_even_large():
    assert fc.even_odd(178418932) == "Even"


def test_odd_small():
    assert fc.even_odd(178418931) == "Odd"


def test_odd_large():
    assert fc.even_odd(178418931) == "Odd"


def test_zero():
    assert fc.even_odd(0) == "Even"


def test_neven_small():
    assert fc.even_odd(-4) == "Even"


def test_neven_large():
    assert fc.even_odd(-178418932) == "Even"


def test_nodd_small():
    assert fc.even_odd(-178418931) == "Odd"


def test_nodd_large():
    assert fc.even_odd(-178418931) == "Odd"


def test_no_integer():
    assert fc.even_odd(1.5) == "Please use an integer value"

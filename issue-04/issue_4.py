import pytest
from one_hot_encoder import fit_transform


def test_fruits_eq():
    actual = fit_transform('Apple')
    expected = [('Apple', [1])]
    assert actual == expected


def test_fruits_not_eq():
    fruits = ['Apple', 'Lemon', 'Orange', 'Apple']
    actual = fit_transform(*fruits)
    expected = [('Apple', [1, 0, 0]),
                ('Lemon', [1, 0, 0]),
                ('Orange', [0, 1, 1]),
                ('Apple', [1, 0, 0])]
    assert actual != expected


def test_fruits_in():
    fruits = ['Apple', 'Lemon', 'Orange', 'Apple']
    container = fit_transform(*fruits)
    key = [('Plum', [0, 0, 0, 1])]
    assert key in container


def test_fruits_exception():
    with pytest.raises(TypeError):
        fit_transform()


def test_empty_string():
    actual = fit_transform(' ', '  ')
    expected = [(' ', [0, 1]), ('  ', [1, 0])]
    assert actual == expected

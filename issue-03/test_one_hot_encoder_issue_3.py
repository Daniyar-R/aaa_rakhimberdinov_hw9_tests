import unittest
from one_hot_encoder import fit_transform


class FitTransformTest(unittest.TestCase):
    def test_fruits_eq(self):
        actual = fit_transform('Apple')
        expected = [('Apple', [1])]
        self.assertEqual(actual, expected)

    def test_fruits_not_eq(self):
        fruits = ['Apple', 'Lemon', 'Orange', 'Apple']
        actual = fit_transform(*fruits)
        expected = [('Apple', [1, 0, 0]),
                    ('Lemon', [1, 0, 0]),
                    ('Orange', [0, 1, 1]),
                    ('Apple', [1, 0, 0])]
        self.assertNotEqual(actual, expected)

    def test_fruits_not_in(self):
        fruits = ['Apple', 'Lemon', 'Orange', 'Apple']
        container = fit_transform(*fruits)
        key = [('Plum', [0, 0, 0, 1])]
        self.assertNotIn(key, container)

    def test_fruits_exception(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_empty_string(self):
        actual = fit_transform(' ', '  ')
        expected = [(' ', [0, 1]), ('  ', [1, 0])]
        self.assertEqual(actual, expected)

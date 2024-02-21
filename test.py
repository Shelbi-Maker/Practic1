import unittest
from app import square


class TestSquareFunction(unittest.TestCase):

    def test_positive_number(self):
        self.assertEqual(square(2), 4)  # 2 в квадрате равно 4

    def test_negative_number(self):
        self.assertEqual(square(-3), 9)  # (-3) в квадрате равно 9

    def test_zero(self):
        self.assertEqual(square(0), 0)  # 0 в квадрате равно 0

    def test_large_number(self):
        self.assertEqual(square(1000), 1000000)  # 1000 в квадрате равно 1000000

    def test_fractional_number(self):
        self.assertEqual(square(2.5), 6.25)  # 2.5 в квадрате равно 6.25


if __name__ == "__main__":
    unittest.main()

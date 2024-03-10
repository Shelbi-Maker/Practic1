import unittest
from app import square

class TestSquare(unittest.TestCase):
    def testsqr5(self):
        self.assertEqual(square(5), 25)

    def testsqr8(self):
        self.assertEqual(square(8), 64)

    def test_sqr_0(self):
        self.assertEqual(square(0), 0)

    def test_sqr_10(self):
        self.assertEqual(square(10), 100)

    def test_sqr_1(self):
        self.assertEqual(square(1), 1)

if __name__ == '__main__':
    unittest.main()

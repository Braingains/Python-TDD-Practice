import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare_5_5_returns_5_is_equal_to_5(self):
        self.assertEqual("5 is equal to 5", compare(5, 5))
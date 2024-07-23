import unittest
from src.validate import is_len_consistent


class TestIsLenConsistent(unittest.TestCase):
    def test_is_iterable_with_iterables(self):
        self.assertTrue(is_len_consistent([
            [1,2,3],
            [4,5,6],
        ]))

    def test_is_iterable_with_non_iterables(self):
        self.assertFalse(is_len_consistent([
            [1,2,3],
            [4,5],
        ]))


if __name__ == "__main__":
    TestIsLenConsistent()

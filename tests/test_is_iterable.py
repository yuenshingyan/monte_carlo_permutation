import unittest
from src.util import _is_iterable
import numpy as np


class TestIsIterable(unittest.TestCase):
    def test_is_iterable_with_iterables(self):
        self.assertTrue(_is_iterable([]))
        self.assertTrue(_is_iterable(()))
        self.assertTrue(_is_iterable({}))
        self.assertTrue(_is_iterable({"A": 1}))
        self.assertTrue(_is_iterable(np.array(())))

    def test_is_iterable_with_non_iterables(self):
        self.assertFalse(_is_iterable(1))
        self.assertFalse(_is_iterable(1.0))
        self.assertFalse(_is_iterable(True))


if __name__ == "__main__":
    TestIsIterable()

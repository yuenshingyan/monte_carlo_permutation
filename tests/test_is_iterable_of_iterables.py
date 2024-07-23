import unittest
from src.util import _is_iterable_of_iterables
import numpy as np


class TestIsIterableOfIterables(unittest.TestCase):
    def test_is_iterable_of_iterables_with_iterable_of_iterables(self):
        self.assertTrue(_is_iterable_of_iterables([[]]))
        self.assertTrue(_is_iterable_of_iterables([{}]))
        self.assertTrue(_is_iterable_of_iterables(np.array(
            [[1, 2, 3], [4, 5, 6]]
        )))

    def test_is_iterable_of_iterables_with_non_iterable_of_iterables(self):
        self.assertFalse(_is_iterable_of_iterables(1))
        self.assertFalse(_is_iterable_of_iterables(1.0))
        self.assertFalse(_is_iterable_of_iterables(True))
        self.assertFalse(_is_iterable_of_iterables("A"))
        self.assertFalse(_is_iterable_of_iterables([]))
        self.assertFalse(_is_iterable_of_iterables(()))
        self.assertFalse(_is_iterable_of_iterables({}))
        self.assertFalse(_is_iterable_of_iterables(np.array([])))


if __name__ == "__main__":
    TestIsIterableOfIterables()

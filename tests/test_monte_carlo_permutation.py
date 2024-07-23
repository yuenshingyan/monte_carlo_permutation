from typing import Iterable
import unittest
import numpy as np
from src.monte_carlo_permutation import monte_carlo_permutation


class TestMonteCarloPermutation(unittest.TestCase):
    def test_is_iterable_with_iterables(self):
        p_value, dis = monte_carlo_permutation(
            signals=[np.random.random(size=10)] * 3,
            returns=[np.random.random()] * 10
        )
        self.assertIsInstance(p_value, float)
        self.assertIsInstance(dis, Iterable)


if __name__ == "__main__":
    TestMonteCarloPermutation()

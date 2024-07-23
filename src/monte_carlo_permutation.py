"""This module contains the `monte_carlo_permutation` function."""

from src.info import VERSION, AUTHOR

__all__ = ["monte_carlo_permutation"]
__version__ = VERSION
__author__ = AUTHOR

from typing import Iterable
import numpy as np
from src.util import _is_iterable, _is_iterable_of_iterables
from src.validate import is_len_consistent


def monte_carlo_permutation(signals: list[Iterable], returns: Iterable,
                            m: int = 5000):
    """Compute and return the p-value and sample distribution of Monte Carlo
    Permutation test.

    Procedures of Monte Carlo Permutation test:

    1) Shuffle market data (i.e. market returns or price difference that
    reflects the change in value of an asset). Market data does not need to
    be de-trended.

    2) Pair long/short signals with shuffled market data from step 1) without
    replacement.

    3) Compute the rules' returns by multiplying the signals with the shuffled
    market data.

    4) Compute the average of rules' returns.

    5) Select and store the max among all signals as sample distribution.

    6) Repeat steps 1) to 5) for `m` times, where `m` is a large number like
    5000.

    7) Compute the best expected returns by multiplying the raw market data
    with long/short signals. Then, use the best expected returns to compute
    the p-value with sampling distribution formed in step 6).

    Parameters
    ----------
    signals : list[Iterable]
        List of long/short signals (+1 for long and -1 for short).
    returns : Iterable
        Returns of asset.
    m : int = 5000
        Number of Bootstrapping.

    Returns
    -------
    p_value : float
        p-value of Monte Carlo Permutation test.
    sample_distribution : np.ndarray
        Sample Distribution.

    Raises
    ------
    ValueError
        - If Argument `signals` is not an iterable or iterable of iterables.
        - If Argument `returns` is not an iterable or iterable of iterables.
        - If Argument `m` is not an int.
        - If Argument `signals` contains `np.nan`.
        - If Argument `returns` contains `np.nan`.
    """
    if not _is_iterable(signals):
        ValueError(
            "Argument `signals` must be an iterable or iterable of iterables.")

    if not _is_iterable(returns):
        ValueError(
            "Argument `returns` must be an iterable or iterable of iterables.")

    if not isinstance(m, int):
        raise ValueError("Argument `m` must be an int.")

    if not is_len_consistent(signals):
        raise ValueError(
            "All iterables in argument `signals` must have the length.")

    if np.any(np.isnan(signals)):
        raise ValueError("Argument `signals` must not contains `np.nan`.")

    if np.any(np.isnan(returns)):
        raise ValueError("Argument `returns` must not contains `np.nan`.")

    if not isinstance(returns, np.ndarray):
        returns = np.array(returns)

    if not _is_iterable_of_iterables(returns):
        signals = [signals]

    # Compute the threshold as the maximum of expected return of all signals.
    threshold = np.max(np.mean([s * returns for s in signals], axis=1))

    # Permutate and multiply returns with signals for `m` times.
    sample_distribution = np.zeros(shape=m)
    for i in range(m):

        # Permutate returns.
        returns = np.random.choice(a=returns, size=len(returns))

        # Multiply the same Permutated returns with all signals.
        permutated = np.zeros(shape=len(signals))
        for j, s in enumerate(signals):
            permutated[j] = np.mean(s * returns)

        # Select the best permutated value as part of the sample distribution.
        sample_distribution[i] = np.max(permutated)

    # Compute p-value.
    p_value = np.mean(sample_distribution >= threshold)

    return p_value, sample_distribution

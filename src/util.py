"""This module contains all utility functions."""

from src.info import VERSION, AUTHOR

__all__ = [
    "_is_iterable_of_iterables",
    "_is_iterable",
]
__version__ = VERSION
__author__ = AUTHOR

from typing import Any


def _is_iterable_of_iterables(arg: Any) -> bool:
    """Helper function that checks if `arg` is an iterable of iterables.

    Parameters
    ----------
    arg : Any
        Argument of any type.

    Returns
    -------
    bool
        - If `arg` is str.
        - If `arg` is an iterable.
        - If `arg` is not an iterable.
    """
    try:
        if isinstance(arg, str):
            return False

        if len(arg) == 0:
            return False

        return all(_is_iterable(a) for a in arg)
    except TypeError:
        return False


def _is_iterable(arg: Any) -> bool:
    """Helper function that checks if `arg` is an iterable or not.

    Parameters
    ----------
    arg : Any
        Argument of any type.

    Returns
    -------
    bool
        - If `arg` is an iterable.
        - If `arg` is not an iterable.
    """
    try:
        iter(arg)
        return True
    except TypeError:
        return False

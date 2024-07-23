"""This module contains validation functions."""

from src.info import VERSION, AUTHOR

__all__ = [
    "is_len_consistent",
]
__version__ = VERSION
__author__ = AUTHOR

from typing import Any


def is_len_consistent(arg: Any):
    ref_len = len(arg[0])
    for item in arg[1:]:
        if len(item) != ref_len:
            return False

    return True

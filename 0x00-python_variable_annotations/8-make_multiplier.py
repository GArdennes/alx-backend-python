#!/usr/bin/env python3

"""
8-make_multiplier
"""

from typing import Callable


def make_multiplier(
        multiplier: float
        ) -> Callable[[float], float]:
    """
    Function takes a string and numbers and returns a tuple.
    """
    def product(x: float) -> float:
        """
        A function that multiplies two floats
        """
        return multiplier * x
    return product

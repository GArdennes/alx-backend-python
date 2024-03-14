#!/usr/bin/env python3

"""
9-element_length
"""

from typing import Sequence


def element_length(
        lst: Sequence[str]
        ) -> list[tuple[str, int]]:
    """
    Function takes a list of strings
    Returns a list of tuples containing the string
    and its length.
    """
    return [(i, len(i)) for i in lst]

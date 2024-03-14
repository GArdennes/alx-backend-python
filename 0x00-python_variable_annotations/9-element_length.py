#!/usr/bin/env python3

"""
9-element_length
"""

from typing import Sequence, List, Tuple


def element_length(
        lst: Sequence[str]) -> List[Tuple[str, int]]:
    """
    Function takes a list of strings
    Returns a list of tuples containing the string
    and its length.
    """
    return [(i, len(i)) for i in lst]

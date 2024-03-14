#!/usr/bin/env python3

"""
9-element_length
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(
        lst: Iterable[Sequence]
        ) -> List[Tuple[Sequence, int]]:
    """
    Function takes a list of strings
    Returns a list of tuples containing the string
    and its length.
    """
    return [(i, len(i)) for i in lst]

#!/usr/bin/env python3

"""
100-safe_first_element
"""

from typing import Sequence


def safe_first_element(lst: Sequence) -> object:
    """
    Returns the first element of a sequence
    or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

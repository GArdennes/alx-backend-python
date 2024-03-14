#!/usr/bin/env python3

"""
101-safely_get_value
"""

from typing import Mapping, Any, Union


def safely_get_value(
        dct: Mapping[Any, Any],
        key: Any, default: Union[None, Any] = None
        ) -> Union[Any, None]:
    """
    Retrieves a value from a dictionary
    with a default if the key is missing.
    """
    if key in dct:
        return dct[key]
    else:
        return default

#!/usr/bin/env python3
"""
1-async_comprehension
"""
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension.
    """
    numbers = [number async for number in async_generator()]
    return numbers

#!/usr/bin/env python3
"""
1-concurrent_coroutines
"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Waits for n random delays concurrently,
    each between 0 and max_delay seconds.
    Returns a list of the delays in ascending order,
    without using sort().
    """
    tasks = [
            asyncio.create_task(
                wait_random(max_delay)
                ) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return results

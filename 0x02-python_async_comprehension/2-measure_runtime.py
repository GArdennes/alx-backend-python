#!/usr/bin/env python3
"""
2-measure_runtime
"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that will execute async_comprehension
    four times in parallel and return total runtime.
    """
    start_time = time.time()
    tasks = [
            asyncio.create_task(
                async_comprehension()
                ) for _ in range(4)
            ]
    await asyncio.gather(*tasks)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

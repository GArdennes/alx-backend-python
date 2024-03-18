#!/usr/bin/env python3
"""
4-tasks
"""
import asyncio
task_wait_random = __import__("0-basic_async_syntax").task_wait_random


async def task_wait_n(n, max_delay):
    """
    Waits for n random delays concurrently using tasks,
    returning results in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return results

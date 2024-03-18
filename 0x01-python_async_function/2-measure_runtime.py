#!/usr/bin/env python3
"""
2-measure_runtime
"""
import asyncio
import time
wait_n = __import__(‘1-concurrent_coroutines’).wait_n


async def measure_time(n, max_delay):
    """
    Measures the total execution time
    for wait_n(n, max_delay), and returns total_time/n.
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return float(elapsed_time/n)

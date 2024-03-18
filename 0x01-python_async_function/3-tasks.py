#!/usr/bin/env python3
"""
3-tasks
"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_n(max_delay):
    """
    Takes an integer max_delay and returns an asyncio.task
    """
    return asyncio.create_task(wait_random(max_delay))

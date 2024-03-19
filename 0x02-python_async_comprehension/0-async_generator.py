#!/usr/bin/env python3
"""
0-async_generator
"""
import asyncio
from random import randint
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
  """
  Asynchronously generates random numbers between 0 and 10.
  """
  for _ in range(10):
    await asyncio.sleep(1)
    yield randint(0, 10)

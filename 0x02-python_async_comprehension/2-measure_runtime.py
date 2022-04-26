#!/usr/bin/env python3

"""
Async Comprehensions
"""


import time
import asyncio


async_comprehension = __import__(
    '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure runtime
    """
    start = time.time()
    await async_comprehension()
    return time.time() - start

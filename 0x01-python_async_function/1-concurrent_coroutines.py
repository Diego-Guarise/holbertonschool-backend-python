#!/usr/bin/env python3
"""
Test file for printing the correct output of the wait_n coroutine
"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for n times
    """
    wait_list = []

    for tmp in range(n):
        wait_list.append(await wait_random(max_delay))

    return sorted(wait_list)

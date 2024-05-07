#!/usr/bin/env python3
"""
wait_n(n, max_delay)
"""
import asyncio
from typing import List
from asyncio import Task

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for `n` random delays and return a list of the delays.

    Args:
        n (int): The number of random delays to wait for.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of the random delays.
    """
    tasks: List[Task] = [wait_random(max_delay) for _ in range(n)]
    delays: List[float] = [await task for task in asyncio.as_completed(tasks)]
    return delays

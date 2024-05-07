#!/usr/bin/env python3
"""
task_wait_n
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for `n` random delays and return a list of the delays.

    Args:
        n (int): The number of random delays to wait for.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of the random delays.
    """
    tasks: List[asyncio.Task] = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = [await task for task in asyncio.as_completed(tasks)]
    return delays

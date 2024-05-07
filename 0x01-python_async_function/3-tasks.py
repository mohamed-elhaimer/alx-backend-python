#!/usr/bin/env python3
"""
task_wait_random
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Asynchronously waits for a random number of seconds.

    Args:
        max_delay (int): The maximum number of seconds to wait.

    Returns:
        asyncio.Task: A task representing the asynchronous operation.

    """
    return asyncio.create_task(wait_random(max_delay))

#!/usr/bin/env python3
"""
measure_time
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average time taken to execute `wait_n` function `n` times with
    a maximum delay of `max_delay`.

    Args:
        n (int): The number of times to execute `wait_n`.
        max_delay (int): The maximum delay for each execution of `wait_n`.

    Returns:
        float: The average time taken to execute `wait_n` function.

    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    result = (end_time - start_time) / n
    return result

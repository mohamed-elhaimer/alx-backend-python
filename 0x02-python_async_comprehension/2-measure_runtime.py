#!/usr/bin/env python3
"""write a measure_runtime coroutine that will execute
 async_comprehension four times in parallel using asyncio.gather."""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime- function to return measure the total runtime
    Arguments:
        no arguments
    Returns:
        the total runtime"""
    start_time = time.time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end_time = time.time()
    runtime = end_time - start_time
    return runtime

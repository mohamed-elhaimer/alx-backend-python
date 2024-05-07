#!/usr/bin/env python3
"""Write an asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """return a random value after wait random seconds
      between 0 and maw_delay"""
    if max_delay < 0:
        raise ValueError("max_delay must be a positive number")

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay

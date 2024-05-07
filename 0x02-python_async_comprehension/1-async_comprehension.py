#!/usr/bin/env python3
"""write a coroutine called async_comprehension that takes no arguments"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension- function to return 10 random numbers
    Arguments:
        no arguments
    Returns:
        10 random numbers
    """
    result = [item async for item in async_generator()]
    return result

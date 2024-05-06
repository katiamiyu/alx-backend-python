#!/usr/bin/env python3

"""
Write an asynchronous coroutine that takes in an integer argument
(max_delay,along with a default value of 10) named wait_random that
waits for a random delay between 0 and max_delay (included and
float value) seconds and eventually returns it value.
"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay (included and
    float value) seconds and eventually returns it value.
    """
    val: int
    val = random.uniform(0, max_delay)
    await asyncio.sleep(val)
    return val

import asyncio
from copy import copy
import sys
import random

async def merge(a, b, start, mid, finish, event_in1, event_in2, event_out):
    await asyncio.gather(event_in1.wait(), event_in2.wait())
    a, i1, i2 = copy(a), start, mid
    for _ in range(start, finish):
        if i2 >= finish or i1 < mid and a[i1] < a[i2]:
            b[_] = a[i1]
            i1 += 1
        else:
            b[_] = a[i2]
            i2 += 1

    event_out.set()


async def mtasks(a):
    b = copy(a)

    def make_coroutine(event_out, l, r):
        if r - l <= 1:
            event_out.set()
            return []
        event_in1, event_in2 = asyncio.Event(), asyncio.Event()
        coroutine = merge(b, b, l, (l + r) // 2, r, event_in1, event_in2, event_out)
        return make_coroutine(event_in1, l, (l + r) // 2) + make_coroutine(event_in2, (l + r) // 2, r) + [coroutine]

    return make_coroutine(asyncio.Event(), 0, len(a)), b

exec(sys.stdin.read())

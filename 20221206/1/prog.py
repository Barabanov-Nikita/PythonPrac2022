import asyncio


end_event = asyncio.Event()
async def writer(queue, delay):
    number = 0
    while not end_event.is_set():
        await asyncio.sleep(delay)
        await queue.put(f"{number}_{delay}")
        number += 1

async def stacker(queue, stack):
    while not end_event.is_set():
        elem = await queue.get()
        await stack.put(elem)

async def reader(stack, n, delay):
    number = 0
    while not end_event.is_set():
        await asyncio.sleep(delay)
        elem = await stack.get()
        print(elem)
        number += 1
        if number == n:
            end_event.set()


async def main():
    queue, stack = asyncio.Queue(), asyncio.LifoQueue()
    delay1, delay2, delay3, n = eval(input())
    await asyncio.gather(writer(queue, delay1), writer(queue, delay2), stacker(queue, stack), reader(stack, n, delay3))

asyncio.run(main())

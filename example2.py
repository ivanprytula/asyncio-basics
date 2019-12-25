import time
import asyncio

# start = time.time()


# def tic():
#     return 'at %1.1f seconds' % (time.time() - start)


async def long_task1():
    print(f"gr1 started work: {time.strftime('%X')}")
    await asyncio.sleep(5)
    print(f"gr1 ended work: {time.strftime('%X')}")


async def long_task2():
    print(f"gr2 started work: {time.strftime('%X')}")
    await asyncio.sleep(5)
    print(f"gr2 ended work: {time.strftime('%X')}")


async def fast_task3():
    print(f"Let's do some stuff while the coroutines are blocked, {time.strftime('%X')}")
    await asyncio.sleep(1)
    print("Done!")


ioloop = asyncio.get_event_loop()
tasks = [
    ioloop.create_task(long_task1()),
    ioloop.create_task(long_task2()),
    ioloop.create_task(fast_task3())
]
ioloop.run_until_complete(asyncio.wait(tasks))
ioloop.close()

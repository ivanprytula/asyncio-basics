import asyncio
import time


async def say_after():
    for i in range(5):
        await asyncio.sleep(1)
        continue
    print("Done!!!")


async def numbers():
    print(1 + 1)
    # await asyncio.sleep(10)
    # TODO: insert here async function!!!!!
    print(5)


async def main():
    # print(1 + 1)
    task_q = asyncio.ensure_future(say_after())
    task_n = asyncio.ensure_future(numbers())
    # print(task_q)
    # task_n = asyncio.create_task(say_after())
    # await task_n
    await asyncio.gather(task_q, task_n)
    # asyncio.run(say_after())
    # print(2 + 1)


asyncio.run(main())

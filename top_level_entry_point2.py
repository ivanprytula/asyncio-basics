import asyncio


# import time


async def say_after():
    await asyncio.sleep(5)
    print("Done!!!")


# async def numbers():
#     await asyncio.sleep(5)


async def main():
    print(1 + 1)
    # task_q = asyncio.ensure_future(say_after())
    # task_n = asyncio.ensure_future(numbers())

    # task_n = asyncio.create_task(say_after())
    # await task_n

    await say_after()

    # await asyncio.gather(task_q, task_n)
    print(2 + 1)


asyncio.run(main())

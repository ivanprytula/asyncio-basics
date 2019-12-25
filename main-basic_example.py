import asyncio


async def main():
    print('Hello')
    # await asyncio.sleep(10)
    import time
    time.sleep(10)
    print('World!')


asyncio.run(main())


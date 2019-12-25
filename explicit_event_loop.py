import asyncio


async def go():
    future = asyncio.Future()
    future.set_result(None)

    await asyncio.sleep(3.0)
    await future
    print('foo')


loop = asyncio.get_event_loop()
loop.run_until_complete(go())
loop.close()

import asyncio
from utils import async_timed, delay

@async_timed()
async def delay(delay_sec: int) -> int:
    await asyncio.sleep(delay_sec)
    return delay_sec

@async_timed()
async def main():
    future1 = asyncio.create_task(coro=delay(2))
    future2 = asyncio.create_task(coro=delay(3))
    await future1
    await future2

asyncio.run(main=main())

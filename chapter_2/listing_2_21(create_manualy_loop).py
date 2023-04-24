import asyncio
from utils import async_timed, delay


@async_timed()
async def main() -> None:
    # await delay(5, 1)                             # <function main at 0x7fdf70133640> завершилась за 8.0117 с
    # await delay(3, 2)
    task1 = asyncio.create_task(delay(5, 1))
    task2 = asyncio.create_task(delay(3, 2))        # <function main at 0x7f18ac16b640> завершилась за 5.0038 с
    await task1
    await task2

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(main())
finally:
    loop.close()

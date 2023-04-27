import asyncio
import aiohttp
from aiohttp import ClientSession
import logging

from utils import fetch_status, async_timed

"""
Здесь представим логику что есть несколько длинных запросов и если появляется
исключение то все остальные задачи мы снимаем, используем метод Task.cancel()
"""
@async_timed()
async def main() -> None:
    async with ClientSession() as session:
        featchers = [
            asyncio.create_task(fetch_status(session, 'https://example.com', delay=3)),
            asyncio.create_task(fetch_status(session, 'https://example.com', delay=3)),
            asyncio.create_task(fetch_status(session, 'https://example.com', delay=3))
        ]
        done, pending = await asyncio.wait(featchers, return_when=asyncio.FIRST_COMPLETED )

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for done_task in done:
            print(await done_task)


asyncio.run(main())

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
        pending = [
            asyncio.create_task(fetch_status(session, 'https://example.com', delay=1)),
            asyncio.create_task(fetch_status(session, 'https://example.com', delay=2)),
            asyncio.create_task(fetch_status(session, 'https://example.com', delay=3))
        ]
        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED )
            print(f'Число завершившихся задач: {len(done)}')
            print(f'Число ожидающих задач: {len(pending)}')

            for done_task in done:
                try:
                    print(await done_task)
                except:
                    print('Boom')


asyncio.run(main())

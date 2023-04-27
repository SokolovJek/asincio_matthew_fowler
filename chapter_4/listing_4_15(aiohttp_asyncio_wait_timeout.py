import asyncio
import aiohttp
from aiohttp import ClientSession
import logging

from utils import fetch_status, async_timed


@async_timed()
async def main() -> None:
    async with ClientSession() as session:
        pending = [
            asyncio.create_task(fetch_status(session, 'https://example.com')),
            asyncio.create_task(fetch_status(session, 'https://example.com')),
            asyncio.create_task(fetch_status(session, 'https://example.com', delay=3))
        ]
        done, pending = await asyncio.wait(pending, timeout=1)

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for done_task in done:
            try:
                print(await done_task)
            except:
                print('Boom')


asyncio.run(main())

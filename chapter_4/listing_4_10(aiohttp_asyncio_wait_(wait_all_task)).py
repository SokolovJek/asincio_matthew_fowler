import asyncio
import aiohttp
from aiohttp import ClientSession

from utils import fetch_status, async_timed


@async_timed()
async def main() -> None:
    async with ClientSession() as session:
        featchers = [
            asyncio.create_task(fetch_status(session, 'https://example.com')),
            asyncio.create_task(fetch_status(session, 'https://example.com')),
            asyncio.create_task(fetch_status(session, 'https://example.com', delay=3))
        ]
        done, pending = await asyncio.wait(featchers, return_when='ALL_COMPLETED') #  ALL_COMPLETED this params is default

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for done_task in done:
            result = await done_task
            print(result)

asyncio.run(main())

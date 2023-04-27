import asyncio
import aiohttp
from aiohttp import ClientSession
from utils import fetch_status, async_timed
import time


@async_timed()
async def main():
    async with ClientSession() as session:
        url = 'https://www.example.com'
        fetchers = [fetch_status(session=session, url=url, delay=1),
                  fetch_status(session=session, url=url, delay=10),
                  fetch_status(session=session, url=url, delay=10),]
        for finished_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await finished_task
                print(result)
            except asyncio.TimeoutError:
                print('Произошел таймаут')

asyncio.run(main())
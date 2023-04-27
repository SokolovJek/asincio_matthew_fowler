import aiohttp
from aiohttp import ClientSession
import asyncio

from utils import async_timed, fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ['https://example.com', 'python://example.com']
        tasks = [fetch_status(session, url) for url in urls]
        status_code = await asyncio.gather(*tasks)
        print(status_code)

asyncio.run(main())

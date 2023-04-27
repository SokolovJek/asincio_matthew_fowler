import aiohttp
from aiohttp import ClientSession
import asyncio

from utils import async_timed, fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ['https://example.com', 'python://example.com', 'https://example.com', 'python://example.com',]
        tasks = [fetch_status(session, url) for url in urls]
        status_code = await asyncio.gather(*tasks, return_exceptions=True)
        result_successful = [i for i in status_code if not isinstance(i, Exception)]
        result_exception =  [i for i in status_code if isinstance(i, Exception)]
        print(f'exception {result_exception}')
        print(f'result {result_successful}')
        print(f'all results {status_code}')

asyncio.run(main())
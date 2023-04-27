import asyncio
import aiohttp
from aiohttp import ClientSession
from utils import async_timed, fetch_status


@async_timed()
async def main() -> None:
    async with ClientSession() as session:
        url = 'https://www.example.com'
        status = await fetch_status(session, url)
        print(f'Состояние для {url} было равно {status}')


asyncio.run(main())

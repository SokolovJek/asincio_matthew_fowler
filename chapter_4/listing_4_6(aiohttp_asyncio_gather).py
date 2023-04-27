import asyncio
import aiohttp
from aiohttp import ClientSession
from utils import fetch_status, async_timed


@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ['https://example.com' for _ in range(1000)]
        requests = [fetch_status(session=session, url=url) for url in urls]
        status_code = await asyncio.gather(*requests)                                 # <function main at 0x7fb45c133ac0> завершилась за 5.4 с
        # Сейчас имеем выполение за 5.4 сек, а если захоти запустить синхронно
        # status_codes = [await fetch_status(session, url) for url in urls]           # <function main at 0x7fb45c133ac0> завершилась за 187.4275 с
        print(status_codes)


asyncio.run(main())

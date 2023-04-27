import asyncio
import aiohttp
from aiohttp import ClientSession
from utils import fetch_status, async_timed
import time


@async_timed()
async def add_data(fut: asyncio.Future()) -> list:
    data = []
    data.append(await fut)
    data.append(time.perf_counter())
    print(data)
    return data

@async_timed()
async def main():
    async with ClientSession() as session:
        url = 'https://www.example.com'
        fetchers = [fetch_status(session=session, url=url, delay=1),
                  fetch_status(session=session, url=url, delay=10),
                  fetch_status(session=session, url=url, delay=1),]
        for finished_task in asyncio.as_completed(fetchers):
            await finished_task
            # await add_data(finished_task)
        # print(type(fetch_status))                                       # <class 'function'>
        # result  = fetch_status(session=session, url=url, delay=5)
        # print(type(result))                                             # <class 'coroutine'>
        # print(await result)


asyncio.run(main())
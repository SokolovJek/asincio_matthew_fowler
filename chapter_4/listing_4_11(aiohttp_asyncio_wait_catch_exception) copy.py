import asyncio
import aiohttp
from aiohttp import ClientSession
import logging

from utils import fetch_status, async_timed


@async_timed()
async def main() -> None:
    async with ClientSession() as session:
        good_request = fetch_status(session, 'https://example.com')
        bed_request = fetch_status(session, 'bed://example.com')
        featchers = [
            asyncio.create_task(good_request),
            asyncio.create_task(bed_request)
        ]
        done, pending = await asyncio.wait(featchers, return_when='ALL_COMPLETED') #  ALL_COMPLETED this params is default

        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for done_task in done:
            # result = await done_task возбудит исключение
           if done_task.exception() is None:
               print('done_task=', done_task.result())
           else:
            logging.error("При выполнении запроса возникло исключение ", exc_info=done_task.exception())


asyncio.run(main())

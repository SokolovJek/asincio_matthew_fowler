import asyncio
import aiohttp
from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url: str) -> int:
    """
    Если запрос к url займет более 10 мс, то будет возбуждено
    исключение asyncio.TimeoutError
    """
    ten_millis = aiohttp.ClientTimeout(total=.01)                   # время ожидание подключения 0.01 ms
    async with session.get(url, timeout=ten_millis) as response:
        return response.status


async def main():
    session_timeout = aiohttp.ClientTimeout(total=1, connect=.1)  # время ожидание подключения 1 сек а время подключения 100 мс, это будет распостронятся на всех
    async with ClientSession() as session:
        try:
            status = await fetch_status(session, 'https://www.youtube.com/')
            print(f'Статус запроса = {status}')
        except asyncio.TimeoutError:
            print('Very long request')


asyncio.run(main())

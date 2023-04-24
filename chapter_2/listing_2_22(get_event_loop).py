import asyncio
from utils import async_timed, delay


def call_later() -> None:
    print('Меня вызовут в ближайшее время')

@async_timed()
async def main() -> None:
    # loop = asyncio.get_event_loop()
    loop = asyncio.get_running_loop()    # лутше использовать ее
    loop.call_soon(callback=call_later)  # функция будет запущена на следующей итерации
    await delay(1)

asyncio.run(main())

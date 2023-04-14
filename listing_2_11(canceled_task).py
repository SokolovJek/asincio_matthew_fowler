import asyncio
from utils import delay
from asyncio import CancelledError


async def main() -> None:
    long_task = asyncio.create_task(delay(10, 1))

    second_elapsed = 0

    while not long_task.done():
        print('Задача не закочилась, следующая проверка через секунду.')
        await asyncio.sleep(1)
        second_elapsed += 1
        if second_elapsed == 5:
            long_task.cancel()
    try:
        await long_task                     # таким образом мы можеи отловить исключение
    except CancelledError:
        print("Наша задача была снята")

asyncio.run(main())

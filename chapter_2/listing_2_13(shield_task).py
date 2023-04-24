import asyncio
from utils import delay
from asyncio.exceptions import TimeoutError


async def main() -> None:
    long_task = asyncio.create_task(coro=delay(10))
    try:
        result = await asyncio.wait_for(fut=asyncio.shield(long_task), timeout=5)
        print(result)
    except TimeoutError:
        print("Задача заняла более 5с, скоро она закончится!")
        result = await long_task
        print(result)

asyncio.run(main=main())


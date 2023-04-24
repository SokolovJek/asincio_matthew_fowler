import asyncio
from utils import delay


async def main() -> None:
    long_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(fut=long_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Тайм аут')
        print(f'Задача была снята? Ответ: {long_task.cancelled()}')

asyncio.run(main())




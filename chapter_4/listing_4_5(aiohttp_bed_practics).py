import asyncio
from utils import delay, async_timed


@async_timed()
async def main():
    delay_time = [3, 3, 3]
    results = []
    [results.append(await asyncio.create_task(delay(time))) for time in delay_time] # поскольку мы применяем await сразу же после создания Задачи, тио выполнение не будет конкурентным
    print(f'result = {results}')

asyncio.run(main())

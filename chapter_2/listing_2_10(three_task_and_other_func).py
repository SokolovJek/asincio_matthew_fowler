import asyncio
from utils import delay
import time


# Конкурентное выполнение нескольких задач

async def hello_every_one_second() -> None:
    for i in range(2):
        await asyncio.sleep(1)
        print('Здесь я бы могла выполнять свой код')

def sync_func() -> None:
    for i in range(2):
        time.sleep(1)
        print('Здесь я бы могла выполнять свой код')

async def main() -> None:
    start_time = time.time()
    task_one = asyncio.create_task(delay(4, 1))
    task_two = asyncio.create_task(delay(3, 2))
    task_three = asyncio.create_task(delay(3, 3))
    await hello_every_one_second()     # this is magic 3s!!!:)
    # sync_func()                      # это неудача выполнение 5с
    await task_one
    await task_two
    await task_three
    # await hello_every_one_second()     # это неудача выполнение 5с

    end_time = time.time()
    print(f'running time = {end_time - start_time:.4f}')

asyncio.run(main())

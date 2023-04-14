from utils import delay
import asyncio
import time


# Конкурентное выполнение нескольких задач

async def main():
    start_time = time.time()
    sleap_one = asyncio.create_task(delay(4, 1))
    sleap_two = asyncio.create_task(delay(3, 2))
    sleep_three = asyncio.create_task(delay(3, 3))

    await sleap_one
    await sleap_two
    await sleep_three
    end_time = time.time()
    print(f'runing time {end_time - start_time:.4f}')

asyncio.run(main())


# засыпаю на 3 с.
# засыпаю на 3 с.
# засыпаю на 3 с.
# сон в течении 3 с. закочился.
# сон в течении 3 с. закочился.
# сон в течении 3 с. закочился.
# runing time 3.0044
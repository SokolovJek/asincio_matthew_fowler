import asyncio
from utils import delay, async_timed

@async_timed()
async def cpu_bound() -> int:
    counter = 0
    for i in range(100_000_000):
        counter += 1
    return counter

@async_timed()
async def main() -> None:
    another_async_function = asyncio.create_task(delay(1))
    task1 = asyncio.create_task(cpu_bound())
    task2 = asyncio.create_task(cpu_bound())
    # another_async_function = asyncio.create_task(delay(5))
    result3 = await another_async_function
    result1 = await task1                       # task1 blockt task2 and another_async_function
    result2 = await task2
    # result3 = await another_async_function

    print(f'result1 = {result1}')
    print(f'result2 = {result2}')
    print(f'result3 = {result3}')

asyncio.run(main())

# выполняется <function main at 0x7f1654127b50> с аргументами () {}
# выполняется <function cpu_bound at 0x7f1654113880> с аргументами () {}
# <function cpu_bound at 0x7f1654113880> завершилась за 9.3663 с
# выполняется <function cpu_bound at 0x7f1654113880> с аргументами () {}
# <function cpu_bound at 0x7f1654113880> завершилась за 9.0935 с
# result1 = 100000000
# result2 = 100000000
# <function main at 0x7f1654127b50> завершилась за 18.4604 с

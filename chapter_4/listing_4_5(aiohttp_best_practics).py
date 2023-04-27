import asyncio
from utils import delay, async_timed


@async_timed()
async def main():
    delay_time = [3, 3, 3]
    results = []
    tasks = []
    [tasks.append(asyncio.create_task(delay(time))) for time in delay_time] # это работакет поскольку функция create_task возвращает управление сразу и мы нечего не ждем
    [results.append(await task) for task in tasks]
    print(f'result = {results}')

asyncio.run(main())

"""
Все ок время выполнение равно 3 секундам.
Но есть недостатки:
1) мы неперехватываем исключение
2) мы ждем пока все задачи выполнятся и только потом обрабатываем результат\
3) нагромождение кода
"""
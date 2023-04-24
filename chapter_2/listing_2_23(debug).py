import asyncio
from utils import async_timed


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100000000):
        counter = counter + 1
    return counter

async def main() -> None:
    task_one = asyncio.create_task(cpu_bound_work())
    # loop = asyncio.get_event_loop()
    # loop.slow_callback_duration = 10    # если нужно изменить время предупреждения
    await task_one


asyncio.run(main(), debug=True) # По умолчанию параметры заданы так, что предупреждение выдается, если сопрограмма работает дольше 100 мс

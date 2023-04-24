"""
Добавление обработчика сигнала, снимающего все задачи
"""
import asyncio
from asyncio import AbstractEventLoop
import signal
from typing import Set

from utils import delay


def canceled_tasks():
    print('Получен сигнал SIGINT!')
    tasks: Set[asyncio.Task] = asyncio.all_tasks()
    print(f'Снимается {len(tasks)} задач.')
    [task.cancel() for task in tasks]

async def main():
    loop: AbstractEventLoop = asyncio.get_running_loop()                      # возвращающая множество всех работающих задач
    loop.add_signal_handler(sig=signal.SIGINT, callback=canceled_tasks)

    await delay(10)

asyncio.run(main())

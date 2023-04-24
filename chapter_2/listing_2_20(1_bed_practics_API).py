import requests
import asyncio
from utils import async_timed


@async_timed()
async def get_example_status() -> int:
    return requests.get('https://yandex.ru/maps').status_code

@async_timed()
async def main() -> None:
    task1 = asyncio.create_task(get_example_status())
    task2 = asyncio.create_task(get_example_status())
    task3 = asyncio.create_task(get_example_status())
    await task1
    await task2
    await task3

asyncio.run(main())

# выполняется <function main at 0x7f7e3d0b7760> с аргументами () {}
# выполняется <function get_example_status at 0x7f7e3d0a3400> с аргументами () {}
# <function get_example_status at 0x7f7e3d0a3400> завершилась за 1.6752 с
# выполняется <function get_example_status at 0x7f7e3d0a3400> с аргументами () {}
# <function get_example_status at 0x7f7e3d0a3400> завершилась за 2.0748 с
# выполняется <function get_example_status at 0x7f7e3d0a3400> с аргументами () {}
# <function get_example_status at 0x7f7e3d0a3400> завершилась за 2.0817 с
# <function main at 0x7f7e3d0b7760> завершилась за 5.8324 с
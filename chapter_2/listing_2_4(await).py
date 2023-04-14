import asyncio


async def add_one(number: int) -> int:
    return number + 1

async def main() -> None:
    one_plus_one = await add_one(1) # приостановить и ждять результат add_one(1)
    two_plus_one = await add_one(2) # приостановить и ждять результат add_one(2)
    print(one_plus_one)
    print(two_plus_one)

asyncio.run(main())

# по сути это обычное выполнение последовательного кода так как операций ввода\выввода у нас нет.abs(x)

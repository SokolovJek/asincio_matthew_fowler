import asyncio


async def delay(delay_second: int, num_func=0) -> int:
    """Повторно используемая сопрограмма delay"""
    print(f'засыпаю на {delay_second} с. Function:{num_func}')
    await asyncio.sleep(delay_second)
    print(f'сон в течении {delay_second} с. закочился. Function:{num_func}')
    return delay_second

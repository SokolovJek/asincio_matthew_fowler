import asyncio
from utils import delay

"""
Здесь мы передали gather две сопрограммы. Первой для завершения требуется 3 с, второй  – одна. Можно ожидать, что результатом
будет список [1, 3], а по факту [3, 1]
"""
async def main():
    results = await asyncio.gather(delay(3), delay(1))
    print(results)

asyncio.run(main())

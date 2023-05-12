import asyncpg
import asyncio
from asyncpg import Record
from typing import List
from bd_commands import product_query


async def main() -> None:
    connection = await asyncpg.connect(host='127.0.0.1',
                                        port=5432,
                                        user='postgres',
                                        database='products',
                                        password='postgres')
    print('Creating the product database...')
    queries = [connection.feath(product_query),       # exeption = RuntimeWarning
               connection.execute(product_query)
               ]
    """
    В SQL одному подключению к базе соответствует
    один сокет. Поскольку подключение всего одно, а мы пытаемся прочитать одновременно результаты нескольких запросов, естественно,
    возникает ошибка.
    """
    results = await asyncio.gather(*queries)
    # print(await connection.execute(product_query))

asyncio.run(main())


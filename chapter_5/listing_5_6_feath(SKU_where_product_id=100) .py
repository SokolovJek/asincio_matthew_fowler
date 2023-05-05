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
    results: List[Record] = await connection.fetch(product_query)
    for result in results:
        print(f'id: {result["product_id"]}, product_name: {result["product_name"]}, product_color={result["product_color_name"]}, size={result["product_size_name"]}\n')

    await connection.close()

asyncio.run(main())


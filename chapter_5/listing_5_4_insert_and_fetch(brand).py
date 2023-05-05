import asyncpg
import asyncio
from asyncpg import Record
from typing import List
from bd_commands import brand_query


async def main() -> None:
    connection = await asyncpg.connect(host='127.0.0.1',
                                        port=5432,
                                        user='postgres',
                                        database='products',
                                        password='postgres')
    # await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'LEVIS')")
    # await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Seven')")

    result: List[Record] = await connection.fetch(brand_query)

    for brand in result:
        print(f'id: {brand["brand_id"]}, name: {brand["brand_name"]}')

    await connection.close()

asyncio.run(main())

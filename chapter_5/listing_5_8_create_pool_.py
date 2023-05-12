import asyncpg
import asyncio
from asyncpg import Record
from typing import List
from bd_commands import product_query
from utils import async_timed

@async_timed()
async def query_product(pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(product_query)

@async_timed()
async def main() -> None:
    async with asyncpg.create_pool(host='127.0.0.1',
                                           port=5432,
                                           user='postgres',
                                           database='products',
                                           password='postgres',
                                           min_size=6,
                                           max_size=6) as pool:

        result = await asyncio.gather(query_product(pool),
                                      query_product(pool),
                                      query_product(pool),
                                      query_product(pool),
                                      query_product(pool),
                                      query_product(pool),
                                      query_product(pool),
                                      query_product(pool),
                                      query_product(pool),
                                      query_product(pool),
                                      query_product(pool),
                                      query_product(pool),
                                      query_product(pool),
                                      query_product(pool))
        print(result)


asyncio.run(main())

import asyncpg
import asyncio
from bd_commands import product_query
from utils import async_timed


async def query_product(pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(product_query)

@async_timed()
async def query_product_synchronously(pool, queries):
    return [await query_product(pool) for _ in range(queries)]

@async_timed()
async def query_product_concurently(pool, queries):
    queries = [query_product(pool) for _ in range(queries)]
    return await asyncio.gather(*queries)

async def main() -> None:
    async with asyncpg.create_pool(host='127.0.0.1',
                                           port=5432,
                                           user='postgres',
                                           database='products',
                                           password='postgres',
                                           min_size=6,
                                           max_size=6) as pool:
        await query_product_concurently(pool, 10_000)
        await query_product_synchronously(pool, 10_000)
        await query_product_concurently(pool, 10_000)

asyncio.run(main())

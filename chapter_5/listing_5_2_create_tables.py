import asyncpg
import asyncio
import bd_commands


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                        port=5432,
                                        user='postgres',
                                        database='products',
                                        password='postgres')
    statements = [  bd_commands.CREATE_BRAND_TABLE,
                    bd_commands.CREATE_PRODUCT_TABLE,
                    bd_commands.CREATE_PRODUCT_COLOR_TABLE,
                    bd_commands.CREATE_PRODUCT_SIZE_TABLE,
                    bd_commands.CREATE_SKU_TABLE,
                    bd_commands.SIZE_INSERT,
                    bd_commands.COLOR_INSERT]
    print('Создается база данных зкщвгсеы...')
    for statement in statements:                            # INSERT будут выполнены синхронно. Поскольку одни таблицы зависят от других
        status = await connection.execute(statement)        # сопрограмма, поэтому завершения SQL-команд следует ожидать с помощью await
        print(status)
    print('База данных product создана!')
    await connection.close()

asyncio.run(main())

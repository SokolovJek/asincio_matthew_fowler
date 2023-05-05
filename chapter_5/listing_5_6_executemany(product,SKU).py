from operator import index
import asyncpg
import asyncio
from random import randint, sample
from typing import List, Tuple, Union
import os


path_dir = os.path.dirname(os.path.abspath(__file__))
path_to_file = os.path.join(path_dir, 'common_words.txt')


def load_common_worlds(path) -> List[str]:
    # получаем список слов из файла
    with open(path) as common_words:
        return common_words.readlines()


def gen_product(common_words: List[str],
                brand_id_start: int,
                brand_id_end: int,
                product_to_create: int) -> List[Tuple[str, int]]:
    # генерируем список с картежами(описание_продукта, id_продукта) для создания продуктов
    products = []
    for _ in range(product_to_create):
        description = [common_words[index] for index in sample(range(1000), 10)]
        brand_id = randint(brand_id_start, brand_id_end)
        products.append((' '.join(description), brand_id))
    return products

def gen_sku(product_id_start: int,
            product_id_end: int,
            skus_to_create: int) -> List[Tuple[int,int,int]]:
    # генерируем список с картежами(id_продукта, id_размера, id_цвета) для создания единиц на складе продуктов
    skus = []
    for _ in range(skus_to_create):
        product_id = randint(product_id_start, product_id_end)
        size_id = randint(1, 3)
        color_id = randint(1, 2)
        skus.append((product_id, size_id, color_id))
    return skus

async def main() -> None:
    """
    В результате выполнения этой функции мы получим базу данных, содержащую 1000 товаров и 100 000 SKU.
    """
    common_words = load_common_worlds(path=path_to_file)
    connection = await asyncpg.connect(host='127.0.0.1',
                                        port=5432,
                                        user='postgres',
                                        database='products',
                                        password='postgres')

    product_tuples = gen_product(common_words,
                                 brand_id_start=1,
                                 brand_id_end=100,
                                 product_to_create=1000)
    await connection.executemany("INSERT INTO product VALUES(DEFAULT, $1, $2)",
                                 product_tuples)
    sku_tuples = gen_sku(product_id_start=1,
                         product_id_end=1000,
                         skus_to_create=100_000)
    await connection.executemany("INSERT INTO sku VALUES(DEFAULT, $1, $2, $3)",
                                 sku_tuples)
    await connection.close()


asyncio.run(main())

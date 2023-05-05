from operator import index
import asyncpg
import asyncio
from random import sample
from typing import List, Tuple
import os


path_dir = os.path.dirname(os.path.abspath(__file__))
path_to_file = os.path.join(path_dir, 'common_words.txt')


def load_common_worlds(path) -> List[str]:
    # получаем список слов из файла
    with open(path) as common_words:
        return common_words.readlines()

def generate_brand_names(words: List[str]) -> List[Tuple[str]]:
    # получаем список слов(бренд), случайной последовательности
    return [(words[index],) for index in sample(range(100), 100)]

async def insert_brads(common_words, connection) -> int:
    # вставляем все бренды одной командой
    brands = generate_brand_names(common_words)
    insert_brands = 'INSERT INTO brand VALUES(DEFAULT, $1)'
    return await connection.executemany(insert_brands, brands) #За кулисами executemany в цикле обходит список марок и генерирует по одной команде INSERT для каждой марки

async def main() -> None:
    common_words = load_common_worlds(path=path_to_file)
    connection = await asyncpg.connect(host='127.0.0.1',
                                        port=5432,
                                        user='postgres',
                                        database='products',
                                        password='postgres')
    await insert_brads(common_words, connection)

asyncio.run(main())

# words = load_common_worlds(path=path_to_file)
# print(words)
# brands = generate_brand_names(words)
# print(brands)
# print('random_sample__indexes_list = ', sample(range(100), 100))
